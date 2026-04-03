import os
import random
import numpy as np
import pandas as pd

np.random.seed(42)
random.seed(42)

base_dir = os.path.dirname(os.path.dirname(__file__))
out_path = os.path.join(base_dir, "data", "sample_game_data.csv")

n_users = 1500
days = pd.date_range("2026-01-01", periods=60, freq="D")
regions = ["NA", "EU", "APAC", "LATAM"]
platforms = ["PC", "Mobile", "Console"]
acq = ["Organic", "Ads", "Referral", "Influencer", "Cross-Promo"]

rows = []
for uid in range(1, n_users + 1):
    install_date = np.random.choice(days[:40])
    region = random.choice(regions)
    platform = random.choice(platforms)
    source = random.choice(acq)
    variant = np.random.choice(["A", "B"], p=[0.5, 0.5])
    payer_prob = 0.09 if variant == "A" else 0.115
    retained_bias = 0.48 if variant == "A" else 0.54

    active_span = min(np.random.geometric(0.11), 30)

    for d in range(active_span):
        event_date = install_date + pd.Timedelta(days=d)
        if event_date > days[-1]:
            break

        retain_factor = max(0.15, retained_bias - d * 0.015 + np.random.normal(0, 0.03))
        if np.random.rand() > retain_factor:
            break

        sessions = max(1, int(np.random.poisson(2.2 if variant == "A" else 2.5)))
        session_minutes = max(8, np.random.normal(28 if variant == "A" else 31, 10))
        levels_completed = max(0, int(np.random.poisson(2.4 if variant == "A" else 2.8)))
        purchase = 1 if np.random.rand() < payer_prob / max(1, d + 1) ** 0.15 else 0
        revenue = round(np.random.gamma(2, 4.5), 2) if purchase else 0.0

        rows.append([
            uid, str(event_date.date()), region, platform, source, variant,
            sessions, round(session_minutes, 1), levels_completed, purchase, revenue
        ])

df = pd.DataFrame(rows, columns=[
    "user_id", "event_date", "region", "platform", "acquisition_source",
    "test_variant", "sessions", "avg_session_minutes", "levels_completed",
    "purchase_flag", "revenue_usd"
])

df.to_csv(out_path, index=False)
print(f"Saved dataset to: {out_path}")
