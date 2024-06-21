import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Load the saved model
model = tf.keras.models.load_model('handwritten_character_recognition_model.h5')

# Define the mapping of labels to characters
label_to_char = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J',
                 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T',
                 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'}

def preprocess_image(image_path):
    # Load the image
    image = Image.open(image_path).convert('L')  # Convert to grayscale
    # Resize the image to 28x28
    image = image.resize((28, 28))
    # Convert image to numpy array and normalize pixel values
    image_array = np.array(image) / 255.0
    # Reshape to match the input shape of the model
    image_array = np.expand_dims(image_array, axis=0)
    image_array = np.expand_dims(image_array, axis=-1)
    return image_array

def predict_character(image_path):
    # Preprocess the image
    image_array = preprocess_image(image_path)
    # Predict the label of the image
    predictions = model.predict(image_array)
    predicted_label = np.argmax(predictions)
    # Add 1 to the predicted label
    predicted_label +=1
    return label_to_char[predicted_label]

def display_prediction(image_path):
    # Predict the character from the image
    predicted_char = predict_character(image_path)
    # Load the image for display
    image = Image.open(image_path).convert('L')
    # Display the image and prediction
    plt.imshow(image, cmap='gray')
    plt.title(f'Predicted Character: {predicted_char}')
    plt.axis('off')
    plt.show()

# Provide the path to the handwritten image
image_path = 'projectimage5.jpg'  # Change this to your image file path
display_prediction(image_path)