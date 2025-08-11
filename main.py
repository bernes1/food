import random
import json
# Todo move this to a json file and then read the json file into the program
def read_file():
    with open('places.json', 'r+') as file:
      places = json.load(file)
    return places


def add_place(name: str,food_type: str,category: str ,distance: int):
    with open('places.json', 'r') as file:
        places = json.load(file)
    #todo add functionality for adding new places to the list
    id = len(places)
    new_place = {
        "id": id+1,
        "name": name,
        "food_type": food_type,
        "category": category,
        "distance": distance,
        "tag": {}
    }
    places.append(new_place)
    with open('places.json', 'w') as file:
        json.dump(places, file, indent=4) 

def choose_random_place():
    data = read_file()
    place = random.choice(data)
    print(place)


def choose_place():
    data = read_file()
    for place in data: 
        print(place)


def main():
    print("This is a random place to eat")
    add_place("bastard","burger","greasy",0)
    #choose_place()



if __name__ == "__main__":
    main()