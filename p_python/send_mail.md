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
