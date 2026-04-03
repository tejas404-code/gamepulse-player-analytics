-- Game analytics SQL queries for portfolio/demo use

-- 1) Daily Active Users
SELECT
  event_date,
  COUNT(DISTINCT user_id) AS dau
FROM sample_game_data
GROUP BY event_date
ORDER BY event_date;

-- 2) Revenue by test variant
SELECT
  test_variant,
  SUM(revenue_usd) AS total_revenue,
  AVG(revenue_usd) AS avg_revenue_per_event
FROM sample_game_data
GROUP BY test_variant;

-- 3) Conversion rate by variant
SELECT
  test_variant,
  AVG(CASE WHEN purchase_flag = 1 THEN 1.0 ELSE 0.0 END) AS conversion_rate
FROM sample_game_data
GROUP BY test_variant;

-- 4) Region-level engagement
SELECT
  region,
  AVG(avg_session_minutes) AS avg_session_minutes,
  AVG(sessions) AS avg_sessions,
  AVG(levels_completed) AS avg_levels_completed
FROM sample_game_data
GROUP BY region
ORDER BY avg_session_minutes DESC;

-- 5) Acquisition source quality
SELECT
  acquisition_source,
  COUNT(DISTINCT user_id) AS players,
  SUM(revenue_usd) AS revenue,
  AVG(purchase_flag * 1.0) AS conversion_rate
FROM sample_game_data
GROUP BY acquisition_source
ORDER BY revenue DESC;
