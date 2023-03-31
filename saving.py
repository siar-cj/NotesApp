import os
import logging

# Configure the logging module
def create_logger():
    try:
        # Create a log file in the saving directory
        with open(a:=os.path.join(return_saving_dir(), 'notesapp.log'), 'x'):
            pass  # create the file if it doesn't exist
        # Set up the logging module to use the log file
        logging.basicConfig(filename=a, level=logging.INFO)
    except OSError as e:
        logging.error(f"{e}: occurred while creating logger")

def check_access():
    try:
        # Check if the saving directory, config directory, notes directory, and notes files exist
        create_saving_dir()
        create_logger()
        if configdir_exists() and notesdir_exists() and check_notes_exists():
            # If they do, return True
            return True
        else:
            # If they don't, create the config and notes directories and return True
            print('creating notes and config directories')
            create_configdir()
            create_notesdir()
            return True
    except OSError as e:
        logging.error(f"{e}: occurred while checking access")

def create_saving_dir():
    try:
        # Check if the saving directory exists, and create it if it doesn't
        if not os.path.exists(return_saving_dir()):
            os.mkdir(return_saving_dir())
            return True
        else:
            return False
    except OSError as e:
        logging.error(f"{e}: occurred while creating saving directory")

def saving_dir_exists():
    try:
        # Check if the saving directory exists
        return os.path.exists(return_saving_dir())
    except OSError as e:
        logging.error(f"{e}: occurred while checking saving directory")

def configdir_exists():
    try:
        # Check if the config directory exists
        return os.path.exists(return_configdir())
    except OSError as e:
        logging.error(f"{e}: occurred while checking config directory")
        return False

def notesdir_exists():
    try:
        # Check if the notes directory exists
        return os.path.exists(return_notesdir())
    except OSError as e:
        logging.error(f"{e}: occurred while checking notes directory")
        return False

def create_configdir():
    try:
        # Create the config directory
        os.mkdir(return_configdir())
    except OSError as e:
        logging.error(f"{e}: occurred while creating config directory")

def return_configdir():
    # Return the path to the config directory in the saving directory
    return os.path.join(return_saving_dir(), 'CONFIGURATION')

def return_notesdir():
    # Return the path to the notes directory in the saving directory
    return os.path.join(return_saving_dir(), 'NOTES')

def return_saving_dir():
    # Return the path to the saving directory in the current working directory
    return os.path.join(os.getcwd(), 'SAVING')

def return_logger():
    # Return the path to the logger file in the current working directory
    return os.path.join(return_saving_dir(), 'notesapp.log')
    

def create_notesdir():
    try:
        # Create the notes directory
        os.mkdir(return_notesdir())
    except OSError as e:
        logging.error(f"{e}: occurred while creating notes directory")

def check_notes_exists():
    try:
        # Get a list of note file names from the notes directory and the config directory,
        # and check if they have the same set of names
        notes_files = [os.path.splitext(os.path.basename(f))[0] for f in os.listdir(return_notesdir())]
        config_files = [os.path.splitext(os.path.basename(f))[0] for f in os.listdir(return_configdir())]
        if set(notes_files) == set(config_files):
            return True
    except OSError as e:
        logging.error(f"{e}:occurred while checking notes existence")
