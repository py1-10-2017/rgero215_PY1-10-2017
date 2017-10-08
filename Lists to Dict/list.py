def list_to_dict(list_one, list_two):
    new_dict = {}
    new_dict = zip(list_one, list_two)
    return new_dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

print dict(list_to_dict(name, favorite_animal))
