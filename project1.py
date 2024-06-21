import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from PIL import Image

# Load the saved model
model = tf.keras.models.load_model('handwritten_character_recognition_model.h5')


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
    return predicted_label


def display_prediction(image_path):
    # Load the image
    image = Image.open(image_path)
    # Display the input image
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Input Image')
    plt.axis('off')

    # Predict the character
    predicted_label = predict_character(image_path)

    # Display the output (predicted label)
    plt.subplot(1, 2, 2)
    plt.text(0.5, 0.5, f'Predicted Label: {predicted_label}', fontsize=12, ha='center')
    plt.title('Output (Prediction)')
    plt.axis('off')

    plt.show()


# Provide the path to the handwritten image
image_path = 'handwritting.jpeg'  # Change this to your image file path
display_prediction(image_path)