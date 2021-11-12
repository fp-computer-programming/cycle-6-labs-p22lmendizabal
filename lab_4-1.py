#author: LM(AMDG) 11/12/21
list1 = ["red", "orange", "yellow", "green"]
list1.extend(["blue", "indigo", "navy"])
print(list1)
print(list1.count("yellow"))
list1.insert(3, "purple")
print(list1)
list1.clear()
print(list1.count("red"))