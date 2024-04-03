import streamlit as st
import cv2
import sys
import cv2
import depthai as dai
import numpy as np
import time

syncNN = True

# Create pipeline
pipeline = dai.Pipeline()

# Define sources and outputs
camRgb = pipeline.createColorCamera()
# detectionNetwork = pipeline.create(dai.node.YoloDetectionNetwork)
xoutRgb = pipeline.createXLinkOut()
# nnOut = pipeline.create(dai.node.XLinkOut)

xoutRgb.setStreamName("rgb")
# nnOut.setStreamName("nn")

# Properties
camRgb.setPreviewSize(416, 416)
camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
camRgb.setInterleaved(False)
camRgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.BGR)
camRgb.setFps(60)
camRgb.preview.link(xoutRgb.input)


def video_disp():
    stop_button_pressed = st.button("Stop")
    frame_placeholder = st.empty()
    frame_placeholder2 = st.empty()
    with dai.Device(pipeline) as device:

    # Output queues will be used to get the rgb frames and nn data from the outputs defined above
        qRgb = device.getOutputQueue(name="rgb")
        startTime = time.monotonic()
        color2 = (255, 255, 255)
        counter =0         

        while True:
            
            inRgb = qRgb.get()

            if inRgb is not None:
                frame = inRgb.getCvFrame()
                cv2.putText(frame, "NN fps: {:.2f}".format(counter / (time.monotonic() - startTime)),
                            (2, frame.shape[0] - 4), cv2.FONT_HERSHEY_TRIPLEX, 0.4, color2)

            

            if frame is not None:
                counter+=1
            frame=cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
            frame_placeholder.image(frame,channels="RGB")
            #frame_placeholder2.image(frame,channels="RGB")
            if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed:
                break
    
def main ():
    st.title("Webcam feed on browser")
    start_button_pressed = st.button("Start")
    if start_button_pressed:
        video_disp()
if __name__ == "__main__":
    main()
