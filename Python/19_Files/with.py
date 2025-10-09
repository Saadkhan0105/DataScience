# f = open("saad.txt", "r")
# content = f.read()
# print(content)
# f.close()

with open("saad.txt", "r") as f:
    content = f.read()
    print(content)