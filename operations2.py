
def calculate_pay():
  # Get user input for hours and rate
 hours_worked = float(input("Enter hours worked: "))
 rate_per_hour = float(input("Enter rate per hour ($): "))
 total_pay = hours_worked * rate_per_hour
 print("Total pay for {hours_worked} hours at ${rate_per_hour}/hour: ${total_pay:.2f}")

# Call the function to run the program
 calculate_pay()
