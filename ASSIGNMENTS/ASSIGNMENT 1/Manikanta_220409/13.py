import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

monthly_revenue = np.random.randint(1000, 5000, 12)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

plt.figure(figsize=(10, 6))
plt.plot(months, monthly_revenue, '--o', label="Revenue")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (₹)")
plt.legend()
plt.grid(True)
plt.show()

