import mysql.connector

def create_wearhouse_table(cursor):
    query = """
    CREATE TABLE wearhouse (
        id INT AUTO_INCREMENT PRIMARY KEY,
        category VARCHAR(255) default NULL,
        serial_number VARCHAR(255) default NULL,
        order_number VARCHAR(255) default NULL,
        suplier VARCHAR(255) default NULL,
        company VARCHAR(255) default NULL,
        country VARCHAR(255) default NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        type INT default 1
        
    )
    """
    cursor.execute(query)

def main():
    connection = mysql.connector.connect(
        host="192.168.100.19",
        user="yekta",
        password="Yekta-5310",
        database="qc2"
    )
    cursor = connection.cursor()

    create_wearhouse_table(cursor)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    main()
