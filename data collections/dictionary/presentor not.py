d={1:10,2:20,3:30,4:40,5:50,6:60}
def is_key_present(x):
    if x in d:
        print(x,'is present in the dictionary')
    else:
        print(x,'is not present in the dictionary')
x=int(input("enter key"))
is_key_present(x)