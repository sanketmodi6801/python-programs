def normal_function(a,b,c,d,e):
    print(a,b,c,d,e)

normal_function("sanket","zalak","mummy","papa","python")
# What if i want to add more three names??? then i need to add more variables and work will be fizzy..!!

def funargs(normal,*args,**kwargs):
    print(normal)

    for items in args:
        print(items)

    for key, value in kwargs:
        print(f"{key} is {value}")

list1 = ["sanket","zalak","mummy","papa","python"]
normal = "sanket is the most intelligent man..!!!"
kw = {"sanket":"intelligent","zalak": "brave","mummy":"strong","papa":"calm","python":"fine language"}

funargs(normal,list1,kw)
#  mare game tetlu add karvu hoy list ma add karis etle function ma aavi j jashe args ni madad thi...!!
#  dictionary ma add karis etle functiom ma aavi j jashe...!! kwargs ni madad thi...!!
#  ahiya khali [*] asterick no imprtance hoy che...!! single args mate double kwargs mate...!!