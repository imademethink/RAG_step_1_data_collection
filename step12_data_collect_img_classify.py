from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np


# Image Classification and Labeling:
#       Automatically assign a category (e.g., "cat," "dog," "car") to an entire image using
#       pre-trained Convolutional Neural Networks (CNNs) like ResNet or VGG-16


# over 1.2 million images across 1,000 categories
# https://deeplearning.cms.waikato.ac.nz/examples/inference/#class-map-lookup-tables
# 1. Load the pre-trained ResNet50 model
# 'weights=imagenet' loads the patterns learned from the ImageNet dataset
model = ResNet50(weights='imagenet')

def classify_image(img_path):
    # 2. Load and resize the image to 224x224 (required by ResNet)
    img = image.load_img(img_path, target_size=(224, 224))
    # 3. Convert image to a numerical array and add a "batch" dimension
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    # 4. Preprocess the image (scales pixels to the format the model expects)
    x = preprocess_input(x)
    # 5. Make the prediction
    preds = model.predict(x)
    # 6. Decode the results into human-readable labels
    # Returns the top 3 most likely categories
    print('Predicted:', decode_predictions(preds, top=3)[0])

# classify dog
path_img31 = "data\\dog_img\\dog1.jpg"
path_img32 = "data\\dog_img\\dog2.jpeg"
path_img33 = "data\\dog_img\\dog3.png"
path_img34 = "data\\dog_img\\dog4.jpg"
classify_image(path_img31)
classify_image(path_img32)
classify_image(path_img33)
classify_image(path_img34)

# classify cat
path_img41 = "data\\dog_img\\cat1.png"
path_img42 = "data\\dog_img\\cat2.jpg"
path_img43 = "data\\dog_img\\cat3.jpeg"
path_img44 = "data\\dog_img\\cat4.jpeg"
path_img45 = "data\\dog_img\\cat5.jpeg"
classify_image(path_img41)
classify_image(path_img42)
classify_image(path_img43)
classify_image(path_img44)
classify_image(path_img45)

# classify combined dog, cat, rat
path_img51 = "data\\dog_img\\all1.jpg"
path_img52 = "data\\dog_img\\all2.jpg"
path_img53 = "data\\dog_img\\all3.jpg"
classify_image(path_img51)
classify_image(path_img52)
classify_image(path_img53)

# google for        what are ResNet object categories
# google for        what are VGG-16 object categories


