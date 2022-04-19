import os

## Caution!! 
## this file can only run when it is in same dir with the file want to change. 

# fetch all file name in this dir
def get_list():
    all_name = os.listdir()
    # print(all_name)
    return all_name
  
n = 0
# print(get_list())
# make a principle for rename

for i in get_list():
    # path = '1-' + cafeIndex + '-' + str(n) + '.png'
    final_name = 'face_val_' + str(n) + '.png'
    print(i)
    #if the dir includes other files you don't want to change, use if '.png' to pick it up 
    if '.png' in i:          
        #os.rename( before, after )
        os.rename(i , final_name)
        n += 1