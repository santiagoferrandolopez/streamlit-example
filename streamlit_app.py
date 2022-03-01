import pandas as pd
import streamlit as st
import numpy as np
# Importing the libraries

import pandas as pd
import numpy as np

st.title("Ponsse Data Analysis")

# Importing the dataset
Cobra = "C:\\Users\\administra\\Ponsse\\cobra_hv.xlsx"
Ergo = "C:\\Users\\administra\\Ponsse\\ergo_hv.xlsx"
Ambas= "C:\\Users\\administra\\Ponsse\\cobra_ergo_hv.xlsx"

df = pd.read_excel(Cobra)
dff = pd.read_excel(Ergo)
both=pd.read_excel(Ambas)

st.dataframe(df)
st.dataframe(dff)
st.dataframe(both)

