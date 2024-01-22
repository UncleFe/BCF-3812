def create_customers_query(customers_count):
    file_path = 'C:\\Python\\BCF-3812\\Queries\\Customers_sql_query.txt'

    with open(file_path, 'w') as file:
        file.write(f'"INSERT INTO Customers (CustomerID, Name, ContactInfo) VALUES"\n')


    with open(file_path, 'a') as file:
     
        for i in range(1, customers_count):
            customer_id = i
            name = f'Customer Name {i}'
            contact_info = f'Contact Info {i}'

            if(i+1<customers_count):
                query = f"({customer_id}, '{name}', '{contact_info}'),\n"
            else:
                query = f"({customer_id}, '{name}', '{contact_info}');\n"
        
            file.write(query)

    print(f"File was created, file location is: {file_path}")
