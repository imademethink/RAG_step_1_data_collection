from deepface import DeepFace


# Facial Recognition and Emotion Detection:
#           Detect human faces and verify identities or analyze facial landmarks to predict emotions
#           like "happy," "sad," or "surprised".
#           Libraries like Dlib and Face_recognition are industry standards for these tasks.



# Facial Recognition (Identity)
#
# This process answers the question: "Who is this?"
# Face Landmarks: The system identifies key points (eyes, nose, mouth).
# Face Encoding: The image is converted into a vector of numbers (usually 128 or 256 measurements)
#   representing the unique geometry of the face.
# Comparison: The system calculates the "Euclidean distance" between two vectors.
#   If the distance is small, the faces match.



path_img_org = "data\\img\\obama1.png"
path_img_new = "data\\img\\obama2.jpg"

# Facial Recognition (Identity)
result = DeepFace.verify(img1_path = path_img_org, img2_path = path_img_new)
print("Is same person:", result["verified"])


# Emotion Detection (State)
#
#   This process answers the question: "How is this person feeling?"
#   Landmark Analysis: The system looks for specific movements
#   (e.g., raised eyebrows for "surprised" or pulled-back lip corners for "happy").
#   Classification: Usually, a Convolutional Neural Network (CNN) is trained on thousands
#   of labeled images to categorize these movements into discrete emotions.

# Analyze an image for emotions
# It detects 'dominant_emotion' among: angry, fear, neutral, sad, disgust, happy, surprise


path_img_org = "data\\img\\obama1.png"
results = DeepFace.analyze(img_path = path_img_org, actions = ['emotion'])
print(f"Dominant Emotion: {results[0]['dominant_emotion']}")
print(f"Confidence: {results[0]['emotion'][results[0]['dominant_emotion']]:.2f}%")

path_img_new = "data\\img\\obama2.jpg"
results = DeepFace.analyze(img_path = path_img_new, actions = ['emotion'])
print(f"Dominant Emotion: {results[0]['dominant_emotion']}")
print(f"Confidence: {results[0]['emotion'][results[0]['dominant_emotion']]:.2f}%")






# future scope
# Generative Image Synthesis: Create entirely new images from text prompts or modify existing ones using Generative Adversarial Networks (GANs) or Diffusion models.

# Data Augmentation for Training: Artificially expand your training dataset by applying AI-friendly transformations like random cropping, flipping, or lighting adjustments. The Albumentations library is highly optimized for this purpose.
