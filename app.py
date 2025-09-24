# app.py
# Position Sizing Calculator with Dynamic Scenarios
# Made with ❤️ by Viraj Shah

import streamlit as st

st.set_page_config(page_title="Position Sizing Calculator", page_icon="❤️")

st.markdown("""
### Position Sizing Calculator

Made with ❤️ by **Viraj Shah**

> **Disclaimer:**  
> This Streamlit app is for educational purposes only and does *not* constitute financial advice.  
> Please consult a qualified financial advisor before making investment decisions.
---
""")

def calculate_percentage_risk(capital, risk_percent, cmp, stoploss_percent):
    risk_amount = (risk_percent / 100) * capital
    stoploss_price = cmp - (cmp * stoploss_percent / 100)
    position_size = int(risk_amount / (cmp - stoploss_price))
    return stoploss_price, position_size, risk_amount

def calculate_absolute_risk(abs_risk, cmp, stoploss_percent):
    stoploss_price = cmp - (cmp * stoploss_percent / 100)
    position_size = int(abs_risk / (cmp - stoploss_price))
    return stoploss_price, position_size

def calculate_portfolio_risk(portfolio_capital, risk_percent, cmp, stoploss_percent, stocks_count):
    risk_per_stock = (risk_percent / 100) * portfolio_capital / stocks_count
    stoploss_price = cmp - (cmp * stoploss_percent / 100)
    position_size_per_stock = int(risk_per_stock / (cmp - stoploss_price))
    return stocks_count, stoploss_price, position_size_per_stock, risk_per_stock

st.subheader("Select Position Sizing Scenario")

scenario = st.selectbox(
    "Calculator Type",
    ["Risk as % of Capital", "Risk as Absolute Value", "Portfolio Risk"]
)

if scenario == "Risk as % of Capital":
    capital = st.number_input('Total Capital', min_value=0.0, value=100000.0)
    risk_percent = st.number_input('Risk Percentage', min_value=0.0, max_value=100.0, value=5.0)
    cmp = st.number_input('Current Market Price (CMP)', min_value=0.0, value=1000.0)
    stoploss_percent = st.number_input('Stoploss Percentage', min_value=0.0, max_value=100.0, value=2.0)

    if st.button("Calculate"):
        stoploss_price, position_size, risk_amount = calculate_percentage_risk(
            capital, risk_percent, cmp, stoploss_percent
        )
        st.success(f"Stoploss Price: ₹{stoploss_price:,.2f}")
        st.success(f"Position Size: {position_size} units")
        st.info(f"Risk Amount: ₹{risk_amount:,.2f}")

elif scenario == "Risk as Absolute Value":
    capital = st.number_input('Total Capital', min_value=0.0, value=100000.0)
    abs_risk = st.number_input('Absolute Risk Amount', min_value=0.0, value=2000.0)
    cmp = st.number_input('Current Market Price (CMP)', min_value=0.0, value=1000.0)
    stoploss_percent = st.number_input('Stoploss Percentage', min_value=0.0, max_value=100.0, value=2.0)

    if st.button("Calculate"):
        stoploss_price, position_size = calculate_absolute_risk(
            abs_risk, cmp, stoploss_percent
        )
        st.success(f"Stoploss Price: ₹{stoploss_price:,.2f}")
        st.success(f"Position Size: {position_size} units")

elif scenario == "Portfolio Risk":
    portfolio_capital = st.number_input('Portfolio Capital', min_value=0.0, value=200000.0)
    risk_percent = st.number_input('Risk Percentage on Portfolio', min_value=0.0, max_value=100.0, value=2.0)
    stocks_count = st.number_input('Number of Stocks in Portfolio', min_value=1, value=10)
    cmp = st.number_input('Average CMP per Stock', min_value=0.0, value=1000.0)
    stoploss_percent = st.number_input('Stoploss Percentage per Stock', min_value=0.0, max_value=100.0, value=2.0)

    if st.button("Calculate Portfolio"):
        stocks, stoploss_price, position_size, risk_per_stock = calculate_portfolio_risk(
            portfolio_capital, risk_percent, cmp, stoploss_percent, stocks_count
        )
        st.success(f"Number of Stocks: {stocks}")
        st.success(f"Stoploss Price per Stock: ₹{stoploss_price:,.2f}")
        st.success(f"Position Size per Stock: {position_size} units")
        st.info(f"Risk Amount per Stock: ₹{risk_per_stock:,.2f}")

st.markdown("""
---
❤️ *Made with love by Viraj Shah*  
**Disclaimer:** This app is for educational purposes only and is not financial advice.
""")
