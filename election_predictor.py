#this program takes a set of parameters and uses these to predict the outcome of the election
from matplotlib import pyplot as plt
from decimal import Decimal

#For each age group, show the polling predictions for likelihood to vote conservative, brexit, lib-dem, labour. Likelihoods are shown as decimals. This won't total to 1, as it excludes Other.
eighteen_to_twentyfour = [.25, .03, .12, .48]
twentyfive_thirtyfour = [.22, .04, .15, .46]
thirtyfive_fiftyfour = [.40, .04, .17, .30]
fiftyfive_sixtyfour = [.47, .05, .15, .26]
sixtyfive_plus = [.61, .03, .14, .17]

#Polling predictions for likelihood of Scottish voters to vote for each main party (all age groups)
snp = .44
scot_tories = .26
scot_lab = .16
scot_lib = .11
scot_turnout = .66

# total_electorate = 45775800
england_electorate = 38371400
wales_electorate = 2230100
scotland_electorate = 3925800
nireland_electorate = 1248400

#number of voters (UK) by age (000) - broken down by specific age (e.g. 18), so I will create a function to add the specific ages.
electorate_eighteen_to_twentyfour = [385, 401, 411, 426, 432, 434, 448]
electorate_twentyfive_thirtyfour = [447, 457, 471, 463, 454, 455, 440, 448, 447, 434]
electorate_thirtyfive_fiftyfour = []
electorate_fiftyfive_sixtyfour = [449, 440, 424, 406, 396, 387, 371, 357, 342, 341]
# I already know that the total number of people over 65 is 8200000
def calculate_total_voters(group):
    total = 0
    for item in group:
            total += item
    return total * 1000

youngest = calculate_total_voters(electorate_eighteen_to_twentyfour)
second_youngest = calculate_total_voters(electorate_twentyfive_thirtyfour)
second_oldest = calculate_total_voters(electorate_fiftyfive_sixtyfour)
oldest = 8200000

def check_uk_electorate():
    total = england_electorate + scotland_electorate + wales_electorate + nireland_electorate
    return total

total_electorate = check_uk_electorate()

#the group 35-54 was much bigger than the others, so rather than counting 20 numbers, I have calculated the number of these voters by subtracting the other groups from the total electorate
def calculate_third_group():
    rest = youngest + second_youngest + second_oldest + oldest
    return total_electorate - rest

third_youngest = calculate_third_group()

#likelihood to vote (%)
turnout_eighteen_twentyfour = .58
turnout_twentyfive_thirtyfour = .63
turnout_thirtyfive_fiftyfour = .66
turnout_fiftyfive_sixtyfour = .74
turnout_sixtyfive_plus = .80

def calculate_number_of_voters(group, turnout):
    voters = Decimal(group) * Decimal(turnout)
    return round(voters)

youngest_voters = calculate_number_of_voters(youngest, turnout_eighteen_twentyfour)
second_youngest_voters = calculate_number_of_voters(second_youngest, turnout_twentyfive_thirtyfour)
thirtyfive_fifty_four_voters = calculate_number_of_voters(third_youngest, turnout_thirtyfive_fiftyfour)
fiftyfive_sixtyfour_voters = calculate_number_of_voters(second_oldest, turnout_fiftyfive_sixtyfour)
oldest_voters = calculate_number_of_voters(oldest, turnout_sixtyfive_plus)

def count_all_voters():
    total = youngest_voters + second_youngest_voters + thirtyfive_fifty_four_voters + fiftyfive_sixtyfour_voters + oldest_voters
    return round(total)
total_turnout = count_all_voters()

def count_tory_vote(poll, group):
    vote = poll[0] * group
    return round(vote)

youngest_tory_vote = count_tory_vote(eighteen_to_twentyfour, youngest_voters)
second_youngest_tory_vote = count_tory_vote(twentyfive_thirtyfour, second_youngest_voters)
thirtyfive_fifty_four_tory_vote = count_tory_vote(thirtyfive_fiftyfour, thirtyfive_fifty_four_voters)
fiftyfive_sixtyfour_tory_vote = count_tory_vote(fiftyfive_sixtyfour, fiftyfive_sixtyfour_voters)
oldest_tory_vote = count_tory_vote(sixtyfive_plus, oldest_voters)

total_tory_vote = youngest_tory_vote + second_youngest_tory_vote + thirtyfive_fifty_four_tory_vote + fiftyfive_sixtyfour_tory_vote + oldest_tory_vote

print("The predicted total Tory vote is {}.".format(total_tory_vote))

def count_labour_vote(poll, group):
    vote = poll[3] * group
    return round(vote)

youngest_labour_vote = count_labour_vote(eighteen_to_twentyfour, youngest_voters)
second_youngest_labour_vote = count_labour_vote(twentyfive_thirtyfour, second_youngest_voters)
thirtyfive_fifty_four_labour_vote = count_labour_vote(thirtyfive_fiftyfour, thirtyfive_fifty_four_voters)
fiftyfive_sixtyfour_labour_vote = count_labour_vote(fiftyfive_sixtyfour, fiftyfive_sixtyfour_voters)
oldest_labour_vote = count_labour_vote(sixtyfive_plus, oldest_voters)

total_labour_vote = youngest_labour_vote + second_youngest_labour_vote + thirtyfive_fifty_four_labour_vote + fiftyfive_sixtyfour_labour_vote + oldest_labour_vote
print("The predicted total Labour vote is {}.".format(total_labour_vote))

def count_brexit_vote(poll, group):
    vote = poll[1] * group
    return round(vote)

youngest_brexit_vote = count_brexit_vote(eighteen_to_twentyfour, youngest_voters)
second_youngest_brexit_vote = count_brexit_vote(twentyfive_thirtyfour, second_youngest_voters)
thirtyfive_fifty_four_brexit_vote = count_brexit_vote(thirtyfive_fiftyfour, thirtyfive_fifty_four_voters)
fiftyfive_sixtyfour_brexit_vote = count_brexit_vote(fiftyfive_sixtyfour, fiftyfive_sixtyfour_voters)
oldest_brexit_vote = count_brexit_vote(sixtyfive_plus, oldest_voters)

total_brexit_vote = youngest_brexit_vote + second_youngest_brexit_vote + thirtyfive_fifty_four_brexit_vote + fiftyfive_sixtyfour_brexit_vote + oldest_brexit_vote
print("The predicted total Brexit Party vote is {}.".format(total_brexit_vote))
brexit_percentage = round((total_brexit_vote / total_turnout) * 100)
print("The Brexit Party got {}% of the vote.".format(brexit_percentage))

def count_lib_vote(poll, group):
    vote = poll[2] * group
    return round(vote)

youngest_lib_vote = count_lib_vote(eighteen_to_twentyfour, youngest_voters)
second_youngest_lib_vote = count_lib_vote(twentyfive_thirtyfour, second_youngest_voters)
thirtyfive_fifty_four_lib_vote = count_lib_vote(thirtyfive_fiftyfour, thirtyfive_fifty_four_voters)
fiftyfive_sixtyfour_lib_vote = count_lib_vote(fiftyfive_sixtyfour, fiftyfive_sixtyfour_voters)
oldest_lib_vote = count_lib_vote(sixtyfive_plus, oldest_voters)

total_lib_vote = youngest_lib_vote + second_youngest_lib_vote + thirtyfive_fifty_four_lib_vote + fiftyfive_sixtyfour_lib_vote + oldest_lib_vote
print("The predicted total Lib Dem vote is {}.".format(total_lib_vote))
lib_percentage = round((total_lib_vote / total_turnout) * 100)
print("The Lib Dems got {}% of the vote.".format(lib_percentage))

def count_snp_vote():
    vote = snp * scot_turnout * scotland_electorate
    return round(vote)

snp_vote = count_snp_vote()
print("The predicted SNP vote is {}.".format(snp_vote))

labour_percentage = round((total_labour_vote / total_turnout) * 100)
tory_percentage = round((total_tory_vote / total_turnout) * 100)

def announce_result():
    winner = ""
    loser = ""
    winner_percentage = 0
    loser_percentage = 0
    if total_labour_vote > total_tory_vote:
        winner = "Labour"
        loser = "Conservative"
        winner_percentage = labour_percentage
        loser_percentage = tory_percentage
    else:
        winner = "Conservative"
        loser = "Labour"
        winner_percentage = tory_percentage
        loser_percentage = labour_percentage
    return "The winners are the {winner} Party. They got {winner_percentage}% of the vote. The losers are the {loser} Party. They got {loser_percentage}% of the vote. ".format(winner=winner, winner_percentage=winner_percentage, loser=loser, loser_percentage=loser_percentage)

print(announce_result())
party = ["Tory", "Brexit Party", "Lib Dem", "Labour", "SNP"]
share_of_vote = [tory_percentage, brexit_percentage, lib_percentage, labour_percentage, snp]
plt.plot(party, share_of_vote)
plt.show()
