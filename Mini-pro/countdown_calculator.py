a,b,c = [int(x) for x in input("Enter the S date").split()]
print(f"Date is {a} {b} {c}")

d,e,f = [int(x) for x in input("Enter the E date").split()]
print(f"Date is {d} {e} {f}")

year = f - c
month = e - b
day = d - a

var1 = 1
var2 = 1

if month < 0:
    var1 = var1 * 12 - abs(month)
    year -=1
    month = var1
    print(day, " day ", month, " month ", year, " year " )
    if day<0:
        var2  = var2*30 - abs(day)
        day = var2
        month -= 1
        print(day, " day ", month, " month ", year, " year " )
    else:
        print(day, " day ", month, " month ", year, " year " )
else:
    print(day, " day ", month, " month ", year, " year " )


