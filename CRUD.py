import os
import json
import saving

notes_dir = saving.returnnotesdirectory()
config_dir = saving.returnconfigdirectory()


def get_note_info_from_user():
    filename = input("Enter header:").strip()
    subject = input("Enter subject:")
    other_info = input("enter additional info")
    content = input("content: ")
    return filename, subject, other_info, content



def create_note(filename, subject, other_info, content):
    new_file = os.path.join(notes_dir, f'{filename}.txt')
    new_json_file = os.path.join(config_dir, f'{filename}.json')
    a = {}
    a[filename] = [subject, other_info]
    try:
        try:
            with open(new_json_file, 'w') as f:
                json.dump(a,f)
        except TypeError as f:
            print(f"An error occurred while encoding data to JSON: {f}")    
        try:
            with open(new_file, "w") as f:
                f.write(content)
        except TypeError as f:
            print(f"An error occurred while encoding data to text file: {f}")
    except OSError as f:
        print(f'{f},went wrong try again.')
    
    


    


def read_notes():
    files = os.listdir(notes_dir)
    for i in files:
        print(i)
    open_note = input("enter note title to be read") 
    while not os.path.exists(os.path.join(notes_dir, f'{open_note}.txt') and not os.path.join(notes_dir, f'{open_note}.json')):
         open_note = input("enter note title to be read") 
    directory = os.path.join(notes_dir, f'{open_note}.txt')
    try:
        with open(directory) as f:
            print(f.read())
    except OSError as f:
        print(f'{f},went wrong try again.')
    


def update_note(filename=None,content):
    while not filename or not os.path.exists(os.path.join(notes_dir,filename+'.txt')or not os.path.join(notes_dir,f'{filename}'+'.json')):
        filename = input("Enter note to be updated:").strip()
    file_path = os.path.join(notes_dir,f'{filename}'+'.txt') 
    try:
        with open(file_path,"a") as f:
            f.write('\n'+content)
    except OSError as f:
        print(f'{f},went wrong try again.')
    

def delete_note(filename=None):
    while not filename or not os.path.exists(os.path.join(notes_dir,filename+'.txt')or not os.path.join(notes_dir,f'{filename}'+'.json')):
        filename = input("Enter note to be deleted:").strip()
    file_path = os.path.join(notes_dir,f'{filename}'+'.txt')
    file_path1 =  os.path.join(notes_dir,f'{filename}'+'.json')  
    try:
        os.remove(file_path)
        os.remove(file_path1)
        print('files removed')
    except OSError as f:
        print(f'{f},went wrong try again.')
