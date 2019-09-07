from data import people, basic_plants_list, plants_list, plants_dict

# check to see if any plants in plants_dict to see if ther are any grasses in there
#run code again search for catus to test that it still works when there arent any

if bool(plants_dict) and any([plant.plant_type == "Grass" for plant in plants_dict.values()]):
	print("found a grass plant type")
else:
	print("didnt find a grass type")


