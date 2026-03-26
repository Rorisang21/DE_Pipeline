# Data Engineering Pipeline Project

## Overview

This project implements a data pipeline that extracts, transforms, and loads customer, order, and order item data into a PostgreSQL database.

The primary goal of the pipeline is to ensure data quality, enforce constraints, and maintain referential integrity across related datasets.

---

## Project Structure

- `schema.sql`  
  Defines the database schema including tables, primary keys, foreign keys, and constraints.

- `pipeline.py`  
  Handles data extraction, transformation, and loading into PostgreSQL.

- `SOLUTION.md`  
  Documents design decisions, data cleaning logic, and trade-offs made during development.

---

## Pipeline Workflow

### 1. Extract
- Customer and order item data are read from CSV files  
- Order data is read from a JSONL file  

### 2. Transform

#### Customers
- Emails converted to lowercase  
- Duplicate emails removed (keeping earliest signup date)  
- Invalid email formats filtered out  
- Columns cleaned and standardized  

#### Orders
- Status values normalized (e.g. "processing" → "placed")  
- Invalid statuses removed  
- Timestamps converted to datetime format  
- Orders with invalid customer references removed  

#### Order Items
- Records with zero or negative quantity removed  
- Records with zero or negative unit price removed  
- Records with invalid order references removed  

---

### 3. Load

- Data is loaded into PostgreSQL using SQLAlchemy  
- Tables are loaded in the correct order:
  1. customers  
  2. orders  
  3. order_items  

This ensures all foreign key constraints are satisfied.

---

## Data Integrity

Data validation is enforced at two levels:

- **Transformation stage (Python)**  
- **Database constraints (PostgreSQL)**  

This ensures that only clean and consistent data is stored.

---

## Key Features

- Enforces referential integrity across tables  
- Handles real-world data issues such as duplicates and invalid relationships  
- Aligns transformation logic with database constraints  
- Provides a reproducible pipeline for data processing  

---

## How to Run

1. Ensure PostgreSQL is running  
2. Create tables using `schema.sql`  
3. Update database connection in `pipeline.py`  
4. Run the pipeline:

```bash
python pipeline.py
