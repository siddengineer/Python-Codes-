class Employee:
    def __init__(self, emp_code, first_name, last_name, designation, basic_pay):
        self.emp_code = emp_code
        self.first_name = first_name
        self.last_name = last_name
        self.designation = designation
        self.basic_pay = basic_pay

        # Allowances
        self.da = 0.10   # 10%
        self.hra = 0.15  # 15%
        self.wa = 0.05   # 5%

        # Deductions
        self.pf = 0.08   # 8%
        self.lic = 0.02  # 2%

    def calculate_gross(self):
        return self.basic_pay + \
               (self.basic_pay * self.da) + \
               (self.basic_pay * self.hra) + \
               (self.basic_pay * self.wa)

    def calculate_deductions(self):
        return (self.basic_pay * self.pf) + \
               (self.basic_pay * self.lic)

    def calculate_net_salary(self):
        return self.calculate_gross() - self.calculate_deductions()

    def generate_payslip(self, month):
        print(f"\n----- PAYSLIP FOR {month} -----")
        print(f"Employee Code: {self.emp_code}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Designation: {self.designation}")
        print(f"Basic Pay: {self.basic_pay}")
        print(f"DA: {self.basic_pay * self.da}")
        print(f"HRA: {self.basic_pay * self.hra}")
        print(f"WA: {self.basic_pay * self.wa}")
        print(f"Gross Salary: {self.calculate_gross()}")
        print(f"PF Deduction: {self.basic_pay * self.pf}")
        print(f"LIC Deduction: {self.basic_pay * self.lic}")
        print(f"Total Deductions: {self.calculate_deductions()}")
        print(f"Net Salary: {self.calculate_net_salary()}")
        print("-------------------------------\n")


# ================= MAIN SYSTEM =================

employees = []

def add_employee():
    code = int(input("Enter Employee Code: "))
    first = input("Enter First Name: ")
    last = input("Enter Last Name: ")
    desig = input("Enter Designation: ")
    pay = float(input("Enter Basic Pay: "))

    employees.append(Employee(code, first, last, desig, pay))
    print("Employee Added Successfully!\n")


def edit_employee():
    code = int(input("Enter Employee Code to Edit: "))

    for emp in employees:
        if emp.emp_code == code:
            emp.designation = input("Enter New Designation: ")
            emp.basic_pay = float(input("Enter New Basic Pay: "))
            print("Employee Updated Successfully!\n")
            return

    print("Employee Not Found!\n")


def delete_employee():
    code = int(input("Enter Employee Code to Delete: "))

    for emp in employees:
        if emp.emp_code == code:
            employees.remove(emp)
            print("Employee Deleted Successfully!\n")
            return

    print("Employee Not Found!\n")


def generate_payslip():
    code = int(input("Enter Employee Code: "))
    month = input("Enter Month: ")

    for emp in employees:
        if emp.emp_code == code:
            emp.generate_payslip(month)
            return

    print("Employee Not Found!\n")


# ================= MENU =================

while True:
    print("===== ADVANCED PAYROLL SYSTEM =====")
    print("1. Add Employee")
    print("2. Edit Employee")
    print("3. Delete Employee")
    print("4. Generate Payslip")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_employee()
    elif choice == 2:
        edit_employee()
    elif choice == 3:
        delete_employee()
    elif choice == 4:
        generate_payslip()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice!\n")