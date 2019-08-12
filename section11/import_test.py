
import challenge_blackJack

# print(__name__)
# challenge_blackJack.play()

g = sorted(globals())
for x in g:
    print(x)

# _function = represents a protected function (one that should be touched)

personal_details = ["tim", 24, "australia"]

name, _, country = personal_details

print(name, country)
print(_)