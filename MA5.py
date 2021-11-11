# muzammil lab 12 MA5.py
# I declare that I did not collaborate with anyone in this micro-assignment. 
# Besides the lab and class notes, I used the following resources: 


import sqlite3
import matplotlib.pyplot as plt
connection = None
cursor = None

def connect(path):
    # using global variables already defined in main method, not new variables
    global connection, cursor
    # create a connection to the sqlite3 database
    connection = sqlite3.connect(path)
    # create a cursor object which will be used to execute sql statements
    cursor = connection.cursor()
    # execute a sql statement to enforce foreign key constraint
    cursor.execute(' PRAGMA foreign_keys=ON; ')
    # commit the changes we have made so they are visible by any other connections
    connection.commit()
    return

def query1():
    # using globally define dconnection and cursor
    global connection, cursor
    
    # define the sql query string with variables
    query = '''SELECT C.NEIGHBOURHOOD, SUM(C.FEMALE)/CAST(SUM(C.MALE) AS FLOAT)
    FROM Census2014 C
    GROUP BY C.NEIGHBOURHOOD
    HAVING SUM(C.MALE)+SUM(C.FEMALE)>:num1 AND SUM(c.MALE)>0'''
    
    number=int(input("what is the threshold value?"))
    
    # execute query with provided flags
    cursor.execute(query, {'num1':number})
    
    # get list of tuples
    rows = cursor.fetchall()
    # need list of years and revenues for plotting pie chart
    NEIGHBOURHOOD = []
    ratio = []
    # iterate through results to build lists
    for row in rows:
        NEIGHBOURHOOD.append(row[0])
        ratio.append(row[1])
        
    # pass lists to plotting functions to generate and save charts
    pie_chart(NEIGHBOURHOOD, ratio, 'Query 1 Pie Chart')
    bar_chart(NEIGHBOURHOOD, ratio, 'Query 1 Bar Chart', 'NEIGHBOURHOOD', 'ratio')
    connection.commit()
    
    return

def query2():
    # using globally define dconnection and cursor
    global connection, cursor
    
    # define the sql query string with variables
    query = '''SELECT '2009' AS YEAR, SUM(C.FEMALE),SUM(C.MALE)
               FROM   CENSUS2009 AS C
               WHERE  C.AGE>=:min_age AND C.AGE<=max_age
               UNION
               SELECT '2012' as YEAR,SUM(C.FEMALE),SUM(C.MALE)
               FROM   CENSUS2012 AS C
               WHERE  C.AGE>=:min_age AND C.AGE<=max_age
               UNION
               SELECT '2014' AS YEAR,SUM(C.FEMALE),SUM(C.MALE)
               FROM   CENSUS2014 AS C
               WHERE  C.AGE>=:min_age AND C.AGE<=max_age
               UNION
               SELECT '2016' AS YEAR,SUM(C.FEMALE),SUM(C.MALE)
               FROM   CENSUS2016 AS C
               WHERE  C.AGE>=:min_age AND C.AGE<=max_age
               
               '''
    
    # need to get two inputs from user for year range
    max_age=int(input("What is the max AGE?"))
    min_age=int(input("what is the min AGE?"))
    
    # execute query with provided years
    cursor.execute(query, {'min_age': min_age , 'max_age': max_age})
    
    # get list of tuples
    rows = cursor.fetchall()
    # need list of years and revenues for plotting pie chart
    years = []
    sum_female = []
    sum_male=[]
    # iterate through results to build lists
    for row in rows:
        years.append(row[0])
        sum_female.append(row[1])
        sum_male.append(row[2])
        
    # pass lists to plotting functions to generate and save charts
    bar_chart2(sum_male,sum_female, years, 'Query 2 Bar Chart', 'Years', 'SUMS')
    connection.commit()
    
    return

# define pie chart plotting function
# takes list of values and labels and title string
# saves pie chart to file
def pie_chart(values, labels, title):
    # see matplotlib website for more details
    # https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html
    
    # if lists empty, print warning
    if len(values) < 1:
        print('Warning: empty input so generated plot will be empty')
        
    # create a pie chart
    plt.pie(values, # these are the values that will make up the pie slices
            labels=labels, # these are names/labels for each slice
            autopct='%1.1f%%') # putting fomatted percent values on slices
    
    # give plot a title
    plt.title(title)
    
    # save plot to file
    # we'll use passed title to give file name
    path = './{}_piechart.png'.format(title)
    plt.savefig(path)
    print('Chart saved to file {}'.format(path))
    
    # close figure so it doesn't display
    plt.close()
    return

# define bar chart plotting function
# takes list of values and labels and title string
# saves plot to file
def bar_chart(values, labels, title, x_label, y_label):
    # see matplotlib website for more details
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html
    
    # if lists empty print warning
    if len(values) < 1:
        print('Warning: empty input so generated plot will be empty')
    
    # create bar chart
    plt.bar(range(len(values)), # x coordinates of bars will be 0, 1,... len(values)-1
            values, # height of bars will be values
            tick_label=labels) # label bars with years
    
    # label x and y axis
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    
    # give plot a title
    plt.title(title)
    
    # save plot to file
    # we'll use passed title to give file name
    path = './{}_barchart.png'.format(title)
    plt.savefig(path)
    print('Chart saved to file {}'.format(path))
    
    # close figure so it doesn't display
    plt.close()
    return

def bar_chart2(male_values, female_values, years, title, x_label, y_label):
    # see matplotlib website for more details
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html
    
    # if lists empty print warning
    if len(years) < 1:
        print('Warning: empty input so generated plot will be empty')
        
    xs = list(range(len(years)))
    width = 0.35
    x_male = [x - width/2 for x in xs]
    x_female = [x + width/2 for x in xs]
    
    
    fig, ax = plt.subplots()
    
    ax.bar(x_male, male_values, width, label='Male')
    ax.bar(x_female, female_values, width, label='Female')
    
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.set_xticks(xs)
    ax.set_xticklabels(years)
    ax.legend()
    
    # save plot to file
    # we'll use passed title to give file name
    path = './{}_barchart2.png'.format(title)
    plt.savefig(path)
    print('Chart saved to file {}'.format(path))
    
    # close figure so it doesn't display
    plt.close()
    return
    
# define the main method that will run when our python program runs
def main():
    global connection
    # we will hard code the database name, could also get from user
    db_path = './ma5.db'
    # create connection using function defined above
    connect(db_path)
    # loop program until user chooses to exit
    while(True):
        # prompt user to selet query
        print('\nPlease select query to execute')
        print('1. ratio of female over male residents for each neighbourhood')
        print('2. change of male and female residents in a given age range over 2009-2016')
        print('3. Exit program')
        query_selection = input('Selection: ')
        # input function will return string so compare to strings
        if query_selection == '1':
            query1()
        elif query_selection == '2':
            query2()
        # if user selects 3 break program while loop and exit program
        elif query_selection == '3':
            print('Goodbye :)')
            break
        # if user enters anything but 1, 2, or 3 prompt for valid input
        else:
            print("\nInvalid input!\nSelection must be 1, 2, or 3")
    
    # close connection before exiting
    connection.close()
  
# run main method when program starts
if __name__ == "__main__":
    main()
