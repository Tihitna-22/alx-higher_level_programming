def safe_print_list(my_list=[], x=0):
    i = 0
    for a in range(x):
        try:
            print(my_list[a],end='')
            i += 1
        except IndexError:
            break
    print()
    return i
