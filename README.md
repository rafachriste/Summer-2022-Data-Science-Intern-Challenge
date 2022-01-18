# Summer-2022-Data-Science-Intern-Challenge

This Repository contains the resolution of the 'Summer 2022 Data Science Intern Challenge'

## Question 1
 On Shopify, we have exactly 100 sneaker shops, and each of these shops sells only one model of shoe. We want to do some analysis of the average order value (AOV).  When we look at orders data over a 30 day window, we naively calculate an AOV of $3145.13. Given that we know these shops are selling sneakers, a relatively       affordable item, something seems wrong with our analysis. 

  a. Think about what could be going wrong with our calculation. Think about a better way to evaluate this data. 

  b. What metric would you report for this dataset? 
 
  c. What is its value?
  
  

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
SELECT od.ProductID, p.ProductName, SUM(od.Quantity)
FROM Orders o
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE c.Country = "Germany"
GROUP BY od.ProductID
ORDER BY SUM(od.Quantity) DESC
LIMIT 1
```
   - Answer: 
  
|    ProductName     |Quantity|
|--------------------|--------|
|Boston Crab Meat    |   160  |
 
  
