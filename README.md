# Ultimate Frisbee Club Network Project

## Overview
This project explores who elite U.S. club ultimate players are beyond on-field statistics.
It focuses on:
- Origin stories (how players found ultimate)
- Professions and off-field identities
- Geographic hubs of elite ultimate
- Age at which players join club teams
- Social and team networks, separated by gender division

## Data
Currently, the `data/` folder contains **mock data** to illustrate structure.

### players.csv
- player_id
- name
- gender_division
- profession
- origin_story
- age_joined_club
- hub_city

### team_memberships.csv
- player_id
- team
- year
- gender_division

## Visualizations to Build
- Sankey diagram: origin_story → club division
- Bar charts: professions by division
- Map: geographic hubs of elite club ultimate
- Network graph: players connected by shared teams (faceted by division)
- Distribution: age_joined_club by division

## Notes on Real Data
There is no single public dataset containing personal background information for club players.
To extend this project:
- Use USA Ultimate rosters
- Scrape team websites and player bios
- Manually curate origin/profession data for top clubs
- Clearly document assumptions and missing data

## Ethics
This project should avoid sensitive personal data and rely only on publicly available or self-disclosed information.

## Structure
- data/: CSV files
- src/: analysis and visualization scripts (to be added)
- visualizations/: exported figures
