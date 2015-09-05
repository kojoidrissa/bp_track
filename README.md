#Bloodpressure tracker
##Phase 0.5
CLI script app (Python, later JavaScript, writing to a CSV file?) to track the following:

-  Systolic pressure
-  Diastolic pressure
-  Heart rate
-  iso date (2015-05-09)
-  iso time (18:26:26)

###Data structure
I want to keep track of various stats, be able to chart them over time, but also deal with possible multiple measurements in a single day (BP). Ideas:
-  I might need a dictionary for each day and have those each added to a list.
-  How would I set up a database table to track this? Then, which columns and values would I use for charting & comparing over time?
    +  For now, one table for BP, another for other info. Use date as key for time series comparison.


##Phase 1
Simple web app (JavaScript writing to a text file? Meteor? Flask writing to a text file?) to track the same stats as 0.5

##Phase 2
-  Write to a database instead of a text file
-  Visualize the trends of Phase 1

##Phase 3
-  Decided what other health/biometric data to track/record like steps or amount of exercise
