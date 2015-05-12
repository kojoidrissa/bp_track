import csv

systolic = int(input("Enter your systolic pressure: "))
dias = int(input("Enter your diastolic pressure: "))
heart = int(input("Enter your heart rate: "))

#Capturing the date/time information as strings for now. I'll work out
#converting them into date/time objects later. Probably after I 
#connect this to a database. Now it's just text logging
bp_date = str(input("Enter the date in ISO format (2015-05-09)--> "))
bp_time = str(input("Enter the time in ISO format (18:26:26)--> "))

#Realized I should capture weight and number of steps for the day
#Weight will be in Kilos; I can convert to LBs later if I want
##at some point, I'll want to add something that asks 
##which unit you're using
weight_kg = int(input("Enter your weight in kilograms: "))
#A proxy for exercise/activity; a trend worth tracking to correlate w/
#blood pressure fluctuations
steps = int(input("Enter your steps for the day: "))
