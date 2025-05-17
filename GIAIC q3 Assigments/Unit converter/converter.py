
import streamlit as st

def temp_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    return value

def main():
    st.title("🌡️ Temperature Unit Converter")

    units = ["Celsius", "Fahrenheit", "Kelvin"]

    from_unit = st.selectbox("Convert from:", units)
    to_unit = st.selectbox("Convert to:", units)

    value = st.number_input("Enter the temperature value:", format="%.2f")

    if st.button("Convert"):
        result = temp_converter(value, from_unit, to_unit)
        st.success(f"{value:.2f} {from_unit} = {result:.2f} {to_unit}")

if __name__ == "__main__":
    main()
