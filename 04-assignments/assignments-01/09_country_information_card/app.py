import streamlit as st
import requests

def fetch_country_info(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        country_data = data[0]
        name = country_data['name']['common']
        capital = country_data['capital'][0]
        population = country_data['population']
        area = country_data['area']
        currency = country_data['currencies'].keys()
        region = country_data['region']
        return name, capital, population, area, currency, region
    else:
        return None
    
def main():
    st.title("Country Information Card")
    country_name = st.text_input("Enter the country name:")
    if country_name:
        name, capital, population, area, currency, region = fetch_country_info(country_name)
        if name:
            st.write(f"Name: {name}")
            st.write(f"Capital: {capital}")
            st.write(f"Population: {population}")
            st.write(f"Area: {area}")
            st.write(f"Currency: {currency}")
            st.write(f"Region: {region}")
        else:
            st.write("Country not found")
            
if __name__ == "__main__":
    main()