import os
import logging

# Configure the logging module
def create_logger():
    try:

        with open(a:=os.path.join(return_saving_dir(), 'notesapp.log'), 'x'):
            pass  # create the file if it doesn't exist
        logging.basicConfig(filename=a, level=logging.INFO)
    except OSError as e:
        logging.error(f"{e}: occurred while creating logger")

def check_access():
    try:
        create_saving_dir()
        create_logger()
        if configdir_exists() and notesdir_exists() and check_notes_exists():
            return True
        else:
            print('creating notes and config directories')
            create_configdir()
            create_notesdir()
            return True
    except OSError as e:
        logging.error(f"{e}: occurred while checking access")

def create_saving_dir():
    try:
        if not os.path.exists(return_saving_dir()):
            os.mkdir(return_saving_dir())
            return True
        else:
            return False
    except OSError as e:
        logging.error(f"{e}: occurred while creating saving directory")

def saving_dir_exists():
    try:
        return os.path.exists(return_saving_dir())
    except OSError as e:
        logging.error(f"{e}: occurred while checking saving directory")

def configdir_exists():
    try:
        return os.path.exists(return_configdir())
    except OSError as e:
        logging.error(f"{e}: occurred while checking config directory")
        return False

def notesdir_exists():
    try:
        return os.path.exists(return_notesdir())
    except OSError as e:
        logging.error(f"{e}: occurred while checking notes directory")
        return False

def create_configdir():
    try:
        os.mkdir(return_configdir())
    except OSError as e:
        logging.error(f"{e}: occurred while creating config directory")

def return_configdir():
    return os.path.join(return_saving_dir(), 'CONFIGURATION')

def return_notesdir():
    return os.path.join(return_saving_dir(), 'NOTES')

def return_saving_dir():
    return os.path.join(os.getcwd(), 'SAVING')

def create_notesdir():
    try:
        os.mkdir(return_notesdir())
    except OSError as e:
        logging.error(f"{e}: occurred while creating notes directory")

def check_notes_exists():
    try:
        notes_files = [os.path.splitext(os.path.basename(f))[0] for f in os.listdir(return_notesdir())]
        config_files = [os.path.splitext(os.path.basename(f))[0] for f in os.listdir(return_configdir())]
        if set(notes_files) == set(config_files):
            return True
    except OSError as e:
        logging.error(f"{e}: occurred while checking notes existence")
