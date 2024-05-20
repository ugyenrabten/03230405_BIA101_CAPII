# Defining the Employee class
class Employee:
    # Initializing an Employee object with name and income, validating income type and value
    def __init__(self, name, income):
        # Check if income is a positive number and of type int or float
        if not isinstance(income, (int, float)) or income <= 0:
            raise ValueError("Income must be a positive number.")
        # Assigning name and income attributes
        self.name = name
        self.income = income
        # Initializing deductions dictionary
        self.deductions = {}

    # Method to calculate tax based on income and deductions
    def calculate_tax(self):
        # Calculating deductions
        self.calculate_deductions()
        # Subtracting total deductions from income to get taxable income
        taxable_income = self.income - sum(self.deductions.values())
        tax = 0
        # Applying tax rates based on taxable income table
        if taxable_income <= 300000:
            tax = 0
        elif taxable_income <= 400000:
            tax = (taxable_income - 300000) * 0.1
        elif taxable_income <= 650000:
            tax = (taxable_income - 400000) * 0.15 + 10000
        elif taxable_income <= 1000000:
            tax = (taxable_income - 650000) * 0.2 + 35000
        elif taxable_income <= 1500000:
            tax = (taxable_income - 1000000) * 0.25 + 75000
        else:
            tax = (taxable_income - 1500000) * 0.3 + 125000
        # Applying surcharge if tax exceeds 1 million
        if tax >= 1000000:
            tax *= 1.1
        return tax

    # Method to calculate deductions based on income
    def calculate_deductions(self):
        # Setting initial values for deductions
        self.deductions['NPPF'] = 0
        self.deductions['GIS'] = 0
        # Calculating education allowance deduction
        self.deductions['Education Allowance'] = min(350000, self.income * 0.1)
        # Calculating other deductions
        self.deductions['Other'] = self.income * 0.05

    # String representation of the Employee object
    def __str__(self):
        # Returning a formatted string representing the employee
        return f"Employee: {self.name}, Income: {self.income}, Tax: {self.calculate_tax()}"

# Define GovernmentEmployee class inheriting from Employee
class GovernmentEmployee(Employee):
    def __init__(self, name, income, employee_type='Regular'):
        # Calling parent class 
        super().__init__(name, income)
        # Validating employee type
        if employee_type not in ['Regular']:
            raise ValueError("Invalid employee type. Only 'Regular' is supported.")
        # Assigning employee type attribute
        self.employee_type = employee_type

# Define PrivateEmployee class inheriting from Employee
class PrivateEmployee(Employee):
    def __init__(self, name, income, employee_type='Regular'):
        # Calling parent class 
        super().__init__(name, income)
        # Validating employee type
        if employee_type not in ['Regular']:
            raise ValueError("Invalid employee type. Only 'Regular' is supported.")
        # Assigning employee type attribute
        self.employee_type = employee_type

# Define ContractEmployee class inheriting from Employee
class ContractEmployee(Employee):
    def __init__(self, name, income):
        # Calling parent class
        super().__init__(name, income)
        # Validating income for contract employees
        if income < 0:
            raise ValueError("Income cannot be negative for contract employees.")

# User input validation for employee details
while True:
    try:
        # Asking for employee name
        name = input("Enter employee name: ")
        # Asking for employee income
        income_str = input("Enter employee income: ")
        # Checking if income is a numeric value
        if not income_str.replace('.', '', 1).isdigit():
            raise ValueError("Income must be a numeric value.")
        # Converting income to float
        income = float(income_str)
        # Checking if income is greater than zero
        if income <= 0:
            raise ValueError("Income must be greater than zero.")
        # Breaking the loop if inputs are valid
        break
    except ValueError as ve:
        # Printing error message
        print(ve)

# User input validation for employee type
while True:
    # Asking for employee type
    employee_type = input("Enter employee type (Government/Private/Contract): ").lower()
    # Checking if employee type is valid
    if employee_type not in ['government', 'private', 'contract']:
        print("Invalid employee type. Please choose from 'government', 'private', or 'contract'.")
    else:
        # Create an instance of the appropriate employee type
        if employee_type == 'government':
            employee = GovernmentEmployee(name, income)
        elif employee_type == 'private':
            employee = PrivateEmployee(name, income)
        else:
            employee = ContractEmployee(name, income)
        
        # Calculate the tax amount
        tax_amount = employee.calculate_tax()

        # Print employee details and tax payable
        print(employee)
        print(f"{employee.name}'s total tax payable is {tax_amount}. Thank you for using our service.")
        break
