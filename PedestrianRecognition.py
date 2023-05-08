#!/usr/bin/python
#coding=utf-8
import cv2
import imutils
import numpy as np
import torch
from tqdm import tqdm
from jetcam.csi_camera import CSICamera

model = torch.hub.load('ultralytics/yolov5', 'custom', path="/media/tiny/venvs/yolo_env/peatones/best/bestJetson.pt",force_reload=True)
cap = CSICamera(width=1080, height=720, capture_width=1080, capture_height=720, capture_fps=30)
#cap = cv2.VideoCapture("/media/tiny/venvs/yolo_env/UNAM.mp4")
out = cv2.VideoWriter('PruebaJetsonYolo.avi',cv2.VideoWriter_fourcc('M','J','P','G'),20 , (1080,720))
n, nframes = 0, 300
for _ in tqdm(range(nframes), ncols=100):
    frame = cap.read()
    #frame = cv2.resize(frame,(1080,720))
    # Detectar personas en el marco
    detect = model(frame)
    #out.write()
    out.write(np.squeeze(detect.render()))
    if cv2.waitKey(1) == 27: break
out.release()


