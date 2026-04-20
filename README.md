# 😎 Face-Triggered SexyBack Player

A fun and slightly dramatic Python application that monitors your screen and automatically plays **SexyBack** (or any song of your choice) the moment your face is detected in the feed! 

---

## 📌 Overview

This project uses **real-time screen capture** and **facial recognition** to trigger a soundtrack for your presence. It captures frames from your monitor, compares them against a library of "known faces," and manages audio playback dynamically. If you leave the screen, the music stops; if you return, the beat drops again.

---

## ✨ Features

- **Screen-Based Detection**: Unlike traditional webcam apps, this monitors a region of your **screen feed** using `mss`.
- **Known Face Matching**: Checks detected faces against images stored in the `faces/` directory.
- **Instant Playback**: Uses `pygame.mixer` for low-latency audio triggering.
- **Anti-Flicker Logic**: Implements a "missing frame limit" to ensure the music doesn't stop during brief detection gaps.
- **Customizable**: Easily swap out the trigger song or the face library.

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| **Language** | Python |
| **Face Recognition** | `face_recognition` (dlib-based) |
| **Image Processing** | `OpenCV` & `NumPy` |
| **Screen Capture** | `mss` |
| **Audio Playback** | `Pygame` |

---

## 📂 Project Structure

```
Facial Recognition Based Song Player/
├── code.py          # The main detection & playback logic
├── requirements.txt   # Python dependencies
├── sexyback.mp3       # The default "entrance" theme
├── pony.mp3           # Secondary track
└── faces/             # Place images of yourself here (.jpg, .png)
```

---

## 🚀 Setup & Installation

### Prerequisites
- Python 3.8+
- **CMake** (Required for the `face-recognition` library's `dlib` dependency)

### 1. Clone the repository
```bash
git clone https://github.com/ananyareddygandlaparthi/Face-Triggered-Sexyback-Player.git
cd Face-Triggered-Sexyback-Player
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

> [!IMPORTANT]
> If you encounter errors installing `face-recognition`, ensure you have **CMake** and **Visual Studio C++ Build Tools** installed on Windows.

### 3. Add your face
Place a clear photo of yourself in the `faces/` directory. The app will load all images in this folder as "authorized" triggers.

### 4. Run the app
```bash
python code.py
```

---

## ⚙️ Configuration

You can tweak these variables at the top of `code.py`:
- `MUSIC_FILE`: Change this to `"pony.mp3"` or your favorite track.
- `FACE_TOLERANCE`: Adjust (lower = stricter) if you get false positives.
- `MONITOR_REGION`: Defaults to your main monitor.

---

