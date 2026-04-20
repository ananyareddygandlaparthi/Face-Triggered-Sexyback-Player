

import face_recognition
import cv2
import numpy as np
import os
from mss import mss
import pygame
import time

MUSIC_FILE = "sexyback.mp3"
KNOWN_FACES_DIR = "faces"
MONITOR_REGION = mss().monitors[1]

FACE_TOLERANCE = 0.5
FRAME_DELAY = 0.05
MISSING_FRAMES_LIMIT = 1

DEBUG_SHOW_FRAME = False


if not os.path.exists(MUSIC_FILE):
    raise FileNotFoundError(f"Music file not found: {MUSIC_FILE}")


pygame.mixer.init()


known_face_encodings = []
for filename in os.listdir(KNOWN_FACES_DIR):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(KNOWN_FACES_DIR, filename)
        image = face_recognition.load_image_file(img_path)
        encodings = face_recognition.face_encodings(image)
        if encodings:
            known_face_encodings.append(encodings[0])
            print(f"Loaded face: {filename}")
        else:
            print(f"No face found in {filename}")

if not known_face_encodings:
    raise ValueError("No valid faces found in 'faces' folder.")


sct = mss()
face_detected = False
missing_counter = 0

try:
    while True:
        frame = np.array(sct.grab(MONITOR_REGION))[:, :, :3]

        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        matched = False
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=FACE_TOLERANCE)
            if True in matches:
                matched = True
                break

        if matched:
            if not face_detected:
                print("Face detected")
                pygame.mixer.music.load(MUSIC_FILE)
                pygame.mixer.music.play()
                face_detected = True
            missing_counter = 0
        else:
            if face_detected:
                missing_counter += 1
                if missing_counter >= MISSING_FRAMES_LIMIT:
                    print("Face disappeared")
                    pygame.mixer.music.stop()
                    face_detected = False

        if DEBUG_SHOW_FRAME:
            for (top, right, bottom, left) in face_locations:
                top *= 2
                right *= 2
                bottom *= 2
                left *= 2
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            cv2.imshow("Screen Feed", frame)
            if cv2.waitKey(1) == ord('q'):
                break

        time.sleep(FRAME_DELAY)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    pygame.mixer.music.stop()
    if DEBUG_SHOW_FRAME:
        cv2.destroyAllWindows()
