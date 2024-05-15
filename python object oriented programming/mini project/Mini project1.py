class Programmer:
    def __init__(self, name, age, address, phone, programming_languages, salary, monthly_bonus):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.programming_languages = programming_languages
        self.salary = salary
        self.monthly_bonus = monthly_bonus


class Assistant:
    def __init__(self, name, age, address, phone, is_bilingual, salary, monthly_bonus):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.is_bilingual = is_bilingual
        self.salary = salary
        self.monthly_bonus = monthly_bonus


def calculate_payroll(employees):
    """
    Function to calculate and print the monthly salary of each employee
    and the total amount that the startup owner has to pay per month.
    """
    total = 0
    print("\n========= Welcome to our Payroll System =========\n")
    for employee in employees:
        # Calculate monthly salary
        monthly_salary = round(employee.salary / 12, 2) + employee.monthly_bonus
        print(f"{employee.name.capitalize()}'s salary is: ${monthly_salary}")
        total += monthly_salary
    # Display total payroll for the month
    print("\nThe total payroll this month will be: $", total)


# Instances (employees)
jack = Programmer("Jack", 45, "5th Avenue", "555-563-345", ["Python", "Java"], 90000, 1000)
isabel = Programmer("Isabel", 25, "6th Avenue", "234-245-853", ["JavaScript"], 75000, 800)
nora = Assistant("Nora", 23, "7th Avenue", "562-577-333", True, 40000, 500)

# List of instances
employees = [jack, isabel, nora]

# Function call (Passing the list of instances as argument)
calculate_payroll(employees)
