# Write a program that stores data about goods, their quantity, and price. When the program starts, this information
# is displayed on the screen. Next, the user should be prompted to enter the item numbers and their new quantity.
# Changes to data should be completed when the user enters a specially specified character (for example,
# 0). After that, all data about the items should be displayed again.

dict_prod = {"names": [], "quant": [], "price": []}

b = list(dict_prod.values())

name = b[0]
qnt = b[1]
prc = b[2]

while True:
    try:
        choice_n = int(input("0.Exit\n1.Add Prod\nEnter your choice : "))
    except ValueError:
        print("\nChoose only digits from the given option")
        continue
    else:
        if choice_n == 1:
            prod_n = input("Enter product name : ")
            qntty = input("Enter quantity : ")
            prod_p = int(input("Enter price of the product : "))

            if prod_n in name:
                ind = name.index(prod_n)

                qnt.remove(qnt[ind])
                prc.remove(prc[ind])

                qnt.insert(ind, qntty)
                prc.insert(ind, prod_p)
            else:
                name.append(prod_n)
                qnt.append(qntty)
                prc.append(prod_p)
        else:
            break

print(f"\n {dict_prod} \n")

print("\n\nList of Products\n")


for i in range(len(name)):
    print(f"Your Prod. is {name[i]}, Quantity - {qnt[i]} and Price is {prc[i]}")
