import streamlit as st
import requests
import datetime

'''
# TaxiFareModel front
'''
'''
### Date & Time
'''


d = st.date_input(
    "Date",
    datetime.date(2019, 7, 6))
t = st.time_input('Time', datetime.time(8, 45))

d_t=datetime.datetime.combine(d,t)

st.write('Date and time of the fare:', d_t)
'''
### From
'''
pickup_longitude = st.number_input('pickup longitude')
st.write('pickup longitude is ', pickup_longitude)

pickup_latitude = st.number_input('pickup latitude')
st.write('pickup latitude is ', pickup_latitude)
'''
### To
'''
dropoff_longitude = st.number_input('dropoff longitude')
st.write('dropoff longitude is ', dropoff_longitude)

dropoff_latitude = st.number_input('dropoff latitude')
st.write('dropoff latitude is ', dropoff_latitude)
'''
### Number of passengers
'''
option = st.selectbox('Passenger count', [1,2,3,4,5,6])
st.write ('Passenger count is', option)









'''
## Fare Estimation
'''
if st.button('Calculate'):
    # print is visible in the server output, not in the page
    print('button clicked!')
    url = 'https://taxifare.lewagon.ai/predict'

    params={'pickup_datetime':d_t,
            'pickup_longitude':pickup_longitude,
            'pickup_latitude':pickup_latitude,
            'dropoff_longitude':dropoff_longitude,
            'dropoff_latitude':dropoff_latitude,
            'passenger_count':option
                }
    results=requests.get(url,params=params).json()
    result=results["fare"]

    st.write ('Taxi_fare is', result)
