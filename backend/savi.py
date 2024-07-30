from model import *

def calculate_and_save_savi(image_path, output_directory, counter):
    with rasterio.open(image_path) as src:
        band_red = src.read(4)
        band_nir = src.read(8)

    savi = ((band_nir - band_red) / (band_nir + band_red + 0.5)) * 1.5

    min_savi = np.nanmin(savi)
    max_savi = np.nanmax(savi)

    colormap_savi = plt.cm.RdYlGn
    norm_savi = plt.Normalize(vmin=min_savi, vmax=max_savi)

    plt.figure(figsize=(2, 2))
    plt.imshow(savi, cmap=colormap_savi, norm=norm_savi)
    plt.axis('off')

    os.makedirs(output_directory, exist_ok=True)

    output_filename = os.path.join(output_directory, f"savi-test_{counter}.png")
    plt.savefig(output_filename, dpi=300, bbox_inches='tight', pad_inches=0.1)
    # plt.show()
    # plt.close()

    print(f"Processed SAVI: {output_filename}")

    