from data import people, basic_plants_list, plants_list

# add bool(person) b if person == [] all(person) will return true
if bool(people) and all([person[1] for person in people]):
	print("sending email")
else:
	print("user must edit the list of recipeints")


if any([plant.plant_type == "Grass" for plant in plants_list]):
	print("This pack contains grass")
else:
	print("no grass in this pack")
