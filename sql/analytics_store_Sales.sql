SELECT store, SUM(weekly_sales) AS total_sales
FROM sales_database.cleaned_sales_data
GROUP BY store
ORDER BY total_sales DESC;

