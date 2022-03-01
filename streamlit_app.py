from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
"""
# Importing the dataset
Cobra = "C:\\Users\\administra\\Ponsse\\cobra_hv.xlsx"
Ergo = "C:\\Users\\administra\\Ponsse\\ergo_hv.xlsx"
Ambas= "C:\\Users\\administra\\Ponsse\\cobra_ergo_hv.xlsx"

df = pd.read_excel(Cobra)
dff = pd.read_excel(Ergo)
both=pd.read_excel(Ambas)
