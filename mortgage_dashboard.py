import streamlit as st

st.set_page_config(page_title="Mortgage Eligibility Checker", layout="centered")

st.title("🏡 Mortgage Eligibility Dashboard")
st.write("Estimate how much mortgage you might be eligible for based on your financial data.")

income = st.number_input("💼 Gross Annual Income (€)", min_value=0, step=1000, format="%d")
savings = st.number_input("💰 Current Savings (€)", min_value=0, step=1000, format="%d")
existing_debts = st.number_input("📉 Total Existing Debts (€)", min_value=0, step=1000, format="%d")
age = st.slider("🎂 Your Age", min_value=18, max_value=70, value=30)

if st.button("Check Eligibility"):
    mortgage_cap = (income * 4.5) - existing_debts + (savings * 0.9)
    mortgage_cap = round(mortgage_cap, 2)

    if mortgage_cap < 100000:
        st.error("❌ Based on your inputs, you may not be eligible for a mortgage above €100,000.")
        st.write("💡 Try increasing your savings or reducing your debts.")
    else:
        st.success(f"✅ Estimated Mortgage Eligibility: €{mortgage_cap:,.2f}")
        st.write("This is a rough estimate. Actual eligibility depends on lenders, credit score, and more.")

    st.markdown("---")
    st.subheader("📊 Mortgage Breakdown")
    st.write(f"- Base amount (Income x 4.5): €{income * 4.5:,.2f}")
    st.write(f"- Deducted debts: €{existing_debts:,.2f}")
    st.write(f"- Added savings (90%): €{savings * 0.9:,.2f}")
