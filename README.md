# Face Recognition & Attendance System

A Python-based face recognition and attendance management system built with OpenCV and SQLite.

## Features

- Real-time face detection and recognition using OpenCV.
- Register new users through a webcam.
- Store face encodings locally.
- Automatically record attendance.
- Prevent duplicate attendance records on the same day.
- Identify unknown faces.
- Voice announcements for recognized and unknown faces.
- Export attendance records to CSV.

## Technologies

- Python
- OpenCV
- SQLite
- NumPy
- Pickle
- CSV
- Windows Speech Synthesis

## Project Structure

```text
PYTHON_FACE_RECOGNITION/
│
├── db.py
├── download_models.py
├── enroll.py
├── faceio.py
├── recognize.py
├── speaker.py
├── models/
└── attendance.db
```

## Installation

Install the required package:

```bash
pip install opencv-python
```

## How to Run

**1. Download the required AI models:**

```bash
python download_models.py
```

**2. Register a person:**

```bash
python enroll.py
```

Enter a name and press SPACE to capture a face.

**3. Start face recognition:**

```bash
python recognize.py
```

Press Q to exit.

**4. Export attendance records:**

```bash
python db.py
```

The attendance report will be saved as `report.csv`.

## Requirements

- Python 3.x
- A working webcam
- Internet connection for downloading models
- Windows recommended for voice announcements

## Privacy

Face data is stored locally. Always obtain permission before collecting or processing anyone's facial data.

## Author

0MORADI0

GitHub: https://github.com/0MORADI0
