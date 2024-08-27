import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    url = "https://github.com/MEADecarb/programtree/raw/main/Programlist%20-%20Sheet1.csv"
    try:
        return pd.read_csv(url)
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

def display_table(programs, data):
    filtered_data = data[data['Program Name'].isin(programs)]
    if not filtered_data.empty:
        for _, row in filtered_data.iterrows():
            st.markdown(f"[{row['Program Name']}]({row['URL']})")
    else:
        st.warning("No matching programs found.")

def main():
    st.title("MEA Program Selection Tool")

    data = load_data()
    if data.empty:
        st.stop()

    entity_type = st.selectbox(
        "What type of entity are you?",
        [
            "Select an option",
            "Residential Homeowner",
            "Commercial Entity / For-Profit Business",
            "Non-Profit Organization",
            "State Agency or Local Government",
            "Electric Utility or Energy Infrastructure Stakeholder",
            "Public Educational Organization",
            "Private Educational Organization"
        ]
    )

    if entity_type == "Select an option":
        st.warning("Please select an entity type.")
        return

    programs = []
    
    if entity_type == "Residential Homeowner":
        clean_energy_interest = st.selectbox(
            "Are you interested in a Clean Energy or Energy Storage Project?",
            ["Select an option", "Yes", "No"]
        )
        if clean_energy_interest == "Select an option":
            st.warning("Please select an option.")
        elif clean_energy_interest == "Yes":
            programs = [
                "Residential Clean Energy Rebate Program",
                "Maryland Solar Access Program",
                "Maryland Energy Storage Income Tax Credit"
            ]
        else:
            programs = ["Inflation Reduction Act HOME Energy Efficiency and Electrification Rebate Program"]

    elif entity_type == "Commercial Entity / For-Profit Business":
        commercial_interest = st.selectbox(
            "What are you interested in?",
            [
                "Select an option",
                "Clean Energy Technologies",
                "Energy Efficiency Technologies",
                "Electric Vehicles and EV Charging Technologies",
                "Capacity Building and Resiliency Planning"
            ]
        )
        if commercial_interest == "Select an option":
            st.warning("Please select an option.")
        elif commercial_interest == "Clean Energy Technologies":
            programs = [
                "OPEN Innovation Energy Grant Program",
                "Maryland Offshore Wind Workforce Training & Education Program",
                "Solar Canopy and Dual Use Technology Grant Program"
            ]
        elif commercial_interest == "Energy Efficiency Technologies":
            programs = [
                "Mechanical Insulation Grant Program",
                "Energy Efficiency Equity Grant Program",
                "Commercial, Industrial, & Agricultural Grant Program"
            ]
        elif commercial_interest == "Electric Vehicles and EV Charging Technologies":
            programs = [
                "Electric Vehicle Supply Equipment Rebate Program",
                "Medium-Duty and Heavy-Duty Zero-Emission Vehicle Grant Program"
            ]
        elif commercial_interest == "Capacity Building and Resiliency Planning":
            programs = [
                "Resilient Maryland Program",
                "Energy Efficiency and Conservation Block Grant"
            ]

    elif entity_type == "Non-Profit Organization":
        non_profit_interest = st.selectbox(
            "Are you interested in:",
            [
                "Select an option",
                "Clean Energy Technologies",
                "Energy Efficiency Technologies",
                "Electric Vehicles and EV Charging Technologies",
                "Capacity Building and Resiliency Planning"
            ]
        )
        if non_profit_interest == "Select an option":
            st.warning("Please select an option.")
        elif non_profit_interest == "Clean Energy Technologies":
            programs = [
                "OPEN Innovation Energy Grant Program",
                "Solar Canopy and Dual Use Technology Grant Program"
            ]
        elif non_profit_interest == "Energy Efficiency Technologies":
            programs = [
                "Energy Efficiency Equity Grant Program",
                "Resilient Maryland Program"
            ]
        elif non_profit_interest == "Electric Vehicles and EV Charging Technologies":
            programs = ["Electric Vehicle Supply Equipment Rebate Program"]
        elif non_profit_interest == "Capacity Building and Resiliency Planning":
            programs = ["Resilient Maryland Program"]

    elif entity_type == "State Agency or Local Government":
        government_interest = st.selectbox(
            "Are you interested in:",
            [
                "Select an option",
                "Clean Energy Technologies",
                "Energy Efficiency Technologies",
                "Electric Vehicles and EV Charging Technologies",
                "Capacity Building and Resiliency Planning",
                "Improving Resiliency and Energy Grid Infrastructure"
            ]
        )
        if government_interest == "Select an option":
            st.warning("Please select an option.")
        elif government_interest == "Clean Energy Technologies":
            programs = [
                "OPEN Innovation Energy Grant Program",
                "Solar Canopy and Dual Use Technology Grant Program",
                "Maryland Offshore Wind Workforce Training & Education Program"
            ]
        elif government_interest == "Energy Efficiency Technologies":
            programs = [
                "Mechanical Insulation Grant Program",
                "Energy Efficiency and Conservation Block Grant"
            ]
        elif government_interest == "Electric Vehicles and EV Charging Technologies":
            programs = [
                "Electric Vehicle Supply Equipment Rebate Program",
                "Medium-Duty and Heavy-Duty Zero-Emission Vehicle Grant Program"
            ]
        elif government_interest == "Capacity Building and Resiliency Planning":
            programs = [
                "Resilient Maryland Program",
                "Maryland Smart Energy Communities"
            ]
        elif government_interest == "Improving Resiliency and Energy Grid Infrastructure":
            programs = ["Clean Energy Siting Grant/Feasibility Study"]

    elif entity_type == "Electric Utility or Energy Infrastructure Stakeholder":
        utility_interest = st.selectbox(
            "Are you interested in:",
            [
                "Select an option",
                "Clean Energy Technologies",
                "Energy Efficiency Technologies",
                "Capacity Building and Resiliency Planning",
                "Improving Resiliency and Energy Grid Infrastructure"
            ]
        )
        if utility_interest == "Select an option":
            st.warning("Please select an option.")
        elif utility_interest == "Clean Energy Technologies":
            programs = [
                "OPEN Innovation Energy Grant Program",
                "Solar Canopy and Dual Use Technology Grant Program"
            ]
        elif utility_interest == "Energy Efficiency Technologies":
            programs = ["Mechanical Insulation Grant Program"]
        elif utility_interest == "Capacity Building and Resiliency Planning":
            programs = ["Resilient Maryland Program"]
        elif utility_interest == "Improving Resiliency and Energy Grid Infrastructure":
            programs = ["Clean Energy Siting Grant/Feasibility Study"]

    elif entity_type == "Public Educational Organization":
        public_edu_type = st.selectbox(
            "Are you a:",
            ["Select an option", "K-12 Public School", "Public College or Higher Learning Institution"]
        )
        if public_edu_type == "Select an option":
            st.warning("Please select an option.")
        elif public_edu_type == "K-12 Public School":
            programs = [
                "Decarbonizing Public Schools Program",
                "Electric School Bus Grant Program"
            ]
        elif public_edu_type == "Public College or Higher Learning Institution":
            programs = ["Higher Education Clean Energy Grant Pilot Program"]

    elif entity_type == "Private Educational Organization":
        private_edu_type = st.selectbox(
            "Are you a:",
            ["Select an option", "K-12 Private School", "Private College or Higher Learning Institution"]
        )
        if private_edu_type == "Select an option":
            st.warning("Please select an option.")
        elif private_edu_type == "K-12 Private School":
            programs = ["Commercial, Industrial, & Agricultural Grant Program"]
        elif private_edu_type == "Private College or Higher Learning Institution":
            programs = ["Higher Education Clean Energy Grant Pilot Program"]

    display_table(programs, data)

if __name__ == "__main__":
    main()
