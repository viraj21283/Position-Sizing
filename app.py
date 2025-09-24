# app.py
# Streamlit Position Sizing Calculator
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

def calc_position_size(capital, risk, entry_price, stop_loss_price):
    risk_per_unit = abs(entry_price - stop_loss_price)
    if risk_per_unit == 0:
        st.error("Entry Price and Stop Loss Price cannot be the same.")
        return 0
    position_size = risk / risk_per_unit
    return int(position_size)

with st.form("position_sizer_form"):
    st.subheader("Enter Your Details")
    capital = st.number_input('Total Capital', min_value=0.0, value=100000.0)
    risk_type = st.selectbox(
        'Risk Input Type',
        ('Absolute amount (currency units)', 'Percentage of Capital', 'Percentage of Previous Profit')
    )

    risk = 0.0  # Default risk initialization
    # Show only relevant risk field
    if risk_type == 'Absolute amount (currency units)':
        risk = st.number_input('Amount Willing to Risk (currency units)', min_value=0.0, value=2000.0)
    elif risk_type == 'Percentage of Capital':
        risk_percent = st.number_input('Risk Percentage of Capital', min_value=0.0, max_value=100.0, value=2.0)
        risk = (risk_percent / 100) * capital
    elif risk_type == 'Percentage of Previous Profit':
        previous_profit = st.number_input('Previous Realized Profit (currency units)', min_value=0.0, value=10000.0)
        risk_percent = st.number_input('Risk Percentage of Previous Profit', min_value=0.0, max_value=100.0, value=50.0)
        risk = (risk_percent / 100) * previous_profit

    entry_price = st.number_input('Entry Price', min_value=0.0, value=1500.0)
    stop_loss_price = st.number_input('Stop Loss Price', min_value=0.0, value=1470.0)

    submitted = st.form_submit_button("Calculate Position Size")

if submitted:
    position_size = calc_position_size(capital, risk, entry_price, stop_loss_price)
    if position_size > 0:
        st.success(f'**Position Size:** {position_size} units')
        st.info(f"""
            **Summary:**  
            - Capital: {capital}
            - Risk Amount: {risk}
            - Entry Price: {entry_price}
            - Stop Loss Price: {stop_loss_price}
        """)
        st.markdown("""
        ---
        ❤️ *Made with love by Viraj Shah*  
        **Disclaimer:** This app is for educational purposes only and is not financial advice.
        """)
