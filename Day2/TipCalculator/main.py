#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.??

#Write your code below this line ??

print("Welcome to the Tip Calculator.")

total_bill = float(input("What was your total bill ? "))
tip_percentage = float(input("What percentage tip would you like to give ? 10, 12, 15 or other? "))
total_people = int(input("How many people to split the bill? "))

# tip_amount = (total_bill * tip_percentage)/100
# total_bill = total_bill + tip_amount
# bill_share = round((total_bill + ((total_bill * tip_percentage)/100)) / total_people,2)
bill_share = "{:.2f}".format((total_bill + ((total_bill * tip_percentage)/100)) / total_people)

print(f"Each person should pay: ${bill_share}")