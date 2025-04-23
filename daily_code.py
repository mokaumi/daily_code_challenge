mum = "yes"
dad = "no"

def check_parental_consent(mum, dad):   
    if mum == "yes" and dad == "no":
        return "mum"
    elif mum == "no" and dad == "yes":
        return "dad"
    elif mum == "yes" and dad == "yes":
        return "both"
    else:
        return "none"

# Call the function and print the result
print(check_parental_consent(mum, dad))

if mum and dad:
    print("Both parents have given consent.")
elif mum:
    print("Only mum has given consent.")
elif dad:
    print("Only dad has given consent.")
else:
    print("Neither parent has given consent.")
    

