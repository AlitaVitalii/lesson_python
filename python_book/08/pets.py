def describe_pet(pet_name, animal_type="dog"):
    """выводит инфо о животном"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('vedma', 'cat')
describe_pet('ben')
describe_pet()