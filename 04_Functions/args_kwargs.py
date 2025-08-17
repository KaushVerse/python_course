# Variable-length Arguments
def demo(*args, **kwargs):
    print("Args", args)
    print("Kwargs", kwargs)


demo(1, 2, 3, name="Kaushik", age=21)