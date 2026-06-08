
# PROGRAMMER:   Marlena Fabrick
# PROGRAM NAME: Miles Per Gallon Calculator — Using Functions
# DATE WRITTEN: 11/11/2020
# UPDATED:      2026 — fixed swapped Gallons/Miles labels in writeResults(),
#                      moved header to top, removed unused toFixed(), fixed
#                      calcmpg → calcMPG naming, updated comments
#
# PURPOSE: Calculate the miles per gallon for a vehicle using modular
#          functions for input validation, calculation, and output.
#          Demonstrates function definition, parameters, and return values.
#
# FUNCTIONS:
#   checkFloatDataType(dataType) — validates that input is a positive float
#   calcMPG(miles, gals)        — calculates and returns miles per gallon
#   writeResults()              — displays the formatted MPG report

# ============================================================
# Declare Variables in alpha order
# Initialize / declare variables
gallons_used = 0.0
miles_per_gallon = 0.0
miles_driven = 0.0

# ============================================================
# FUNCTION DEFINITIONS

# Function to validate data type and check for negative/zero values
def checkFloatDataType(dataType):  # formal parameter to hold/store input
    while True:
        try:
            dataType = float(input())
        except ValueError:
            print("Wrong data type entered — please enter a positive numeric value.\n")
            continue
        else:
            if dataType <= 0:
                print("Negative value or zero entered — re-enter a positive numeric value.\n")
                continue
            else:
                break  # Valid input received, exit loop
    return dataType
    # end checkFloatDataType function

# Function to calculate miles per gallon
def calcMPG(miles, gals):
    mpg = miles / gals  # Divide miles driven by gallons used
    return mpg
    # end calcMPG function

# Function to display the formatted MPG report
def writeResults():
    # Output Operations — display results in aligned columns
    print("=" * 65)
    print("CAR MILEAGE INFORMATION")
    print("=" * 65)
    print("Miles Driven     = " + format(miles_driven,      "10,.2f"))  # Fixed: was showing gallons
    print("Gallons Used     = " + format(gallons_used,      "10,.2f"))  # Fixed: was showing miles
    print("Miles Per Gallon = " + format(miles_per_gallon,  "10,.2f"))
    print("=" * 65)
    print()
    # END writeResults function

# ============================================================
# INPUT OPERATIONS

# Collect miles driven — call function to validate data type
print("How many miles were driven using your vehicle?")
miles_driven = checkFloatDataType(miles_driven)

# Collect gallons used — call function to validate data type
print("How many gallons were used by the vehicle?")
gallons_used = checkFloatDataType(gallons_used)

# ============================================================
# CALCULATE MILES PER GALLON — call calcMPG function
miles_per_gallon = calcMPG(miles_driven, gallons_used)

# ============================================================
# OUTPUT — call writeResults function to display the report
writeResults()

# END PROGRAM
