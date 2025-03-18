import streamlit as st
st.set_page_config(page_title="Unit Converter", layout="centered")

conversion_factors = {
    "Plane Angle": {"Degree": 1.0, "Arcsecond": 1/3600, "Gradian": 0.9, "Milliradian": 0.0572958, "Minute of arc": 1/60, "Radian": 57.2958},
    "Length": {"Meter": 1.0, "Kilometer": 1000.0, "Centimeter": 0.01, "Millimeter": 0.001, "Micrometer": 1e-6, "Nanometer": 1e-9, "Mile": 1609.34, "Yard": 0.9144, "Foot": 0.3048, "Inch": 0.0254, "Nautical Mile": 1852.0},
    "Mass": {"Kilogram": 1.0, "Gram": 0.001, "Milligram": 1e-6, "Microgram": 1e-9, "Pound": 0.453592, "Ounce": 0.0283495, "Stone": 6.35029, "Ton (metric)": 1000.0},
    "Temperature": {
        "Celsius": {"to_base": lambda x: x, "from_base": lambda x: x},
        "Fahrenheit": {"to_base": lambda x: (x - 32) * 5/9, "from_base": lambda x: (x * 9/5) + 32},
        "Kelvin": {"to_base": lambda x: x - 273.15, "from_base": lambda x: x + 273.15}
    },
    "Speed": {"Meters per second": 1.0, "Kilometers per hour": 0.277778, "Miles per hour": 0.44704, "Knots": 0.514444, "Feet per second": 0.3048},
    "Time": {"Second": 1.0, "Minute": 60.0, "Hour": 3600.0, "Day": 86400.0, "Week": 604800.0, "Month": 2629746.0, "Year": 31556952.0},
    "Volume": {"Liter": 1.0, "Milliliter": 0.001, "Cubic meter": 1000.0, "Cubic centimeter": 0.001, "Gallon (US)": 3.78541, "Gallon (UK)": 4.54609, "Quart": 0.946353, "Pint": 0.473176},
    "Pressure": {"Pascal": 1.0, "Kilopascal": 1000.0, "Bar": 100000.0, "Atmosphere": 101325.0, "PSI": 6894.76, "Torr": 133.322},
    "Energy": {"Joule": 1.0, "Kilojoule": 1000.0, "Calorie": 4.184, "Kilocalorie": 4184.0, "Kilowatt-hour": 3600000.0, "Electronvolt": 1.60218e-19},
    "Power": {"Watt": 1.0, "Kilowatt": 1000.0, "Megawatt": 1000000.0, "Horsepower": 745.7},
    "Fuel Economy": {"Miles per gallon (US)": 1.0, "Miles per gallon (UK)": 1.20095, "Kilometers per liter": 0.425144, "Liters per 100km": 235.215},
    "Data Transfer Rate": {"Bits per second": 1.0, "Kilobits per second": 1000.0, "Megabits per second": 1000000.0, "Gigabits per second": 1000000000.0},
    "Digital Storage": {"Bit": 1.0, "Byte": 8.0, "Kilobyte": 8000.0, "Megabyte": 8000000.0, "Gigabyte": 8000000000.0, "Terabyte": 8000000000000.0}
}

def convert_units(value, from_unit, to_unit, category):
    factors = conversion_factors.get(category, {})
    if category == "Temperature":
        return factors[to_unit]["from_base"](factors[from_unit]["to_base"](value))
    return (value * factors[from_unit]) / factors[to_unit]

st.title("Unit Converter")

conv_type = st.selectbox("Conversion Type", list(conversion_factors.keys()))
from_u = st.selectbox("From Unit", list(conversion_factors[conv_type].keys()))
to_u = st.selectbox("To Unit", list(conversion_factors[conv_type].keys()))
val = st.number_input("Enter Value", value=1.0, step=0.1)

if st.button("Convert"):
    result = convert_units(val, from_u, to_u, conv_type)
    st.write(f"**Result:** {result:.4f} {to_u}")
