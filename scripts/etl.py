from scripts import db_manager
import pandas as pd
import pathlib
from sqlalchemy import create_engine
import re
import nltk
from nltk.corpus import stopwords

DB_INFO = {
    "db_name" : "system_data",
    "user" : "postgres",
    "password" : "root",
    "db_address" : "localhost",
    "port" : 5432
}

#Create the pattern for regex ETL process
pattern = re.compile(r"[\u0041-\u1EFF\s]+\s?")

#Download and create a set with the stop-words in english, according to the language of dataset.
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


#Create a function for the iteration in each row inside the csv
def iterator_func (x):
    match = pattern.findall(x)
    return "".join(i for i in match if i not in stop_words)


try:
    #Open the database, create a connection and upload the data to a database after the ETL process.
    with open(pathlib.Path("database\\train.csv")) as f:
        csv_table = pd.read_csv(f, header=None)
    conn = db_manager.create_connection()
    uri = f"postgresql+psycopg://{DB_INFO['user']}:{DB_INFO['password']}@{DB_INFO['db_address']}:{DB_INFO['port']}/{DB_INFO['db_name']}"
    engine = create_engine(uri)

    #Remove incorret values from the first index, stop words and ponctuation characters using regex and nltk
    for x in csv_table.index():
        if csv_table.loc[x, 0] != "1" or csv_table.loc[x, 0] != "2":
            csv_table.drop(x, inplace=True, erros="ignore")
        
    #Remove incorret values from the first index, stop words and ponctuation characters using regex and nltk
    csv_table[1] = csv_table[1].astype("str")
    csv_table[2] = csv_table[2].astype("str")
    print("Type converting to string are done, starting the REGEX function...")
    csv_table[1] = csv_table[1].apply(iterator_func)
    csv_table[2] = csv_table[2].apply(iterator_func)
    print("Regex iterations are done...")

    #Upload the data to a postgresql database
    csv_table.to_sql(name="training_data",
                     con=engine,
                     if_exists='replace')

except Exception as e:
    print(f"An exception as raised: {e}")