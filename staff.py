import csv
employees = open("employees.csv", "r")
salaries = []
info = []
try:
    csv_reader = csv.DictReader(employees)
    for row in csv_reader:
        employee_type = row["employee_type"]
        if employee_type == "Manager":
            info.append({"name": row["first_name"]+ " "+ row["last_name"], "salaries":int(row["salary"])})
            salaries.append(int(row["salary"]))
finally:
    employees.close()

minimum = (min(info, key = lambda x:x["salaries"]))
lis = list(minimum)
average = int(sum(salaries) / len(salaries))
print("The average salary of managers is {}".format(average))
print(f"{minimum[lis[0]]} has the lowest salary(${minimum[lis[1]]})")