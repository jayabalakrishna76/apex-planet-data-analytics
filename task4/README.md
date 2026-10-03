# Task 4 – Advanced Analytics & Statistical Modeling

## 📌 Project Overview

This project is part of **Task 4 – Advanced Analytics & Statistical Modeling**. The objective is to analyze an Amazon e-commerce order dataset using statistical analysis, hypothesis testing, time-series analysis, clustering, and predictive modeling.

The project uses Python and Jupyter Notebook to extract meaningful insights from order, sales, product, and fulfillment data.

---

## 🎯 Objectives

- Perform descriptive statistical analysis.
- Analyze the distribution of order quantity and order amount.
- Conduct hypothesis testing using t-test and chi-square test.
- Calculate confidence intervals.
- Analyze sales trends over time.
- Perform K-Means clustering.
- Use the Elbow Method to determine the appropriate number of clusters.
- Visualize clusters using PCA.
- Build a Logistic Regression model to predict order cancellation.
- Evaluate the predictive model using classification metrics.
- Identify important predictive features.
- Generate actionable business insights.

---

## 📂 Dataset

The project uses an Amazon order-processing dataset containing information about orders, products, sales, fulfillment, shipping, and order status.

### Important Features

| Feature | Description |
|---|---|
| `Order ID` | Unique order identifier |
| `Date` | Order date |
| `Status` | Order fulfillment/cancellation status |
| `Fulfilment` | Fulfillment method |
| `Sales Channel` | Sales channel |
| `Category` | Product category |
| `Size` | Product size |
| `ASIN` | Amazon product identifier |
| `Qty` | Quantity ordered |
| `Amount` | Order amount in INR |
| `ship-city` | Shipping city |
| `ship-state` | Shipping state |
| `B2B` | Business-to-business indicator |

---

## 🛠️ Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- Scikit-learn

---

## 🔬 Project Workflow

### 1. Data Loading

The Amazon dataset is loaded using Pandas and inspected for:

- Number of rows and columns
- Column names
- Data types
- Missing values
- Duplicate records

### 2. Data Cleaning

The dataset is prepared by:

- Removing unnecessary columns
- Removing duplicate records
- Converting `Date` to datetime format
- Converting `Qty` and `Amount` to numeric values
- Handling missing values

### 3. Descriptive Statistics

Statistical measures are calculated for important numerical variables:

- Mean
- Median
- Mode
- Standard deviation
- Skewness
- Minimum and maximum values
- Quartiles

### 4. Hypothesis Testing

#### T-Test

An independent t-test is performed to determine whether there is a statistically significant difference in order amounts between different fulfillment methods.

#### Chi-Square Test

A chi-square test is used to investigate the relationship between:

**Product Category ↔ Order Status**

A significance level of **0.05** is used.

### 5. Confidence Interval

A **95% confidence interval** is calculated for the average order amount.

### 6. Time-Series Analysis

Daily sales are analyzed to identify trends.

The project includes:

- Daily sales aggregation
- Sales trend visualization
- 7-day moving average

### 7. K-Means Clustering

K-Means clustering is applied using order-level numerical features such as:

- Quantity
- Order Amount

The data is standardized using `StandardScaler`.

### 8. Elbow Method

The Elbow Method is used to determine a suitable number of clusters.

The selected clustering configuration is then used for segmentation.

### 9. PCA Visualization

Principal Component Analysis (PCA) reduces the clustering features to two dimensions so that the clusters can be visualized.

### 10. Predictive Modeling

A **Logistic Regression** model is developed to predict whether an order is cancelled.

Target:

- `1` → Cancelled
- `0` → Not Cancelled

The dataset is divided into:

- **80% Training**
- **20% Testing**

### 11. Model Evaluation

The model is evaluated using:

- Accuracy
- Precision
- Recall
- Classification Report
- Confusion Matrix

Feature coefficients are also analyzed to identify the most influential available predictors.

---

## 📊 Business Insights

The analysis helps identify:

- Order value distribution and variability.
- Differences in order values between fulfillment methods.
- Relationships between product categories and order status.
- Sales trends over time.
- Different order-value and quantity segments.
- Factors associated with order cancellations.
- Potential areas for improving fulfillment and cancellation management.

---

## ⚠️ Dataset Limitation

The dataset does not contain a dedicated **Customer ID** field. Therefore, the clustering analysis is treated as **order/product segmentation** rather than true customer segmentation.

This limitation is explicitly considered when interpreting the clustering results.

---

## 📁 Project Structure

```text
Task-4-Advanced-Analytics/
│
├── processed_data.csv
│
├── Task_4_Advanced_Analytics_Amazon.ipynb
│
├── task4_processed_amazon_data.csv
│
└── README.md
```

---

## ▶️ How to Run

### 1. Install required libraries

```bash
pip install pandas numpy matplotlib seaborn scipy scikit-learn jupyter
```

### 2. Start Jupyter Notebook

```bash
jupyter notebook
```

### 3. Open

```text
Task_4_Advanced_Analytics_Amazon.ipynb
```

### 4. Place the dataset in the same folder

```text
processed_data.csv
```

### 5. Run the notebook cells sequentially

---

## 📌 Conclusion

This project demonstrates the application of **advanced statistical analysis, hypothesis testing, time-series analysis, unsupervised learning, dimensionality reduction, and predictive modeling** to an Amazon e-commerce dataset.

The analysis provides a data-driven understanding of sales behavior, order patterns, fulfillment differences, order segmentation, and cancellation prediction.

---

## 👨‍💻 Author

**Sai Dheeraj**

Artificial Intelligence and Data Science

### Internship Task

**Apex Planet Software