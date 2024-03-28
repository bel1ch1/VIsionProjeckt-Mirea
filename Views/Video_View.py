import streamlit as st
import cv2


class Video_View:
    def __init__(self, camera_id=0, camera_name="test"):
        self.camera_id = camera_id
        self.camera_name = camera_name

    def video_output(camera_id, camera_name):
        cap = cv2.VideoCapture(camera_id)
        while True:
            ret, frame = cap.read()

            if not ret:
                break

            cv2.imshow(camera_name, frame)
            cap.release()
            cv2.destroyAllWindows()
