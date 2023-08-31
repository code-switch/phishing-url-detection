import sys
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from src.exception import CustomException
from src.logger import logging
import os
from dataclasses import dataclass
# from src.components.data_transformation import DataTransformation
# from src.components.data_transformation import DataTransformationConfig


@dataclass #A decorator is used to add additional functionality to class 'DataTransformationConfig'
class DataTransformationConfig: #creating this class to make some variables related to data transformation task
    preprocessor_obj_file_path = os.path.join('src\data','preprocessor.pkl')

class DataTransformation: 
    '''
    creating this class to actually perform data transformation task inside it.
    '''
    def __init__(self): #constructor is created to create compulsory(mandatory) variables that are must for data transformation task
        self.data_transformation_config=DataTransformationConfig()
    
    def get_data_transformation_object(self):
        """
        This function is responsible for data transformation
        """
        
        try:

            numerical_data = ['qty_dot_url', 'qty_hyphen_url', 'qty_underline_url', 'qty_slash_url', \
                'qty_dot_domain', 'qty_slash_directory', 'qty_equal_directory',\
                'qty_and_directory', 'qty_exclamation_directory', 'qty_tilde_directory', 'qty_comma_directory',\
                'qty_dollar_directory', 'directory_length', 'qty_dot_file', 'qty_hyphen_file',\
                'qty_at_file', 'qty_and_file', 'qty_space_file', 'qty_tilde_file', 'qty_plus_file',\
                'qty_percent_file', 'file_length', 'qty_hyphen_params', 'qty_underline_params',\
                'qty_slash_params', 'qty_percent_params', 'params_length',\
                'time_domain_expiration', 'ttl_hostname']

            categorical_data = ['qty_questionmark_directory']

            
            num_pipeline = Pipeline(
                steps=[
                        ('imputer',SimpleImputer(strategy = 'median')),
                        ('scaler', StandardScaler())
                        ]
                )
            
            cat_pipeline = Pipeline(
                steps = [
                        ('imputer',SimpleImputer(strategy = 'most_frequent'))
                        ('Scaler', StandardScaler()),
                        ('onehotencoding',OneHotEncoder())
                        ]
                )

            logging.info('Numerical col standard scaling completed')
            logging.info('categorical col encoding completed')

            #combining the numberical & categorical pipeline together
            preprocessor = ColumnTransformer(
                [
                    ('num_pipeline',num_pipeline, numerical_data),
                    ("cat_pipeline",cat_pipeline, categorical_data)
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException

    def initiate_data_transformation(self,train_data_path,train_label_path, test_data_path, test_label_path):

        try:
            train_df = pd.read_csv(train_data_path)
            train_label = pd.read_csv(train_label_path)
        
            test_df = pd.read_csv(test_data_path)
            test_label = pd.read_csv(test_label_path)

            logging.info('Reading train & test data completed')

            logging.info('obtaining preprocessing object')

            preprocessing_obj = self.get_data_transformation_object()

            target_col = 'phishing'  
            
            numerical_data = ['qty_dot_url', 'qty_hyphen_url', 'qty_underline_url', 'qty_slash_url', \
                'qty_dot_domain', 'qty_slash_directory', 'qty_equal_directory',\
                'qty_and_directory', 'qty_exclamation_directory', 'qty_tilde_directory', 'qty_comma_directory',\
                'qty_dollar_directory', 'directory_length', 'qty_dot_file', 'qty_hyphen_file',\
                'qty_at_file', 'qty_and_file', 'qty_space_file', 'qty_tilde_file', 'qty_plus_file',\
                'qty_percent_file', 'file_length', 'qty_hyphen_params', 'qty_underline_params',\
                'qty_slash_params', 'qty_percent_params', 'params_length',\
                'time_domain_expiration', 'ttl_hostname']
            
            logging.info(f'applying preprocessing object on training df & testing df')
            
            train_df_arr = preprocessing_obj.fit_transform(train_df)
            test_df_arr = preprocessing_obj.transform(test_df)

            train_arr = np.c_[train_df_arr, np.array(train_label)]
            test_arr = np.c_[test_df_arr, np.array(test_label)]
            
            logging.info(f'saved preprocessing object')            
            
            save_obj(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )
        except:
            pass
            

