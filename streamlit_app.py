from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

x = st.slider('x')
st.write(x, 'squared is', x * x)
