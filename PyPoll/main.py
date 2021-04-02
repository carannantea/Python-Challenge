# Import modules
import csv
import os

# Set CSV File path
csvpath = os.path.join('Resources','election_data.csv')
output_path = os.path.join('Analysis','Election_Results.txt')

with open(output_path, 'w', newline='') as writetxt:
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        #print(csvreader)

        # Print Header and Data for sanity check
        csv_header = next(csvreader)
        #print(f"CSV Header: {csv_header}"

        # Iterate through each row in csv file.
        for row in csvreader:
            voter_count += 1
            if row[2] == poll.keys():
            
            # Count votes for each candidate
            if row[2] == 'Khan':
                khan_count += 1
            elif row[2] == 'Correy':
                correy_count += 1
            elif row[2] == 'Li':
                li_count += 1
            elif row[2] == 'O\'Tooley':
                tooley_count += 1

        candidates = {''}

        # Calculate and format percentage of votes per candidate


        # Printing in terminal
        print('!!! ELECTION RESULTS !!!')
        print('------------------------')
        print(f'Total Votes: {voter_count}')
        print('------------------------')
        print(f'Votes for Khan: {khan_percent} [{khan_count}]')
        print(f'Votes for Correy: {correy_percent} [{correy_count}]')
        print(f'Votes for Li: {li_percent} [{li_count}]')
        print(f'Votes for O\'Tooley: {tooley_percent} [{tooley_count}]')
        print('------------------------')
        #print(f'The winner is... {winner}')

    # Print to txt file
    csvwriter = csv.writer(writetxt, delimiter = ' ')
    csvwriter.writerow(['ELECTION','RESULTS'])
    csvwriter.writerow(['---------------------'])
    csvwriter.writerow(['Votes','for','Khan:',khan_percent, [khan_count]])
    csvwriter.writerow(['Votes','for','Correy:',correy_percent, [correy_count]])
    csvwriter.writerow(['Votes','for','Li:',li_percent, [li_count]])
    csvwriter.writerow(['Votes','for','O\'Tooley:',tooley_percent, [tooley_count]])
    csvwriter.writerow(['---------------------'])
    csvwriter.writerow(['The','Winner','Is','...'])