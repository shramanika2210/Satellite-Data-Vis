import os
import numpy as np
from PIL import Image
from tensorflow import keras
import matplotlib.pyplot as plt

# Function to load and preprocess test images
def load_and_preprocess_test_data(test_folder, target_size=(64, 64)):
    test_images = []
    image_paths = []

    for image_file in os.listdir(test_folder):
        image_path = os.path.join(test_folder, image_file)
        if os.path.isfile(image_path) and image_file.endswith('.png'):
            # Load PNG image using PIL
            image = Image.open(image_path)

            # Resize the image to the target size
            resized_image = image.resize(target_size)

            # Convert resized image to numpy array
            image_data = np.array(resized_image)

            test_images.append(image_data)
            image_paths.append(image_path)

    # Convert lists to numpy arrays
    test_images = np.array(test_images)

    # Normalize pixel values to be between 0 and 1
    test_images = test_images / 255.0

    return test_images, image_paths

def predict_and_display_results(test_folder, model_path, class_names):
# Load and preprocess test data
    test_images, image_paths = load_and_preprocess_test_data(test_folder)

    # Load the trained model
    model = keras.models.load_model(model_path, compile=False)

    # Predict on test data
    predictions = model.predict(test_images)

    # Convert predictions to class labels
    predicted_labels = np.argmax(predictions, axis=1)

    # Decode class labels using the class_names
    decoded_labels = [class_names[label] for label in predicted_labels]

    # Store the predicted results in a list
    predicted_results = list(zip(image_paths, decoded_labels))

    # Display predictions
    for image_path, predicted_label in predicted_results:
        # Load the image using PIL for display
        image = Image.open(image_path)

        # Display the image
        # plt.imshow(image)
        # plt.axis('off')
        # plt.show()

        # Print the predicted label
        print(f"Predicted Class for {os.path.basename(image_path)}: {predicted_label}")
        print("-" * 30)

    return predicted_results