# Code will read a comma separated text file containing election data for Voter ID,County,Candidate
# and produce the election results printing to the screen and saving to file

# operating system
import os
# Comma Separated Values
import csv

# Variables
CorreyVotes = 0
LiVotes = 0
KhanVotes = 0
OTooleyVotes = 0
TotVotes = 0

# Path setting (This is the path on local Windows 10 machine given the current working folder)
path = os.path.join('Python-Challenge', 'PyPoll', 'Resources', 'election_data.csv')

# with to open file and ensure it closes
with open(path, newline='') as csvfile:

    # Comma delimited file definition
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Deal with header
    csv_header = next(csvreader)
    row = next(csvreader)

    for row in csvreader:
        
        # Counting total votes
        TotVotes += 1
        
        # Counting votes for each candidate
        if (row[2] == "Correy"):
            CorreyVotes += 1
        elif (row[2] == "Li"):
            LiVotes += 1
        elif (row[2] == "Khan"):
            KhanVotes += 1
        else:
            OTooleyVotes += 1
            
    # Calculating % votes for each candidate
    CorreyPerc = CorreyVotes / TotVotes
    LiPerc = LiVotes / TotVotes
    KhanPerc = KhanVotes / TotVotes
    OTooleyPerc = OTooleyVotes / TotVotes
    
    # Who is the winner, take the max of votes
    winner = max(CorreyVotes, LiVotes, KhanVotes, OTooleyVotes)

    if winner == KhanVotes:
        winner_name = "Khan"
    elif winner == CorreyVotes:
        winner_name = "Correy"
    elif winner == LiVotes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 

# Print to screen
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {TotVotes}")
print(f"---------------------------")
print(f"Khan: {KhanPerc:.3%}({KhanVotes})")
print(f"Correy: {CorreyPerc:.3%}({CorreyVotes})")
print(f"Li: {LiPerc:.3%}({LiVotes})")
print(f"O'Tooley: {OTooleyPerc:.3%}({OTooleyVotes})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")

# Path setting in order to write file (This is the path on local Windows 10 machine given the current working folder)
ElectionResult = os.path.join('Python-Challenge', 'PyPoll', 'Analysis', 'election_data_revised.text')

# write the output
with open(ElectionResult, 'w',) as OutPutFile:

    OutPutFile.write(f"Election Results\n")
    OutPutFile.write(f"---------------------------\n")
    OutPutFile.write(f"Total Votes: {TotVotes}\n")
    OutPutFile.write(f"---------------------------\n")
    OutPutFile.write(f"Khan: {KhanPerc:.3%}({KhanVotes})\n")
    OutPutFile.write(f"Correy: {CorreyPerc:.3%}({CorreyVotes})\n")
    OutPutFile.write(f"Li: {LiPerc:.3%}({LiVotes})\n")
    OutPutFile.write(f"O'Tooley: {OTooleyPerc:.3%}({OTooleyVotes})\n")
    OutPutFile.write(f"---------------------------\n")
    OutPutFile.write(f"Winner: {winner_name}\n")
    OutPutFile.write(f"---------------------------\n")
