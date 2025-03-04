### Change the background color of a panel title in Grafana 
```
To change the background color of a panel title in Grafana from black to blue while keeping the text white,
you can use custom styling options.
Grafana allows some customization through its UI or by applying CSS overrides (depending on your version and setup). Here's how you can achieve this:

Option 1: Through Grafana UI (Limited Customization)
- Edit the Panel:
Open your Grafana dashboard.
Click on the panel title where it currently shows white text on a black background.
Select "Edit" from the dropdown menu.

-  Panel Options:
In the panel editor, go to the "Panel" tab (usually on the right-hand side).
Look for "Panel Title" or "General" settings.

- Custom Styling (if available):
Grafana’s default UI doesn’t directly allow changing the title background color. However, some newer versions (Grafana 8.0+) support "Field Options" or "Panel Styling" where you might find a "Background" or "Color" setting. If you see this, set the background to a blue shade (e.g., #0000FF for pure blue or pick a shade from the color picker).

- Save Changes:
Apply the changes and check if the background updates. If this option isn’t available, proceed to Option 2.

Option 2: Using Custom CSS (Advanced)
---------------------------------
If the UI doesn’t provide a direct way to change the panel title background, you can override it with custom CSS. This requires admin access to your Grafana instance and depends on self-hosting or a setup where you can modify the configuration.

- Locate the Panel Title CSS Class:

 Right-click the panel title in your browser and select "Inspect" (in Chrome/Firefox) to open developer tools.
Look for the HTML element that defines the panel title. It might have a class like .panel-title or .grafana-panel-title (exact class depends on your Grafana version).

- Add Custom CSS:
If you have access to Grafana’s configuration files (e.g., self-hosted setup):
Go to the Grafana installation directory (e.g., /usr/share/grafana/public/ or wherever your instance is hosted).
Find or create a custom CSS file (e.g., custom.css) in the public/css folder.
Alternatively, if your Grafana supports a "Custom Branding" or "Custom CSS" option in the admin settings, use that.

- Apply the Style:
Add the following CSS to change the background to blue while keeping the text white:
 
.panel-title {
    background-color: #0000FF !important; /* Blue background */
    color: #FFFFFF !important; /* White text */
}
Adjust the hex code (#0000FF) to any blue shade you prefer (e.g., #1E90FF for Dodger Blue).

- Restart Grafana:
If you modified files manually, restart the Grafana server to apply changes (e.g., sudo systemctl restart grafana-server on Linux).

- Verify:
Reload your dashboard and check if the panel title now has a blue background.


Notes:
Grafana Version: The exact steps might vary slightly based on your Grafana version (e.g., 9.x, 10.x as of March 2025). Check the documentation for your version if the above doesn’t match.
Permissions: Custom CSS requires admin access. If you’re on a hosted Grafana (e.g., Grafana Cloud) without CSS control, you’re limited to UI options.
Fallback: If neither works, consider using a "Text" panel with HTML/CSS styling as a workaround to mimic a title with your desired colors.
```
