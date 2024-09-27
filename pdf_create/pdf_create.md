### 2 images per pdf page
```
import os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import inch

def create_pdf_with_images(folder_path, output_pdf):
    # Get all PNG files in the folder
    image_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    
    # Sort image files to maintain a consistent order
    image_files.sort()

    # Create a canvas for the PDF
    c = canvas.Canvas(output_pdf, pagesize=landscape(letter))
    
    # Define some dimensions
    page_width, page_height = landscape(letter)
    img_width = page_width / 2 - 2 * inch  # Half of the page width with some margins
    img_height = page_height / 2 - 2 * inch  # Adjust the image height as per your preference
    
    x_offset = inch  # Start with a 1 inch margin from the left
    y_positions = [page_height / 2 + 0.5 * inch, inch]  # Top and bottom y positions for the images
    
    for i, image_file in enumerate(image_files):
        # Get the full path of the image file
        img_path = os.path.join(folder_path, image_file)

        # Calculate the position of the image (two images per page)
        column = i % 2
        row = i % 2  # Use row position for positioning

        # Add image filename on top of the image
        x_position = x_offset + column * (img_width + inch)
        y_position = y_positions[row] + img_height + 0.25 * inch
        c.setFont("Helvetica-Bold", 12)
        c.drawString(x_position, y_position, image_file)

        # Add the image
        c.drawImage(ImageReader(img_path), x_position, y_positions[row], width=img_width, height=img_height)

        # Every two images, create a new page
        if (i + 1) % 2 == 0 or i == len(image_files) - 1:
            c.showPage()  # Add a new page

    # Save the PDF
    c.save()

# Example usage
folder_path = 'path_to_your_images_folder'
output_pdf = 'output_images.pdf'
create_pdf_with_images(folder_path, output_pdf)


```
