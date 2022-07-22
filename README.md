# Election_Analysis

## Overview of Election Audit 
The Colorado Board of Elections is conducting an election audit for a recent local congressional election. The tabulated election results are provided as a csv file and dataset was analyzed with Python to answer the following questions:

1. How many votes were cast in this congressional election?
2. What was the number of votes and the percentage of total votes for each county in the precinct?
3. Which county had the largest number of votes?
4. What was the number of votes and the percentage of the total votes each candidate received?
5. Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

## Resources
### Data Source 
- election_results.csv

### Software
- Python 3.7.6
- Visual Studio Code 1.69

## Election-Audit Results
The images below displays the election results printed to the command line and saved to a text file: 

![election results](https://user-images.githubusercontent.com/108038989/180363444-998a4037-8f60-4460-af8f-c86c25b5bbc1.png)

### 1. How many votes were cast in this congressional election?
The analysis revealed that the total number of votes cast in the congressional election was 369,711. 
This was derived with the following code:

    # Add our dependencies.
    import csv
    import os
    
    # Assign a variable to load a file from a path.
    file_to_load = os.path.join("Resources", "election_results.csv")
    # Assign a variable to save the file to a path.
    file_to_save = os.path.join("analysis", "election_analysis.txt")

    # Initialize a total vote counter.
    total_votes = 0

    # Open the election results and read the file
    with open(file_to_load) as election_data:
        file_reader = csv.reader(election_data)

        # Read the header row.
        headers = next(file_reader)

        # Print each row in the CSV file.
        for row in file_reader:
            # Add to the total vote count.
            total_votes += 1

    # Print the total votes.
    print(total_votes)

### 2. What was the number of votes and the percentage of total votes for each county in the precinct?
There were three counties in the precinct. Jefferson county received 38,855 votes (10.5% of total votes), Denver county received 306,055 votes (82.8% of total votes), and Arapahoe county received 24,801 votes (6.7% of total votes). 
This was derived with the following relevant code:

     # Create a county list and county votes dictionary.
     county_options = []
     county_votes = {}

     # Read the csv and convert it into a list of dictionaries
     with open(file_to_load) as election_data:
         reader = csv.reader(election_data)
         # Read the header
         header = next(reader)

         # For each row in the CSV file.
         for row in reader:
             # Add to the total vote count
             total_votes = total_votes + 1
             # Extract the county name from each row.
              county_name = row[1]
              # Write an if statement that checks that the county does not match any existing county in the county list.
              if county_name not in county_options:
                 # Add the existing county to the list of counties.
                 county_options.append(county_name)
                 # Begin tracking the county's vote count.
                 county_votes[county_name] = 0
              # Add a vote to that county's vote count.
              county_votes[county_name] += 1

     # Save the results to our text file.
     with open(file_to_save, "w") as txt_file:

         # Print the final vote count (to terminal)
         election_results = (
             f"\nElection Results\n"
             f"-------------------------\n"
             f"Total Votes: {total_votes:,}\n"
             f"-------------------------\n"
             f"County Votes:\n")
         print(election_results, end="")

         # Write a for loop to get the county from the county dictionary.
         for county_name in county_votes:
             # Retrieve the county vote count.
             votes = county_votes.get(county_name)              
             # Calculate the percentage of votes for the county.
             county_votes_percentage = float(votes) / float(total_votes) * 100 
             # Print the county results to the terminal.
             county_results = (
                 f"{county_name}: {county_votes_percentage:.1f}% ({votes:,})\n")
             # Print each candidate, their voter count, and percentage to the terminal.
             print(county_results)

### 3. Which county had the largest number of votes?
The county with the largest number of votes was Denver with 306,055 votes or 82.8% of the total votes. 
This was derived with the following relevant code:

    # Track the largest county and county voter turnout.
    winning_county = ""
    winning_county_count = 0
    winning_county_percentage = 0

        # Write an if statement to determine the winning county and get its vote count.
        if (votes > winning_county_count) and (county_votes_percentage > winning_county_percentage):
            winning_county = county_name
            winning_county_count = votes
            winning_county_percentage = county_votes_percentage

    # Print the county with the largest turnout to the terminal.
    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    print(winning_county_summary)

### 4. What was the number of votes and the percentage of the total votes each candidate received?
There were three candidates in this election. Charles Casper Stockham received 85,213 votes (23.0% of total votes), Diana DeGette received 272,892 votes (73.8% of total votes), and Raymon Anthony Doane received 11,606 votes (3.1% of total votes).
This was derived with the following relevant code:

    # Initialize a total vote counter.
    total_votes = 0

    # Candidate options and candidate votes
    candidate_options = []
    # 1. Declare the empty dictionary.
    candidate_votes = {}

    # Open the election results and read the file.
    with open(file_to_load) as election_data:
        file_reader = csv.reader(election_data)
        # Read the header row.
        headers = next(file_reader)

        # Print each row in the CSV file.
        for row in file_reader:
            # Add to the total vote count.
            total_votes += 1
            # Print the candidate name from each row.
            candidate_name = row[2]
            if candidate_name not in candidate_options:
                # Add the candidate name to the candidate list.
                candidate_options.append(candidate_name)
               # Begin tracking that candidate's vote count.
                candidate_votes[candidate_name] = 0
            # Add a vote to that candidate's count
            candidate_votes[candidate_name] += 1

    # Print the candidate vote dictionary.
    print(candidate_votes)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)

### 5. Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
The winner of the election Diana DeGette with 272,892 votes or 73.8% of the total votes.
This was derived with the following relevant code:

    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

## Election-Audit Summary
In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.

There is a statement to the election commission that explores how this script can be used for any election, with two examples for modifying the script. 

He expects the code used for this analysis should be dynamic to be able to reuse in future for not only other congressional districts but also for senatorial districts and local elections.
