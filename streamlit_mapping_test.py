import pandas as pd
import numpy as np
import streamlit as st

DATA_URL = ('https://raw.githubusercontent.com/safety-analytics-mapping/streamlit_testing/main/data/data.csv')


@st.cache_data
def load_data(rows):
    data = pd.read_csv(DATA_URL, nrows=rows)
    return data[data['lat']>0]

data = load_data(1000)

st.title("Sample data map app")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


st.subheader('Number of event by hour')
hist_values = np.histogram(
    data['hr'], bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

# hour_to_filter = st.slider('hour', 0, 23, 8)  # min: 0h, max: 23h, default: 8
add_slider = st.sidebar.slider(
    'Select a range of values',
    0, 23, (8, 17)
)

filtered_data = data[data['hr'].between(add_slider[0], add_slider[1])]
st.subheader(f'Map of all events between {add_slider[0]}:00 and {add_slider[1]}:00')
st.map(filtered_data)

records = filtered_data.lat.count()
st.subheader(f'{records} records found')