# Bill Split Calculator

print("--- Bill Split Calculator ---")

amount = float(input("Enter Amount: $"))
tip = float(input("Enter Tip Amount: $"))
no_of_people = int(input("Enter No. of People: "))

total_tip = (tip / 100) * amount
total_amount = total_tip + amount

print(f'Total Amount(Including Tip): ${total_amount}') 

amount_per_person = total_amount / no_of_people
print(f'Each Person pays : ${amount_per_person}')

print("------------------------------")
