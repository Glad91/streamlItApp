import streamlit as st
import numpy_financial as npf

def main():
    st.title("Calculateur de Prêt")
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

    # Display the results
    st.write(f"Mensualités à payer (hors assurance) : {monthly_payment:.2f} €")
    st.write(f"Mensualités à payer (assurance incluse) : {total_monthly_payment:.2f} €")
    st.write(f"Coût total des intérêts sur la période : {total_interest:.2f} €")
    st.write(f"Coût total de l'assurance sur la période : {total_insurance_cost:.2f} €")

if __name__ == "__main__":
    main()