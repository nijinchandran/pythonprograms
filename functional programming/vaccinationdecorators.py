def vaccination_booking(func):
    def wrapper(a,b,c):
        if b<18:
            raise Exception("you are not eligible for vaccination")
        else:
            return func(a,b,c)
    return wrapper


@vaccination_booking
def vaccine(name,age,place):
    return  "eligible"
print(vaccine("anu",19,"kochi"))

