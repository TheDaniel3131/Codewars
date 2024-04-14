def say_hello(name, city, state):
    full_name = ' '.join(i for i in name)
    return f"Hello, {full_name}! Welcome to {city}, {state}!"


def say_hello(name, city, state):
    return "Hello, {}! Welcome to {}, {}!".format(" ".join(name), city, state)


def say_hello(name, city, state):
    return f"Hello, {' '.join(name)}! Welcome to {city}, {state}!"


def say_hello(name, city, state):
    name = " ".join(name)
    return "Hello, %s! Welcome to %s, %s!" %(name,city,state)