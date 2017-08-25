def cycler(set, int setlength, int n):
    tmp = []
    for elem in set:
        tmp.append(chr((ord(elem)- ord(set[0]) + n) % setlength + ord(set[0])))
    return tmp
