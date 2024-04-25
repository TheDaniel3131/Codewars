def validate(username, password):
    return Database().login(username, password)


def validate(username, password):
    database = Database()
    return database.login(username, password)


def validate(username, password):
    if '||' in password or '//' in password: return "Wrong username or password!"
    database = Database()
    return database.login(username, password)



# Good version
database = Database()
def validate(username, password):
    if "||" in password or "//" in password: return "Wrong username or password!"
    return database.login(username, password)


# Bad version but still working
validate = Database().login
