import mysql.connector
class assembled_parts:
    def create_table(cursor):
        query = """
        CREATE TABLE IF NOT EXIST assembled_pard  (
            id INT AUTO_INCREMENT PRIMARY KEY,
            category VARCHAR(255) default NULL,
            serial_number VARCHAR(255) default NULL,
            order_number VARCHAR(255) default NULL,
            suplier VARCHAR(255) default NULL,
            company VARCHAR(255) default NULL,
            country VARCHAR(255) default NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            name VARCHAR(255) default NULL
        )
        """
        cursor.execute(query)

