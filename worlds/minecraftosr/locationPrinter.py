import json

def load_data_file(file_path: str) -> dict:
    # Load the JSON data directly from a file on disk
    with open(file_path, "r") as file:
        return json.load(file)

location_id_offset: int = 42000

# Load the locations.json file (make sure it's in the correct path)
location_info = load_data_file("data/locations.json")

# Create a dictionary that maps location names to ids
location_name_to_id = {name: location_id_offset + index for index, name in enumerate(location_info["all_locations"])}

# Open the file for writing
with open("locations.txt", "w") as file:
    for name, index in location_name_to_id.items():
        # Write each location to the file in the desired format
        file.write(f'put("{name}", {index}L);\n')
