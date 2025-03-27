import json


def load_data(file_path):
    """Loads a JSON file from the given file path."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Serializes a single animal object to an HTML string."""
    output = '<li class="cards__item">\n'

    if 'name' in animal_obj:
        output += f'<div class="card__title">{animal_obj["name"]}</div>\n'

    output += '<p class="card__text">\n'

    if 'characteristics' in animal_obj and 'diet' in animal_obj['characteristics']:
        output += f'<strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'

    if 'locations' in animal_obj and len(animal_obj['locations']) > 0:
        output += f'<strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'

    if 'taxonomy' in animal_obj and 'order' in animal_obj['taxonomy']:
        output += f'<strong>Type:</strong> {animal_obj["taxonomy"]["order"]}<br/>\n'

    output += '</p>\n</li>'
    return output


def main():
    """Main function to read data, generate HTML and write to file."""
    with open('animals_template.html', 'r') as template_file:
        html_template = template_file.read()

    animals_data = load_data('animals_data.json')

    output = ''
    for animal in animals_data:
        output += serialize_animal(animal)

    final_html = html_template.replace('__REPLACE_ANIMALS_INFO__', output)

    with open('animals.html', 'w') as html_file:
        html_file.write(final_html)

    print("HTML file generated successfully: animals.html")


if __name__ == "__main__":
    main()
