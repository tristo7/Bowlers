"""
program: bowlers.py
date: 11/18/13
purpose:
to take in a text file with bowlers and their scores, then return a
text file that states whether they where above the average or
below it
"""

#function to get the average of the amount of points
def get_avrg(avrg):
    avrg = list(avrg)
    total = 0
    average = 0
    for i in range(len(avrg)):
        total += float(avrg[i])
    average = total/(len(avrg))
    return average


#open doc, read it, turn into a list
scores = open('bowlingscores.txt', 'r')
bowlers = scores.read()
bowlerlist = bowlers.split()

#create a list of the point values
points = []
for i in range(1, len(bowlerlist), 2):
    points.append(bowlerlist[i])
    
#get the average from function
average = get_avrg(points)
#create a dictionary, then loop it to set values for the bowlers
dictionary = {}
output = ''
for i in range(0, len(bowlerlist), 2):
    dictionary[bowlerlist[i]] = float(bowlerlist[i+1])
for key in dictionary.keys():
    if dictionary[key]==300:
        output += key + " scored a perfect game!\n"
    elif dictionary[key]<average:
        output += key + " scored below average.\n"
    elif dictionary[key]>average:
        output += key + " scored above average.\n"
    elif dictionaru[key]==average:
        output += key + " scored exactly average.\n"

#create/open the destination txt file for writing
score_averages = open('bowlingaverage.txt', 'w')

#write output to the file
score_averages.write(output)

#close all relevant files to be tidy
scores.close()
score_averages.close()
    
