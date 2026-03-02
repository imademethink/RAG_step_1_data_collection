import cv2
from ultralytics import YOLO

# Object detection in a video:


# Load model and open video
model = YOLO("yolov8n.pt")  # or yolov8s.pt, yolov8m.pt
# path_vid3 = "data\\vid\\vid3.mp4"
path_vid3 = "data\\vid\\vid4.mp4"
cap = cv2.VideoCapture(path_vid3)  # Use '0' for webcam

while cap.isOpened():
    success, frame = cap.read()
    if not success: break

    # Run inference and plot results
    results = model(frame, stream=False)
    # Simple way: Specify HD resolution for inference
    # results = model.predict(source=path_vid3, imgsz=1080, show=False)

    for r in results:
        cv2.imshow("YOLOv8 Detection", r.plot())

    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
cv2.destroyAllWindows()
