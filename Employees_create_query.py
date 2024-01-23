import random
def create_employees_query(count_employees):
    file_path='C:\\Python\\BCF-3812\\Queries\\Employees_sql_query.txt'

    with open(file_path, 'w') as file:
        file.write(f'INSERT INTO Employees (EmployeeID, Name, LastName, Position) VALUES\n')

    with open(file_path, 'a') as file:        
        position_employees =['Worker', 'Bad worker', 'Good worker']
        for i in range(1, count_employees):
            employee_id = i
            name = f"Employee name {i}"
            last_name = f"Employee last name {i}"
            position = random.choice(position_employees)

            if(i+1<count_employees):
                query = f"({employee_id}, '{name}', '{last_name}', '{position}'),\n"
            else:
                query = f"({employee_id}, '{name}', '{last_name}', '{position}');\n"

            file.write(query)

    print(f"File was created, file location is: {file_path}")

