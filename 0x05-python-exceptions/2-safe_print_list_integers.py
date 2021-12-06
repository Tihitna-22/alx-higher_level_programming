def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for a in range(x):
        try:
            print("{:d}".format(my_list=[]))
            i += 1
        except(TypeError, ValueError):
            continue
    print()
    return i
