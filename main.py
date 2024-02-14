# data and array managament
import pandas as pd
import numpy as np

# visualization libraries
import matplotlib.pyplot as plt
import seaborn as sb
import missingno as msno

# sckikit-learn libraries
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import pickle

MODEL_PATH = 'LogisticRegression().pkl'
SCALER_PATH = 'StandardScaler().pkl'

# Load the Scikit-Learn model
model_filename = MODEL_PATH
with open(model_filename , 'rb') as f:
    model = pickle.load(f)

# Load the Scaler
scaler_filename = SCALER_PATH
with open(scaler_filename, 'rb') as f:
    scaler = pickle.load(f)

##

print(input("Hello. Put the name of the file:"))




