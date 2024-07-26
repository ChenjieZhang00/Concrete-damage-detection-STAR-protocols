import xml.etree.ElementTree as ET
import os


# Function to convert XML to TXT format
def xml_to_txt(xml_file_path, txt_file_path, class_mapping):
    # Parse the XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Get image dimensions
    size = root.find('size')
    width = int(size.find('width').text)
    height = int(size.find('height').text)

    # Open the TXT file for writing
    with open(txt_file_path, 'w') as txt_file:
        # Iterate over each object in the XML
        for obj in root.findall('object'):
            # Get object class and bounding box coordinates
            class_name = obj.find('name').text
            bbox = obj.find('bndbox')
            x_min = int(bbox.find('xmin').text)
            y_min = int(bbox.find('ymin').text)
            x_max = int(bbox.find('xmax').text)
            y_max = int(bbox.find('ymax').text)

            # Compute class ID
            class_id = class_mapping.get(class_name, -1)  # Default to -1 if class not found

            if class_id == -1:
                print(f"Warning: Class '{class_name}' not found in mapping.")
                continue

            # Compute normalized bounding box coordinates
            x_center = (x_min + x_max) / 2 / width
            y_center = (y_min + y_max) / 2 / height
            bbox_width = (x_max - x_min) / width
            bbox_height = (y_max - y_min) / height

            # Write to the TXT file
            txt_file.write(f"{class_id} {x_center} {y_center} {bbox_width} {bbox_height}\n")


# Example usage
if __name__ == "__main__":
    # Define the class mapping (class_name to class_id)
    class_mapping = {
        'person': 0,
        'car': 1,
        'bike': 2,
        # Add more classes as needed
    }

    # Directory containing XML files
    xml_directory = 'path/to/xml_directory'
    txt_directory = 'path/to/txt_directory'

    # Create the TXT directory if it does not exist
    if not os.path.exists(txt_directory):
        os.makedirs(txt_directory)

    # Process each XML file in the directory
    for xml_file_name in os.listdir(xml_directory):
        if xml_file_name.endswith('.xml'):
            xml_file_path = os.path.join(xml_directory, xml_file_name)
            txt_file_name = os.path.splitext(xml_file_name)[0] + '.txt'
            txt_file_path = os.path.join(txt_directory, txt_file_name)
            xml_to_txt(xml_file_path, txt_file_path, class_mapping)
