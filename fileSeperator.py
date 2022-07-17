import os,shutil
import types

audioExtensions = ('.mp3','.m4a','.wav','.flac')
imageExtensions = ('.jpeg','.jpg','.png','.svg','.gif')
videoExtensions = ('.mp4','.mkv','.MKV','.flv','.mpeg')
documentExtensions = ('.doc','.pages','.pdf','.txt')
sourceCodeExtensions = ('.cpp','.c','.py','.java','.html','.css')

# Taking folderPath as an input from the user
folderPath = input("Enter the path of the folder:\n")

# function returning all the files with the same types
def fileFinder(folder_path,file_extensions):
    files = []
    for file in os.listdir(folder_path):
        for extension in file_extensions:
            if file.endswith(extension):
                files.append(file)
    return files

print(fileFinder(folderPath,imageExtensions))