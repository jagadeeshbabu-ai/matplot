import matplotlib.pyplot as plt

months = [
    "Jan", "Feb", "Mar",
    "Apr", "May", "Jun",
    "Jul", "Aug", "Sep",
    "Oct", "Nov", "Dec"
]

revenue_2025= [
    4242.37, 4242.37, 4242.37,
    5310.67, 5310.67, 5310.67,
    5558.77, 5558.77, 5558.77,
    6033.63, 6033.63, 6033.63
]


revenue_2024 = [
    4242.18, 4242.18, 4242.18,
    4689.71, 4689.71, 4689.71,
    4814.80, 4814.80, 4814.80,
    5324.18, 5324.18, 5324.18
]


plt.xlabel("months")
plt.ylabel("revenue in crores")
plt.title("dmart monthly revenue")
plt.plot(months,revenue_2025,marker="o",markersize=4,color="green",markerfacecolor="red")
plt.plot(months,revenue_2024,marker="o",markersize=4,color="red",markerfacecolor="white")
plt.grid()
plt.legend(["revenue_2025","revenue_2024"],loc="upper left")
plt.tight_layout()
plt.savefig("dmart_monthly_revenue.png")
plt.show()
