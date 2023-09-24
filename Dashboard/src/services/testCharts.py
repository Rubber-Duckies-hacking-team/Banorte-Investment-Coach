import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Create a histogram
arr = np.random.normal(1, 1, size=100)
fig_hist, ax_hist = plt.subplots()
ax_hist.hist(arr, bins=20)

# Display the histogram using st.pyplot()
st.pyplot(fig_hist)

# Assuming you have a DataFrame called specific_df with "Date" and "Closing_Price" columns
# Replace this with your actual data
# Example data:
specific_df = pd.DataFrame({
    "Date": ["2023-09-01", "2023-09-02", "2023-09-03", "2023-09-04", "2023-09-05"],
    "Closing_Price": [100, 105, 102, 110, 108]
})

# Input company_name (you can get it from the user)
company_name = "Your Company Name"

# Create a line chart
fig_line, ax_line = plt.subplots(figsize=(15, 6))
ax_line.plot(specific_df["Date"], specific_df["Closing_Price"], marker=".")
ax_line.set_title("Closing Prices Over Time for stock " + company_name)
ax_line.set_xlabel("Date")
ax_line.set_ylabel("Closing Price")
ax_line.set_xticklabels(specific_df["Date"], rotation=45)
ax_line.grid(True)

# Display the line chart using st.pyplot()
st.pyplot(fig_line)
