# % of votes each candidate won
# total number of votes each candidate won


total_num_votes = 0
candidates_list = []
vote_count = {"charles"}
individual_votes = []

csvpath = os.path.join (PyPoll_ElectionData.csv)

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_headers = next(csvreader) # uses up first row and leaves the rest of data

    for x in csvreader:
        # print (x)
        

        total_num_votes += 1

        name = x[2]

        if name not in candidates_list:

            candidates_list.append(name)
            vote_count[name] = 1

            # if the candidate already exists the increment by 1

        else:
            vote_count[name]