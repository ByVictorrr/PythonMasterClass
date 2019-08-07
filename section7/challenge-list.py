menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])

menu.append(["spam", "egg", "spam", "spam", "bacon", "bacon", "spam"])
menu.append(["spam","egg", "bacon", "sausage", "spam"])

for meal in menu:
    if not "spam" in meal:
        for item in meal:
            print(item)
 