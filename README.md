# Summer-2022-Data-Science-Intern-Challenge

This Repository contains the resolution of the 'Summer 2022 Data Science Intern Challenge'

## Question 1
 On Shopify, we have exactly 100 sneaker shops, and each of these shops sells only one model of shoe. We want to do some analysis of the average order value (AOV).  When we look at orders data over a 30 day window, we naively calculate an AOV of $3145.13. Given that we know these shops are selling sneakers, a relatively       affordable item, something seems wrong with our analysis. 

  a. Think about what could be going wrong with our calculation. Think about a better way to evaluate this data. 
   - When the total order amount is divided by 5,000, we assume that the amount of shoes purchased in orders does not vary as much as it actually does. For instance, we have some orders whose value reaches $704,000, increasing the AOV a lot. It is also easy to notice the presence of outliers in the data when comparing measures of central tendency, as the median and mode are more similar and the mean is a much higher value.
When we put the data into a histogram, we can see that majority of the order value is below $3,000 (even less than the AOV).

  b. What metric would you report for this dataset? 
   - When we check the outliers and the majority of the order values we can see that those 63 outliers are very distinct than the majority of the average order amount and we have to process them separately. Therefore, I would report either the Median or the mean of the order values without the outliers, as more accurate values (preferably the mean of the without the outliers).
 
  c. What is its value?
   - Mean of the order values without the outliers: 302.58
  

## Question 2
 For this question you’ll need to use SQL. Follow this link to access the data set required for the challenge. Please use queries to answer the following questions. Paste your queries along with your final numerical answers below.
 
  a. How many orders were shipped by Speedy Express in total?
     
```mysql
SELECT COUNT(*) 
FROM Orders o
JOIN Shippers s ON o.ShipperID = s.ShipperID
WHERE s.ShipperName = "Speedy Express";
```

  - Answer: 54 
     
  b. What is the last name of the employee with the most orders?
  
```mysql
SELECT e.LastName, COUNT(*)
FROM Employees e
JOIN Orders o ON e.EmployeeID = o.EmployeeID
GROUP BY o.EmployeeID 
ORDER BY COUNT(*) DESC
LIMIT 1
```
   - Answer: 
  
|LastName|Orders|
|--------|------|
|Peacock |  40  |

  c. What product was ordered the most by customers in Germany?
  
```mysql
SELECT od.ProductID, p.ProductName, COUNT(od.Quantity)
FROM Orders o
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE c.Country = "Germany"
GROUP BY od.ProductID
ORDER BY COUNT(od.Quantity) DESC
LIMIT 1
```
   - Answer: 
  
|    ProductName     |Orders|
|--------------------|------|
|Gorgonzola Telino   |  160 |
 
  
