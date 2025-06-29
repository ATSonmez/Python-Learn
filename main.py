capitals = {"USA": "Washington D.C.", 
            "India": "New Delhi", 
            "China": "Beijing",
            "Russia": "Moscow"}

#print(capitals.get("Japan"))
#if capitals.get("Japan"):
 #   print("That capital exists")
#else:
 #   print("That capital doesn't exist")

#capitals.update({"Germany": "Berlin"})
#capitals.update({"USA": "Detroit"})
#capitals.pop("China")
#capitals.popitem()
#keys = capitals.keys()
#print(keys)

#for key in capitals.keys():
 #   print(key)

#values = capitals.values()

#for value in capitals.values():
 #   print(value)
items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")
