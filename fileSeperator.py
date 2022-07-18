import os,shutil
import types

DictExtensions = {
    'audio_Extensions' : ('.mp3','.m4a','.wav','.flac'),
    'image_Extensions' : ('.jpeg','.jpg','.png','.svg','.gif','.ai'),
    'video_Extensions' : ('.mp4','.mkv','.MKV','.flv','.mpeg'),
    'document_Extensions' : ('.doc','.pages','.pdf','.txt'),
    'sourceCode_Extensions' : ('.cpp','.c','.py','.java','.html','.css'),
    'dmg_Extensions' : ('.dmg'),
    'other_Extensions' : ('.rar','.zip','.download','.tar'),
}


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

for extensiontypes, typeTuple in DictExtensions.items():
    folder_name = extensiontypes.split('_')[0] + 'Files'
    folder_path = os.path.join(folderPath,folder_name)
    if os.path.exists(folder_path):
        pass
    else:
        os.mkdir(folder_path)
    
    myItems = fileFinder(folderPath,typeTuple)
    
    if myItems == []:
        try:
            os.rmdir(folder_path)
        except:
            pass
    else:
        for item in myItems:
            item_path = os.path.join(folderPath,item)
            new_item_path = os.path.join(folder_path,item)
            shutil.move(item_path,new_item_path)