print("Hello world")
print("Hello World")


counties=["arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")

else:
    print("El Paso is not the list of counties.")

if "arapahoe" in counties and "El Paso" not in counties:
    print("only Arapahoe is inthe list of counties.")
else:
    print("arapahoe is in the list of counties and El paso is not in the list of counties")


for county in counties:
    print(county)


# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)
