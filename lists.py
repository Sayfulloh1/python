names = ["ibroximjon", "jasurbek", "bekzodjon", "hojiakbar"]
print(names)  # ibroximjon, jasurbek, bekzodjon, hojiakbar

names.remove("ibroximjon")  # jasurbek, bekzodjon, hojiakbar
print(names[0:])  # jasurbek, bekzodjon, hojiakbar

names.append("azizbek")  # jasurbek, bekzodjon, hojiakbar, azizbek
print(names)  # jasurbek, bekzodjon, hojiakbar, azizbek

names.sort()  # azizbek, bekzodjon, hojiakbar, jasurbek
print(names)  # azizbek, bekzodjon, hojiakbar, jasurbek

names.insert(1, "muhammadqodir")  # 'azizbek', 'muhammad qodir', 'bekzodjon', 'hojiakbar', 'jasurbek'
print(names)  # 'azizbek', 'muhammad qodir', 'bekzodjon', 'hojiakbar', 'jasurbek'

names.pop(2)  # 'azizbek', 'muhammad qodir', 'hojiakbar', 'jasurbek'
print(names)  # 'azizbek', 'muhammad qodir', 'hojiakbar', 'jasurbek'

del names[2:]
print(names)  # 'azizbek', 'muhammad qodir'

names.extend(["javohir", 'muhammadaziz'])
print(names)  # 'azizbek', 'muhammad qodir', 'javohir, muhammad aziz'

names.reverse()
print(names)  #'muhammad aziz', 'javohir', 'muhammad qodir', 'azizbek'

print(max(names))
print(min(names))
print(len(names))

have = names.__contains__("muhammadaziz")
print(have)