def a():
    print('a')

    def b():
        print('b')

    return b()


res = a()

a()() # reference
