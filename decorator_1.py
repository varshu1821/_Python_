def out():
    str1 = "welcome to"
    def inn():
        str2 = "PYTHON"
        out = str1 + str2
        return out
    return inn
var = out()
print(var())
print(var.__name__)
