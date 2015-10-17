#Create a character array that will hold the various attributes that a user can pick from when chooising their
#career path.
print "Chooise five attributes that you either possess are are interested in."

#An array that holds the attributes that will be displayed for the user to choose from
attributes = ["patience", "communication", "mathematics", "creativity", "open-minded", "innovative", "artistic-talent", "curiosity", "resilient", "technical-skills"]

#Animator holds the certain attributes for this career
Animator = ["creativity", "open-minded", "artistic-talent", "innovative"]
#Banker holds the certain attributes for this career
Banker = ["mathematics", "resilient", "communication"]
#Software holds the certain attributes for this career
Software = ["communication", "technical-skills", "innovative"]
#Doctor holds the certain attributes for this career
Doctor = ["communication", "patience", "resilient"]
#Designer holds the certain attributes for this career
Designer = ["open-minded", "curiosity", "innovative", "artistic-talent"]



#Create a function that will ask the user for their top five choices
def Choice(array, Animator, Banker, Software, Doctor, Designer):
    #Hold the number of attributes that match the animation career
    Animator_count = 0
    #Hold the number of attributes that match the banker career
    Banker_count = 0
    #Hold the number of attributes that match the software career
    Software_count = 0
    #Hold the number of attributes that match the doctor career
    Doctor_count = 0
    #Hold the number of attributes that match the designer career
    Designer_count = 0
    #Array that holds the attributes that the user have previously chosen
    Chosen = []
    
    #Index will keep count the number choice the user is on
    index = 1
    #Print the attributes the user can choose from
    print array
    #Create a loop that will ask the user for their choice five times
    while index < 6:
        #Print a statement telling the user their number choice
        print "Choice", index, ": "
        #Get the user's input and set it to the variable choice
        choice = raw_input( )
        
        #Create a infinite loop that will run if the user inputs a invalid choice
        while choice not in array:
            #Print a statement telling the user they can only choose from the list above
            print "Can only choose from the list above."
            #Get the user's input and set it equal to choice
            choice = raw_input( )
            #Create a if statement that checks if the user's input is valid
            if choice in array:
                #If true, break the loop
                break
        #Create a infinite loop that will run if the user inputs a choice previously chosen
        while choice in Chosen:
            #Print a statement telling the user they already choice this, and to choose another
            print "You already chose this, choose another."
            #Get the user's input and set it equal to the variable choice
            choice = raw_input( )
            #Create a if statement that checks if choice has not been previously picked
            if choice not in Chosen:
                #If true, break the loop
                break
        #Append choice to the Chosen array so we can account for the user's choices already picked
        Chosen.append(choice)
        
        #Create a if statement that checks if choice is an attribute of an animator
        if choice in Animator:
            #If true, increment the count by one
            Animator_count+=1
        
        #Create a if statement that checks if choice is an attribute of a banker
        if choice in Banker:
            #If true, increment the count by one
            Banker_count+=1

        #Create a if statement that checks if choice is an attribute of software
        if choice in Software:
            #If true, increment the count by one
            Software_count+=1

        #Create a if statement that checks if choice is an attribute of doctor
        if choice in Doctor:
            #If true, increment the count by one
            Doctor_count+=1

        #Create a if statement that checks if choice is an attribute of designer
        if choice in Designer:
            #If true, increment the count by one
            Designer_count+=1
        
        #Increment index by one
        index+=1

    #Create an array that will hold the counts for each career
    results = [Animator_count, Banker_count, Designer_count, Doctor_count, Software_count]
    #Sort the results array, so we know what the top 3 career choices are
    results2 = sorted(results)
    #Create a index of zero that will loop through the first 3 indexes in results
    index = 0
    #Print a statement telling the user their top 3 career choices are
    print "Based on your attributes your top 3 career choices are: "
    print " "
    size = len(results2)
    one = "Banker"
    two = "Animator"
    three = "Designer"
    four = "Doctor"
    five = "Software Engineer"
    #Create a while loop that will loop through the first three indexes in the results array
    career = []
    while index < 3:
        #If the index of the result is equal to animator, print a statement telling the user so
        if results2[size-1] == Animator_count and two not in career:
            print two
            career.append(two)
        
        #If the index of the result is equal to animator, print a statement telling the user so
        elif results2[size-1] == Banker_count and one not in career:
            print one
            career.append(one)
        #If the index of the result is equal to designer, print a statement telling the user so
        elif results2[size-1] == Designer_count and three not in career:
            print three
            career.append(three)

        #If the index of the result is equal to doctor, print a statement telling the user so
        elif results2[size-1] == Doctor_count and four not in career:
            print four
            career.append(four)
        #If the index of the result is equal to software, print a statement telling the user so
        elif results2[size-1] == Software_count and five not in career:
            print five
            career.append(five)
        #Increment index by one
        index+=1
        size-=1



#Call the Choice function to run the program
Choice(attributes, Animator, Banker, Software, Doctor, Designer)
