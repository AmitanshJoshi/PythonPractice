import os

# fileData = open("demo.txt")
# print(fileData.read())
# fileData.close()

#Always close the file as buffer may not save the latest changes

# fileData = open("demo.txt", "w")
# fileData.write("Overwritten the entire data present in the file")
# fileData = open("demo.txt","r")
# print(fileData.read())
# fileData.close()



# fileData = open("demo.txt","r")
# print(fileData.read())
# fileData.close()

# try:
#     fileData = open("Newfile.txt","x")
#     fileData = open("Newfile.txt", "w")
#     fileData.write("Added the data to the file")
#     fileData = open("Newfile.txt", "r")
#     print(fileData.read())
#
# except:
#     print("File already exist")
#
# try:
#     if os.path.exists("demo.txt"):
#         os.remove("demo.txt")
# except:
#     print("the file does not exist in the machine")


# try:
#     if os.path.exists("CheckDeleteFolder"):
#         os.rmdir("CheckDeleteFolder")
#
# except:
#     print("the directory with the name does not exist")

# os.remove("Newfile.txt")