import streamlit as st
import pickle

pickle_in = open('cocafe.pkl','rb')
classifier = pickle.load(pickle_in)

gender = st.radio(
    "เพศ",
    ('ชาย','หญิง'))
 
if gender == 'ชาย':
    val1 = 0
elif gender == 'หญิง': 
    val1 = 1
#st.write(val1)

age = st.slider('ระบุอายุ', 0, 75 , 18)
#st.write("ฉัน ", age, 'ปี')

occupation = st.radio(
    "อาชีพ",
    ('นักเรียน-นักศึกษา', 'ข้าราชการ', 'ธุรกิจส่วนตัว', 'พนักงานเอกชน'))
 
if occupation == 'นักเรียน-นักศึกษา':
    val2 = 1
elif occupation == 'ข้าราชการ': 
    val2 = 2
elif occupation == 'ธุรกิจส่วนตัว': 
    val2 = 3
elif occupation == 'พนักงานเอกชน': 
    val2 = 4
#st.write(val2)

taste = st.radio(
    "รสชาติ",
    ('เน้นมาก', 'เน้นปานกลาง', 'เน้นน้อย'))
 
if taste == 'เน้นมาก':
    val3 = 3
elif taste == 'เน้นปานกลาง': 
    val3 = 2
elif taste == 'เน้นน้อย':
    val3 = 1
#st.write(val3)

bakery = st.radio(
    "มีเบเกอรี่ขาย",
    ('เน้นมาก', 'เน้นปานกลาง', 'เน้นน้อย'))
 
if bakery == 'เน้นมาก':
    val4 = 3
elif bakery == 'เน้นปานกลาง': 
    val4 = 2
elif bakery == 'เน้นน้อย':
    val4 = 1
#st.write(val4)

price = st.radio(
    "ราคา",
    ('ถูก', 'ปานกลาง', 'สูง'))
 
if price == 'ถูก':
    val5 = 3
elif price == 'ปานกลาง': 
    val5 = 2
elif price == 'สูง':
    val5 = 1
#st.write(val5)

location = st.radio(
    "โลเคชัน",
    ('ไกล', 'พอดี', 'ใกล้'))
 
if location == 'ไกล':
    val6 = 3
elif location == 'พอดี': 
    val6 = 2
elif location == 'ใกล้':
    val6 = 1
#st.write(val6)

atmosphere = st.radio(
    "บรรยากาศ",
    ('เน้นมาก', 'เน้นปานกลาง', 'เน้นน้อย'))
 
if atmosphere == 'เน้นมาก':
    val7 = 3
elif atmosphere == 'เน้นปานกลาง': 
    val7 = 2
elif atmosphere == 'เน้นน้อย':
    val7 = 1
#st.write(val7)

submit = st.button('Predict')
if submit:
    #prediction = classifier.predict([[gender, age, occupation, taste, bakery, price, location, atmosphere]])
    prediction = classifier.predict([[val1,age,val2,val3,val4,val5,val6,val7]])
    #prediction = classifier.predict([[0,18,1,3,1,3,3,3]])

    if prediction == 0:
        st.success("คุณเหมาะกับคาเฟ่ประเภทที่ 1")
    else:
        st.error("คุณเหมาะกับคาเฟ่ประเภทที่ 2")