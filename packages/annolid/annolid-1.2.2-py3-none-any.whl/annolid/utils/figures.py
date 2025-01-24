import os
import matplotlib.pyplot as plt
from PIL import Image

# Define the folder containing the images
folder_name = "/Users/chenyang/Downloads/NIHMS517142-supplement-S_movie_1_results"  # Replace with your folder name
output_file = f"{folder_name}_figure.png"  # Output figure name

# Get the list of PNG files in the folder
image_files = [os.path.join(folder_name, f) for f in os.listdir(folder_name) if f.endswith(".png")]

# Sort the files if necessary (optional, ensures order)
image_files.sort()

# Read the images
images = [Image.open(img) for img in image_files]

# Create a figure
fig, axes = plt.subplots(2, 3, figsize=(15, 10))  # 2 rows, 3 columns

# Loop through the axes and images
for ax, img, fname in zip(axes.flatten(), images, image_files):
    ax.imshow(img)
    ax.axis("off")  # Remove axes
    ax.set_title(os.path.basename(fname).replace('.png','').replace('_',' ').capitalize())  # Set title as file name

# Hide any unused axes (if fewer images than grid spaces)
for ax in axes.flatten()[len(images):]:
    ax.axis("off")

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig(output_file, dpi=300)
plt.show()

print(f"Figure saved as {output_file}")