import matplotlib.pyplot as plt
years = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
users = [1.21, 1.435, 1.69, 1.96, 2.243, 2.728, 2.99]

plt.title("instagram year to growth")
plt.xlabel("years")
plt.ylabel("user billions")
plt.plot(years,users,marker="*",markersize=4,color="blue",markerfacecolor="red")
plt.grid()
plt.legend(users,loc="upper left")
plt.tight_layout()
plt.savefig("instagram.png")

plt.show()