import csv
import os

#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote

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
    #for i, v in vote_count.items():
        #print(f"Percentage for {i} is %{round(v/vote_count*100,2)}")
    for i, v in vote_count.items():
        print(f"Name {i}: ({v})")
    max_votes = 0
    name = ""
    for i,v in vote_count.items():
        if max_votes < v: 
        # 0 < 85213 , 85213 < 272892
            max_votes = v
            name = i
        else:
            continue
    print(f"Winner: {name}")