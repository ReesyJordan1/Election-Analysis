import csv #adding dependencies
import os 

# Assign a variable for the file to load and the path.
#file_to_load="Resources/election_results.csv" or
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file or Assign a variable to load a file from a path.
file_to_save=os.path.join("analysis", "election_analysis.txt")


# Open the election results and read the file and  Read the file object with the reader function.
# election_data=open(file_to_lead, "r")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# To do: perform analysis.
#    print(election_data)

# Close the file.
#election_data.close()


# Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")

    # To do: read and analyze the data here.
    #file_reader = csv.reader(election_data)
    #Print each row in the CSV file.
    #for row in file_reader:
    #    print(row)

       # Read and print the header row.
    headers = next(file_reader)
    print(headers) 
