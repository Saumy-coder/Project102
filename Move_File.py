
import os
import shutil

from_dir = 'C:/Users/saumy/Downloads'
to_dir = "C:/Users/saumy/Documents/"

list_of_files = os.listdir(from_dir)
exten = ['.txt','.doc','docx.','.pdf']
for x in list_of_files:
    name,ext = os.path.splitext(x)
    if ext == '':
        continue
    elif ext in exten:
        path1 = from_dir+'/'+name+ext
        path2 = to_dir+'/'+"Document_Files"
        path3 = path2+'/'+name+ext

        if os.path.exists(path2)==True:
            shutil.move(path1,path3)
        else:
            os.makedirs(to_dir + '/' + "Document_Files")
            shutil.copy(path1,path3)

    