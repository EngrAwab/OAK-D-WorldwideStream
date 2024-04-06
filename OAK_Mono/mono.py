import cv2
import depthai as dai
import numpy as np
import time
import streamlit as st 
pipeline = dai.Pipeline()
monoLeft = pipeline.create(dai.node.MonoCamera)
monoLeft.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
monoLeft.setBoardSocket(dai.CameraBoardSocket.CAM_B)

monoRight = pipeline.create(dai.node.MonoCamera)
monoRight.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
monoRight.setBoardSocket(dai.CameraBoardSocket.CAM_C)

monoRight_xout = pipeline.create(dai.node.XLinkOut)
monoLeft_xout = pipeline.create(dai.node.XLinkOut)
monoLeft_xout.setStreamName('left')
monoRight_xout.setStreamName('right')
monoRight.out.link(monoRight_xout.input)
monoLeft.out.link(monoLeft_xout.input)

def video_disp():
    stop_button_pressed = st.button("Turn off camera")
    frame_placeholder = st.empty()
    
    with dai.Device(pipeline) as device:
        right = device.getOutputQueue(name="right")
        left = device.getOutputQueue(name="left")
        startTime = time.monotonic()
        color2 = (255, 255, 255)
        counter =0         
        
        while True:
            
            inright = right.get()
            inleft = left.get()
            
            frame_l = inleft.getCvFrame()
            frame_r =inright.getCvFrame()
            cv2.putText(frame_l, "NN fps: {:.2f}".format(counter / (time.monotonic() - startTime)),
                        (2, frame_l.shape[0] - 4), cv2.FONT_HERSHEY_TRIPLEX, 0.4, color2)
            cv2.putText(frame_r, "NN fps: {:.2f}".format(counter / (time.monotonic() - startTime)),
                        (2, frame_r.shape[0] - 4), cv2.FONT_HERSHEY_TRIPLEX, 0.4, color2)
            
            frame = np.concatenate((frame_r, frame_l), axis=1)
            frame=cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
            frame_placeholder.image(frame,channels="RGB")
            counter+=1
                # displayFrame("rgb", frame)

            if cv2.waitKey(1) == ord('q'):
                break
    frame_l.release()
    frame_r.release()

def main ():
    st.title("Webcam feed on browser")
    
    start_button_pressed = st.button("Turn on Camera")
    if start_button_pressed:
        video_disp()
if __name__ == "__main__":
    main()
