name=(input("Enter Your Name : ")).strip().capitalize()
weight=float(input("Enter Your Weight in (KG) : ").strip())
length=float(input("Enter Your length in (Meter) : ").strip())
bmi=(weight)/(length)**2

if bmi<18.5:
    type="Underweight"
elif bmi<25:
    type="Normal Weight"
elif bmi<30:
    type="Overweight"
else:
   type="Obesity"
print(type)
with open("bmi_result.txt","a") as file:
    file.write(f"Name: {name} , Weight: {weight} , Length: {length} , BMI {bmi:.2f} \n")
print(f"Hello {name} , Your Result Has Been Saved ! ")
