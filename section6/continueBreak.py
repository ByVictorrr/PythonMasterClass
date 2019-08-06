# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if(item == "spam"):
#         break
#     else:
#         print("buy " + item)

meal = ["egg", "bacon", "ass", "sausages"]
nasty_food_item = ''
for item in meal:
    if(item == "spam"):
        nasty_food_item = item
        break

if nasty_food_item:
    print("Cant I have anything without spam")
else:
    print("spam not in meal")

