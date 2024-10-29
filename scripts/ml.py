import torchtext; torchtext.disable_torchtext_deprecation_warning()
from torchtext.data import get_tokenizer
import numpy as np
import pandas as pd
import db_manager as db


class machine_learning:
    try:
        tokenizer = get_tokenizer("basic_english")
        conn = db.create_connection()
        pd.read_sql("system_data", conn)

    except Exception as e:
        print(f"An Exception was ocurred: {e}")

#TODO: Create a machine Learning algorithm to enjoy the recommendation system.