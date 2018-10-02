def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(*args, **kwargs)
        result = func(*args, **kwargs)
        return result
    print("hello")
    return wrapper

@my_decorator
def add(a, b):
    return a+b
@my_decorator
def app():
    pass

app()

add(1,3)


# a = my_decorator(add)
# print(a(1,3))
# def app(func):
#     return func(1,3)

# def ad(a,b):
#     return a+b
# print(app(ad))