import psycopg2

#Database informations, just a dict containing all the information needed to control the database
DB_INFO = {
    "db_name" : "treated_data",
    "user" : "postgres",
    "password" : "root",
    "db_address" : "localhost",
    "port" : 5432
}

class db_manager:
    
    #Define the informations about the database service
    def __init__(self, dbname, user, password, db_address, port):
        DB_INFO["db_name"] = dbname
        DB_INFO["user"] = user
        DB_INFO["password"] = password
        DB_INFO["db_address"] = db_address
        DB_INFO["port"] = port

    #Create a connection to manage the database
    def create_connection():
        try:
            connection = psycopg2.connect(dbname=DB_INFO["db_name"],
                                          user=DB_INFO["user"],
                                          password=DB_INFO["password"],
                                          host=DB_INFO["db_address"])
            cursor = connection.cursor()
            return cursor
        except Exception as e:
            connection.close()
            print(f"Exception occurred: {e}")