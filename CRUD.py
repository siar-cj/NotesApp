import os
import saving
import json
notes_directory = saving.returnnotesdirectory()
config_directory = saving.returnconfigdirectory()
directory = saving.returndirectory()


def ask_for_info():
    filename = input("Enter header:").strip()
    subject = input("Enter subject:")
    other_info = input("enter additional info")
    content = input("content: ")
    return filename, subject, other_info, content


def create(filename, subject, other_info, content):
    new_file = os.path.join(notes_directory,filename+".txt")
    new_jsonfile =os.path.join(config_directory,filename+".json")
    a = {}
    content  = input()
    a[filename] = [subject,other_info]
    json.dump(a,new_jsonfile)
    text_file = open(new_file,"w")
    text_file.write(content)
    text_file.close()


def read():
    files = os.listdir(notes_directory)
    for i in files:
        print(i)
    open_note = input()  
    directory = os.path.join()
    with open(directory) as f:
        print(f.read())


def update(filename = input("Enter note to be updated:").strip()):
    
    if saving.check_notes_exists(filename):
        f = open(filename,'a+')
        content = input()
        f.write(content)
        f.close()
    else:
        print("NO such file exists")


def delete(filename = input("Enter note to be updated:").strip()):
    if saving.check_notes_exists(filename):
        os.remove(f'{notes_directory}+{filename}+".txt"')
        os.remove(f'{config_directory}+{filename}+".json"')
        return True
    else:
        print("No such directory exists")
        return False 
