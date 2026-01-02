
import pandas as pd
import matplotlib.pyplot as plt

players = pd.read_csv("../data/players.csv")

# Profession distribution
players["profession"].value_counts().plot(kind="bar")
plt.title("Professions of Club Ultimate Players (Mock Data)")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Age joined club by division
players.boxplot(column="age_joined_club", by="gender_division")
plt.title("Age Joined Club by Division")
plt.suptitle("")
plt.ylabel("Age")
plt.show()
