# import torch
# print(torch.__version__)
# print(torch.cuda.is_available())
from ultralytics import YOLO
# load an official model or a custom model
model = YOLO('E:\\YOLO Model\\yolov8n.pt')
# predict with the model on an image,return a list of results objects
# Inference Sources:png1,png2
results = model(['F:\\Photo\\ID\\Shenyutong-2 inches-20230624-2.png','F:\\Photo\\ID\\Shenyutong-2 inches-20230625-2.png'], save=False)
for result in results:
    # Boxes object can be used to index, manipulate, and convert bounding boxes to different formats. Box format conversion operations are cached, meaning they're only calculated once per object, and those values are reused for future calls
    boxes=result.boxes
    masks=result.masks
    keypoints=result.keypoints
    probs=result.probs
    print(boxes.conf,boxes[1].xyxy)
# model.predict('F:\\Photo\\ID', save=True, imgsz=640,iou=0.7,max_det=6,conf=0.9,line_width=1)