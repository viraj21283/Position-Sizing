# app.py
# Position Sizing Calculator
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

def calc_stoploss_price(cmp, stoploss_percent):
    return cmp - (cmp * stoploss_percent / 100)

def calc_position_size(risk_amount, cmp, stoploss_price):
    per_unit_risk = abs(cmp - stoploss_price)
    if per_unit_risk == 0:
        return 0
    return int(risk_amount / per_unit_risk)

def calc_portfolio_positions(portfolio_capital, risk_percent, stocks_count):
    risk_total = (risk_percent / 100) * portfolio_capital
    risk_per_stock = risk_total / stocks_count if stocks_count else 0
    return stocks_count, risk_total, risk_per_stock

st.subheader("Select Calculator Type")

calc_type = st.selectbox(
    "Calculator Type",
    ["Risk as % of Capital", "Risk as Absolute Value", "Portfolio Risk"]
)

if calc_type == "Risk as % of Capital":
    capital = st.number_input('Total Capital', min_value=0.0, value=100000.0)
    risk_percent = st.number_input('Risk Percentage', min_value=0.0, max_value=100.0, value=5.0)
    cmp = st.number_input('Current Market Price (CMP)', min_value=0.0, value=1000.0)
    stoploss_percent = st.number_input('Stoploss Percentage', min_value=0.0, max_value=100.0, value=2.0)

    if st.button("Calculate"):
        risk_amount = (risk_percent / 100) * capital
        stoploss_price = calc_stoploss_price(cmp, stoploss_percent)
        position_size = calc_position_size(risk_amount, cmp, stoploss_price)
        st.success(f"Stoploss Price: ₹{stoploss_price:,.2f}")
        st.success(f"Position Size: {position_size} units")
        st.info(f"Risk Amount: ₹{risk_amount:,.2f}")

elif calc_type == "Risk as Absolute Value":
    capital = st.number_input('Total Capital', min_value=0.0, value=100000.0)
    abs_risk = st.number_input('Absolute Risk Amount', min_value=0.0, value=2000.0)
    cmp = st.number_input('Current Market Price (CMP)', min_value=0.0, value=1000.0)
    stoploss_percent = st.number_input('Stoploss Percentage', min_value=0.0, max_value=100.0, value=2.0)

    if st.button("Calculate"):
        stoploss_price = calc_stoploss_price(cmp, stoploss_percent)
        position_size = calc_position_size(abs_risk, cmp, stoploss_price)
        st.success(f"Stoploss Price: ₹{stoploss_price:,.2f}")
        st.success(f"Position Size: {position_size} units")
        st.info(f"Risk Amount: ₹{abs_risk:,.2f}")

elif calc_type == "Portfolio Risk":
    portfolio_capital = st.number_input('Portfolio Capital', min_value=0.0, value=200000.0)
    risk_percent = st.number_input('Risk Percentage on Portfolio', min_value=0.0, max_value=100.0, value=2.0)
    stocks_count = st.number_input('Number of Stocks in Portfolio', min_value=1, value=10)

    if st.button("Calculate Portfolio"):
        stocks_count, risk_total, risk_per_stock = calc_portfolio_positions(portfolio_capital, risk_percent, stocks_count)
        st.success(f"Number of Stocks: {stocks_count}")
        st.info(f"Total Portfolio Risk: ₹{risk_total:,.2f}")
        st.info(f"Risk Amount per Stock: ₹{risk_per_stock:,.2f}")

st.markdown("""
---
❤️ *Made with love by Viraj Shah*  
**Disclaimer:** This app is for educational purposes only and is not financial advice.
""")
