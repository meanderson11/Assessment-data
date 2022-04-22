log_file = open("um-server-01.txt") 
#This allows the "um-server-01.txt" file to be opend and saved into the 'log_file that is a variable file.

def sales_reports(log_file): 
    # This is a function that is called sales_report. This can access the content in the text file.

    for line in log_file:
        #This line loops through every variable line.

        line = line.rstrip()
        #This function is used method returns a copy of the string with trailing characters removed.

        day = line[0:3]  # This returns the first through fourth element of line and assigns it to the day variable

        if day == "Tue":
            print(line)
            #This prints line if day = tue

sales_reports(log_file)
 #This calls the sales_report function that was created earlier.  It passes log_file as an argument

def sale_reports(log_file):

    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
         
        if day == "Mon":
            print(line)

sale_reports(log_file)

