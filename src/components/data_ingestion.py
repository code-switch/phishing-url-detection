import os
import sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

def ingestion_operation():

    @dataclass
    class dataIngestionConfig: #creating this class to create some variables related to data ingestion task
        train_data_path: str = os.path.join('src\data','train_x.csv')
        test_data_path: str = os.path.join('src\data','test_x.csv') 
        train_label_path: str = os.path.join('src\data','train_y.csv')
        test_label_path: str = os.path.join('src\data','test_y.csv')
        
    class dataIngestion: #creating this class to actually perform data ingestion task inside it.
        def __init__(self): #constructor is created to create compulsory(mandatory) variables that are must for data ingestion task
            self.data_config = dataIngestionConfig()

        def initiate_data_ingestion(self): #class method is created to get data from source location & store that data to target location
            logging.info('Entered the data ingestion method or component') #logging the tasks into log file to keep track of tasks.

            try:

                df = pd.read_csv('notebook/x_data.csv ')
                labels = pd.read_csv('notebook/y_data.csv')

                logging.info('read the data as dataframe "df" & class labels in "labels" variables')

                train_x,test_x, train_y, test_y = train_test_split(df, labels, train_size= 0.8, random_state=12)
                
                os.makedirs(os.path.dirname(self.data_config.train_data_path), exist_ok=True)
                os.makedirs(os.path.dirname(self.data_config.test_data_path), exist_ok=True)
                os.makedirs(os.path.dirname(self.data_config.train_label_path), exist_ok=True)
                os.makedirs(os.path.dirname(self.data_config.test_label_path), exist_ok=True)

                train_x.to_csv(self.data_config.train_data_path, index = False, header=True)
                test_x.to_csv(self.data_config.test_data_path, index = False, header=True)
                train_y.to_csv(self.data_config.train_label_path, index = False, header=True)
                test_y.to_csv(self.data_config.test_label_path, index = False, header=True)
                
                logging.info('data ingestion is completed')

                return(self.data_config.train_data_path, self.data_config.test_data_path, \
                    self.data_config.train_label_path, self.data_config.test_label_path)
            
            except Exception as e:
                raise CustomException(e,sys)
        

if __name__=="__main__":
    obj = ingestion_operation.dataIngestion()
    data_path = obj.initiate_data_ingestion()






