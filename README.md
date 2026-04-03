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

## Example business questions answered
1. Did Variant B improve player engagement?
2. Which regions show the strongest retention?
3. Which acquisition channels bring the highest-value players?
4. Did the tested feature improve monetization?

## Resume bullet you can use
Built a gaming analytics project using Python, SQL, and dashboard-style reporting to analyze player retention, A/B test performance, engagement, and monetization trends across 1,500+ simulated users, translating gameplay data into product insights.

## Interview explanation
"I built this project to show how I would analyze player behavior in a gaming product. I used Python and SQL to evaluate retention, engagement, and monetization, then compared A/B test variants to see whether a feature improved player outcomes. I structured it like a real analyst workflow so I could demonstrate both technical analysis and business storytelling."

## Note
This uses synthetic data for portfolio/demo purposes.
