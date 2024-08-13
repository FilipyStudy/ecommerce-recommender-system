import torchtext; torchtext.disable_torchtext_deprecation_warning()
from torchtext.data import get_tokenizer
import numpy as np
import pandas as pd
import db_manager as db


class machine_learning:

    def tokenize():
        connection = db.create_connection()
        table = pd.read_sql('system_data', connection)

#TODO: Create a machine Learning algorithm to enjoy the recommendation system.