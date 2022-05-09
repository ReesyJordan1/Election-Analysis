# import csv
# from distutils import text_file #adding dependencies
# import os 

# # Assign a variable for the file to load and the path.
# #file_to_load="Resources/election_results.csv" or
# file_to_load = os.path.join("Resources", "election_results.csv")

# # Create a filename variable to a direct or indirect path to the file or Assign a variable to load a file from a path.
# file_to_save=os.path.join("analysis", "election_analysis.txt")

# # Initialize a total vote counter.
# total_votes = 0

# # Declaring a new list called Candidate Options
# candidate_options = []

# #Declare an empty dictionary
# Candidate_votes={}

# # Open the election results and read the file and  Read the file object with the reader function.
# # election_data=open(file_to_lead, "r")
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)

# # To do: perform analysis.
# #    print(election_data)

# # Close the file.
# #election_data.close()


# # Using the open() function with the "w" mode we will write data to the file.
# # open(file_to_save, "w")

#     # Read and print the header row.
#     headers = next(file_reader)
#     #print(headers) 

#  # To do: read and analyze the data here.
#     #file_reader = csv.reader(election_data)
#     #Print each row in the CSV file.
#     for row in file_reader:
#         #print(row)
# # Add to the total vote count (increment a variable) by using number = number + 1 or
#         total_votes += 1

#         # Print the total votes.
#         #print(total_votes)

#         # Print the candidate name from each row
#         candidate_name = row[2]

#         # If the candidate does not match any existing candidate...
#         if candidate_name not in candidate_options:
#                 # Add it to the list of candidates.
#                 candidate_options.append(candidate_name)

#                 #Begin tracking that candidate's vote count by creating each candidate as a key for the dictionary and set the cote count to 0
#                 Candidate_votes[candidate_name] = 0

#         # Add a vote to that candidate's count every time that candidate name appears
#         Candidate_votes[candidate_name] += 1

# # Save the results to our text file.
# with open(file_to_save, "w") as txt_file:

# # Print the final vote count to the terminal.
#     election_results = (
#         f"\nElection Results\n"
#         f"-------------------------\n"
#         f"Total Votes: {total_votes:,}\n"
#         f"-------------------------\n")
#     print(election_results, end="")
#     # Save the final vote count to the text file.
#     txt_file.write(election_results)

#     # Print the candidate list.
#     #print(Candidate_votes) 

#     # Determine the percentage of votes for each candidate by looping through the counts.
#     # Iterate through the candidate list.
    
#      #Determining the winner. First Declare a variable for Winning Candidate and Winning Count Tracker equal to and winning percentage equal to 0
#     winning_candidate = ""
#     winning_count = 0
#     winning_percentage = 0

#     for candidate_name in Candidate_votes:
#         # Retrieve vote count of a candidate.
#         votes = Candidate_votes[candidate_name]
#         # Calculate the percentage of votes.
#         vote_percentage = float(votes) / float(total_votes) * 100
#         # Print the candidate name and percentage of votes.
#         # print(f"{candidate_name}: received {vote_percentage}% of the vote.") 0r update the f string to only print two decimal places
#         print(f"{candidate_name}: received {float(votes) / float(total_votes) * 100:.2f}% of the vote.")

#         if (votes > winning_count) and (vote_percentage > winning_percentage):
#             # If true then set winning_count = votes and winning_percent =
#             # vote_percentage.
#             winning_count = votes
#             winning_percentage = vote_percentage
#             # Set the winning_candidate equal to the candidate's name.
#             winning_candidate = candidate_name


#     # To do: print out each candidate's name, vote count, and percentage of
#     # votes to the terminal.
#     #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
#             candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")  

#     # Print each candidate, their voter count, and percentage to the terminal.
#     print(candidate_results)
#     #  Save the candidate results to our text file.
#     txt_file.write(candidate_results)

#     # Determine winning vote count and candidate
#     # Determine if the votes are greater than the winning count.
#     winning_candidate_summary = (
#         f"-------------------------\n"
#         f"Winner: {winning_candidate}\n"
#         f"Winning Vote Count: {winning_count:,}\n"
#         f"Winning Percentage: {winning_percentage:.1f}%\n"
#         f"-------------------------\n")
#     print(winning_candidate_summary)

#     # Save the winning candidate's name to the text file.
#     txt_file.write(winning_candidate_summary)

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)