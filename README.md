# mortgage-dashboard-streamlit

**Mortgage Eligibility Dashboard** is a simple Streamlit web app that estimates how much mortgage you might be eligible for based on your financial data.

---

## Features

- Input your **gross annual income**, **current savings**, **existing debts**, and **age** through an easy-to-use form  
- Calculates estimated mortgage eligibility using a straightforward formula  
- Provides a clear breakdown of the mortgage calculation  
- Displays eligibility feedback with actionable suggestions  

---

## How It Works

The mortgage eligibility is roughly calculated as:

Mortgage Cap = (Income × 4.5) - Existing Debts + (Savings × 0.9)

yaml
Kopiëren
Bewerken

- If the result is below €100,000, the app indicates you might not be eligible for a mortgage above that amount.  
- Otherwise, it shows your estimated eligibility amount.  

---

## Screenshots

![Dashboard Screenshot](./screenshot.png)  
*Example user interface for the mortgage eligibility calculator.*

---

## Tech Stack

- Python 3.8+  
- [Streamlit](https://streamlit.io/) for the web app frontend  
- Runs locally or deployed on [Streamlit Community Cloud](https://streamlit.io/cloud)  

---

## Getting Started

### Prerequisites

Make sure you have Python installed (version 3.8 or higher) and `pip` for package management.

### Installation

1. Clone the repo:

```bash
git clone https://github.com/EditaKristofora/mortgage-dashboard-streamlit.git
cd mortgage-dashboard-streamlit
Install dependencies:

bash
Kopiëren
Bewerken
pip install streamlit
Run the app:

bash
Kopiëren
Bewerken
streamlit run mortgage_dashboard.py
Open http://localhost:8501 in your browser to view the app.

Deployment
You can deploy this app easily on Streamlit Community Cloud:

Go to https://streamlit.io/cloud

Connect your GitHub repo

Deploy your app with a click!

Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
Created by Edita Kristofora
