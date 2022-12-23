import os
def check_access():
   #check if config file directory and notes directory exists, if it doesnt create respectively and return true
  if configdir_exists() and Notesdir_exists() and check_notes_exists:
    return True
  else:
    create_configdir()
    create_notesdir()
    return True
       

def saving_dir():
  if not os.path.exists(f'{os.getcwd()}'+'Saving'):
    os.mkdir(os.path.join(f'{os.getcwd()}','Saving'))
  return True  


def configdir_exists():
     if os.path.exists(return_configdir()):
      return True


def Notesdir_exists():
  if os.path.exists(return_configdir()):
      return True
  else:
    return False    
     #check if notes dir exists


def create_configdir():
  os.mkdir(os.path.join(f'{os.getcwd()}'+'SAVING','CONFIGURATION'))
    #make config directory


def create_notesdir():
  os.mkdir(os.path.join(f'{os.getcwd()}','SAVING','NOTES'))
    #make notes config dir


def check_notes_exists():
  #returns true if both note file and respective json file exists
  configdir = []
  notesdir = []
  for  files in os.walk(return_notesdir()):
    for i in files:
      configdir.append(os.path.splitext(os.path.join(f'{return_notesdir()}',i))[0])
  
  for files in os.walk(return_configdir()):
    for i in files:
      notesdir.append(os.path.splitext(os.path.join(f'{return_configdir()}',i))[0])    
  if set(configdir)== set(notesdir):
    return True

  

    

def return_configdir():
  return os.path.join(f'{os.getcwd()}','SAVING','CONFIGURATION')
    

def return_notesdir():
  #returns notes directory
  return os.path.join(f'{os.getcwd()}','SAVING','NOTES')
    

