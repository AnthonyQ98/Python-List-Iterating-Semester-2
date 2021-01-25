"""
Anthony Quinn
25 Jan 2021
Week 1 Lab 2 Exercises
Lists
"""
# Exercise 1

"""
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
"""

# Exercise 2
hours = []
days = 0
total = 0
hours_worked = 1
counter = 0
over_six_hours = 0
while counter < 5:
    hours_worked = int(input("Hours worked: "))
    if hours_worked < 9 and hours_worked > 0:
        counter += 1
        total += hours_worked
        hours.append(hours_worked)
        if hours_worked > 6:
            over_six_hours += 1
    else:
        print("Error: Enter a number between 0 and 9.")

for i in range(5):
    print("Day {}: ".format(i) + str(hours[i]) + " hours.")

average = total / counter
print("Average daily hours: ", round(average, 2))
print("Total hours: ", total)
print("Total days with more than 6 hours: ", over_six_hours)




