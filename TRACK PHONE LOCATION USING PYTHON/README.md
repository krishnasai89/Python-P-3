# Installing required python packages
```terminal
pip install phonenumbers
```
*Now that we have the packages, we are ready to import it in our python script.*
```py
import phonenumbers
from phonenumbers import geocoder
```
- This imports the phonenumbers module and the geocoder submodule for location lookups.
```py
phone_number = phonenumbers.parse("+91 xxx-xxx-xxxx")
```
- This converts the given string "+91xxx-xxx-xxxx" into a phone number object that the library can work with.
```py
print("\nPhone Numbers Location")
```
- This is a simple print statement to provide a header in the output.
```py
print(geocoder.description_for_number(phone_number, "en"))
```
- This gets the geographical location of the phone number in English ("en") and prints it.

## Output of the code :
```cmd
Phone Numbers Location
India
```