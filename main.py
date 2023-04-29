myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
answer = round(myBill / numberOfPeople)
print("You all owe", answer)
tip = int(input("What percent do you want ot leave: 15,18, or 20 percent?"))
bill_with_tip = tip /100 * myBill + myBill
bill_per_person = bill_with_tip / numberOfPeople
final_amount = round(bill_per_person, 2)
print("You all owe", final_amount)