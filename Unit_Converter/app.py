import streamlit as st


#Title
st.title("⚖️🔁 Unit Converter")

#Sidebar
st.sidebar.title("Choose Unit")

#Unit options
unit_selct= st.sidebar.radio(
    "Select Unit",
            ["Length", "Weight", "Time", "Speed", "Temperature", "Volume", "Area", "Digital Storage"])

#Unit conversion functions
conv_list = {
      "Length":{"Meters":0.001, "Kilometers":1000, "Feet":0.3048, "Inches": 0.0254, "Yards": 0.9144, "Miles": 1609.34},
      "Weight": {"Gram":1, "Kilogram":1000, "Milligram":0.001, "Tonne":1000000, "Pound":453.592, "Ounce":28.3495} , 
      "Time" : {"Second":1, "Minute":60, "Hour":3600, "Day":86400, "Week":604800},
      "Speed": {"Meters per second":1, "Kilometers per hour":0.27778, "Miles per hour":0.44704},
      "Volume": {"Liter":1, "Milliliter":0.001, "Cubic meter":1000, "Gallon(US)":3.78541, "Gallon(UK)":4.54609},
      "Area" :{"Square meter":1, "Square kilometer":1000000, "Acre":4046.86, "Hectare":10000},
      "Digital Storage" :{"Bit":1, "Byte":8, "Kilobyte":8*10**3, "Megabyte":8*10**6, "Gigabyte":8*10**9, "Terabyte":8*10**12}
 }


# Conversion of Temperature
def temperature_conv(value,unit_from,unit_to):

    if unit_from == unit_to:
      return value
    
    if unit_from == "Celsius":
        if unit_to == "Fahrenheit":
            return (value * 9/5) + 32
        elif unit_to == "Kelvin":
            return value + 273.15
        
    elif unit_from == "Fahrenheit":
        if unit_to == "Celsius":
            return (value - 32) * 5/9
        elif unit_to == "Kelvin":
            return (value - 32) * 5/9 + 273.15

    elif unit_from == "Kelvin":
        if unit_to == "Celsius":
            return value - 273.15
        elif unit_to == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32   
    return None

#conversion of general units
def gen_unit_conv(value,unit_from,unit_to,conv_unit_list):

    if unit_from == unit_to:
      return value
    
    base_val = value * conv_unit_list[unit_from]
    return base_val / conv_unit_list[unit_to]

#user Input
if unit_selct == "Temperature":
    unit_list = ["Celsius","Fahrenheit" , "Kelvin"]
    unit_from = st.selectbox("From", unit_list)
    unit_value=st.number_input("Enter Value", min_value=1.0, format="%.2f")
    unit_to = st.selectbox("To", unit_list)
    precision= st.slider("Select Decimal Precision", min_value=0, max_value=6, value=2)
    converted_value = round(temperature_conv(unit_value,unit_from,unit_to), precision) 

else:    
    unit_list = list(conv_list[unit_selct].keys())
    unit_from = st.selectbox("From", unit_list)
    unit_value=st.number_input("Enter Value", min_value=1.0, format="%.2f")
    unit_to = st.selectbox("To", unit_list)
    precision= st.slider("Select Decimal Precision", min_value=0, max_value=6, value=2)
    converted_value = round(gen_unit_conv(unit_value,unit_from,unit_to ,conv_list[unit_selct]), precision) 

st.write(f"{unit_value} {unit_from} is equal to {converted_value} {unit_to}")

st.write("©️ Created by Laiba Anwar")
