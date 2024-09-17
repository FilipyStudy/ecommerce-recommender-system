from scripts import db_manager
import pandas as pd
import pathlib
from sqlalchemy import create_engine
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

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
nltk.download('wordnet')
stop_words = set(stopwords.words('english'))


#Create a function for the iteration in each row inside the csv
def remove_ponctuation (x):
    match = pattern.findall(x)
    return "".join(i for i in match if i not in stop_words).lower()


#TODO: Finish the spell correction algorithm.
def spell_correction (x):
    return None


#Initialize the lemmatizer method:
lemmatizer = WordNetLemmatizer().lemmatize

try:
    #Open the database, create a connection and upload the data to a database after the ETL process.
    with open(pathlib.Path("database\\train.csv")) as f:
        csv_table = pd.read_csv(f, header=None)
    conn = db_manager.create_connection()
    uri = f"postgresql+psycopg://{DB_INFO['user']}:{DB_INFO['password']}@{DB_INFO['db_address']}:{DB_INFO['port']}/{DB_INFO['db_name']}"
    engine = create_engine(uri)

    #Remove incorret values from the first index, stop words and ponctuation characters using regex and nltk
    csv_table[1] = csv_table[1].astype("str")
    csv_table[2] = csv_table[2].astype("str")
    print("Type converting to string are done, starting the REGEX function...")
    csv_table[1] = csv_table[1].apply(remove_ponctuation)
    csv_table[2] = csv_table[2].apply(remove_ponctuation)
    print("Regex iterations are done...")
    
    #Lemmatization process to create lemma's and help the model to contextualize the data.
    print("Starting Lemmatizing process...")
    csv_table[1] = csv_table[1].apply(lemmatizer)
    csv_table[2] = csv_table[2].apply(lemmatizer)
    print("Lemmatizing process done!")

    #Upload the data to a postgresql database
    csv_table.to_sql(name="training_data",
                     con=engine,
                     if_exists='replace')

except Exception as e:
    print(f"An exception as raised: {e}")