import os
import pandas as pd
from scipy.stats import ttest_ind

base_dir = os.path.dirname(os.path.dirname(__file__))
data_path = os.path.join(base_dir, "data", "sample_game_data.csv")
df = pd.read_csv(data_path)
df["event_date"] = pd.to_datetime(df["event_date"])

# Daily metrics
daily = df.groupby("event_date").agg(
    dau=("user_id", "nunique"),
    revenue=("revenue_usd", "sum"),
    avg_session=("avg_session_minutes", "mean")
).reset_index()

# Variant performance
variant = df.groupby("test_variant").agg(
    users=("user_id", "nunique"),
    avg_sessions=("sessions", "mean"),
    avg_session_minutes=("avg_session_minutes", "mean"),
    conversion_rate=("purchase_flag", "mean"),
    avg_revenue=("revenue_usd", "mean")
).reset_index()

# simple significance test on session length
a = df[df["test_variant"] == "A"]["avg_session_minutes"]
b = df[df["test_variant"] == "B"]["avg_session_minutes"]
stat, p_value = ttest_ind(a, b, equal_var=False)

print("\n=== Daily Metrics Sample ===")
print(daily.head())

print("\n=== A/B Variant Summary ===")
print(variant)

print(f"\nT-test on avg session minutes: p-value = {p_value:.5f}")
if p_value < 0.05:
    print("Result: statistically significant difference between variants.")
else:
    print("Result: no statistically significant difference detected.")
