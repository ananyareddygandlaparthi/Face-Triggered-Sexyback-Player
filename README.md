# Face-Triggered SexyBack Player 🎶

Plays **SexyBack by Justin Timberlake** whenever a chosen face appears on screen — automating the “every time X appears, SexyBack plays” trend.  

A fun Python project that runs in the background, watches your screen, and whenever it recognizes a face, it automatically plays SexyBack. When the face disappears, the music stops.

This project automates the recent “\[show name\] but every time \[someone\] appears SexyBack plays” trend on social media by handling the detection and playback for you.


<br>
<br>


## ✨ Features

<br>

- Real-time face recognition from your screen using **face_recognition** and **mss**
- Plays and stops music automatically with **pygame**
- Customizable: just add or swap images in the `faces/` folder — the more you add, the better the recognition
- Works best with clear, front-facing images (side profiles or obscured faces are less reliable)
- Lightweight and runs in the background
- Optional debug mode to see the detected faces on-screen  



<br>
<br>


## ⚙️ Quickstart

<br>
1. **Clone the repo:**
   ```bash
   git clone https://github.com/ananyareddygandlaparthi/Face-Triggered-Sexyback-Player.git
   cd Face-Triggered-Sexyback-Player
   ```
<br>
<br>

2. **Install dependencies:**
   ```bash
   pip install face_recognition opencv-python numpy mss pygame
   ```
<br>
<br>

   ⚠️ **Note:** `face_recognition` requires `dlib`.  
   If installation fails, check [these instructions](https://www.pyimagesearch.com/2017/03/27/how-to-install-dlib/).

<br>
<br>

3. **Add your reference images** to the `faces/` folder.  
   - The more images you add, the better recognition will work.  
   - Use **clear, front-facing images** (side profiles aren’t great).  
   - For the sake of example, Carlos Sainz is included by default.  

<br>
<br>

4. **Place your audio file** in the repo root and name it:  
   `sexyback.mp3`

<br>
<br>

5. **Run it:**
   ```bash
   python main.py
   ```
<br>
<br>

6. *(Optional)* Enable debug mode to visualize detection:  
   In `main.py`, set:  
   ```python
   DEBUG_SHOW_FRAME = True
   ```
<br>
<br>



## 📌 Notes

<br>


- You can swap out the `faces/` images to track whoever you want.  
- More images = better recognition.  
- Plays **SexyBack** by default, but you can replace `sexyback.mp3` with any `.mp3`.  

<br>
<br>

## 🕺 Inspiration

<br>


This project is a playful automation of the **“every time \[someone\] appears, SexyBack plays”** trend that’s been circulating on social media. Now it happens in real-time, hands-free.
