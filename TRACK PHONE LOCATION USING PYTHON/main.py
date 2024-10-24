import phonenumbers
from phonenumbers import geocoder

phone_number = phonenumbers.parse("+919019934143")

print("\nPhone Numbers Location")
print(geocoder.description_for_number(phone_number, "en"))