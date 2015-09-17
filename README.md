# Bowlers
Score Evaluation

This Python script was created as a project in my Fundamentals of Computing class. It was one of the first projects we were assigned to work on independently. The objective of this project was to both read from and write to a text file, as well as create a dictionary.

input from bowlingscores.txt:
>     David
>     102
>     Hector
>     300
>     Mary
>     195
>     Jane
>     160
>     Sam
>     210
>     Tristin
>     295

The script reads in an arbitrary amount of names and scores from a text file. It then creates a list containing both names and scores separating at line breaks. Next, a separate score list (points) is created and passed into a function to calculate the average score for the game.

    def get_avrg(avrg):
    	avrg = list(avrg)
    	total = 0
		average = 0
    	for i in range(len(avrg)):
    		total += float(avrg[i])
    	average = total/(len(avrg))
    	return average
    
This function takes the points list as an argument. It then iterates over the list to get a total. Finally, it returns the average by dividing the total by the number of items in the list.

A dictionary is then used to associate relative scores to the average score. The results are then saved into a new text file.

output from bowlingaverage.txt:
>     Sam scored below average.
>     David scored below average.
>     Hector scored a perfect game!
>     Jane scored below average.
>     Tristin scored above average.
>     Mary scored below average.
