### Find the folder, where script is located
``` 
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the folder under the script's location
d = "IMG"
folder_path = os.path.join(script_dir, d)
os.makedirs(folder_path)

# Print the full path of the created folder
print(f'Folder created at: {folder_path}')
```

#### Space in file name
```
If the image file name contains spaces, it can cause issues with embedding images in HTML emails, as spaces in cid references or URLs aren't properly handled. To fix this, you need to replace spaces in file names with characters that HTML can interpret correctly, such as %20 (the URL encoding for a space), or simply remove the spaces.

Solution:
Replace spaces in file names with underscores or another suitable character before using them in the HTML body and Content-ID.
Here’s how you can update the code to handle file names with spaces:

Updated Code:
python
Copy code
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Create the main message container
msg = MIMEMultipart('related')

# Create the HTML body with image references
html = '<html><body>'
for f in image_files:
    fname = os.path.basename(f)
    # Replace spaces with underscores or URL encoding (%20)
    fname_clean = fname.replace(' ', '_')
    html += f'<p><img src="cid:{fname_clean}" alt="{fname_clean}" style="max-width:500px;"></p>'
html += '</body></html>'

# Attach the HTML part to the message
html_added = f'<pre>{text}<br></pre>{html}'
part_html = MIMEText(html_added, 'html')
msg.attach(part_html)

# Attach the images as inline content
for f in image_files:
    fname = os.path.basename(f)
    fname_clean = fname.replace(' ', '_')  # Clean the file name (replace spaces)
    
    print(f'attaching {os.path.normpath(f)}')
    with open(f, "rb") as fil:
        img_data = fil.read()
    
    # Create the image MIME part
    image_part = MIMEImage(img_data, name=fname_clean)
    
    # Set the Content-ID to reference it in the HTML (use cleaned file name)
    image_part.add_header('Content-ID', f'<{fname_clean}>')
    
    # Set Content-Disposition to inline (optional, but clarifies intent)
    image_part.add_header('Content-Disposition', 'inline', filename=fname_clean)
    
    # Attach the image to the email
    msg.attach(image_part)
Key Adjustments:
Replace spaces in the file name using fname_clean = fname.replace(' ', '_') (or you can use %20 for URL encoding).
This avoids issues with spaces in cid references.
Use the cleaned file name both in the src of the HTML and the Content-ID header.
Explanation:
Spaces in the cid: references need to be replaced or escaped because they break the URL-like format required by HTML.
By replacing spaces with underscores (or another character), you ensure the image reference works correctly without spaces causing broken links.
This should resolve the issue with spaces in file names causing broken image links in your email. Let me know how it works!
```



### Issue: image in html body
```
I am using Python   to send e-mail with html body.
There are images which need to be inside html body.
My current code creates html body 
and it send e-mail with attached images, but the images are not displayed inside the html body,
Please fix it.

           html = '<html><body>'
           for f in image_files:
                fname = os.path.basename(f)
                html += f'<p><img src="cid:{fname}" alt="{fname}" style="max-width:500px;"></p>'
           html += '</body></html>'

            for f in image_files:
                print(f'attaching {os.path.normpath(f)}')
                with open(f, "rb") as fil:
                    part = MIMEApplication(
                        fil.read(),
                        Name=os.path.basename(f)
                    )
                part['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(f)
                part['Content-ID'] = os.path.basename(f)
                msg.attach(part)

            html_added = f'<pre>{text}<br></pre>{html}'
            part_html = MIMEText(html_added, 'html')
            msg.attach(part_html)
```

```
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os

# Define your dictionaries
d1 = {
    'item1': {'key1': 'value1', 'key2': 'value2'},
    'item2': {'key3': 'value3', 'key4': 'value4'},
    # Add more items if needed
}

# Folder containing the PNG images
image_folder = '/path/to/image/folder'

# Function to generate an HTML table from a dictionary
def generate_table(d2):
    table_html = '<table border="1" style="border-collapse: collapse;">'
    table_html += '<tr><th>Key</th><th>Value</th></tr>'
    for k, v in d2.items():
        table_html += f'<tr><td>{k}</td><td>{v}</td></tr>'
    table_html += '</table>'
    return table_html

# Function to generate the HTML body of the email
def generate_email_body(d1):
    body_html = '<html><body>'
    
    for key, d2 in d1.items():
        # Add the key as a heading
        body_html += f'<h2>{key}</h2>'
        
        # Add the table for d2
        body_html += generate_table(d2)
        
        # Add the corresponding image
        image_path = os.path.join(image_folder, f'{key}.png')
        if os.path.exists(image_path):
            body_html += f'<p><img src="cid:{key}" alt="{key}" style="max-width:500px;"></p>'
        else:
            body_html += f'<p><strong>Image not found for {key}</strong></p>'
    
    body_html += '</body></html>'
    return body_html

# Email setup
sender_email = 'your_email@example.com'
receiver_email = 'recipient@example.com'
subject = 'Email with Dictionary Data and Images'

# Create the email message object
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the HTML body to the email
email_body = generate_email_body(d1)
msg.attach(MIMEText(email_body, 'html'))

# Attach the images from the dictionary keys
for key in d1.keys():
    image_path = os.path.join(image_folder, f'{key}.png')
    if os.path.exists(image_path):
        with open(image_path, 'rb') as img_file:
            img = MIMEImage(img_file.read())
            img.add_header('Content-ID', f'<{key}>')  # This ID is referenced in the email body
            msg.attach(img)

# Sending the email
try:
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(sender_email, 'your_password')
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print('Email sent successfully!')
except Exception as e:
    print(f'Error: {e}')

```

### FIX
```
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Create the main message container
msg = MIMEMultipart('related')

# Create the HTML body with image references
html = '<html><body>'
for f in image_files:
    fname = os.path.basename(f)
    html += f'<p><img src="cid:{fname}" alt="{fname}" style="max-width:500px;"></p>'
html += '</body></html>'

# Attach the HTML part to the message
html_added = f'<pre>{text}<br></pre>{html}'
part_html = MIMEText(html_added, 'html')
msg.attach(part_html)

# Attach the images as inline content
for f in image_files:
    fname = os.path.basename(f)
    print(f'attaching {os.path.normpath(f)}')
    with open(f, "rb") as fil:
        img_data = fil.read()
    
    # Create the image MIME part
    image_part = MIMEImage(img_data, name=fname)
    
    # Set the Content-ID to reference it in the HTML (cid)
    image_part.add_header('Content-ID', f'<{fname}>')
    image_part.add_header('Content-Disposition', 'inline', filename=fname)
    
    # Attach the image to the email
    msg.attach(image_part)



Key Changes:
-------------
MIMEImage is used instead of MIMEApplication for image files.
This is necessary to ensure the images are recognized as inline content.
Content-ID and Content-Disposition** headers**:
Content-ID is used to embed the images in the HTML by using the cid: reference.
Content-Disposition is set to 'inline' to ensure the image is displayed in the body rather than as an attachment.
Order of attaching:
The HTML part is attached first, and the images are attached after to ensure the references match.

Example:
If you have an image called image1.jpg, the HTML will include:

 
<img src="cid:image1.jpg" alt="image1.jpg" style="max-width:500px;">
```
