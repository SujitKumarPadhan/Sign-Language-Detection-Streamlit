# backend/camera_stream.py

import cv2
import mediapipe as mp
import time

from backend.hand_landmarker import create_hand_landmarker
from backend.gesture_rules import detect_gesture
from backend.drawing_utils import draw_text, draw_landmarks

# Create hand landmarker once
landmarker = create_hand_landmarker()


def process_frame(frame):

    print("Frame received")

    # Convert BGR to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Create MediaPipe Image
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    try:
        # Use real timestamp instead of global counter
        results = landmarker.detect_for_video(
            mp_image,
            int(time.time() * 1000)
        )

        print("Detection completed")

    except Exception as e:
        print("MediaPipe Error:", e)
        return frame

    # If hand detected
    if results.hand_landmarks:

        # Draw hand skeleton
        frame = draw_landmarks(
            frame,
            results.hand_landmarks
        )

        # Use first hand for gesture recognition
        hand = results.hand_landmarks[0]

        # Detect gesture
        sign = detect_gesture(hand)

        # Draw gesture name
        frame = draw_text(
            frame,
            sign
        )

    return frame