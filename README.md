# GamePulse: Player Retention and A/B Test Analytics

A GitHub-ready portfolio project designed for **Data Analyst Intern** roles in gaming companies like Tencent.

## Project Goal
This project simulates a real-world gaming analytics workflow:
- analyze large-scale player behavior data
- measure retention, engagement, and monetization
- compare **A/B test variants**
- generate clear visual insights for product and business teams

## Why this project is relevant
This project directly matches common requirements in gaming data roles:
- **SQL** for KPI analysis
- **Python** for cleaning and analytics
- **A/B testing** for feature evaluation
- **Data visualization** for reporting
- business storytelling using player metrics

## Dataset
The sample dataset contains synthetic player activity across:
- regions: NA, EU, APAC, LATAM
- platforms: PC, Mobile, Console
- acquisition sources
- A/B test variants (A = control, B = treatment)

## KPIs covered
- Daily Active Users (DAU)
- Revenue by day
- Day-1 retention
- Conversion rate by A/B variant
- Average session length
- Levels completed per session window

## Project Structure
```bash
gamepulse-analytics/
├── README.md
├── requirements.txt
├── data/
│   └── sample_game_data.csv
├── scripts/
│   ├── generate_sample_data.py
│   └── analyze_game_data.py
├── sql/
│   └── game_analytics_queries.sql
└── assets/
    └── dashboard_mockup.png
```

## How to run
```bash
pip install -r requirements.txt
python scripts/analyze_game_data.py
```
