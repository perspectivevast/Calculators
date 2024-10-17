#For research purposes only

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    # Get user inputs with hints
    total_mg_vial = get_positive_float("Enter the total mg in the vial: ")
    mg_dose = get_positive_float("Enter the desired mg dose (between 1.0 and 15.0 mg): ")
    units_to_draw = get_positive_float("Enter the units (cc/ml) you want to draw up (between 0.10 ml and 1.0 ml): ")

    # Calculate the output
    output = (total_mg_vial / mg_dose) * units_to_draw

    # Display the result
    print(f"Total mg in vial is {total_mg_vial:.2f} mg, desired dose is {mg_dose:.2f} mg, "
          f"desired draw in a 1cc/ml syringe is {units_to_draw:.2f} ml. "
          f"The final output is: {output:.2f} ml BAC water to add.")

    # Wait for user input before closing
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()