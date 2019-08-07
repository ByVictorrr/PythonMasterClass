import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans","bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta  = ["pasta", "cheese"]

with shelve.open("recipes",writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled_eggs"] = scrambled_eggs
    # recipes["soup"] = soup
    # recipes["pasta"] = pasta
    
    # recipes["blt"].append("butter")
    # recipes["pasta"].append("tomata")

    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list

    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list

    #recipes["soup"].append("melons")

    recipes["soup"] = soup
    # clears soup from cache and writes to db
    recipes.sync()
    soup.append("cream")


    
    

    for snack in recipes:
        print(snack, recipes[snack])

