def outer_f():
    a = 30

    def inner_f():
        print(a)

    inner_f()


outer_f()
