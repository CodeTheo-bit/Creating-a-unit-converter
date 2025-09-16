def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def miles_to_km(miles):
    """Converts miles to kilometers."""
    return miles * 1.60934

def km_to_miles(km):
    """Converts kilometers to miles."""
    return km / 1.60934

def kg_to_lbs(kg):
    """Converts kilograms to pounds."""
    return kg * 2.20462

def lbs_to_kg(lbs):
    """Converts pounds to kilograms."""
    return lbs / 2.20462

conversions = {
    '1': {
        'title': 'Temperature',
        'units': {
            '1': {'from': 'Celsius', 'to': 'Fahrenheit', 'func': celsius_to_fahrenheit},
            '2': {'from': 'Fahrenheit', 'to': 'Celsius', 'func': fahrenheit_to_celsius}
        }
    },
    '2': {
        'title': 'Distance',
        'units': {
            '1': {'from': 'Miles', 'to': 'Kilometers', 'func': miles_to_km},
            '2': {'from': 'Kilometers', 'to': 'Miles', 'func': km_to_miles}
        }
    },
    '3': {
        'title': 'Weight',
        'units': {
            '1': {'from': 'Kilograms', 'to': 'Pounds', 'func': kg_to_lbs},
            '2': {'from': 'Pounds', 'to': 'Kilograms', 'func': lbs_to_kg}
        }
    }
}

def main():
    """Main program loop for the Unit Converter."""
    print("Welcome to the Python Unit Converter! 🌡️📏⚖️")
    print("Enter 'exit' at any time to quit.")

    while True:
        print("\n--- Main Menu ---")
        for key, value in conversions.items():
            print(f"{key}. {value['title']}")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '4' or choice.lower() == 'exit':
            print("Thank you for using the converter. Goodbye! 👋")
            break
        
        if choice in conversions:
            category = conversions[choice]
            print(f"\n--- {category['title']} Conversion ---")
            
            for unit_key, unit_data in category['units'].items():
                print(f"{unit_key}. {unit_data['from']} to {unit_data['to']}")
            
            sub_choice = input("Enter your conversion choice: ")
            
            if sub_choice in category['units']:
                try:
                    value_input = input(f"Enter the value in {category['units'][sub_choice]['from']}: ")
                    if value_input.lower() == 'exit':
                        continue
                        
                    value = float(value_input)
                    
                    conversion_data = category['units'][sub_choice]
                    converted_value = conversion_data['func'](value)
                    
                    print(f"\nResult: {value:.2f} {conversion_data['from']} is equal to {converted_value:.2f} {conversion_data['to']}.")
                    
                except ValueError:
                    print("Error: Invalid input. Please enter a valid number.")
            else:
                print("Invalid choice. Please select a valid conversion.")
        else:
            print("Invalid choice. Please select a number from the menu.")

if __name__ == "__main__":
    main()