import torch
import torchvision
from torchvision.transforms import functional as F
import numpy as np
import cv2
from PIL import Image

# Semantic and Instance Segmentation:
#           Partition an image into meaningful regions at the pixel level.
#           While semantic segmentation labels all pixels of a class (e.g., all "grass"),
#           instance segmentation distinguishes between individual objects of the
#           same class (e.g., each separate "person").



# 1. Load a pre-trained Mask R-CNN model (Instance Segmentation)
model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True)
model.eval()  # Set to evaluation mode

def segment_image(img_path):
    # 2. Load and prepare image
    img = Image.open(img_path).convert("RGB")
    img_tensor = F.to_tensor(img).unsqueeze(0)

    # 3. Perform Inference
    with torch.no_grad():
        prediction = model(img_tensor)

    # 4. Process Results
    # prediction[0]['masks'] contains the pixel-level masks
    # prediction[0]['labels'] contains the category IDs
    # prediction[0]['scores'] contains the confidence scores

    masks = prediction[0]['masks']
    scores = prediction[0]['scores']

    # Filter for high confidence (e.g., > 0.8)
    high_conf_masks = masks[scores > 0.8]

    print(f"Detected and segmented {len(high_conf_masks)} individual instances.")

    # (Optional) To visualize, you can overlay these masks on the original image
    return high_conf_masks

def draw_mask_on_image(image_path, masks, threshold=0.5, alpha=0.5):
    # 1. Load original image
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Create a copy to draw on
    overlay = img.copy()

    for i in range(len(masks)):
        # 2. Get binary mask (H, W)
        # Convert tensor to numpy and threshold it
        mask = masks[i, 0].cpu().detach().numpy()
        binary_mask = mask > threshold

        # 3. Pick a random color
        color = np.random.randint(0, 255, (3,), dtype="uint8")

        # 4. Color the overlay where the mask is True
        overlay[binary_mask] = color

    # 5. Blend the overlay with the original image
    # final = (alpha * overlay) + ((1 - alpha) * original)
    cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)

    # Show result
    Image.fromarray(img).show()


path_img51 = "data\\img\\ppl1.jpg"
masks1 = segment_image(path_img51)
draw_mask_on_image(path_img51, masks1)

path_img52 = "data\\img\\ppl2.jpg"
masks2 = segment_image(path_img52)
draw_mask_on_image(path_img52, masks2)

