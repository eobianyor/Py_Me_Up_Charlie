# import neccessary plugins
import os
import csv

# create a path
election_data_csv = os.path.join('..', 'Resources', 'election_data.csv')

# initialize variables
AllCandidates = list()
CandidateSet = set()
profitLoss = []
Total_votes = 0
candidate0Votes = 0
candidate0percent = 0
candidate1Votes = 0
candidate1percent = 0
candidate2Votes = 0
candidate2percent = 0
candidate3Votes = 0
candidate3percent = 0
candidate4Votes = 0
candidate4percent = 0
winner = "No winner"
winner_percentage = 100

# Open csv file
with open(election_data_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')

    header = next(csv_reader)
    # Seed profit/loss amount (pl_Amt) so it cancels out for line 1
    pl_Amt = 867884

    for a, b, c in csv_reader:
        # Count candidate votes
        if (c).lower() == "correy":
            AllCandidates.append("Correy")
            candidate1Votes = candidate1Votes + 1
        elif (c).lower() == "khan":
            AllCandidates.append("Khan")
            candidate2Votes = candidate2Votes + 1 
        elif (c).lower() == "li":
            AllCandidates.append("Li")
            candidate3Votes = candidate3Votes + 1 
        elif (c).lower() == "o'tooley":
            AllCandidates.append("O'Tooley")
            candidate4Votes = candidate4Votes + 1 
        else:
            AllCandidates.append(c)
            candidate0Votes = candidate0Votes + 1

# Calculate votes and vote percentages
Total_votes = (candidate0Votes + candidate1Votes + candidate2Votes + candidate3Votes + candidate4Votes)
candidate1percent = (candidate1Votes/Total_votes)*100
candidate2percent = (candidate2Votes/Total_votes)*100
candidate3percent = (candidate3Votes/Total_votes)*100
candidate4percent = (candidate4Votes/Total_votes)*100

# Decide the winner
if candidate1Votes > candidate2Votes and candidate3Votes and candidate4Votes:
    winner = "Correy"
    winner_percentage = candidate1percent
elif candidate2Votes > candidate1Votes and candidate3Votes and candidate4Votes:
    winner = "Khan"
    winner_percentage = candidate2percent
elif candidate3Votes > candidate1Votes and candidate2Votes and candidate4Votes:
    winner = "Li"
    winner_percentage = candidate3percent
elif candidate4Votes > candidate1Votes and candidate2Votes and candidate3Votes:
    winner = "O'Tooley"
    winner_percentage = candidate4percent

# # QC statements
print("Election Results")
print("----------------------------------------- ")
print(f"Candidate Correy finished with {candidate1Votes} which represents {candidate1percent:.0f}% of the votes")
print(f"Candidate Khan finished with {candidate2Votes} which represents {candidate2percent:.0f}% of the votes")
print(f"Candidate Li finished with {candidate3Votes} which represents {candidate3percent:.0f}% of the votes")
print(f"Candidate O'Tooley finished with {candidate4Votes} which represents {candidate4percent:.0f}% of the votes")
print(f"The winner, with {winner_percentage:.0f}% of the votes is " + winner)

CandidateSet = set(AllCandidates)
print(candidate0Votes)
print(len(AllCandidates))
print(len(CandidateSet))
print(CandidateSet)
print(Total_votes)
