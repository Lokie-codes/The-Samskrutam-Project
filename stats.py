import string
import datetime
# Input filename from user
filename = input("Please Enter the Filename : ")

try:
    with open(filename, 'r') as f:
        # Read file content and clean from punchuations
        lines = f.read()
        cleanWords = [i.strip(string.punctuation) for i in lines.split()]

        # Load current date and time in format
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # Write stats to a stats log file
        with open('stats.log', 'a') as l:
            l.write("{} - {} - Word Count : {}".format(date, filename, len(cleanWords)))

except:
    print("Error Loading file...")
