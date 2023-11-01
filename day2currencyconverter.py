DollarToKsh = 150
KshToDollar =0.0067

print('''
      Welcome To Currency Converter
      1.Convert from dollars to Ksh
      2.Convert from Ksh to Dollar
      3.Exit
      
      


      

      ''')
choice = input("Please make a choice: ")
if choice == "1":   
 dollars = float(input("Enter amount in $ "))
 output = dollars * DollarToKsh
 print("The amount in Ksh is:",output)
elif choice == "2":
 Ksh = float(input("Enter amount in Ksh: "))
 output = Ksh * KshToDollar 
 print("The amount in Dollar is:",output)

elif choice =="3":
  exit
else:
 print("Invalid Option")