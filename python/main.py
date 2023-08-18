import ProgressBar
import time

#Creating a new instance
barr = ProgressBar.ProgressBar(width = 10, finalCount = 100, emptyChar = " ", progressChar = "#", showPercentage = True)

#Adding custom brackets
bracket_index = barr.add_brackets("T", "T")

#Setting the new brackets
barr.set_brackets(bracket_index)

#Doing some work
for i in range (100):
    barr.tick()
    time.sleep(0.05)
