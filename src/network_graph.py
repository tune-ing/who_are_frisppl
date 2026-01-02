
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

players = pd.read_csv("../data/players.csv")
memberships = pd.read_csv("../data/team_memberships.csv")

# Build graph: players connected if they shared a team
G = nx.Graph()

for _, row in players.iterrows():
    G.add_node(row["player_id"], label=row["name"], division=row["gender_division"])

for team, group in memberships.groupby(["team", "year", "gender_division"]):
    ids = group["player_id"].tolist()
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            G.add_edge(ids[i], ids[j], team=team[0])

# Draw network (simple layout)
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=False, node_size=300)

labels = nx.get_node_attributes(G, "label")
nx.draw_networkx_labels(G, pos, labels, font_size=8)

plt.title("Club Ultimate Player Network (Mock Data)")
plt.show()
