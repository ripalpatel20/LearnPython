shopList = ["apple", "banana", "cherry"]
shopList.append("test")
print(shopList)
print(shopList.__len__())
shopList.__delitem__(3)
print(shopList)
print(shopList.__len__())
shopList2 = ["apple2", "banana2", "cherry2"]
total = shopList+shopList2
print(total.__len__())
print("ripal" + "patel")
