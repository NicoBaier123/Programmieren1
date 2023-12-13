year=int(input("Enter current year:"))
month=int(input("Enter current month:"))
birth_year = int(input("Enter you birth year:"))
birth_month=int(input("Enter your birth month:"))
nyears=(year-birth_year)

if birth_month>month:
    nnyears=(nyears-1)
else:
    nnyears=nyears
print("Your age is " +str(nnyears))
