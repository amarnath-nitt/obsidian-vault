# SQL Interview Questions

## SQL Basics

### 1. What is SQL? What are different types of SQL commands?

**Answer:**
SQL (Structured Query Language) is used to communicate with relational databases.

**SQL Command Types:**

**1. DDL (Data Definition Language):**
- Define database structure
- Commands: `CREATE`, `ALTER`, `DROP`, `TRUNCATE`

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

ALTER TABLE users ADD COLUMN age INT;

DROP TABLE users;

TRUNCATE TABLE users; -- Removes all rows, keeps structure
```

**2. DML (Data Manipulation Language):**
- Manipulate data
- Commands: `SELECT`, `INSERT`, `UPDATE`, `DELETE`

```sql
INSERT INTO users (id, name, email) VALUES (1, 'Alice', 'alice@example.com');

UPDATE users SET age = 25 WHERE id = 1;

DELETE FROM users WHERE id = 1;

SELECT * FROM users;
```

**3. DCL (Data Control Language):**
- Control access
- Commands: `GRANT`, `REVOKE`

```sql
GRANT SELECT ON users TO user1;
REVOKE SELECT ON users FROM user1;
```

**4. TCL (Transaction Control Language):**
- Manage transactions
- Commands: `COMMIT`, `ROLLBACK`, `SAVEPOINT`

```sql
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

BEGIN TRANSACTION;
DELETE FROM users WHERE id = 1;
ROLLBACK; -- Undo changes
```

---

## SELECT Queries

### 2. What is the difference between WHERE and HAVING?

**Answer:**
- **WHERE**: Filters rows **before** grouping
- **HAVING**: Filters groups **after** grouping

```sql
-- WHERE - filters individual rows
SELECT department, AVG(salary) as avg_salary
FROM employees
WHERE salary > 50000  -- Filter before grouping
GROUP BY department;

-- HAVING - filters groups
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;  -- Filter after grouping

-- Both together
SELECT department, AVG(salary) as avg_salary
FROM employees
WHERE salary > 40000          -- Filter rows first
GROUP BY department
HAVING AVG(salary) > 60000;   -- Then filter groups
```

### 3. What is the difference between DISTINCT and GROUP BY?

**Answer:**
- **DISTINCT**: Removes duplicate rows from result
- **GROUP BY**: Groups rows for aggregate functions

```sql
-- DISTINCT - unique values
SELECT DISTINCT department FROM employees;

-- GROUP BY - aggregation
SELECT department, COUNT(*) as count
FROM employees
GROUP BY department;

-- DISTINCT with multiple columns
SELECT DISTINCT department, job_title FROM employees;

-- GROUP BY with multiple columns
SELECT department, job_title, COUNT(*)
FROM employees
GROUP BY department, job_title;
```

### 4. Explain ORDER BY with multiple columns.

**Answer:**
`ORDER BY` sorts results. Multiple columns create prioritized sorting.

```sql
-- Single column
SELECT * FROM employees ORDER BY salary DESC;

-- Multiple columns - sort by dept first, then salary
SELECT * FROM employees 
ORDER BY department ASC, salary DESC;

-- With expressions
SELECT name, salary * 12 as annual_salary
FROM employees
ORDER BY annual_salary DESC;

-- Using column position (not recommended)
SELECT name, salary FROM employees ORDER BY 2 DESC;

-- NULLS handling
SELECT * FROM employees ORDER BY manager_id NULLS FIRST;
```

---

## JOINs

### 5. Explain different types of JOINs with examples.

**Answer:**

**Tables:**
```sql
-- employees table
id | name    | dept_id
1  | Alice   | 10
2  | Bob     | 20
3  | Charlie | NULL

-- departments table
id | dept_name
10 | Sales
20 | IT
30 | HR
```

**INNER JOIN - Only matching rows:**
```sql
SELECT e.name, d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.id;

-- Result:
name    | dept_name
Alice   | Sales
Bob     | IT
```

**LEFT JOIN (LEFT OUTER JOIN) - All from left, matching from right:**
```sql
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.id;

-- Result:
name    | dept_name
Alice   | Sales
Bob     | IT
Charlie | NULL
```

**RIGHT JOIN (RIGHT OUTER JOIN) - All from right, matching from left:**
```sql
SELECT e.name, d.dept_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.id;

-- Result:
name  | dept_name
Alice | Sales
Bob   | IT
NULL  | HR
```

**FULL OUTER JOIN - All from both tables:**
```sql
SELECT e.name, d.dept_name
FROM employees e
FULL OUTER JOIN departments d ON e.dept_id = d.id;

-- Result:
name    | dept_name
Alice   | Sales
Bob     | IT
Charlie | NULL
NULL    | HR
```

**CROSS JOIN - Cartesian product:**
```sql
SELECT e.name, d.dept_name
FROM employees e
CROSS JOIN departments d;

-- Result: 3 × 3 = 9 rows (every combination)
```

**SELF JOIN - Join table with itself:**
```sql
-- Find employees with same manager
SELECT e1.name as employee, e2.name as colleague
FROM employees e1
INNER JOIN employees e2 ON e1.manager_id = e2.manager_id
WHERE e1.id != e2.id;
```

### 6. What is the difference between INNER JOIN and WHERE for joining?

**Answer:**
Both can join tables, but `JOIN` is more explicit and readable.

```sql
-- Using INNER JOIN (preferred)
SELECT e.name, d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.id
WHERE e.salary > 50000;

-- Using WHERE (old style)
SELECT e.name, d.dept_name
FROM employees e, departments d
WHERE e.dept_id = d.id
AND e.salary > 50000;
```

**Why prefer JOIN:**
- Clearer separation of join condition and filter condition
- Easier to read and maintain
- Supports outer joins naturally

---

## Aggregate Functions

### 7. What are aggregate functions? Explain common ones.

**Answer:**
Aggregate functions perform calculations on multiple rows and return a single value.

```sql
-- COUNT - number of rows
SELECT COUNT(*) FROM employees;
SELECT COUNT(manager_id) FROM employees; -- Excludes NULLs
SELECT COUNT(DISTINCT department) FROM employees;

-- SUM - total of values
SELECT SUM(salary) FROM employees;
SELECT department, SUM(salary) as total_salary
FROM employees
GROUP BY department;

-- AVG - average value
SELECT AVG(salary) FROM employees;
SELECT AVG(DISTINCT salary) FROM employees; -- Unique values only

-- MIN/MAX - minimum/maximum
SELECT MIN(salary), MAX(salary) FROM employees;

-- Multiple aggregates
SELECT 
    COUNT(*) as total_employees,
    AVG(salary) as avg_salary,
    MIN(salary) as min_salary,
    MAX(salary) as max_salary,
    SUM(salary) as total_payroll
FROM employees;
```

---

## Subqueries

### 8. What are subqueries? What are the types?

**Answer:**
A subquery is a query nested inside another query.

**Types:**

**1. Single-row subquery:**
```sql
-- Find employees earning more than average
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

**2. Multiple-row subquery:**
```sql
-- Find employees in IT or Sales departments
SELECT name
FROM employees
WHERE dept_id IN (
    SELECT id FROM departments 
    WHERE dept_name IN ('IT', 'Sales')
);

-- ANY/ALL operators
SELECT name, salary
FROM employees
WHERE salary > ANY (
    SELECT salary FROM employees WHERE department = 'Sales'
);

SELECT name, salary
FROM employees
WHERE salary > ALL (
    SELECT salary FROM employees WHERE department = 'Sales'
);
```

**3. Correlated subquery:**
```sql
-- Find employees earning more than avg in their department
SELECT e1.name, e1.salary, e1.department
FROM employees e1
WHERE salary > (
    SELECT AVG(salary)
    FROM employees e2
    WHERE e2.department = e1.department
);
```

**4. Subquery in FROM clause (derived table):**
```sql
SELECT dept, avg_salary
FROM (
    SELECT department as dept, AVG(salary) as avg_salary
    FROM employees
    GROUP BY department
) as dept_avg
WHERE avg_salary > 60000;
```

**5. EXISTS subquery:**
```sql
-- Find departments with employees
SELECT dept_name
FROM departments d
WHERE EXISTS (
    SELECT 1 FROM employees e 
    WHERE e.dept_id = d.id
);

-- NOT EXISTS
SELECT dept_name
FROM departments d
WHERE NOT EXISTS (
    SELECT 1 FROM employees e 
    WHERE e.dept_id = d.id
);
```

---

## Window Functions

### 9. What are Window Functions?

**Answer:**
Window functions perform calculations across a set of rows related to the current row, without grouping.

**ROW_NUMBER() - Sequential number:**
```sql
SELECT 
    name,
    department,
    salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as row_num
FROM employees;

-- Result:
name    | department | salary | row_num
Alice   | Sales      | 80000  | 1
Bob     | Sales      | 70000  | 2
Charlie | IT         | 90000  | 1
David   | IT         | 85000  | 2
```

**RANK() and DENSE_RANK():**
```sql
SELECT 
    name,
    salary,
    RANK() OVER (ORDER BY salary DESC) as rank,
    DENSE_RANK() OVER (ORDER BY salary DESC) as dense_rank
FROM employees;

-- RANK: 1, 2, 2, 4 (skips 3)
-- DENSE_RANK: 1, 2, 2, 3 (no skip)
```

**NTILE() - Divide into N groups:**
```sql
SELECT 
    name,
    salary,
    NTILE(4) OVER (ORDER BY salary) as quartile
FROM employees;
```

**LAG() and LEAD() - Access previous/next rows:**
```sql
SELECT 
    name,
    salary,
    LAG(salary, 1) OVER (ORDER BY hire_date) as prev_salary,
    LEAD(salary, 1) OVER (ORDER BY hire_date) as next_salary
FROM employees;
```

**Aggregate functions as Window functions:**
```sql
SELECT 
    name,
    salary,
    AVG(salary) OVER (PARTITION BY department) as dept_avg,
    SUM(salary) OVER (PARTITION BY department) as dept_total,
    salary - AVG(salary) OVER (PARTITION BY department) as diff_from_avg
FROM employees;
```

### 10. What is the difference between RANK(), DENSE_RANK(), and ROW_NUMBER()?

**Answer:**

```sql
SELECT 
    name,
    score,
    ROW_NUMBER() OVER (ORDER BY score DESC) as row_num,
    RANK() OVER (ORDER BY score DESC) as rank,
    DENSE_RANK() OVER (ORDER BY score DESC) as dense_rank
FROM students;

-- Results:
name  | score | row_num | rank | dense_rank
Alice | 95    | 1       | 1    | 1
Bob   | 90    | 2       | 2    | 2
Carol | 90    | 3       | 2    | 2
David | 85    | 4       | 4    | 3
```

- **ROW_NUMBER()**: Always unique, sequential
- **RANK()**: Same rank for ties, skips next ranks
- **DENSE_RANK()**: Same rank for ties, no skipping

---

## Common Table Expressions (CTEs)

### 11. What are CTEs? Why use them?

**Answer:**
CTEs (WITH clause) create temporary named result sets for better readability and recursion.

**Basic CTE:**
```sql
WITH dept_avg AS (
    SELECT department, AVG(salary) as avg_salary
    FROM employees
    GROUP BY department
)
SELECT e.name, e.salary, da.avg_salary
FROM employees e
JOIN dept_avg da ON e.department = da.department
WHERE e.salary > da.avg_salary;
```

**Multiple CTEs:**
```sql
WITH 
    high_earners AS (
        SELECT * FROM employees WHERE salary > 80000
    ),
    it_dept AS (
        SELECT * FROM employees WHERE department = 'IT'
    )
SELECT he.name
FROM high_earners he
INNER JOIN it_dept it ON he.id = it.id;
```

**Recursive CTE:**
```sql
-- Find all employees in hierarchy under manager
WITH RECURSIVE employee_hierarchy AS (
    -- Base case
    SELECT id, name, manager_id, 1 as level
    FROM employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    -- Recursive case
    SELECT e.id, e.name, e.manager_id, eh.level + 1
    FROM employees e
    INNER JOIN employee_hierarchy eh ON e.manager_id = eh.id
)
SELECT * FROM employee_hierarchy;
```

---

## Indexes and Performance

### 12. What is an Index? When to use it?

**Answer:**
An index is a data structure that improves query performance by allowing faster data retrieval.

**Creating indexes:**
```sql
-- Single column index
CREATE INDEX idx_employee_name ON employees(name);

-- Composite index
CREATE INDEX idx_dept_salary ON employees(department, salary);

-- Unique index
CREATE UNIQUE INDEX idx_email ON employees(email);

-- Dropping index
DROP INDEX idx_employee_name;
```

**When to use indexes:**
✅ Columns frequently used in WHERE clauses
✅ Columns used in JOIN conditions
✅ Columns used in ORDER BY
✅ Foreign key columns
✅ Columns with high cardinality (many unique values)

**When NOT to use indexes:**
❌ Small tables
❌ Columns with low cardinality (few unique values)
❌ Tables with frequent INSERTs/UPDATEs (maintenance overhead)
❌ Columns rarely used in queries

### 13. What is the difference between Clustered and Non-Clustered Index?

**Answer:**

| Feature | Clustered Index | Non-Clustered Index |
|---------|----------------|---------------------|
| Storage | Physically reorders table data | Separate structure with pointers |
| Count per Table | Only 1 | Multiple allowed |
| Speed | Faster for range queries | Faster for specific lookups |
| Primary Key | Automatically created | Manually created |
| Space | Less additional space | More space for pointers |

```sql
-- Clustered (usually automatic on PRIMARY KEY)
CREATE TABLE employees (
    id INT PRIMARY KEY,  -- Clustered index
    name VARCHAR(100)
);

-- Non-Clustered
CREATE INDEX idx_name ON employees(name);
```

---

## Database Design

### 14. What is Normalization? Explain Normal Forms.

**Answer:**
Normalization organizes data to reduce redundancy and improve integrity.

**1NF (First Normal Form):**
- Atomic values (no repeating groups)
- Each column contains only one value

```sql
-- Not 1NF
id | name  | phones
1  | Alice | 123, 456

-- 1NF
id | name  | phone
1  | Alice | 123
1  | Alice | 456
```

**2NF (Second Normal Form):**
- Must be in 1NF
- No partial dependencies (all non-key columns depend on entire primary key)

```sql
-- Not 2NF (order_item depends on both order_id and product_id)
order_id | product_id | product_name | quantity
1        | 101        | Laptop       | 2

-- 2NF (split into two tables)
-- orders_products
order_id | product_id | quantity
1        | 101        | 2

-- products
product_id | product_name
101        | Laptop
```

**3NF (Third Normal Form):**
- Must be in 2NF
- No transitive dependencies (non-key columns depend only on primary key)

```sql
-- Not 3NF (city depends on zip_code, not directly on id)
id | name  | zip_code | city
1  | Alice | 12345    | NYC

-- 3NF
-- customers
id | name  | zip_code
1  | Alice | 12345

-- zipcodes
zip_code | city
12345    | NYC
```

### 15. What is Denormalization? When to use it?

**Answer:**
Denormalization intentionally adds redundancy to improve read performance.

**When to use:**
- Read-heavy applications
- Complex joins impacting performance
- Data warehouse/reporting systems

```sql
-- Normalized (requires JOIN)
SELECT o.id, c.name, p.product_name
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN products p ON o.product_id = p.id;

-- Denormalized (faster reads, data duplication)
SELECT id, customer_name, product_name
FROM orders;
```

---

## Transactions & ACID

### 16. What are ACID properties?

**Answer:**

**Atomicity**: All operations in a transaction succeed or all fail
```sql
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT; -- Both succeed or both rollback
```

**Consistency**: Transaction brings database from one valid state to another
- Enforces constraints, triggers, cascades

**Isolation**: Concurrent transactions don't interfere
```sql
-- Transaction 1
BEGIN TRANSACTION;
SELECT balance FROM accounts WHERE id = 1; -- 1000
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

-- Transaction 2 (isolated)
BEGIN TRANSACTION;
SELECT balance FROM accounts WHERE id = 1; -- Still sees 1000 until T1 commits
COMMIT;
```

**Durability**: Committed data is permanently saved
- Even after system failure

---

## Practical Problems

### 17. Find Nth highest salary

**Answer:**

**Method 1: Using LIMIT/OFFSET:**
```sql
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 2; -- 3rd highest (N-1)
```

**Method 2: Using Subquery:**
```sql
SELECT MAX(salary)
FROM employees
WHERE salary < (
    SELECT MAX(salary) FROM employees
); -- 2nd highest
```

**Method 3: Using DENSE_RANK:**
```sql
WITH ranked_salaries AS (
    SELECT 
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) as rank
    FROM employees
)
SELECT salary
FROM ranked_salaries
WHERE rank = 3; -- Nth highest
```

### 18. Find duplicate rows

**Answer:**

```sql
-- Find duplicate emails
SELECT email, COUNT(*) as count
FROM users
GROUP BY email
HAVING COUNT(*) > 1;

-- Get all duplicate rows
SELECT *
FROM users
WHERE email IN (
    SELECT email
    FROM users
    GROUP BY email
    HAVING COUNT(*) > 1
);

-- Using window function
SELECT *
FROM (
    SELECT 
        *,
        ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) as row_num
    FROM users
) as numbered
WHERE row_num > 1;
```

### 19. Delete duplicate rows, keep one

**Answer:**

```sql
-- Using ROW_NUMBER (keep lowest id)
DELETE FROM users
WHERE id NOT IN (
    SELECT MIN(id)
    FROM users
    GROUP BY email
);

-- Using window function
DELETE FROM users
WHERE id IN (
    SELECT id
    FROM (
        SELECT 
            id,
            ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) as row_num
        FROM users
    ) as numbered
    WHERE row_num > 1
);
```

### 20. Find employees earning more than their manager

**Answer:**

```sql
SELECT e1.name as employee, e1.salary, e2.name as manager, e2.salary as manager_salary
FROM employees e1
INNER JOIN employees e2 ON e1.manager_id = e2.id
WHERE e1.salary > e2.salary;
```

### 21. Find department with highest average salary

**Answer:**

```sql
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC
LIMIT 1;

-- Or using subquery
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) = (
    SELECT MAX(avg_salary)
    FROM (
        SELECT AVG(salary) as avg_salary
        FROM employees
        GROUP BY department
    ) as dept_avgs
);
```

### 22. Running total/cumulative sum

**Answer:**

```sql
SELECT 
    date,
    amount,
    SUM(amount) OVER (ORDER BY date) as running_total
FROM sales
ORDER BY date;

-- By category
SELECT 
    date,
    category,
    amount,
    SUM(amount) OVER (PARTITION BY category ORDER BY date) as running_total
FROM sales
ORDER BY category, date;
```
