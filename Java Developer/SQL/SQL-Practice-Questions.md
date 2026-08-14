# SQL Practice Questions

Interview-style SQL queries with answers and explanations.

---

## 📝 Practice Set 1: Joins & Relationships

### Q1: Find the second highest salary
```sql
SELECT MAX(salary) FROM employee WHERE salary < (SELECT MAX(salary) FROM employee);
```

### Q2: Find employees who earn more than their manager
```sql
SELECT e.name FROM employee e JOIN employee m ON e.manager_id = m.id WHERE e.salary > m.salary;
```

### Q3: Find departments with more than 5 employees
```sql
SELECT d.name, COUNT(e.id) as cnt FROM department d JOIN employee e ON e.dept_id = d.id GROUP BY d.name HAVING COUNT(e.id) > 5;
```

---

## 📝 Practice Set 2: GROUP BY & Aggregations

### Q1: Count orders per customer
```sql
SELECT c.name, COUNT(o.id) as order_count, SUM(o.total) as total_spent 
FROM customers c LEFT JOIN orders o ON c.id = o.customer_id GROUP BY c.name;
```

### Q2: Find the most recent order date per customer
```sql
SELECT c.name, MAX(o.order_date) as last_order 
FROM customers c LEFT JOIN orders o ON c.id = o.customer_id GROUP BY c.name;
```

### Q3: Calculate running total of sales
```sql
SELECT order_date, total_amount, 
       SUM(total_amount) OVER (ORDER BY order_date ROWS UNBOUNDED PRECEDING) as running_total
FROM daily_sales;
```

---

## 📝 Practice Set 3: Subqueries & CTEs

### Q1: Find customers who have never placed an order
```sql
SELECT * FROM customers WHERE id NOT IN (SELECT DISTINCT customer_id FROM orders);
```

### Q2: Find the top 3 highest-spending customers using CTE
```sql
WITH customer_spending AS (
    SELECT c.id, c.name, SUM(o.total) as total_spent
    FROM customers c JOIN orders o ON c.id = o.customer_id
    GROUP BY c.id, c.name
)
SELECT * FROM customer_spending ORDER BY total_spent DESC LIMIT 3;
```

### Q2: Find employees who work on all projects
```sql
-- Using division pattern
SELECT e.name FROM employee e 
WHERE NOT EXISTS (
    SELECT p.id FROM project p 
    WHERE NOT EXISTS (
        SELECT * FROM assignment a 
        WHERE a.employee_id = e.id AND a.project_id = p.id
    )
);
```

---

## 📝 Practice Set 4: Window Functions

### Q1: Rank employees by salary within each department
```sql
SELECT name, department_id, salary,
       RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as dept_rank
FROM employees;
```

### Q2: Find the most recent activity per user
```sql
SELECT user_id, activity_type, activity_date,
       ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY activity_date DESC) as rn
FROM user_activities
WHERE rn = 1;
```

### Q3: Find the difference in days between consecutive orders per customer
```sql
SELECT customer_id, order_date,
       DATEDIFF(day, LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date), order_date) as days_since_last_order
FROM customer_orders;
```

---

## 📝 Practice Set 5: Advanced / Edge Cases

### Q1: Find duplicate emails in a table
```sql
SELECT email, COUNT(*) as cnt FROM person GROUP BY email HAVING COUNT(*) > 1;
```

### Q2: Find employees who have been with the company for 5+ years
```sql
SELECT name, hire_date FROM employee WHERE hire_date <= DATEADD(year, -5, GETDATE());
```

### Q2: Find the Nth highest salary (generic, works in MySQL/Postgres/SQL Server)
```sql
-- MySQL
SELECT DISTINCT salary FROM employee ORDER BY salary DESC LIMIT 1 OFFSET N-1;

-- Postgres
SELECT DISTINCT salary FROM employee ORDER BY salary DESC OFFSET N-1 LIMIT 1;

-- SQL Server
SELECT DISTINCT TOP 1 salary FROM (SELECT DISTINCT TOP N salary FROM employee ORDER BY salary DESC) AS sub ORDER BY salary ASC;
```

---

## ✅ Answer Key & Explanations

### Set 1: Joins
- **Q1:** Standard subquery pattern. Alternative: `DISTINCT ON salary` (Postgres) or window function.
- **Q2:** Self-join on manager_id. Uses alias `e` for employee, `m` for manager.
- **Q3:** GROUP BY + HAVING with COUNT.

### Set 2: GROUP BY & Aggregations
- **Q1:** LEFT JOIN ensures customers with 0 orders still appear. COUNT(o.id) counts orders only.
- **Q2:** MAX per group. LEFT JOIN ensures all customers appear even without orders.
- **Q3:** Window function `SUM() OVER (...)` computes running total.

### Set 3: Subqueries & CTEs
- **Q1:** `NOT IN` with subquery. Alternative: `NOT EXISTS` (handles NULLs better).
- **Q2:** CTE computes per-customer totals, then outer query sorts and limits.
- **Q3:** Division pattern — find employees where there's NO project they haven't been assigned to.

### Set 4: Window Functions
- **Q1:** `RANK()` gives same rank to ties, then skips ranks after ties.
- **Q2:** `ROW_NUMBER()` assigns unique ranks; `WHERE rn = 1` keeps only the most recent.
- **Q3:** `LAG()` gets the previous row's value; `DATEDIFF` computes the difference.

### Set 5: Advanced / Edge Cases
- **Q1:** GROUP BY + HAVING COUNT > 1 finds duplicates.
- **Q2:** DATEADD/HAVING compares hire date to 5 years ago.
- **Q3:** Generic Nth highest using LIMIT/OFFSET pattern across DB dialects.

---

## 🔧 Common SQL Optimization Tips

| Tip | Why |
|---|---|
| **Use indexes on JOIN columns** | Avoids full table scans |
| **Avoid SELECT \*** | Reduces data transfer, better index coverage |
| **Use EXISTS over IN for large subqueries** | EXISTS stops at first match; IN evaluates full list |
| **Use window functions over self-joins** | More readable, often more efficient |
| **Index columns used in WHERE, JOIN, ORDER BY, GROUP BY** | Supports predicate pushdown and sorting |
| **Avoid functions on indexed columns in WHERE** | `WHERE YEAR(date) = 2024` won't use index on `date` |

---

## Related

- [Java Developer Index](../00%20-%20Index.md)
- [Java Core Index](../Java%20Core/00%20-%20Index.md)
- [Hibernate Index](../Hibernate/00%20-%20Index.md)