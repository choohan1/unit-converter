import streamlit as st
def convert_units(value, from_unit, to_unit):
    print("value>>>",value)
    print("from_unit>>>",from_unit)
    print("to_unit>>>",to_unit)   
    # 1 kilometer = 1000 meters
    # 1 kilogram = 2.20462 pounds
    # 1 liter = 0.264172 gallons
    # 1 gram = 0.001 kilogram
    if from_unit == "kilometers" and to_unit == "meters":
        return value * 1000
    elif from_unit == "kilograms" and to_unit == "pounds":
        return value * 2.20462
    elif from_unit == "liters" and to_unit == "gallons":
        return value * 0.264172
    elif from_unit == "grams" and to_unit == "kilograms":
        return value * 0.001
    else:
        return None
    
# st.title("Unit Converter")
def main():
    st.title("Unit Converter App")
    st.write("Welcome to the Unit Converter App")
    value = st.number_input("Enter the value to convert:", min_value=0.0, step=0.1)
    from_unit = st.selectbox("Select the unit to convert from:", 
                              ["kilometers", "kilograms", "liters", "grams"])
    to_unit = st.selectbox("Select the unit to convert to:",
                            ["meters", "pounds", "gallons", "kilograms"])
    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit)
        if result is not None:
            st.success(f"{value} {from_unit} is equal to {result} {to_unit}")
        else:
            st.error("Conversion not supported for the selected units.")
if __name__ == "__main__":
    main()
    # st.write("This is a simple unit converter app.")
    # st.write("You can convert between kilometers, kilograms, liters, and grams.")
    # st.write("Select the units and enter the value to convert.")
    # st.write("Click the 'Convert' button to see the result.")
# Run the app using the command: streamlit run app.py
# To run the app, use the command: streamlit run app.py
# To run the app, use the command: streamlit run app.py
# To run the app, use the command: streamlit run app.py
# To run the app, use the command: streamlit run app.py
# To run the app, use the command: streamlit run app.py
# To run the app, use the command: streamlit run app.py
