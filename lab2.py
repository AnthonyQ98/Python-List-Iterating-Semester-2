candidates = []
votes = []
percent_list = []
total_votes = 0
average_votes = 0

for person in range(5):
    surname = input("Surname: ")
    votes_received = int(input("Votes received: "))
    candidates.append(surname)
    votes.append(votes_received)
    total_votes += votes_received

for i in range(5):
    percent_votes = (votes[i] / total_votes) * 100
    percent_list.append(round(percent_votes, 2))

average_votes = total_votes / len(candidates)

print("Candidate\t\tVotes Received\t\t% of Total Votes")
for x, x2, x3 in zip(candidates, votes, percent_list):
    print('%-20s %-20s %s' % (x, x2, x3))

print("\nTotal:      ", total_votes)
print("Average:    ", average_votes)
most_votes_index = votes.index(max(votes))
least_votes_index = votes.index(min(votes))
print("\nWinner:         ", candidates[most_votes_index])
print("Lowest Votes:   ", candidates[least_votes_index])


