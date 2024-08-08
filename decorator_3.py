def upper_stg(ref):
    def process():
        data = ref()
        return data.upper()
    return process()



def my_function():
    return "hello everyone!!"
res = upper_stg(my_function)
print(res)
