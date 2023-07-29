#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote

import csv
import os

total_num_votes = 0
candidates_list = []
vote_count = {}
individual_votes = []

csvpath = os.path.join('election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
     # uses up first row and leaves rest of data
    csv_headers = next(csvreader)

    print(f"Election Results")
    print("-"*25)
  
    for x in csvreader:

        total_num_votes += 1

        name = x[2]

        if name not in candidates_list:
            candidates_list.append(name)
            vote_count[name] = 1
        # if the candidate already exist, just increment the value for the name by 1
        else: 
            vote_count[name] += 1
            
# Writing in output txt file
with open(analysis, "a") as txtfile:
    txtfile.write(f"Election Results \n")
    txtfile.write(f"-"*25)
    txtfile.write("\n")
    txtfile.write(f"Total Votes: {total_num_votes} \n")
    txtfile.write(f"-"*25)
    txtfile.write("\n")
    
    for i, v in vote_count.items():
        percent_vote = (v /total_num_votes) * 100
        percent_vote = round(percent_vote,2) 
        
        print(f"Name: {i}: {percent_vote}% ({v})")
        txtfile.write(f"{i} : {percent_vote}% ({v}) \n")

    for i, v in vote_count.items():
        
        #Total Number of Votes each candidate won          
        max_votes = 0
        name = ""
           
    for i,v in vote_count.items():
        if max_votes < v: 
            max_votes = v
            name = i
        else:
            continue  
    
with open(analysis, "a") as txtfile:
    txtfile.write(f"-"*25)
    txtfile.write("\n")
    txtfile.write(f"Winner: {name}")
            
    print("-"*25)
    print(f"Winner: {name}")
    print("-"*25)
        

