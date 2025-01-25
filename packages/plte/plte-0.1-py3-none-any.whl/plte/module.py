import os

def load_data(filename):
    # Get the path to the file relative to the current script location
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # plte directory
    data_path = os.path.join(base_dir, 'data', filename)
    
    # Open and read the file
    with open(data_path, 'r') as file:
        data = file.read()
    
    return data
