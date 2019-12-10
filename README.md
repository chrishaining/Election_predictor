# Election Predictor

This is a small program I worked on to develop my skills in Python variables, functions, lists and graphs.

Confession :innocent: - the title is a big overstatement. Rather, what this program does is as follows:
  * Estimates the number of votes, and percentage share of the total vote, for five political parties: Conservative, Labour, Brexit Party, Lib Dems and SNP (I'm writing the program in Scotland, hence the inclusion of the SNP).
  * The program is to be used for the 2019 UK General Election.
  * The program combines polling data, turnout figures from the 2017 UK General Election, plus population data. The figures I use are very rough as they are my memories from what I have been reading. The purpose of this program was to practise my Python skills, not to have totally accurate data. To find out the data, go to the Links section below.

The predictor does not take into account that the number of votes does not directly translate into the number of seats. In real life, the party with the most seats wins, even if they do not have the most votes. For example, imagine that:
    * Party A has 50% of the votes, but has fewer seats than Party B. In real life, Party B would win, but my program would predict that Party A would win.
The reason my program does not take such situations into account is because of the nature of the polling data.

## What you need to run the file
* Python version 3
* matplotlib and decimal packages

## Links
To see what the real data are:
* [General election poll tracker](https://www.bbc.co.uk/news/uk-politics-49798197)
* [Voting intention: A generational divide?](https://www.bbc.co.uk/news/election-2019-50543903)
* [ONS population statistics](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/articles/overviewoftheukpopulation/august2019)

## Future developments
If I had more time, the top changes I'd like to make are:
* Refactor the variable names, so that they make sense to others.
* Structure the data differently, so that there are fewer parts to the program. For example, having separate variables for different aspects of each group adds a lot of code. Perhaps I could use [tuples](https://docs.python.org/3/c-api/tuple.html).
* Refactor the functions so that they can be used for different datasets.
* Learn more about how to use graphs with [matplotlib](https://matplotlib.org/).
