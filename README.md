# Olist E-Commerce Analytics

A data analysis project exploring 100,000+ Brazilian e-commerce orders
from 2016 to 2018. Built with Python and SQL to answer real business
questions about delivery performance, revenue, and customer behaviour.

---

## Dataset

**Brazilian E-Commerce Public Dataset by Olist**  
Source: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce  
100k orders made across multiple Brazilian marketplaces between 2016–2018.

---

## Business Questions

1. What percentage of orders were delivered late?
2. Which product categories generated the most revenue?
3. Which states have the fastest average delivery time?
4. How did monthly order volume trend over time?
5. Who are the top customers by total spend?

---

## Tools Used

- Python 3
- pandas — data cleaning and analysis
- SQL — business logic queries
- Oracle / PostgreSQL — database

---

## Project Structure

```
olist-analytics/
├── data/
│   ├── olist_orders_dataset.csv
│   ├── olist_order_items_dataset.csv
│   ├── olist_products_dataset.csv
│   ├── olist_customers_dataset.csv
│   ├── product_category_name_translation.csv
│   └── merged_data.csv
├── python/
│   ├── merge.py       # merges raw CSVs into one dataset
│   └── analysis.py    # answers all 5 business questions
├── sql/               # SQL equivalents of all analyses
└── README.md
```

---

## How to Run

1. Clone the repo
2. Download the Olist dataset from Kaggle and place CSVs in `/data`
3. Run `python/merge.py` to generate the merged dataset
4. Run `python/analysis.py` to see all results
5. SQL queries are in `/sql` — run against your local database

---

## Key Findings

- **Late deliveries:** 7.9% of orders arrived after the estimated delivery date
- **Top category:** Health & beauty generated the most revenue at R$1,233,211
- **Fastest state:** São Paulo had the shortest average delivery time at 8.3 days
- **Order trend:** Peak month was November 2017 with 8,474 orders — likely Black Friday
- **Top customer:** Spent R$13,440 across their orders

---

## Author

achrafhadari.com · linkedin.com/in/achrafhadari
