def outer():
    outer_var = "Outer variable"
    counter = 0
    def inner():
        inner_var = "Inner variable"
        nonlocal counter
        counter += 1
        print(outer_var)
        print(inner_var)
    inner()
    print(counter)
outer()