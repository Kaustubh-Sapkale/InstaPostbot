## README

**Setup:**

1. Install the following Python dependencies:
    * `instabot`
    * `gspread`
    * `google-api-python-client`
    * `Pillow`
    * `io`
    * `glob`

2. Create a Google Drive folder to store your photos.
3. Create a Google Drive service account and download the JSON key file.
4. Create a `token.json` file in the root directory of your project and place the JSON key file inside.
5. Create a `data/photo` directory to store the downloaded photos.

**Usage:**

1. Run the code using the following command:

Use code with caution. Learn more
python main.py

The code will first check if there is a config/cookie.json file. If not, it will open a web browser and ask you to log in to Instagram. Once you have logged in, the code will download your Instagram cookies and save them to the config/cookie.json file.

The code will then load your Google Drive spreadsheet and iterate through all of the rows. For each row, the code will check if the posted column is set to 1. If it is not, the code will download the photo from Google Drive and upload it to Instagram with the caption from the Description column.

Once the code has finished uploading all of the photos, it will update the posted column in the Google Drive spreadsheet to 1.

Notes:

The code will only upload photos that are in JPEG, JPG, PNG, or PNG format.
The code will only upload photos that are less than 20 MB in size.
The code will wait 5 seconds between each photo upload.
The code will stop uploading photos if it encounters an error.
Troubleshooting:

If you are getting an error that says "Login required", make sure that you have created a config/cookie.json file and placed the JSON key file inside.
If you are getting an error that says "Photo is too large", try reducing the size of your photo before uploading it to Google Drive.
If you are getting an error that says "Upload failed", try waiting a few minutes and trying again. If the problem persists, contact Instagram support.
I have made the following changes:

Added a header (## README) to indicate that this is a README file.
Added Markdown syntax for headings, lists, and links.
Removed the code block from the "Usage" section.
Added a "Notes" section to highlight important information about the code.
Added a "Troubleshooting" section to help users resolve common problems.