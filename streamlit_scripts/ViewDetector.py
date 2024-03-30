import streamlit as st
import cv2


def view_detector():

    st.title('video detector')

    st.write("# Видео стрим")

    col1, buff, col2 = st.columns([2, 1, 2])
    with col1:
        frame_placeholder = st.empty()

    with col2:
        btn_stop = st.button("Stop")
        btn_start = st.button("Start")

    if btn_start:
        cap = cv2.VideoCapture(0)
        while cap.isOpened() and not btn_stop:
            ret, frame = cap.read()

            if not ret:
                break

            frame_placeholder.image(frame, channels="BGR")

            if btn_stop:
                break
        cap.release()
        cv2.destroyAllWindows()
