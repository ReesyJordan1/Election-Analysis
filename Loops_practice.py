numbers= [0, 1 , 2 , 3 , 4]
for num in numbers:
    print(num)      

for num in range(5):
    print(num)

counties_tuple=("Arapahoe", "Denver", "Jefferson") 
for county in counties_tuple:
   print(county) 

   counties_dict={"Arapahoe":422829, "Denver":463353, "Jefferson":432438}
   for county in counties_dict:
       print(county)

   for county in counties_dict.values():
       print(county)

for county, voters in counties_dict.items():
    print(county, voters)

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
        print("I received " + str(percentage_votes)+"% of the total votes.")              

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
        print(county + " county has " + str(voters) + " registered voters.")    

        