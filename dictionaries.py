data = {1: "Ibroximjon", 2: "Hojiakbar", 4: "Jamoliddin"}
print(data)
print(data[1])
print(data.get(1))  # Ibroximjon
print(data.get(3))  # None
print(data.get(3, "Not found"))  # Not found
print(data.get(1, "Not found"))  # Ibroximjon

keys = ["math", "physics", "geography"]
values = [103, 120, 132]
newData = dict(zip(keys, values))
print(newData)
newData["literature"] = 140
print(newData)
del newData["literature"]
print(newData)

progs = {"JS": "Atom", "CS": "VS", "Python": ["Pycharm", "Sublime"], "Java": {"JSE": "NetBeans", "JEE": "Oracle"}}
print(progs["JS"])
print(progs["Python"])
print(progs["Java"]["JEE"])
