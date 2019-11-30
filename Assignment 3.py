vatTotal = 0
vat = 0
vatNum = 0

def main():
    total = 0
    sale = []
    num = 0
    vatSale = []
    num = int(input("Please enter the sales figure: "))

    while(num!=-1):
        sale.append(num)

        vatSale.append(addvat(num))
        total+=vatSale[-1]
        num = int(input("Please enter the sales figures: "))

    print("The sales figures entered were: %s\nThe sales figures incuding VAT were: %s"%(sale,vatSale))
    print("The total VAT charged is", vatTotal)
    print("The total sales for this period is ", total)

def addvat(num):
    global vat
    global vatNum
    global vatTotal

    vat = num*0.23
    vatNum = num + vat
    vatTotal +=vat

    return vatNum


main()
    
