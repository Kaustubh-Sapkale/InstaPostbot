import gspread
import requests
import gdown


url = 'https://drive.google.com/open?id=1nDuzetZyJOoeGIOETP-5exglFzqH6GRc'
output = 'images.jpg'
gdown.download(url,  quiet=False)

# gs = gspread.service_account(filename= 'token.json')
# worksheet = gs.open('for_learning').sheet1

# #taking inputs
# all_value = worksheet.get_all_values()




# def get_col_num(text):
#     num = 1
#     found = 0
#     for i in col_name:
#         if i == text:
#             found = 1
#             break
#         else:
#             num+= 1
#     if found:
#         return num
#     else:
#         return 'not found'


# def create_for_post(all_data , index):
#     print(all_data[index])
    

# #getting column name
# col_name = all_value[0]
# print(col_name)


# #getting column number of is posted 

# posted_col_num = get_col_num('posted')
# print(posted_col_num)

# #iterating through all the responces and checking if already posted or not
# k=1
# for i in range(1 ,len(all_value) ):
#     # print('lats se' , k , ' ' , len(all_value[i]))
#     # print(all_value[i][posted_col_num-1])
#     k+=1
#     if all_value[i][posted_col_num-1] == '':
#         create_for_post(all_data = all_value, index= i)
#         print("do something")
#         # print(all_value[i][posted_col_num-1])
