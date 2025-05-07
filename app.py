import tkinter as tk
from tkinter import ttk, messagebox
import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
import threading

path = 'student_images'
images = []
classNames = []
encoded_face_train = []
stop_recognition = False
recognition_thread = None 

def initialize_attendance_file():
    attendance_file = 'Attendance.csv'
    if not os.path.exists(attendance_file):
        with open(attendance_file, 'w') as f:
            f.write('Name, Log In Time, Date\n')

def load_images():
    global images, classNames, encoded_face_train
    images = []
    classNames = []
    encoded_face_train = []

    if not os.path.exists(path):
        messagebox.showerror("Error", f"Image folder '{path}' not found.")
        return

    mylist = os.listdir(path)
    for cl in mylist:
        curImg = cv2.imread(f'{path}/{cl}')
        if curImg is not None:
            images.append(curImg)
            classNames.append(os.path.splitext(cl)[0])
        else:
            print(f"Warning: Unable to read image {cl}")

    encoded_face_train = find_encodings(images)

def find_encodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img)
        if encodings:
            encodeList.append(encodings[0])
        else:
            print("Warning: No face found in one of the images.")
    return encodeList

def mark_attendance(name):
    attendance_file = 'Attendance.csv'
    today_date = datetime.now().strftime('%d-%B-%Y')
    with open(attendance_file, 'r+') as f:
        attendance_records = f.readlines()
        attendance_names = [record.split(',')[0].strip() for record in attendance_records]

        if name not in attendance_names:
            now = datetime.now()
            time = now.strftime('%I:%M:%S %p')
            f.write(f'{name}, {time}, {today_date}\n')

def recognize_faces():
    global stop_recognition
    stop_recognition = False  

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Error", "Could not open webcam.")
        return

    while not stop_recognition:
        success, img = cap.read()
        if not success:
            messagebox.showerror("Error", "Failed to capture image")
            break

        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        faces_in_frame = face_recognition.face_locations(imgS)
        encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)

        for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
            matches = face_recognition.compare_faces(encoded_face_train, encode_face)
            faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
            matchIndex = np.argmin(faceDist)

            if matches and matches[matchIndex]:
                name = classNames[matchIndex].lower()
                y1, x2, y2, x1 = faceloc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                mark_attendance(name)

        cv2.imshow('Webcam', img)
        if cv2.waitKey(1) & 0xFF == ord('q') or stop_recognition:
            break

    cap.release()
    cv2.destroyAllWindows()

def start_recognition():
    global recognition_thread
    load_images()
    if not encoded_face_train:
        messagebox.showwarning("No Data", "No faces found for recognition.")
        return

    recognition_thread = threading.Thread(target=recognize_faces)
    recognition_thread.start()

def stop_face_recognition():
    global stop_recognition
    stop_recognition = True

initialize_attendance_file()

root = tk.Tk()
root.title("Face Recognition Attendance System")
root.geometry("800x600")

header_label = tk.Label(root, text="Face Recognition Attendance System", font=("Helvetica", 20))
header_label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

start_button = ttk.Button(button_frame, text="Start Recognition", command=start_recognition)
start_button.pack(side=tk.LEFT, padx=10)

stop_button = ttk.Button(button_frame, text="Stop Recognition", command=stop_face_recognition)
stop_button.pack(side=tk.LEFT, padx=10)

exit_button = ttk.Button(button_frame, text="Exit", command=root.destroy)
exit_button.pack(side=tk.RIGHT, padx=10)

root.mainloop()
