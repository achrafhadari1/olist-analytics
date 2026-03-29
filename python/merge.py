import pandas as pd
 
# ── LOAD RAW DATA ─────────────────────────────────────────────────────────────
items_df = pd.read_csv("./data/olist_order_items_dataset.csv")
orders_df = pd.read_csv("./data/olist_orders_dataset.csv")
 
# ── MERGE & SAVE ──────────────────────────────────────────────────────────────
olist_df = orders_df.merge(items_df, on="order_id", how="inner")
olist_df.to_csv("./data/merged_data.csv", index=False)
 
print(f"Merged dataset: {len(olist_df)} rows, {olist_df.shape[1]} columns")
 