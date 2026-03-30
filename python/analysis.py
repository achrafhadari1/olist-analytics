import pandas as pd

# ── LOAD DATA ─────────────────────────────────────────────────────────────────
dataframe = pd.read_csv("./data/merged_data.csv")

# ── CLEAN ─────────────────────────────────────────────────────────────────────
# Convert date columns to datetime
date_cols = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
    "shipping_limit_date"
]
for col in date_cols:
    dataframe[col] = pd.to_datetime(dataframe[col])

# Drop rows with no delivery date — can't analyse delivery without it
dataframe = dataframe.dropna(subset=["order_delivered_customer_date"])

# Add is_late and delivery_days columns
dataframe["is_late"] = dataframe["order_delivered_customer_date"] > dataframe["order_estimated_delivery_date"]
dataframe["delivery_days"] = (dataframe["order_delivered_customer_date"] - dataframe["order_purchase_timestamp"]).dt.days

# ── MERGE SUPPORTING DATASETS ─────────────────────────────────────────────────
# Products + English category translation
products_df = pd.read_csv("./data/olist_products_dataset.csv")
translation_df = pd.read_csv("./data/product_category_name_translation.csv")
products_df = products_df.merge(translation_df, on="product_category_name", how="left")
dataframe = dataframe.merge(
    products_df[["product_id", "product_category_name_english"]],
    on="product_id",
    how="left"
)

# Customers (for state data)
customers_df = pd.read_csv("./data/olist_customers_dataset.csv")
dataframe = dataframe.merge(customers_df, on="customer_id", how="inner")

# ── ANALYSIS ──────────────────────────────────────────────────────────────────

# Q1 — Late delivery percentage
late_pct = round((dataframe["is_late"].sum() / len(dataframe)) * 100, 2)
print(f"Q1 — Late deliveries: {late_pct}%")
print()

# Q2 — Revenue by product category (top 10)
revenue = dataframe.groupby("product_category_name_english")["price"].sum().reset_index()
revenue.columns = ["category", "total_revenue"]
revenue = revenue.sort_values("total_revenue", ascending=False).head(10)
print("Q2 — Revenue by category (top 10):")
print(revenue.to_string(index=False))
print()

# Q3 — Average delivery time by state
dt_by_state = dataframe.groupby("customer_state")["delivery_days"].mean().reset_index()
dt_by_state.columns = ["state", "avg_delivery_days"]
dt_by_state = dt_by_state.sort_values("avg_delivery_days")
print("Q3 — Delivery time by state (fastest first):")
print(dt_by_state.to_string(index=False))
print()
# Q4 — Monthly order trend
monthly_stats = dataframe.groupby(
    dataframe["order_purchase_timestamp"].dt.to_period("M")
)["order_id"].count().reset_index()
monthly_stats.columns = ["month", "orders"]
monthly_stats = monthly_stats.sort_values("month")
print("Q4 — Monthly order trend:")
print(monthly_stats.to_string(index=False))
print()

# Q5 — Top 10 customers by total spend
top_customers = dataframe.groupby("customer_id")["price"].sum().reset_index()
top_customers.columns = ["customer_id", "total_spend"]
top_customers = top_customers.sort_values("total_spend", ascending=False).head(10)
print("Q5 — Top 10 customers by spend:")
print(top_customers.to_string(index=False))

revenue.to_csv("./output/revenue_by_category.csv", index=False)
dt_by_state.to_csv("./output/delivery_by_state.csv", index=False)
monthly_stats.to_csv("./output/monthly_stats.csv", index=False)
top_customers.to_csv("./output/top_customers.csv",index=False)
result_df = pd.DataFrame({"late_delivery_percentage": [late_pct]})
result_df.to_csv("./output/late_pct.csv", index=False)
