def hello(name=""):
    if name == "":
        return "Hello, World!";
    else:
        return f"Hello, {name.capitalize()}!";