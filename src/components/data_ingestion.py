import os
import sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class dataIngestionConfig:
    data_point_path: str = os.path.join('data','X.csv')
    target_label_path: str = os.path.join('data','y.csv')
    
class dataIngestion():
    def __init__(self):
        self.data_config = dataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Entered the data ingestion method or component')

        try:

            df = pd.read_csv('notebook/x_data.csv ')
            labels = pd.read_csv('notebook/y_data.csv')

            logging.info('read the data as dataframe "df" & class labels in "labels" variables')
                
            os.makedirs(os.path.dirname(self.data_config.data_point_path), exist_ok=True)

            df.to_csv(self.data_config.data_point_path, index = False, header=True)
            labels.to_csv(self.data_config.target_label_path, index = False)
            
            logging.info('data ingestion is completed')

            return(self.data_config.data_point_path, self.data_config.target_label_path)
        
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=="__main__":
    obj = dataIngestion()
    obj.initiate_data_ingestion()

  
