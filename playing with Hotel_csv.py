
"""---PLEASE NOTE THAT THE PROGRAM WRITTEN BY NABHAM GUPTA IS CASE SENSITIVE TO THE INPUT BE CAREFULL WITH CAPS and small letter---"""

# Could have typecasted everything to lower case but i didn't !  SORRY FOR THAT 
# Rule of programming, if the code works don't touch it X'D. Just kidding!  U can play with my_code

import csv

hotel_csv = "hotels.csv"
state = input("What is the state(Karnataka/Tamilnadu/Maharashtra which will give result for the corresponding state or India can also be an input which will perform the operation on all the states): ")
choice = input("Cost or Rating: ") # basically column 3 or 4
operation = input("Operation cheapest/highest/average: ")

lis1 = []
hotelCodes = []

with open('hotels.csv', "r") as f:
    lines = csv.reader(f)

    def columnAvg(column_index):
      num1 = float(line[column_index])
      lis1.append(num1)
      average = sum(lis1)/len(lis1)
      #return 'The average is:', average
      return average



    def high_low(column_index):
      var1 = float(line[column_index])
      lis1.append(var1)
      hotel_code = line[1]
      hotelCodes.append(hotel_code)

      if(operation == "highest"):
        highest = max(lis1)
        highest_index = lis1.index(highest)
        k = [highest, highest_index]
        return k

      if(operation == "cheapest"):
        cheapest = min(lis1)
        cheapest_index = lis1.index(cheapest)
        return [cheapest, cheapest_index]

  
 # First state selection code
    for line in lines:
      # reads the data from csv file line by line
      if line[2] == state:
        # Matching user input state with our table states...
        if (choice == "Cost"):
          # select column 3 because cost is in 3 index of our table, pass content of column 3 for the operations.
          if (operation == "average"):
            # call average function
            column_3 = columnAvg(3)

          elif(operation == "cheapest" or operation == "highest"):
            # call high_low function
            column_3= high_low(3)
            value = column_3[0]
            indexofvalue = column_3[1]

          else:
            print("invalid input")              # WHEN THE INPUT IS NOT AS ESPECTED 

        if choice == "Rating":
          # select column 4 because ratings is given in column 4 of hotels.csv file
                  if operation == "average":
                      column_4 = columnAvg(4)
                  elif(operation == "cheapest" or operation == "highest"):
                  # call high_low function
                    column_4= high_low(4)
                    rone = column_4[0]
                    indexofvalue = column_4[1]
                  else:
                    print("invalid input")
 #-------------------------------------------------------------------------------------------------
      elif (state == "India"):  # FOR CASE INDIA : DO NOT COMPARE FOR STATES
        for line in lines:
          if(choice == "Cost"):
            if (operation == "average"):
              # call average function
              column_3 = columnAvg(3)

          elif(operation == "cheapest" or operation == "highest"):
            # call high_low function
            column_3= high_low(3)
            value = column_3[0]
            indexofvalue = column_3[1]

          else:
            pass         # BUG here resolved !!!
            #print("invalid input")              # WHEN THE INPUT IS NOT AS ESPECTED 

        if choice == "Rating":
          # select column 4 because ratings is given in column 4 of hotels.csv file
                  if operation == "average":
                      column_4 = columnAvg(4)
                  elif(operation == "cheapest" or operation == "highest"):
                  # call high_low function
                    column_4= high_low(4)
                    rone = column_4[0]
                    indexofvalue = column_4[1]
                  else:
                    print("invalid input")
        pass

     

   
# PRINTING STUFF WRITTEN BELOW (check out the given printing format in the question.)

if (operation == "average"):      # for opeartion as average
    if choice == "Rating":
      print('Average rating of hotel in ' + state + ' is ' + str(column_4))   # BUG HERE @ Resolved !!!
    if choice == "Cost":
      print('Average cost of hotel in ' + state + ' is ' + str(column_3))

elif (operation == "highest" or "cheapest"):       # when operation entered is highest or cheapest
    if choice == "Cost":
      print('Hotel with ' + operation + '' + ' price in ' + state + ' is ' + indexofvalue + ' with price ' + value)
    if choice == "Rating":
      print('Hotel with ' + operation + '' + ' rating in ' + state + ' is ' + str(indexofvalue) + ' with rating ' + str(rone))
      


















