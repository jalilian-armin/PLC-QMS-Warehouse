import classes.MysqlDb as MysqlDb
import hashlib
import bcrypt

class Auth:
    def __init__(self):
        pass
    username = ''
    def register_user(self, username, password):
        hashed_password = self.hash_password(password)
        db = MysqlDb.MysqlDb()
        cursor = db.getCursor()
        #cursor = MysqlDb.MysqlDb().cursor
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, hashed_password))
        db.connection.commit()

    def login(self, username, password):
        self.username = username
        db = MysqlDb.MysqlDb()
        cursor = db.getCursor()
        query = "SELECT password FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        stored_password = cursor.fetchone()

        if stored_password:
            stored_password = stored_password[0].encode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                return True
        return False

    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed
        
    def has_permission(self, permission):
        db = MysqlDb.MysqlDb()
        cursor = db.getCursor()
        query = "SELECT * FROM acl WHERE username = %s AND permission = %s"
        cursor.execute(query, (self.username, permission))
        permission_data = cursor.fetchone()
        return permission_data is not None
