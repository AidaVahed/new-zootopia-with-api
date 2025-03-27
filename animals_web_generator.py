import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


with open('animals_template.html', 'r') as template_file:
  html_template = template_file.read()

animals_data = load_data('animals_data.json')

output = ''

for animal in animals_data:
  animal_info = '<li class="cards__item">'

  if 'name' in animal:
    animal_info += f"<div class='card__title'>Name: {animal['name']}</div>"

  if 'characteristics' in animal and 'diet' in animal['characteristics']:
    animal_info += f"<div class='card__text'>Diet: {animal['characteristics']['diet']}</div>"

  if 'locations' in animal and len(animal['locations']) > 0:
    animal_info += f"<div class='card__text'>Location: {animal['locations'][0]}</div>"

  if 'taxonomy' in animal:
    animal_info += f"<div class='card__text'>Type: {animal['taxonomy'].get('order', 'Unknown')}</div>"

  animal_info += '</li>'
  output += animal_info

final_html = html_template.replace('__REPLACE_ANIMALS_INFO__', output)

with open('animals.html', 'w') as html_file:
  html_file.write(final_html)

print("HTML file generated successfully: animals.html")