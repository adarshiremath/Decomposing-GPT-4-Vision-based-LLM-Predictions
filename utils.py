import pandas as pd
import base64

# Function to get the row values from the CSV file
def get_row_values(file_name):
    # Load the CSV file as a DataFrame
    df = pd.read_csv('./DL_info.csv')

    # Find the row with the given file_name
    row = df[df['File_name'] == file_name]

    # Convert the row values to a dictionary
    row_dict = row.to_dict('records')[0]

    return row_dict

# Function to encode the image as base64
def encode_image(image_path):
  image_64 = base64.b64encode(image_path).decode('utf-8')
  image_64 = "data:image/png;base64," + image_64
  return image_64

def get_ground_truth_type(type):
   lesion_type_mapping = {
        1: 'Bone',
        2: 'Abdomen',
        3: 'Mediastinum',
        4: 'Liver',
        5: 'Lung',
        6: 'Kidney',
        7: 'Soft tissue',
        8: 'Pelvis'
    }
   return lesion_type_mapping[type]