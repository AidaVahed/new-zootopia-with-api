import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')

for animal in animals_data:
  if 'name' in animal:
    print(f"Name: {animal['name']}")

  if 'characteristics' in animal and 'diet' in animal['characteristics']:
    print(f"Diet: {animal['characteristics']['diet']}")

  if 'locations' in animal and len(animal['locations']) > 0:
    print(f"Location: {animal['locations'][0]}")

  if 'taxonomy' in animal:
    print(f"Type: {animal['taxonomy'].get('order', 'Unknown')}")

  print()
