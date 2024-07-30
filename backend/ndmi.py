from model import *


def calculate_and_save_ndmi(image_path, output_directory, counter):
    with rasterio.open(image_path) as src:
        band_nir = src.read(8)
        band_swir = src.read(11)

    ndmi = (band_nir - band_swir) / (band_nir + band_swir)

    min_ndmi = np.nanmin(ndmi)
    max_ndmi = np.nanmax(ndmi)

    colormap_ndmi = plt.cm.RdYlGn
    norm_ndmi = plt.Normalize(vmin=min_ndmi, vmax=max_ndmi)

    plt.figure(figsize=(2, 2))
    plt.imshow(ndmi, cmap=colormap_ndmi, norm=norm_ndmi)
    plt.axis('off')

    os.makedirs(output_directory, exist_ok=True)

    output_filename = os.path.join(output_directory, f"ndmi-test_{counter}.png")
    plt.savefig(output_filename, dpi=300, bbox_inches='tight', pad_inches=0.1)
    # plt.show()
    # plt.close()

    print(f"Processed NDMI: {output_filename}")

    