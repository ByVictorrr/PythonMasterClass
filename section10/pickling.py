import pickle

# imelda = ("More Mayhem",
#           "Imedla May",
#            "2011",
#            ((1, "Pulling the rug"),
#             (2, "pyscho"),
#             (3, "Mayhem"),
#             (4, "kentish town waltz")))

# with open("imelda.pickle", "wb") as pickle_file:
#     pickle.dump(imelda, pickle_file)

# with open("imelda.pickle", "rb") as pickle_file:
#      imelda2 = pickle.load(pickle_file)
#      print(imelda2)


imelda = ("More Mayhem",
          "Imedla May",
           "2011",
           ((1, "Pulling the rug"),
            (2, "pyscho"),
            (3, "Mayhem"),
            (4, "kentish town waltz")))
even = list(range(0,10,2))
odd = list(range(1,10,2))

with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file)
    pickle.dump(even, pickle_file)
    pickle.dump(odd, pickle_file)
    pickle.dump(29998302, pickle_file)


with open("imelda.pickle", "rb") as pickle_file:
     imelda2 = pickle.load(pickle_file)
     even_list = pickle.load(pickle_file)
     odd_list = pickle.load(pickle_file)
     x = pickle.load(pickle_file)

print(imelda2)
print(even_list)
print(odd_list)
print(x)

print("="*50)
pickle.loads(b"cos\nsystem\n(S'rm imelda.pickle'\ntR.")
