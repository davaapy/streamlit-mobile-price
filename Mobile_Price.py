import pickle
import streamlit as st

model = pickle.load(open('Mobile_Price.sav', 'rb'))

st.title('Estimasi Klasifikasi Mobile Price ')

battery_power = st.number_input(
    'Masukan umur', step=1, max_value=100, min_value=1)
m_dep = st.number_input(
    'Masukan Gender,laki laki (Input1),perempuan (Input2)',  step=1, max_value=2, min_value=1)
mobile_wt = st.number_input(
    'Masukan atypical angina: nyeri dada tidak berhubungan dengan jantung')
px_height = st.number_input('Masukan chest pain type')
px_width = st.number_input('Masukan tekanan darah %',
                           step=1, max_value=250, min_value=1)
ram = st.number_input('Masukan nomer serum cholestoral dalam mg/dl')
talk_time = st.number_input('Masukan fasting gula darah',
                            step=1, max_value=250, min_value=1)
three_g = st.number_input(
    'Masukan sinyal detak jantung yang tidak normal', min_value=20.0, step=0.1)
price_range = st.number_input(
    'Masukan denyut jantung maksimum tercapai', step=1, max_value=250, min_value=1)


predict = ''

if st.button(' Estimasi Klasifikasi Mobile Price'):
    predict = model.predict(
        [[battery_power, m_dep, mobile_wt, px_height, px_width, ram, talk_time, three_g, price_range

          ]]
    )
    st.write('Estimasi Klasifikasi Mobile Prices  Dalam Ponds: ', predict)
    st.write('Estimasi Klasifikasi Mobile   Dalam TES: ', predict*8000)
