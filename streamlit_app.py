import pandas as pd
import streamlit as st
import numpy as np
# Importing the libraries

import pandas as pd
import numpy as np

st.title("Harvester Data Analysis")
st.header("Productivity DATA")
st.subheader("MOM analytics")
Ponsse = "https://github.com/santiagoferrandolopez/streamlit-example/blob/master/Ponsse.xlsx"
df=pd.read_excel("Ponsse")
