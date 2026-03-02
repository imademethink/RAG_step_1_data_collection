from ultralytics import YOLO


# Object Detection and Localization:
#           Identify multiple objects within a single image and draw "bounding boxes" around them.
#           This is commonly achieved using high-speed models like
#           YOLO (You Only Look Once) or SSD (Single Shot MultiBox Detector).
#           google for      pre-trained YOLO model list



# 1. Load a pre-trained YOLOv8 model (n = nano, the fastest version)
model = YOLO('yolov8n.pt')

def detect_objects(img_path):
    # 2. Run inference on the image
    # The model automatically handles resizing and normalization
    results = model(img_path)

    # 3. Process the results
    for result in results:
        # Show the result visually (opens a window with bounding boxes drawn)
        result.show()

        # 4. Access raw data if needed
        for box in result.boxes:
            class_id = int(box.cls[0])
            label = model.names[class_id]
            confidence = float(box.conf[0])
            coords = box.xyxy[0].tolist()  # [xmin, ymin, xmax, ymax]

            print(f"Detected {label} with {confidence:.2f} confidence at {coords}")

path_img45 = "data\\dog_img\\all1.jpg"
path_img46 = "data\\dog_img\\all2.jpg"
path_img47 = "data\\dog_img\\all3.jpg"
detect_objects(path_img45)
detect_objects(path_img46)
detect_objects(path_img47)


