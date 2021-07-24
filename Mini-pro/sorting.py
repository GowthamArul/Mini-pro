class Sorting:
    def __init__(self):
        self.lst = [item for item in input("Enter the list of items with space: ").split()]
        print("Given lists are: ",self.lst)
    def splt(self):
        #print("Given values are: ",self.lst)
        numerics = []
        alphabets = []
        for sub in self.lst:
            if sub.isnumeric():
                numerics.append(sub)
            else:
                alphabets.append(sub)
        upper = []
        for i in alphabets:
            #print(i)
            upper.append(i.upper()) # converting alphabets value into upper case for perfect sorting
        #print(upper)
        # self.alp = upper
        for i in range(0, len(numerics)):
            for j in range(i+1, len(numerics)):
                if(numerics[i]>numerics[j]):
                    numerics[i],numerics[j] = numerics[j], numerics[i]
        intergers = list(map(int, numerics))
        for i in range(0, len(upper)):
            for j in range(i+1, len(upper)):
                if(upper[i]>upper[j]):
                    upper[i],upper[j] = upper[j], upper[i]
        if len(intergers) and len(upper) != 0:
            print("Sorted Numerics:",intergers)
            print("Sorted Alphabets:",upper)
        elif len(intergers) != 0:
            print("Sorted Numerics:", intergers)
        elif len(upper) != 0:
            print("Sorted Alphabets:", upper)
        else:
            print("The list is empty!!!")

srt = Sorting()
srt.splt()