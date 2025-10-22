# 🏥 Clinical Data Dashboard

-----

## 🎯 Project Overview

This is a **Streamlit web application** designed to visualize and analyze clinical patient data. It provides an interactive dashboard with Key Performance Indicators (**KPIs**) and various charts (using **Plotly Express**) to gain insights into patient demographics, common medical conditions, doctor workload, and prescription patterns.

The dashboard facilitates a quick and comprehensive understanding of the clinical dataset, which can inform resource allocation and targeted healthcare interventions.

-----

## 📁 Project Structure

This project has a straightforward structure, containing the main application script and the required dataset.

```
.
├── Assignment.8.py                       # The main Streamlit application script
├── patient_id_with_updated_doctors and   # The primary dataset (CSV format) used for the dashboard
│   multiple prescription.csv             
├── README.md                             # This file
└── requirements.txt                      # List of Python dependencies
```

-----

## ⚙️ Installation and Setup

### Prerequisites

  * **Python 3.8+**
  * **Git** (optional, for cloning the repository)

### 1\. Clone the Repository (Optional)

```bash
git clone <repository_url>
cd <project-folder-name>
```

### 2\. Prepare Data File

Ensure the file `patient_id_with_updated_doctors and multiple prescription.csv` is placed in the project's root directory, alongside `Assignment.8.py`.

### 3\. Install Dependencies

Create a `requirements.txt` file with the following contents and install them:

**`requirements.txt`**

```
streamlit
pandas
plotly
```

Run the installation command:

```bash
pip install -r requirements.txt
```

-----

## 🚀 Usage

### Run the Application

Start the Streamlit application from your terminal in the project directory:

```bash
streamlit run Assignment.8.py
```

### Access the Dashboard

Your web browser should automatically open the dashboard at: **`http://localhost:8501`**.

-----

## ✨ Key Features & Visualizations

The dashboard provides a variety of interactive charts to explore the data:

  * **Key Performance Indicators (KPIs):** Displays **Total Patients**, **Average Age**, **Number of Doctors**, and the **Most Common Condition**.
  * **Demographic Insights:** Charts showing **Age Distribution** (Histogram) and **Gender Distribution** (Pie/Bar Chart).
  * **Clinical Analysis:**
      * **Prescriptions per Condition** (Bar Chart).
      * **Patients per Doctor** (Pie Chart showing workload distribution).
      * **Blood Pressure** and **Glucose Level** distributions.

-----

## 🛠️ Technology Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Dashboard** | **Streamlit** | Rapidly building and hosting the web application. |
| **Data Processing** | **Pandas** | Loading, cleaning, and aggregating the CSV data. |
| **Visualization** | **Plotly Express** | Generating rich, interactive, and mobile-friendly charts. |

-----

## 👤 Developer

**VUYYALA HIMACHAND** (Roll Number: 321020)

-----
