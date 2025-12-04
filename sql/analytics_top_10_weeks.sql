SELECT date, SUM(weekly_sales) AS total_sales
FROM sales_database.cleaned_sales_data
GROUP BY date
ORDER BY total_sales DESC
LIMIT 10;

