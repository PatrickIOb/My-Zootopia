import json

# Read the JSON file
with open("animals_data.json", "r") as json_file:
    data = json.load(json_file)

# Read the HTML template
with open("animals_template.html", "r") as html_file:
    template_content = html_file.read()

# Build the output string
output = ''  # define an empty string

for animal_data in data:
    # Name
    if 'name' in animal_data:
        output += f"Name: {animal_data['name']}\n"

    # Characteristics might not exist
    if 'characteristics' in animal_data:
        characteristics = animal_data['characteristics']

        if 'diet' in characteristics:
            output += f"Diet: {characteristics['diet']}\n"
        if 'type' in characteristics:
            output += f"Type: {characteristics['type']}\n"

    # Locations might not exist or be empty
    if 'locations' in animal_data and animal_data['locations']:
        locations = ", ".join(animal_data['locations'])
        output += f"Location: {locations}\n"

    # Add a blank line between animals
    output += "\n"


# Replace the placeholder in the template
new_html = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

# Write the new HTML content to a new file
with open("animals.html", "w") as output_file:
    output_file.write(new_html)
