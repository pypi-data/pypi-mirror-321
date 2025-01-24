from PIL import Image

# Define constants for the photo size
PASSPORT_PHOTO_SIZE_INCHES = (2, 2)  # Passport photo size in inches
PHOTO_PRINT_SIZE_INCHES = (4, 6)     # Standard photo print size in inches
DPI = 300  # Resolution in dots per inch

# Function to create a passport photo layout
def create_passport_photo_layout(input_photo_path, output_path):
    # Open the input passport photo
    passport_photo = Image.open(input_photo_path)

    # # Resize the passport photo to 2x2 inches at 300 DPI
    # passport_photo = passport_photo.resize((PASSPORT_PHOTO_SIZE_INCHES[0] * DPI,
    #                                         PASSPORT_PHOTO_SIZE_INCHES[1] * DPI))

    # Create a blank 4x6 inch image to arrange the passport photos
    photo_print = Image.new('RGB', (PHOTO_PRINT_SIZE_INCHES[0] * DPI, PHOTO_PRINT_SIZE_INCHES[1] * DPI), (255, 255, 255))

    # Arrange passport photos on the 4x6 layout (fits 6 photos: 3 rows of 2)
    for row in range(3):
        for col in range(2):
            x_offset = col * PASSPORT_PHOTO_SIZE_INCHES[0] * DPI
            y_offset = row * PASSPORT_PHOTO_SIZE_INCHES[1] * DPI
            photo_print.paste(passport_photo, (int(x_offset), int(y_offset)))

    # Save the final image for printing at the store
    photo_print.save(output_path, format="JPEG")

# Example usage:
input_photo_path = '/Users/chenyang/Downloads/Chen_passport_photo.jpg'  # Path to your passport photo file
output_path = 'chen_passport_print_layout.jpg'  # Output file for printing

create_passport_photo_layout(input_photo_path, output_path)