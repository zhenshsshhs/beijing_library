import file
need = file.readfile("need.txt", 'r')

needed = file.readfile("needed.txt", 'r')

def inintation():
    needed.sort()
    for i in need:

        if i in needed:
            need.remove(i)
    print(need)
inintation()