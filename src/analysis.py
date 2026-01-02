
import pandas as pd

players = pd.read_csv("../data/players.csv")
memberships = pd.read_csv("../data/team_memberships.csv")

# Basic summaries
print("Players by division")
print(players["gender_division"].value_counts())

print("\nAverage age joined club by division")
print(players.groupby("gender_division")["age_joined_club"].mean())

# Merge for network-style analysis
merged = memberships.merge(players, on=["player_id", "gender_division"])
print("\nSample merged data")
print(merged.head())
