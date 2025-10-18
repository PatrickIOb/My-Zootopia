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
    output += '<li class="cards__item">\n'

    # --- Title (Name) ---
    if 'name' in animal_data:
        output += f'  <div class="card__title">{animal_data["name"]}</div>\n'

    # --- Text section ---
    output += '  <p class="card__text">\n'

    # Characteristics might not exist
    if 'characteristics' in animal_data:
        characteristics = animal_data['characteristics']

        if 'diet' in characteristics:
            output += f'      <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'
        if 'type' in characteristics:
            output += f'      <strong>Type:</strong> {characteristics["type"]}<br/>\n'

    # Locations might not exist or be empty
    if 'locations' in animal_data and animal_data['locations']:
        locations = ", ".join(animal_data['locations'])
        output += f'      <strong>Location:</strong> {locations}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n\n'  # end of one card




# Replace the placeholder in the template
new_html = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

# Write the new HTML content to a new file
with open("animals.html", "w") as output_file:
    output_file.write(new_html)
