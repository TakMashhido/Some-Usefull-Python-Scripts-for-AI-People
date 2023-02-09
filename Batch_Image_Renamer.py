import os
import cv2
import glob

path = input("Enter the path to the folder: ") # ask for the path from the user
name_series = input("Enter the name series for the new files: ") # ask for the name series from the user
exts = ['.jpg', '.jpeg', '.png', '.bmp', '.gif'] # list of all the extensions
files = []

# loop through all the extensions
for ext in exts:
    files.extend(glob.glob(os.path.join(path, "*" + ext))) # get all the files with that extension and add it to the list of files

# batch process all the images
for i, image in enumerate(files):
    img = cv2.imread(image)
    new_file = os.path.join(path, name_series + str(i+1) + '.jpg')
    cv2.imwrite(new_file, img) # convert and save the image as .jpg
    os.remove(image) # delete the original file
