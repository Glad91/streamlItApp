import streamlit as st
import numpy_financial as npf
import streamlit.components.v1 as components

def main():
    # Setting page configuration
    st.set_page_config(page_title="Calculateur de Prêt", page_icon=":money_with_wings:", layout="centered")
    
    # Adding custom CSS for better styling
    st.markdown("""
        <style>
            .stButton button {
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
                padding: 10px 20px;
            }
            .result-card {
                background-color: #f0f2f6;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
                margin: 20px 0;
            }
            .result-title {
                font-weight: bold;
                color: #333;
                margin-bottom: 10px;
            }
            .result-value {
                font-size: 1.5em;
                color: #007BFF;
            }
        </style>
    """, unsafe_allow_html=True)

    # Title and description
    st.title("💰 Calculateur de Prêt")
    st.write("Cette application permet de calculer les mensualités d'un crédit en fonction du montant emprunté, de la durée, et du taux d'intérêt.")

    # Input fields for the loan details
    principal = st.number_input("Montant du prêt (€)", min_value=0, value=50000, step=1000)
    rate = st.number_input("Taux d'intérêt annuel (%)", min_value=0.0, value=3.5, step=0.1) / 100
    years = st.number_input("Durée du prêt (années)", min_value=1, value=7, step=1)
    insurance_rate = st.number_input("Taux d'assurance annuel (%)", min_value=0.0, value=0.5, step=0.1) / 100

    # Calculate monthly payment
    monthly_rate = rate / 12
    months = years * 12
    monthly_payment = npf.pmt(monthly_rate, months, -principal)

    # Calculate total interest over the loan period
    total_payment = monthly_payment * months
    total_interest = total_payment - principal

    # Calculate insurance cost
    annual_insurance_cost = principal * insurance_rate
    total_insurance_cost = annual_insurance_cost * years
    monthly_insurance_cost = annual_insurance_cost / 12

    # Calculate monthly payment including insurance
    total_monthly_payment = monthly_payment + monthly_insurance_cost

    # Display the results in a styled way
    st.markdown("""
        <div class="result-card">
            <div class="result-title">Mensualités à payer (hors assurance) :</div>
            <div class="result-value">{:.2f} €</div>
        </div>
        <div class="result-card">
            <div class="result-title">Mensualités à payer (assurance incluse) :</div>
            <div class="result-value">{:.2f} €</div>
        </div>
        <div class="result-card">
            <div class="result-title">Coût total des intérêts sur la période :</div>
            <div class="result-value">{:.2f} €</div>
        </div>
        <div class="result-card">
            <div class="result-title">Coût total de l'assurance sur la période :</div>
            <div class="result-value">{:.2f} €</div>
        </div>
    """.format(monthly_payment, total_monthly_payment, total_interest, total_insurance_cost), unsafe_allow_html=True)

if __name__ == "__main__":
    main()