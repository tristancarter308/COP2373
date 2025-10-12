import re


#Validate phone number
def validate_phone(phone):
    pattern = r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
    return bool(re.match(pattern, phone))

#Validate social security number
def validate_ssn(ssn):
    pattern = r"^\d{3}-\d{2}-\d{4}$"
    return bool(re.match(pattern, ssn))

#Validate zip code
def validate_zip(zip_code):
    pattern = r"^\d{5}(-\d{4})?$"
    return bool(re.match(pattern, zip_code))

#Main function to retrieve user input and display results
def main():
    #Get user input
    phone = input("Enter your phone number: ")
    ssn = input("Enter your Social Security Number: ")
    zip_code = input("Enter your ZIP Code: ")

    #Display whether user input was valid or invalid
    print("\nValidation Results:")

    #Display phone number validity
    if validate_phone(phone):
        print(f"'{phone}' is a valid phone number.")
    else:
        print(f"'{phone}' is an invalid phone number.")

    #Display social security number validity
    if validate_ssn(ssn):
        print(f"'{ssn}' is a valid social security number.")
    else:
        print(f"'{ssn}' is an invalid social security number.")

    #Display zip code validity
    if validate_zip(zip_code):
        print(f"'{zip_code}' is a valid zip code.")
    else:
        print(f"'{zip_code}' is an invalid zip code.")



if __name__ == "__main__":
    main()