"""
with open("text.csv", "r", encoding="utf-8") as file:
    text = file.read().splitlines()
    l1 = []
    for line in text:
        l2 = []
        for j in line.split(","):
            if type(j) == str:
                l2.append(j.replace('"', "").strip())
            else:
                l2.append(j)
        l1.append(l2)
"""   
"""
with open("generos.csv", "r", encoding="utf-8") as file:
    text = file.read().splitlines()
    l1 = []
    for line in text:
        l2 = []
        for j in line.split(","):
            if type(j) == str:
                l2.append(j.replace('"', "").strip())
            else:
                l2.append(j)
        l1.append(l2)
    print(l1)
"""
