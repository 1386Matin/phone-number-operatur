from phonenumbers import parse
from phonenumbers import geocoder
from phonenumbers import carrier

Phonenumber = input("Enter The Phonenumber : ")

number = parse(Phonenumber)

print(geocoder.description_for_number(number,"en"))
print(carrier.name_for_number(number,"en"))
