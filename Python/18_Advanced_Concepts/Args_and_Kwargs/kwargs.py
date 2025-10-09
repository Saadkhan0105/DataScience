def marks(**kwargs):
    for item in kwargs.keys():
        print(f"the marks of {item} is {kwargs[item]}")
        
marks(Saad=90, Abuzar=80, Umaima=70)