import os
import json
import saving
from logger import log_decorator

# Define the directories and menu
notes_dir = saving.return_notesdir()
config_dir = saving.return_configdir()
@log_decorator
# Define function to get note information from user
def get_note_info_from_user():
    filename = input("Enter header:").strip()
    subject = input("Enter subject:")
    other_info = input("enter additional info")
    content = input("content: ")
    return filename, subject, other_info, content
@log_decorator
# Define function to create a new note
def create_note():
    # Get note information from user
    filename, subject, other_info, content = get_note_info_from_user()
    
    # Define paths for new files
    new_file = os.path.join(notes_dir, filename+'.txt')
    new_json_file = os.path.join(config_dir, filename+'.json')
    
    # Create dictionary with note information
    a = {}
    a[filename] = [subject, other_info]
    
    # Write note information to JSON file
    with open(new_json_file, 'w') as f:
                json.dump(a,f)
                
        # Write note content to text file
    with open(new_file, "w") as f:
                f.write(content)
                
 
        
        
@log_decorator    
# Define function to read notes
def read_notes():
    # List all notes
    files = os.listdir(notes_dir)
    for i in files:
        print(i)
    # Get note to be read from user
    open_note = input("enter note title to be read")
    c = 3
    # Check if note exists, allow 3 attempts
    while not os.path.exists(os.path.join(notes_dir, f'{open_note}.txt') and not os.path.join(notes_dir, f'{open_note}.json'))and c>=0:
         open_note = input("enter note title to be read")
         c-=1
    else:
        directory = os.path.join(notes_dir, open_note+'.txt')
        # Read note content from text file
        with open(directory) as f:
                print((f.read()))
        
    
@log_decorator    
# Define function to update a note
def update_note(filename,content):
    c = 3
    # Check if note exists, allow 3 attempts
    while not filename or not os.path.exists(os.path.join(notes_dir,filename+'.txt')or not os.path.join(notes_dir,f'{filename}'+'.json'))and c>=0:
        filename = input("Enter note to be updated:").strip()
        c-=1
    else:
        file_path = os.path.join(notes_dir,filename+'.txt') 
        # Append new content to existing note
        with open(file_path,"a") as f:
                f.write('\n'+content)
        
    
@log_decorator   
# Define function to delete a note
def delete_note(filename=None):
    c = 3
     # Check if note exists, allow 3 attempts
    while not filename or not os.path.exists(os.path.join(notes_dir,filename+'.txt')or not os.path.join(notes_dir,f'{filename}'+'.json')) and c>=0:
        filename = input("Enter note to be deleted:").strip()
        c-=1
    else:
        file_path = os.path.join(notes_dir,filename+'.txt')
        file_path1 =  os.path.join(notes_dir,filename+'.json')  
        #delete config and text file
        os.remove(file_path)
        os.remove(file_path1)
        print('files removed')
        
    

