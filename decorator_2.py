def my_fun():
    data = "good morning all"
    def solve():
        s = data.upper()
        return s
    return solve()
var = my_fun()
print(var)
