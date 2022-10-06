'''Prints a histogram for a distribution of letter grades 
computed from a collection of numeric grades extracted from a text file.'''
from maphist import Histogram
def main():
    # Create a Histogram instance for computing the frequence
    gradeHist = Histogram('ABCDF')

    # Open a text file containing the grades
    gradeFile = open('cs101grades.txt', 'r')

    # Extract the grades and increment the appropreate counter
    for line in gradeFile:
        grade = int(line)
        gradeHist.incCount(letterGrade(grade))
    
    # Print the Histogram Chart
    printChart( gradeHist )

# Determines the letter grade for the given numeric value
def letterGrade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 90:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

# Prints the histogram as Horizental bar chart
def printChart(gradeHist):
    print("             Grade distribution")
    
    # Print the body of the chart
    letterGrades = ('A','B','C','D','F')
    for letter in letterGrades:
        print('   |')
        print() 
    



