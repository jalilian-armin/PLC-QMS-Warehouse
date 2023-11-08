import mysql.connector

class MysqlDb:
    cursor = None
    connection = None
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            host="192.168.100.12",
            user="yekta",
            password="Yekta-5310",
            database="qc2"
        )
        self.cursor = self.connection.cursor()

    def getCursor(self):
        return self.cursor
    
    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            # commit changes to the database
            self.connection.commit()
            return True
        except:
            # print("Error:", err)

            return False
        
    
    def insert(self, table, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        print(query)
        return self.execute_query(query, tuple(data.values()))
    
    
    def update(self, table, data, condition):
        set_clause = ', '.join([f"{key} = %s" for key in data.keys()])
        query = f"UPDATE {table} SET {set_clause} WHERE {condition}"
        return self.execute_query(query, tuple(data.values()))
    
    def delete(self, table, condition):
        query = f"DELETE FROM {table} WHERE {condition}"
        return self.execute_query(query)
    
    def select(self, table, columns="*", condition=None):
        column_names = ', '.join(columns) if isinstance(columns, list) else columns
        query = f"SELECT {column_names} FROM {table}"
        if condition:
            query += f" WHERE {condition}"
        self.execute_query(query)
        return self.cursor.fetchall()
    def run_migrations(self):
        try:
            with open("./migrations/acl.py", "r") as migration_file:
                migration_code = migration_file.read()
                exec(migration_code)
        except FileNotFoundError:
            pass  # Migration script not found
    