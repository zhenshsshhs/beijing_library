def readfile(path="needed.txt", mode="r"):
    name = []
    with open(path, mode) as f:
        for line in f.readlines():
            line = int(line.strip('\n'))  # 去掉列表中每一个元素的换行符
            if line == 0 or line == '0':
                continue
            name.append(line)
    return name


def writefile(path="needed.txt", mode="a", txt='0'):
    """

    :rtype: object
    """
    with open(path, mode) as f:
        f.write("\n" + str(txt))
    return readfile(path, "r")


if __name__ == '__main__':
    needed = readfile("needed.txt", 'r')
    # needed = writefile("needed.txt", "a")
    txt = 20220130
    if txt in needed:
        print(1)
