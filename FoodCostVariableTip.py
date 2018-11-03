# input list
foodcost = 0.0
tip = 0.0
tax = 0.0
total = 0.0

# Module calc_tip
# if foodcost < 5.99 then tip = 0.10
# if foodcost < 12.01 but > 5.99 then tip = 0.15
# if foodcost < 17.01 but > 12.00 then tip = 0.20
# if foodcost < 25.00 but > 17.00 then tip = 0.25

def calc_tip(foodcost):
    if foodcost < 5.99:
        tip = float(0.10 * foodcost)

    if 5.99 < foodcost < 12.01:
        tip = float(0.15 * foodcost)

    if 12.00 < foodcost < 17.01:
        tip = float(0.20 * foodcost)

    if 17.00 < foodcost < 25.00:
        tip = float(0.25 * foodcost)

    if foodcost > 25.01:
        tip = float(0.30 * foodcost)
    return tip


def calc_tax(foodcost):
    tax = float(0.10 * foodcost)
    return tax

def main():

    foodcost = float(input("What is the food cost?: "))
    tip_result = calc_tip(foodcost)
    tax_result = calc_tax(foodcost)
    total = (foodcost + tip + tax)


    print("your food total is ", foodcost)
    print("Your tax total is ", tax_result)
    print("Your tip total is ", tip_result)
    print("Your total is ", total)

main()