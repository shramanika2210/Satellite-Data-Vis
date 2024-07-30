import os

def run_single_model(input_dir, output_dir, calculate_and_save):
        # Directory containing Sentinel-2 images
    input_directory = input_dir

    # Directory for saving output NDMI images
    output_directory = output_dir

    # Counter for output file names
    counter = 1

    # Iterate through all TIFF files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".tif"):  # Process only TIFF files
            image_path = os.path.join(input_directory, filename)
            calculate_and_save(image_path, output_directory, counter)
            counter += 1

    print("NDMI conversion completed for all images.")