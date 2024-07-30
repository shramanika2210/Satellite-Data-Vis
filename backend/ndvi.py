from model import *


def calculate_and_save_ndvi(image_path, output_directory, counter):
    with rasterio.open(image_path) as src:
        # Read Red and Near Infrared bands (bands 4 and 8 respectively)
        band_red = src.read(4)
        band_nir = src.read(8)

    # Calculate NDVI
    ndvi = (band_nir.astype(float) - band_red.astype(float)) / (band_nir + band_red + 1e-8)

    # Set min/max values from NDVI range for image
    min_ndvi = np.nanmin(ndvi)
    max_ndvi = np.nanmax(ndvi)

    # Setting colormap and normalization
    colormap_ndvi = plt.cm.RdYlGn
    norm_ndvi = plt.Normalize(vmin=min_ndvi, vmax=max_ndvi)

    # Plotting NDVI image without colorbar and axis
    plt.figure(figsize=(2, 2))
    plt.imshow(ndvi, cmap=colormap_ndvi, norm=norm_ndvi)
    plt.axis('off')

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Save the plot as an image file in the specified output directory with sequential numbering
    output_filename = os.path.join(output_directory, f"ndvi-test_{counter}.png")
    plt.savefig(output_filename, dpi=300, bbox_inches='tight', pad_inches=0.1)
    # plt.show()
    # plt.close()  # Close the plot to free memory

    print(f"Processed NDVI: {output_filename}")

    
