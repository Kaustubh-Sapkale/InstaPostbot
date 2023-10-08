#library for posting
from instabot import Bot
#library for google sheet reading
import gspread
#library for downloading photo
import io
import os.path
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from PIL import Image , ImageFont , ImageDraw
import time
import os, random
import glob

alph = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
folder_id = '1XUOV4Dwq_nFCqK4iVtwuO1bEX6PfKq3l059oCyv1hen0BYWP9hdqCd9g3Tq1p-QtPV9hSuC6'

# Define the credentials of the Google account with access to the folder
creds = service_account.Credentials.from_service_account_file('token.json')

# Define the service object for interacting with the Google Drive API
service = build('drive', 'v3', credentials=creds)
# Define a function to download photos from Google Drive
def download_photo(file_id, file_name):
    try:
        # Get the file from Google Drive
        file = service.files().get_media(fileId=file_id).execute()
        
        # Open a file-like buffer to write the image data to
        image_data = io.BytesIO(file)
        
        # Open the image using PIL
        image = Image.open(image_data)
        wid, hgt = image.size 
        newsize = (max(wid,hgt) , max(wid , hgt)) 
        im1 = image.resize(newsize) 
        # Save the image to disk
        im1.save(os.path.join('data/photo', file_name))
        
        print(f'Successfully downloaded {file_name}')
        
    except HttpError as error:
        print(f'An error occurred: {error}')
        return None


#some functions
def get_col_num(text , col_name):
    num = 1
    found = 0
    for i in col_name:
        if i == text:
            found = 1
            break
        else:
            num+= 1
    if found:
        return num
    else:
        return 'not found'


def create_for_post(all_data , index):
    col_name = all_data[0]
    curr_data = all_data[index]
    

    name_col_num = get_col_num('Name'  , col_name)
    description_col_num = get_col_num("Description" , col_name)
    photo_col_num = get_col_num("Photo" , col_name)
    insta_handle_col_num = get_col_num("Insta Handle" , col_name)
    print(all_data[index][name_col_num-1])
    #creating caption
    caption_temp = curr_data[description_col_num -1]
    caption_temp = "Name:- " +curr_data[name_col_num - 1] + '\n' + "Insta Handle :- @" +curr_data[insta_handle_col_num - 1] + '\n\n' + caption_temp
    # print(caption_temp)

    #photo
    photo_link = curr_data[photo_col_num-1]
    photo_id = photo_link[photo_link.index("id")+3:]
    # print(photo_id)
    File = service.files().get(fileId=photo_id).execute()
    FileName = File.get("name")
    # print(FileName)

    # FileType = FileName[FileName.index('.')+1:]
    # print(FileType)
    if '.jpg' in FileName or '.jpeg' in FileName or '.JPG' in FileName or '.JPEG' in FileName or'.PNG' in FileName or '.png' in FileName :
        download_photo(photo_id , 'random.jpg')
        bot.upload_photo('data/photo/random.jpg', caption=caption_temp)
        return True
    else:
        print(f"The photo format of {curr_data[name_col_num - 1]} is not in jpg/JPG/JPEG/PNG")
        return False


    

    # os.remove('data/photo/random.jpg')

def photo_caption(worksheet):
    all_value = worksheet.get_all_values()



    #getting column name
    col_name = all_value[0]
    print(col_name)


    #getting column number of is posted 

    posted_col_num = get_col_num('posted'  , col_name)
    print(posted_col_num)

    #iterating through all the responces and checking if already posted or not
    k=1
    print("length of all values are" , len(all_value))
    for i in range(1 ,len(all_value) ):
        print("loop started")
        # print('lats se' , k , ' ' , len(all_value[i]))
        # print(all_value[i][posted_col_num-1])
        k+=1
        if all_value[i][posted_col_num-1] != '1':
            time.sleep(5)
            status = create_for_post(all_data = all_value, index= i)
            if status:
                cell = alph[posted_col_num]+str(i+1)
                print(cell)
                worksheet.update(cell , 1)             
            else:
                cell = alph[posted_col_num]+str(i+1)
                print(cell)
                worksheet.update(cell , 0)
        print("loop ended")
            # print(all_value[i][posted_col_num-1])

# # f = random.choice(os.listdir("./data/2004_Torun"))

if __name__ == "__main__":

    cookie_del = glob.glob("config/*cookie.json")
    if len(cookie_del) > 0:
        os.remove(cookie_del[0])

    bot = Bot()
    
    bot.login(username="username", password="password")

    #loading sheets part
    gs = gspread.service_account(filename= 'token.json')
    worksheet = gs.open('for_learning').get_worksheet(0)
    photo_caption(worksheet)
    #taking inputs
    

