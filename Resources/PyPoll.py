#The data we need to retrieve:
#1. Total number of votes cast
#2. A complete list of candidates who received votes
#3. Total number of votes each candidate received
#4. Percentage of votes each candidate won
#5. The winner of the election based on popular vote

#from platform import python_branch

# Add our dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1a. Initialize a total vote counter
total_votes = 0

#2a. Candidate Options List
candidate_options = []

#3a. candidate Votes Dictionary, declare an empty dictionary
candidate_votes = {}

#5a. Declare a variable that holds an empty string value for the winning candidate.
winning_candidate = " "
#5b. Declare a variable for the "winning count" equal to zero.
winning_count = 0
#5c. Declare a variable for the "winning_percentage" equal to zero.
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    
    #Read and analyze the data here
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #1b. Add to the total vote count.
        #number = number + 1, which can be augmented to number += 1
        total_votes += 1

        #2b. Print the candidate name from each row
        candidate_name = row[2]

        #2c. Add the candidate name to the candidate list.
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add it to the list of candidates
            candidate_options.append(candidate_name)

            #3b. Begin tacking that candidate's name
            #3c. To begin tracking the candidate's vote count, we initialize each candidate's vote equal to zero. 
            candidate_votes[candidate_name] = 0
        #3d. Increment the votes by 1 every time a candidate name appears in a row.
        candidate_votes[candidate_name] +=1

#1c. Print the total votes
#print(total_votes)

#2d. Print the candidate list.
#print(candidate_options)

#3e. print the candidates vote dictionary
#print(candidate_votes)

#Save the results to text file
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #4. Determine the percentage of votes for each candidate by looping through the counts.
    #4a. Loop through the candidate options list
    for candidate_name in candidate_votes:
        #4b. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        #4c. Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #4d. Print the candidate name and percentage of votes using f-string formatting..
        #print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")

        #4e. Print out each candidate's name, vote count, and percentage of votes to the terminal.
        #commented out to add txt file:
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

        #5. Winning Candidate and Winning Count Tracker
        #5d. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #5e. If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            #5f. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    #5g. Print out the winning candidate summary.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
