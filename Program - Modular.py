#0.
def Read_File():
        Sales = [] #Creates an empty array called 'Sales'
        with open("Choral Shield Data File(TXT).txt","r") as File: #Opens the file and reads from it
                for line in File: #The loop cycles through each line and...
                        Sales.append(line.strip().split(',')) #slipts up the elements and adds it to the 'Sales' array
        return Sales #Passes the 'Sales' array to be used later on in the program

#1.
def Get_Popular_Purchase_Method(Sales): #The module calls the parameter 'Sales' (array)
        OccurrenceOfSchool = 0 #The variable 'OccurrenceOfSchool' is set to 0, This is used to count how many time 'S' shows up
        for counter in range(len(Sales)): #This section of code will repeat for the length of the array 'Sales'
                if Sales[counter][3][0] == 'S': #Checks if the third field of the first letter is equal to 'S'
                        OccurrenceOfSchool = OccurrenceOfSchool+1 #If the element being iterated through is equal to 'S' it will add 1 to the count ('OccurrenceOfSchool')

        OccurrenceOfWebsite = 0 #The variable 'OccurrenceOfWebsite' is set to 0, This is used to count how many time 'W' shows up
        for counter in range(len(Sales)): #This section of code will repeat for the length of the array 'Sales'
                if Sales[counter][3][0] == 'W': #Checks if the third field of the first letter is equal to 'W'
                        OccurrenceOfWebsite = OccurrenceOfWebsite+1 #If the element being iterated through is equal to 'W' it will add 1 to the count ('OccurrenceOfWebsite')

        PopularMethod = 0 #The variable 'PopularMethod' is set to 0
        if OccurrenceOfWebsite > OccurrenceOfSchool: #Checks if the number of times Website shows up is greater than the number of time Schools shows up
                PopularMethod = "Website" #If so it'll set the 'PopularMethod' to Website (As Website has shown uo more times)
        if OccurrenceOfSchool > OccurrenceOfWebsite: #Checks if the number of times School shows up is greater than the number of time Website shows up
                PopularMethod = "School" #If so it'll set the 'PopularMethod' to School (As School has shown uo more times)
        if OccurrenceOfSchool == OccurrenceOfWebsite: #Checks if the number of times Website shows up is eqaul to the number of time Schools shows up
                Equal = True #If there is no popular method e.i. equal numbers of people buying from school and the website, it'll set the variable 'Equal' to True
        else: #Otherwise (A popular method was found) it will...
                Equal = False #Set the variable 'Equal' to False
        return PopularMethod, Equal #Passes the varibales 'PopularMethod' and 'Equal' as they will have to be used later in the program

#2.
def Get_Total_Price(Sales): #The module calls the variable 'Sales' to be used in the program
        WTtickets = [] #Creates an empty array called 'WTtickets'
        Ftickets = [] #Creates an empty array called 'Ftickets'
        for counter in range(len(Sales)): #This section of code will repeat for the length of the array 'Sales'
                if Sales[counter][1][0] == 'W' or Sales[counter][1][0] == 'T': #Checks if the first letter of the first element of the record is equal to 'W' or 'T'
                        WTtickets.append(Sales[counter][2]) #Adds the number of tickets the user has bought to an array
                elif Sales[counter][1][0] == 'F':
                        Ftickets.append(Sales[counter][2]) #Adds the number of tickets the user has bought to an array

        WTtickets = list(map(int, WTtickets)) #The array 'WTtickets' is converted to an integer array
        Ftickets = list(map(int, Ftickets)) #The array 'Ftickets' is converted to an integer array

        WTsum = sum(WTtickets) #Adds up all of the values in the array to sum up hwo many tickets were bought on Wednesday and Thursday
        Fsum = sum(Ftickets) #Adds up all of the values in the array to sum up hwo many tickets were bought on Friday
        Total = (5*WTsum)+(10*Fsum) #Calculates the total money raised by charity
        return Total #Passes the variable 'Total' to be used later in the program

#3.
def Export_Fridays_Sales(Sales): #The module calls the variable 'Sales' to be used in the program
        import csv #Imports a module to be used (for .csv files)
        Friday = [] #Creates an empty array called 'Friday'
        for counter in range(len(Sales)): #This section of code will repeat for the length of the array 'Sales'
                if Sales[counter][1][0] == 'F': #Checks if the first letter of the first element is an 'F' (As that would mean it was bought on friday)
                        Friday.append(Sales[counter]) #Adds the record to the array
        with open("FridayNightData.txt","w") as Export: #Creates a file called 'FridayNightData.txt'
                (csv.writer(Export)).writerows(Friday) #Adds the array (holding all of Friday night's data) to the file

#4.
def Displays_Results(PopularMehtod, Total, Equal): #The module calls the variables 'PopularMehtod', 'Total' & 'Equal' to be used in the program
        import datetime #Imports the module for times
        now = datetime.datetime.now() #creates a variable to contian the current time
        print("\nEssell Academy Choral Shield %d" % now.year) #Displays the title with the current year
        if Equal == True: #Check if 'Equal' is True (If there were no popular mehtods)
                print("\n\nThere is no ‘popular’ method of buying tickets,\nan equal number of people bought from the school and the website.") #Tells user there was no popular results
                print("\nThe total money raised for charity is £{0}".format(Total)) #Displays total
        else: #Otherwise (Equal is not equal to True), so there is a popular method
                print("\n\nThe most popular method of sales is {0}".format(PopularMethod)) #Displays popular method
                print("\nThe total money raised for charity is £{0}".format(Total)) #Displays total

#Main_Program
Sales = Read_File()
PopularMethod, Equal = Get_Popular_Purchase_Method(Sales)
Total = Get_Total_Price(Sales)
Export_Fridays_Sales(Sales)
Displays_Results(PopularMethod, Total, Equal)
