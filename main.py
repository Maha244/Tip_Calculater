
print("Welcome to the tip calculator.")
bill = input("What was the total bill? ")
tip_percent = input("What percentage tip would you like to give ? 10, 12, or 15 ?  ")
tip_person = input("How many people to split the bill ? ")


tip = float(bill) * (int(tip_percent)/100)
total_bill = float(bill) + tip
each_person_bill = round(total_bill / int(tip_person) , 2)
print(f"Each person pay : ${each_person_bill} ")
