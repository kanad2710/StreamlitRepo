import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
#import vega_datasets as vega
from vega_datasets import data
from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title("Example Streamlit App :balloon:")
st.write(
    """Normal Text
    **Bold Text**
    :green[ Colored Text ]
    """
)

st.write(f"""Streamlit Version {st.__version__}""")

# Get the current credentials
# session = get_active_session()

conn = st.connection("snowflake")

# Area Chart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)

#Area Chart
# source = data.unemployment_across_industries()

# st.area_chart(source, x="date", y="count", color="series", stack="center")

# Map

st.write(f"""Example of 3D Map""")

chart_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)


st.pydeck_chart(
    pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=chart_data,
                get_position="[lon, lat]",
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                "ScatterplotLayer",
                data=chart_data,
                get_position="[lon, lat]",
                get_color="[200, 30, 0, 160]",
                get_radius=200,
            ),
        ],
    )
)

# Map


# Map2

# Table_Query = """select DATE_PART(WEEK,to_date(START_TIME)) AS WEEK, COUNT(*) AS Count
#    from snowflake.account_usage.query_history
#    where WEEK > 0 and WEEK < 18
#    GROUP BY WEEK
#    order by WEEK ASC"""

# sql_data2 = session.sql(Table_Query).to_pandas()


#st.subheader("Queries Executed per Week")
#st.dataframe(data=sql_data2, use_container_width=True)
# df = st.dataframe(sql_data2, use_container_width=True)
# df.reset_index(drop=True)

#sql_data2.style.set_properties(subset=['WEEK'], **{'font-weight': 'bold'})

#st.line_chart(data=sql_data2, x="WEEK", y="COUNT")

st.title("Chat Feature")
