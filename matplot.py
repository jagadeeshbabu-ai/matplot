# import matplotlib.pyplot as plt
# months = ["Jan", "Feb", "Mar", "Apr", "May"]
# sales = [120, 150, 140, 180, 210]

# plt.plot(months, sales)
# plt.show()


# import matplotlib.pyplot as plt

# months = ["Jan", "Feb", "Mar", "Apr", "May"]
# sales = [120, 150, 140, 180, 210]

# plt.figure(figsize=(9, 5))

# plt.plot(
#     months,
#     sales,
#     marker="o",
#     linestyle="-",
#     linewidth=2,
#     label="Sales",
    
# )

# plt.title("Monthly Sales Trend")
# plt.xlabel("Month")
# plt.ylabel("Sales (₹ thousands)")

# plt.grid()
# plt.legend()

# plt.tight_layout()
# plt.savefig("monthly_sales.png", dpi=300, bbox_inches="tight")
# plt.show()

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [420, 460, 440, 510, 560, 590]

plt.figure(figsize=(10, 5))
plt.plot(months, sales, marker="o", linewidth=2)

plt.title("E-Commerce Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales (₹ thousands)")

plt.grid()
plt.tight_layout()
plt.show()

