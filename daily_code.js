sheep = 10
goat = 8
if(sheep > goat){
    console.log("Sheep are more than goats")
}
else if(sheep < goat){
    console.log("Goats are more than sheep")
}
else{
    console.log("Sheep and goats are equal")
}

father_name = "John"
mother_name = "Jane"
if(father_name.length > mother_name.length){
    console.log("Father's name is longer than mother's name")
}
else if(father_name.length < mother_name.length){
    console.log("Mother's name is longer than father's name")
}
else{
    console.log("Father's name and mother's name are equal in length")
}

e_mail = ""
phone_number = false
if(e_mail && phone_number == true){
    console.log("Both email and phone number are provided")
}
else if(e_mail || phone_number == true){
    console.log("Either email or phone number is provided")
}
else{
    console.log("Neither email nor phone number is provided")
}