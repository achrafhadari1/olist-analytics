# Olist E-Commerce Analytics

A data analysis project exploring 100,000+ Brazilian e-commerce orders from 2016 to 2018. Built with Python and SQL to answer real business questions about delivery performance, revenue, and customer behaviour.

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
- PostgreSQL / Oracle — database

---

## Project Structure

```
olist-analytics/
├── data/
│   ├── olist_orders_dataset.csv
│   ├── olist_order_items_dataset.csv
│   └── merged_data.csv
├── python/
│   └── merge.py
├── sql/
└── README.md
```

---

## How to Run

1. Clone the repo
2. Download the Olist dataset from Kaggle and place CSVs in `/data`
3. Run `python/merge.py` to generate the cleaned merged dataset
4. SQL queries are in `/sql` — run against your local database

---

## Key Findings

---

## Author

[Achraf Hadari] · [https://www.linkedin.com/in/achrafhadari/]
