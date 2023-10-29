import mysql.connector

def create_acl_table(cursor):
    query = """
    CREATE TABLE acl (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        resource VARCHAR(255) NOT NULL,
        permission VARCHAR(50) NOT NULL,
        UNIQUE KEY unique_acl (user_id, resource, permission)
    )
    """
    cursor.execute(query)

def main():
    connection = mysql.connector.connect(
        host="192.168.100.201",
        user="yekta",
        password="Yekta-5310",
        database="qc2"
    )
    cursor = connection.cursor()

    create_acl_table(cursor)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    main()
