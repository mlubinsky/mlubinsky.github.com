### 2 images per pdf page: ChatGPT
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


Note:

If the aspect ratio of the image is different from the space allocated (img_width and img_height), the image will be stretched or squished to fit exactly.
If you want to maintain the aspect ratio of the images, you may need to compute the dimensions manually and adjust either the width or height accordingly.

Here’s a small adjustment to preserve the aspect ratio of the images:

Adjusted Code (Preserve Aspect Ratio):
python
Copy code
def create_pdf_with_images(folder_path, output_pdf):
    # Get all PNG files in the folder
    image_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    
    # Sort image files to maintain a consistent order
    image_files.sort()

    # Create a canvas for the PDF
    c = canvas.Canvas(output_pdf, pagesize=landscape(letter))
    
    # Define some dimensions
    page_width, page_height = landscape(letter)
    x_offset = inch  # Start with a 1 inch margin from the left
    y_positions = [page_height / 2 + 0.5 * inch, inch]  # Top and bottom y positions for the images

    for i, image_file in enumerate(image_files):
        # Get the full path of the image file
        img_path = os.path.join(folder_path, image_file)
        
        # Load the image to get its size
        img = ImageReader(img_path)
        img_width_orig, img_height_orig = img.getSize()
        
        # Calculate scaling factor to maintain aspect ratio
        scale_factor_width = (page_width / 2 - 2 * inch) / img_width_orig
        scale_factor_height = (page_height / 2 - 2 * inch) / img_height_orig
        scale_factor = min(scale_factor_width, scale_factor_height)

        # Adjusted image size preserving aspect ratio
        img_width = img_width_orig * scale_factor
        img_height = img_height_orig * scale_factor
        
        # Calculate the position of the image (two images per page)
        column = i % 2
        x_position = x_offset + column * (page_width / 2)
        row = i % 2  # Use row position for positioning
        y_position = y_positions[row]

        # Add image filename on top of the image
        c.setFont("Helvetica-Bold", 12)
        c.drawString(x_position, y_position + img_height + 0.25 * inch, image_file)

        # Add the image with the adjusted size
        c.drawImage(img, x_position, y_position, width=img_width, height=img_height)

        # Every two images, create a new page
        if (i + 1) % 2 == 0 or i == len(image_files) - 1:
            c.showPage()  # Add a new page

    # Save the PDF
    c.save()

Changes:
Aspect Ratio Preservation: T
he image is resized based on a scale_factor, which ensures the image maintains its original aspect ratio while still fitting within the allocated space.
```
### 2 images per pdf page: Gemini
```
No, the code does not resize the images to fit the PDF horizontally and vertically. 
The images are set to a fixed width and height of 4 inches. 
If the images are larger than this size, they will be cropped. 
If they are smaller, they will be displayed at their original size.
 
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(images_folder, output_pdf):
    doc = SimpleDocTemplate(output_pdf, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    images = [f for f in os.listdir(images_folder) if f.endswith('.png')]

    for i in range(0, len(images), 2):
        img1 = Image(images[i], width=inch * 4, height=inch * 4)
        img2 = Image(images[i+1], width=inch * 4, height=inch * 4)

        story.append(Paragraph(images[i], styles['Heading3']))
        story.append(img1)
        story.append(Spacer(1, inch * 0.5))

        story.append(Paragraph(images[i+1], styles['Heading3']))
        story.append(img2)
        story.append(Spacer(1, inch * 0.5))

        story.append(PageBreak())

    doc.build(story)

if __name__ == '__main__':
    images_folder = 'images'
    output_pdf = 'images.pdf'
    create_pdf(images_folder, output_pdf)


Here is an example of how to resize the images to fit the PDF:

Python
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate,   
 Image, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet   


def create_pdf(images_folder, output_pdf):
    doc = SimpleDocTemplate(output_pdf, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    images = [f for f in os.listdir(images_folder) if f.endswith('.png')]

    for i in range(0, len(images), 2):
        img1 = Image(images[i], width=inch * 4, height=inch * 4)
        img2 = Image(images[i+1], width=inch * 4, height=inch * 4)

        # Resize the images to fit the PDF horizontally and vertically
        img1.wrap(inch * 4, inch * 4)
        img2.wrap(inch * 4, inch * 4)

        story.append(Paragraph(images[i], styles['Heading3']))
        story.append(img1)
        story.append(Spacer(1, inch * 0.5))

        story.append(Paragraph(images[i+1], styles['Heading3']))
        story.append(img2)
        story.append(Spacer(1, inch * 0.5))

        story.append(PageBreak())

    doc.build(story)

if __name__ == '__main__':
    images_folder = 'images'
    output_pdf = 'images.pdf'
    create_pdf(images_folder, output_pdf)
```
