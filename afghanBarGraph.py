import matplotlib.pyplot as plt

# among people seeking refuge or asylum from AFG to USA in the year 2022. afghan refugee population in the year 2022
refugees_data = { # for each female and male, put the numbers for each age group

    # for row, one element represents age groups ordered "<4", "5-11", "12-17", "18-59", "60+", "-1"

    "Female"  : [0, 5, 5, 61, 0, 0],
    "Male"    : [0, 10, 0, 164, 0, 5]
}
age_groups = ["<4", "5-11", "12-17", "18-59", "60+", "-1*"] # -1 represents unknown, these are x values

fig, ax = plt.subplots()

bar_width = 0.35

x_pos_female = [i - bar_width / 2 for i in range(len(age_groups))]
x_pos_male = [i + bar_width / 2 for i in range(len(age_groups))]

ax.bar(x_pos_female, refugees_data["Female"], color="red", width=bar_width, label = "Female")
ax.bar(x_pos_male, refugees_data["Male"], color="green", width=bar_width, label = "Male")
ax.set_xlabel("Age Group", fontsize=12, color = 'grey')
ax.set_ylabel("Number of Refugees", fontsize=12, color = 'grey')
ax.set_title("Demographics of Afghan Refugees in US, 2022", fontweight="bold", fontsize=12)
ax.legend()

ax.set_xticks([i for i in range(len(age_groups))])
ax.set_xticklabels(age_groups)

plt.xticks(rotation=45, ha="right")

# * '-1' implies unknown age btw. Source: https://data.worldbank.org/indicator/SM.POP.REFG?locations=AF"

plt.annotate ( # for specifications
    text = "* - Unknown age. Source: https://data.worldbank.org/indicator/SM.POP.REFG?locations=AF",
    xy = (5.5, 5),
    xytext = (10, 25),
    arrowprops = dict(facecolor = "black", shrink = 0.05)
)

# plt.tight_layout() completely optional
plt.show()
