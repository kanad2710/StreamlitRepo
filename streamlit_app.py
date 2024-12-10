import streamlit as st
import pandas as pd
import numpy as np
#import vega_datasets as vega
from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title("Github Streamlit Integration")
# st.title("Example Streamlit App :balloon:")
st.write(
    """Normal Text
    **Bold Text**
    :green[ Colored Text ]
    """
)

st.write(f"""Streamlit Version {st.__version__}""")

# Get the current credentials
# session = get_active_session()


# Area Chart
st.title("Area Chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)



