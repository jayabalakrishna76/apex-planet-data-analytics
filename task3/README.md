# 📊 Amazon Sales Data Visualization & Dashboard

## ApexPlanet Software Pvt. Ltd. – Task 3

This project was completed as part of the ApexPlanet Data Analytics Internship – Task 3.

The objective of this task is to analyze Amazon sales data, create meaningful data visualizations using Python, and develop an interactive Power BI dashboard for business analysis.

---

## 🎯 Objective

The main objectives of this project are:

- Analyze Amazon sales data.
- Create meaningful visualizations using Python.
- Identify sales trends and product category performance.
- Analyze order and sales patterns.
- Build an interactive Power BI dashboard.
- Present important business KPIs in an easy-to-understand format.

---

## 📂 Dataset

The project uses an Amazon sales dataset containing information about:

- Order ID
- Date
- Status
- Fulfilment
- Sales Channel
- SKU
- Category
- Size
- Amount
- Qty
- Courier Status
- Ship City
- Ship State
- Ship Country
- B2B
- Other order-related attributes

The dataset was cleaned and stored as:

`data/processed_data.csv`

---

## 🧹 Data Preparation

The dataset was processed before visualization.

Major preparation steps included:

- Loading the dataset using Pandas.
- Checking dataset structure.
- Handling missing values.
- Converting the Date column into datetime format.
- Checking numerical columns.
- Preparing categorical columns for analysis.
- Saving the processed dataset as `processed_data.csv`.

---

# 📈 Python Data Visualization

Python was used to create several visualizations using:

- Pandas
- Matplotlib
- Seaborn
- Plotly

### Visualizations Created

### 1. Daily Sales Trend

A line chart was created to analyze how sales changed over time.

**File:**

`plots/line_chart.png`

---

### 2. Top Product Categories

A bar chart was created to compare sales/product distribution across categories.

**File:**

`plots/bar_chart.png`

---

### 3. Sales Amount Distribution

A histogram was created to understand the distribution of sales amounts.

**File:**

`plots/histogram.png`

---

### 4. Quantity vs Sales Amount

A scatter plot was created to analyze the relationship between quantity sold and sales amount.

**File:**

`plots/scatter_plot.png`

---

### 5. Correlation Heatmap

A heatmap was created to examine relationships between numerical variables.

**File:**

`plots/heatmap.png`

---

### 6. Sales Amount Box Plot

A box plot was created to identify the distribution and possible outliers in sales amounts.

**File:**

`plots/boxplot.png`

---

### 7. Pair Plot

A pair plot was created to compare relationships between selected numerical variables.

**File:**

`plots/pairplot.png`

---

### 8. Interactive Plotly Visualization

An interactive visualization was created using Plotly.

**File:**

`plots/interactive_plot.html`

---

# 📊 Power BI Dashboard

An interactive Power BI dashboard is being developed using the processed Amazon sales dataset.

The dashboard provides an overview of sales performance and allows users to interact with the data using filters and visualizations.

## Dashboard Components

### KPI Cards

The dashboard includes:

- Total Sales
- Total Orders
- Total Quantity
- Average Sales

### Charts

The dashboard includes:

- Daily Sales Trend
- Sales by Category
- Order Status Distribution
- Sales by State
- Top 10 Products by Sales

### Interactive Filters

The dashboard provides filters for:

- Date
- Category
- State
- Status

These filters allow users to explore specific parts of the dataset interactively.

---

# 🧮 Key Performance Indicators

### Total Sales

Total revenue generated from the orders.

```text
Total Sales = SUM(Amount)