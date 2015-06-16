import os
def rename_files():
    #get file name from the folder(prank)
    # r is used to tell python to take files as it is
    file_list = os.listdir(r"prank") 
    print(file_list)
    #to check the current directory
    directory = os.getcwd()
    print "current working directory is ",directory
    #change directory
    d= os.chdir("prank")
    print d
    #rename all the file in the folder prank
    for file_name in file_list:
        #translate is used to remove all numbers from filename
        os.rename(file_name,file_name.translate(None,"0123456789"))  
rename_files()
