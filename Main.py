# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# KDoehlert,9.6.2022,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #

# Import Modules
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of employee objects when script starts
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
list_of_employees = []
for line in lstFileData:
    # Creates employee object from each row of data in list
    employee = Emp(line[0].strip(),line[1].strip(),line[2].strip())
    list_of_employees.append(employee)

while True:
    # Show user a menu of options
    Eio.print_menu_items()

    # Get user's menu option choice
    menu_choice = Eio.input_menu_options()

    # Show user current data in the list of employee objects
    if menu_choice == '1':
        Eio.print_current_list_items(list_of_employees)
        continue

    # Let user add data to the list of employee objects
    elif menu_choice == '2':
        # try-except block added to handle errors that arise from validation in the employee setter properties
        try:
            employee = Eio.input_employee_data()
            list_of_employees.append(employee)
            print("Employee was successfully added.")
        except:
            print()
        continue

    # let user save current data to file
    elif menu_choice == '3':
        success = Fp.save_data_to_file("EmployeeData.txt", list_of_employees)
        if success == True:
            print("Data was successfully saved.")
        continue

    # let user exit program
    elif menu_choice == '4':
        print('Goodbye')
        break

    # handles situations when users give invalid input
    else:
        print('\nPlease make a selection 1 - 4')
        continue
# Main Body of Script  ---------------------------------------------------- #
