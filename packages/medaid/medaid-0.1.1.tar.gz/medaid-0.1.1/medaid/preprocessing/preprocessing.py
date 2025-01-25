import pandas as pd
from medaid.preprocessing.column_removal import ColumnRemover
from medaid.preprocessing.encoder import Encoder
from medaid.preprocessing.scaler import Scaler
from medaid.preprocessing.imputer import Imputer
from medaid.preprocessing.preprocessing_info import PreprocessingCsv
from medaid.preprocessing.numeric_format_handler import NumericCommaHandler
import os

class Preprocessing:
    def __init__(self, target_column, path, imputer_lr_correlation_threshold=0.8, imputer_rf_correlation_threshold=0.2, categorical_threshold=0.2, removal_correlation_threshold=0.9):
        """
        Initialize the preprocessing pipeline.

        Parameters:
        - target_column (str): The name of the target column that will not be preprocessed.
        - output_file (str): The name of the output CSV file where details will be saved.
        """
        self.imputer_lr_correlation_threshold = imputer_lr_correlation_threshold
        self.imputer_rf_correlation_threshold = imputer_rf_correlation_threshold
        self.categorical_threshold = categorical_threshold
        self.removal_correlation_threshold = removal_correlation_threshold
        self.target_column = target_column
        self.numeric_format_handler = NumericCommaHandler()
        self.column_remover = ColumnRemover(self.target_column, self.categorical_threshold, self.removal_correlation_threshold)
        self.encoder = Encoder(self.target_column)
        self.scaler = Scaler(self.target_column)
        self.imputation = Imputer(self.target_column, self.imputer_lr_correlation_threshold, self.imputer_rf_correlation_threshold)
        self.path = path + "/results/preprocessing_details.csv"
        self.preprocessing_info = PreprocessingCsv(self.path)
        self.columns_info = []  

    def preprocess(self, dataframe):
        """
        Run the entire preprocessing pipeline on the provided DataFrame.

        Parameters:
        - dataframe (pd.DataFrame): The DataFrame to preprocess.

        Returns:
        - pd.DataFrame: The preprocessed DataFrame.
        """

        if not isinstance(dataframe, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame.")
        
        # 1. Handle numeric format
        dataframe = self.numeric_format_handler.handle_numeric_format(dataframe)

        # 2. Remove text columns
        dataframe = self.column_remover.remove(dataframe)
        text_column_removal_info = self.column_remover.get_removal_info()

        # 3. Impute missing values
        dataframe = self.imputation.impute_missing_values(dataframe)
        imputation_info = self.imputation.get_imputation_info()

        # 4. Encode categorical variables
        dataframe = self.encoder.encode(dataframe)
        encoding_info = self.encoder.get_encoding_info()

        # 5. Scale numerical features
        dataframe = self.scaler.scale(dataframe)
        scaling_info = self.scaler.get_scaling_info()

        # Save the column info to CSV
        self.save_column_info(text_column_removal_info, imputation_info, encoding_info, scaling_info)

        return dataframe

    def get_column_info(self):
        """
        Retrieve the details of each preprocessing step for all columns.

        Returns:
        - list: Contains details of the preprocessing for each column.
        """
        return self.columns_info

    def save_column_info(self, text_column_removal_info, imputation_info, encoding_info, scaling_info):
        """
        Save the preprocessing details to a CSV file using PreprocessingCsvExporter.

        Parameters:
        - text_column_removal_info (dict): Information about text column removal.
        - imputation_info (dict): Information about imputation.
        - encoding_info (dict): Information about encoding.
        - scaling_info (dict): Information about scaling.
        """
        
        self.preprocessing_info.export_to_csv(text_column_removal_info, imputation_info, encoding_info, scaling_info)

    def get_target_encoding_info(self):
        encoding_info = self.encoder.get_encoding_info()
        if self.target_column in encoding_info and "Mapping" in encoding_info[self.target_column]:
            return encoding_info[self.target_column]["Mapping"]
        return None

