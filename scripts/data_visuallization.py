import pandas as pd
from pandasql import sqldf
import matplotlib.pyplot as plt
from pathlib import Path

class data_visuallization:
    
    #Define a class to visualize the data.
    def show_pie_chart(path):
        #Define the database path
        test_path = Path('./database/test.csv')
        train_path = Path('./database/train.csv')

        #Define the correct database to analyze based on the function parameter
        if path == 'train':
            df = pd.read_csv(train_path, 
                    header=None,
                    names=['classification', 'title', 'description'])
        else:
            df = pd.read_csv(test_path, 
                    header=None,
                    names=['classification', 'title', 'description'])
        
        #Query the data
        query = f"""SELECT classification,
                    COUNT(classification) AS classification_count,
                    CASE
                        WHEN classification = 1 THEN 'Negative'
                        WHEN classification = 2 THEN 'Positive'
                    END AS classification_score
                    FROM df
                    GROUP BY classification"""
        
        #Plot the data
        fig, ax = plt.subplots()
        result = sqldf(query=query, env=None)
        ax.pie(result['classification_count'], 
               labels=result['classification_score'],
               autopct='%1.1f%%',
               colors=['#C1121F', '#FDF0D5'])
        plt.show()
        #Return True for debug purposes
        return True