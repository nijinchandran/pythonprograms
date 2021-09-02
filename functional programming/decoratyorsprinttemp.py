def admin_required(func):
    def wrapper(a,b):
        if a!="admin":
            raise Exception("you are not allowed")
        else:
            return func(a,b)
    return wrapper

@admin_required
def change_pin(user,pin):
    mypin=pin
    return mypin
@admin_required
def delete_ac(user,acno):
    return str(acno)+"delete"

#print(change_pin("admin",1000)
print(delete_ac('admin',1000))