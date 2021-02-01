def LooseChange(total_amount):

    ## create base dictionary to return
    output = {"Pennies": 0, "Nickels": 0, 'Dimes': 0, "Quarters": 0}

    ## if the number is invalid return the base dictionary
    if total_amount <= 0:
        return output

    ## this loop accounts for decimal places
    while not (0 <= total_amount < 1):

        ## count quarters
        if (total_amount - 25) >= 0:
            total_amount -= 25
            output["Quarters"] += 1

        ## count dimes
        elif (total_amount - 10) >= 0:
            total_amount -= 10
            output["Dimes"] += 1

        ## count nickels
        elif (total_amount - 5) >= 0:
            total_amount -= 5
            output["Nickels"] += + 1

        ## count pennies
        elif (total_amount - 1) >= 0:
            total_amount -= 1
            output["Pennies"] += 1

    ## return dictionary filled out
    return output


## Take user input
userinput = float(input("Please enter amount here: "))

## Return answer
print (LooseChange(userinput))
