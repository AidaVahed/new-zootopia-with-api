import json


def load_data(file_path):
    """Loads a JSON file from the given file path."""
    with open(file_path, "r") as handle:
        return json.load(handle)


with open('animals_template.html', 'r') as template_file:
    """Reads the HTML template file."""
    html_template = template_file.read()

animals_data = load_data('animals_data.json')

output = ''

for animal in animals_data:
    animal_info = '<li class="cards__item">'

    if 'name' in animal:
        animal_info += f"Name: {animal['name']}<br/>\n"

    if 'characteristics' in animal and 'diet' in animal['characteristics']:
        animal_info += f"Diet: {animal['characteristics']['diet']}<br/>\n"

    if 'locations' in animal and len(animal['locations']) > 0:
        animal_info += f"Location: {animal['locations'][0]}<br/>\n"

    if 'taxonomy' in animal and 'order' in animal['taxonomy']:
        animal_info += f"Type: {animal['taxonomy']['order']}<br/>\n"

    animal_info += '</li>'
    output += animal_info

final_html = html_template.replace('__REPLACE_ANIMALS_INFO__', output)

with open('animals.html', 'w') as html_file:
    """Writes the generated HTML content to a new file."""
    html_file.write(final_html)

print("HTML file generated successfully: animals.html")
