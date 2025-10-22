"""
INSTRUCTIONS TO RUN THIS APP:
1. Ensure you have Python installed.
2. Place 'patient_id_with_updated_doctors and multiple prescription.csv' in the same directory as this file.
3. Install required packages by running:
   pip install streamlit pandas plotly
4. Start the app with:
   streamlit run app.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# Developer Details
st.markdown("""
**Developer:** VUYYALA HIMACHAND  
**Roll Number:** 321020 
**Class:** V PHARM. D  
---
""")

# Executive Summary
st.markdown("""
### Executive Summary
- The clinical dataset covers a diverse patient population with a wide age range and balanced gender distribution.
- Most patients are managed by a small group of doctors, with a few conditions accounting for the majority of prescriptions.
- The average patient age and the most common medical condition are highlighted in the KPIs below.
- Visualizations provide insights into demographic patterns, doctor workload, and prevalent health issues.
- These trends can inform resource allocation and targeted healthcare interventions.
---
""")

# Load data
csv_file = "patient_id_with_updated_doctors and multiple prescription.csv"
df = pd.read_csv(csv_file)

st.title("Clinical Data Dashboard")

# KPIs
total_patients = df['Patient_ID'].nunique()
avg_age = round(df['Age'].mean(), 1)
num_doctors = df['Doctor_Name'].nunique()
num_conditions = df['Condition'].nunique()
most_common_condition = df['Condition'].mode()[0]

kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)
kpi1.metric("Total Patients", total_patients)
kpi2.metric("Avg. Age", avg_age)
kpi3.metric("Doctors", num_doctors)
kpi4.metric("Conditions", num_conditions)
kpi5.metric("Most Common Condition", most_common_condition)

st.markdown("---")

# Prepare figures
fig_age = px.histogram(
    df,
    x='Age',
    nbins=15,
    color_discrete_sequence=['#636EFA'],
    title='Patient Age Distribution',
    labels={'Age': 'Patient Age'},
    opacity=0.85
)
fig_age.update_layout(bargap=0.1, xaxis_title='Age', yaxis_title='Number of Patients')

fig_gender = px.pie(
    df,
    names='Gender',
    title='Gender Distribution',
    color_discrete_sequence=px.colors.sequential.RdBu
)

fig_condition = px.histogram(
    df,
    x='Condition',
    color_discrete_sequence=['#00CC96'],
    title='Prescriptions per Condition',
    labels={'Condition': 'Medical Condition'},
    opacity=0.85
)
fig_condition.update_layout(bargap=0.2, xaxis_title='Condition', yaxis_title='Number of Prescriptions')

fig_doctor = px.pie(
    df,
    names='Doctor_Name',
    title='Patients per Doctor',
    color_discrete_sequence=px.colors.sequential.Plasma
)

# 2x2 grid layout
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig_age, use_container_width=True)
    st.plotly_chart(fig_condition, use_container_width=True)
with col2:
    st.plotly_chart(fig_gender, use_container_width=True)
    st.plotly_chart(fig_doctor, use_container_width=True)

# Optionally, add more charts below the grid if needed
if df['Blood_Pressure'].nunique() < 20:
    st.subheader("Blood Pressure Category Distribution")
    fig_bp = px.pie(
        df,
        names='Blood_Pressure',
        title='Blood Pressure Category Distribution',
        color_discrete_sequence=px.colors.sequential.Viridis
    )
    st.plotly_chart(fig_bp, use_container_width=True)

st.subheader("Glucose Level Distribution")
fig_glucose = px.histogram(
    df,
    x='Glucose_Level',
    nbins=15,
    color_discrete_sequence=['#EF553B'],
    title='Glucose Level Distribution',
    labels={'Glucose_Level': 'Glucose Level'},
    opacity=0.85
)
fig_glucose.update_layout(bargap=0.1, xaxis_title='Glucose Level', yaxis_title='Number of Patients')
st.plotly_chart(fig_glucose, use_container_width=True)
