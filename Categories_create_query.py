def create_categories_query(categories_count):
    file_path = 'C:\\Python\\BCF-3812\\Queries\\Categories_sql_query.txt'

    with open (file_path, 'w') as file:
        file.write(f'INSERT INTO Categories (CategoryID, Name) VALUES\n')

    with open(file_path, 'a') as file:
        
        for i in range (1, categories_count):
            category_id = i
            name = f'Category Name {i}'
            if(i+1<categories_count):
                query = f"({category_id}, '{name}'),\n"
            else:
                query = f"({category_id}, '{name}');\n"
        
            file.write(query)
    print(f"File was created, file location is: {file_path}")