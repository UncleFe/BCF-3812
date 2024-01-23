def create_suppliers_query(suppliers_count):
    file_path = 'C:\\Python\\BCF-3812\\Queries\\Suppliers_sql_query.txt'

    with open(file_path, 'w') as file:
        file.write(f'INSERT INTO Suppliers (SupplierID, Name, ContactInfo) VALUES\n')

    with open(file_path, 'a') as file:        
        for i in range(1, suppliers_count):
            supplier_id = i
            name = f'Supplier Name {i}'
            contact_info = f'Contact info for Supplier {i}'
            if (i+1<suppliers_count ):
                query = f"({supplier_id}, '{name}', '{contact_info}'),\n"
            else:
                query = f"({supplier_id}, '{name}', '{contact_info}');\n"

            file.write(query)