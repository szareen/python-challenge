import os
import csv

output_path = os.path.join('output', 'results.txt')

# Read the csv 

csvpath = os.path.join('Resources', 'election_data.csv')

total_votes = 0

winning_candidate = ""
winning_count = 0
candidate_options = []
candidate_votes = {}

# Read the csv and convert it into a list of dictionaries
with open(csvpath) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:

        # Adding the total vote count
        total_votes = total_votes + 1

        candidate_name = row["Candidate"]

        # Matching any existing candidate...
        if candidate_name not in candidate_options:

            
            candidate_options.append(candidate_name)

            
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print the results and export the data to our text file
with open(output_path, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)