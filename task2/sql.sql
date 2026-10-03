SELECT* FROM processed_data;
SELECT 'Order ID', Category, Amount
FROM processed_data;
SELECT 'Order ID', Amount
FROM processed_data
WHERE Amount>1000;
SELECT 'Order ID', Amount
FROM processed_data
ORDER BY Amount DESC;
SELECT 'Order ID', Amount
FROM Processed_data
ORDER BY Amount DESC
LIMIT 10;
SELECT Category,
SUM (AMOUNT) AS Total_Sales
FROM processed_data
GROUP BY Category;
SELECT Category,
SUM (Amount) AS Total_Sales
FROM processed_data
GROUP BY Category
HAVING SUM (Amount)>100000;
SELECT Category,
COUNT(*) AS Orders
FROM processed_data
GROUP BY Category;


