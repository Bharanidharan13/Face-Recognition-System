# 🧠 Face Recognition Attendance System

A real-time face recognition-based attendance system built with Python. It detects known faces using a webcam and marks attendance in a CSV file, all through a simple GUI.

---

## 📄 Abstract

This project implements an automated attendance system using facial recognition. It leverages the `face_recognition` and `OpenCV` libraries for face detection and matching, and uses `Tkinter` for the graphical interface. Images of known individuals are used to train the system, and attendance is recorded each time a face is recognized.

---

## ✅ Features

- 🔍 **Real-time face detection and recognition**
- 🧠 **Uses known face encodings from training images**
- 📅 **Automatically logs name, time, and date**
- 🖥️ **Simple GUI with Start, Stop, and Exit options**
- 💾 **CSV-based attendance tracking**
- 🧵 **Multithreaded processing for smooth GUI experience**

---

## 📝 Required Libraries:
- OpenCV (opencv-python): A library used for image and video processing. It provides the functionality to capture frames from the webcam and display them.

- Installation: pip install opencv-python

- Purpose: Used for face detection, frame manipulation, and camera access.

- face_recognition: A library built on top of dlib for easy face recognition. It handles face detection, face encoding, and face comparison.

- Installation: pip install face_recognition

- Purpose: Used to detect faces, extract face encodings, and compare those encodings to recognize faces.

- NumPy (numpy): A library for numerical operations, primarily used for handling large multi-dimensional arrays and matrices.

- Installation: pip install numpy

- Purpose: Used to handle and manipulate data, especially when working with images.

- Tkinter (tk): A GUI library included with Python that allows for the creation of windowed applications.

- Installation: pip install tk (If Tkinter is not already installed with Python)

- Purpose: Provides the graphical interface for the application (buttons, labels, etc.).

---

## 🚀 How to Run
- Add training images

  Place clear frontal face images of students in the student_images/ folder.

  Ensure each image filename matches the student's name (e.g., JohnDoe.jpg).

- Run the script

  Run app.py in python interpreter(prefer:python 3.9.13)

- Use the GUI

  Click Start Recognition to begin detecting faces via webcam.

  Click Stop Recognition to end the recognition process.

  Press Exit to close the application.

---

## 🧪 Output Example (Attendance.csv)

Once a face is recognized, attendance is recorded in the Attendance.csv file, which will look something like this:

Example:

- Name | Log In Time | Date
- Johndoe | 09:45:12 AM | 07-May-2025
- Michael | 09:46:25 AM | 07-May-2025

- Name: The name of the recognized individual.
- Log In Time: The time when the individual was detected.
- Date: The date of attendance.



