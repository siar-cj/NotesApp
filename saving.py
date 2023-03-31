import os
import json
import saving
import logging
notes_dir = saving.return_notesdir()
config_dir = saving.return_configdir()
main_menu = main.menu()
logger = saving.return_logger
logging.basicConfig(filename=logger, level=logging.INFO)
    
    

def get_note_info_from_user():
    filename = input("Enter header:").strip()
    subject = input("Enter subject:")
    other_info = input("enter additional info")
    content = input("content: ")
    return filename, subject, other_info, content



def create_note():
    filename,subject,other_info,content = get_note_info_from_user()
    new_file = os.path.join(notes_dir, filename+'.txt')
    new_json_file = os.path.join(config_dir, filename+'.json')
    a = {}
    a[filename] = [subject, other_info]
    try:
        try:
            with open(new_json_file, 'w') as f:
                json.dump(a,f)
        except TypeError as f:
            logging.error(f"An error occurred while encoding data to JSON: {f}")
            main_menu
        try:
            with open(new_file, "w") as f:
                f.write(content)
        except TypeError as f:
            logging.error(f"An error occurred while encoding data to text file: {f}")
            main_menu
   except OSError as e:
        logging.error(f"{e}: occurred while creating note ")
        main_menu
    
    
def read_notes():
    files = os.listdir(notes_dir)
    for i in files:
        print(i)
    open_note = input("enter note title to be read")
    c = 3
    while not os.path.exists(os.path.join(notes_dir, f'{open_note}.txt') and not os.path.join(notes_dir, f'{open_note}.json'))and c>=0:
         open_note = input("enter note title to be read")
         c-=1
    else:
        directory = os.path.join(notes_dir, open_note+'.txt')
        try:
            with open(directory) as f:
                print((f.read()))
        except OSError as f:
            logging.error(f'{f},went wrong try again.')
    main_menu
    

def update_note(filename,content):
    c = 3
    while not filename or not os.path.exists(os.path.join(notes_dir,filename+'.txt')or not os.path.join(notes_dir,f'{filename}'+'.json'))and c>=0:
        filename = input("Enter note to be updated:").strip()
        c-=1
    else:
        file_path = os.path.join(notes_dir,filename+'.txt') 
        try:
            with open(file_path,"a") as f:
                f.write('\n'+content)
        except OSError as f:
            logging.error(f'{f},went wrong try again.')
    main_menu
    

def delete_note(filename=None):
    c = 3
    while not filename or not os.path.exists(os.path.join(notes_dir,filename+'.txt')or not os.path.join(notes_dir,f'{filename}'+'.json')) and c>=0:
        filename = input("Enter note to be deleted:").strip()
        c-=1
    else:
        file_path = os.path.join(notes_dir,filename+'.txt')
        file_path1 =  os.path.join(notes_dir,filename+'.json')  
        try:
            os.remove(file_path)
            os.remove(file_path1)
            print('files removed')
        except OSError as f:
            logging.error(f'{f},went wrong try again.')
    main_menu
