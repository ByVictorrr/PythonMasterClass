import shelve

books = shelve.open("book")

books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
                    "beans_on_toast": ["beans", "bread"],
                    "scrambled eggs": ["eggs", "butter", "milk"],
                    "soup": ["tin of soup"],
                    "pasta": ["pasta", "cheese"]}
                
books["maintenance"] = {"stuck": ["oil"],
                        "loose": ["gaffer tape"]}

