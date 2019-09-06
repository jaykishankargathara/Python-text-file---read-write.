import os

def createfolder(directory):

    try:
        if not os.path.exists('E:\Python\Folder_Created'):
            os.makedirs('E:\Python\Folder_Created')

    except OSError:
        print('Error: Creating directory' + 'E:\Python\Folder_Created')

createfolder('')