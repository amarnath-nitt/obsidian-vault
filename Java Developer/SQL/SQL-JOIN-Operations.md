# SQL - JOIN Operations

Master all JOIN types with examples and when to use each one.

---

## 📌 JOIN Types Overview

| JOIN Type | Returns | Use Case |
|-----------|---------|----------|
| **INNER JOIN** | Matching rows from both tables | Rows that exist in both tables |
| **LEFT JOIN** | All from left + matching from right | All users with their orders (or NULL) |
| **RIGHT JOIN** | Matching from left + all from right | All orders with their users (or NULL) |
| **FULL JOIN** | All rows from both tables | All users and orders combined |
| **CROSS JOIN** | Cartesian product | All combinations |

---

## 🔗 INNER JOIN

Returns **rows that exist in BOTH tables**.

**Syntax:**
```sql
SELECT columns
FROM table1
INNER JOIN table2 ON table1.id = table2.table1_id;
```

**Example:**
```sql
SELECT u.username, o.order_id, o.amount
FROM users u
INNER JOIN orders o ON u.user_id = o.user_id;
```

**Result:** Only users who placed orders

| username | order_id | amount |
|----------|----------|--------|
| Alice    | 101      | 50.00  |
| Bob      | 102      | 75.00  |

---

## 🔄 LEFT JOIN (LEFT OUTER JOIN)

Returns **ALL rows from LEFT table + matching rows from RIGHT table** (NULL if no match).

**Syntax:**
```sql
SELECT columns
FROM table1
LEFT JOIN table2 ON table1.id = table2.table1_id;
```

**Example:**
```sql
SELECT u.username, o.order_id, o.amount
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id;
```

**Result:** All users, with orders if they have any

| username | order_id | amount |
|----------|----------|--------|
| Alice    | 101      | 50.00  |
| Bob      | 102      | 75.00  |
| Charlie  | NULL     | NULL   |

---

## ➡️ RIGHT JOIN (RIGHT OUTER JOIN)

Returns **matching rows from LEFT table + ALL rows from RIGHT table** (NULL if no match).

**Syntax:**
```sql
SELECT columns
FROM table1
RIGHT JOIN table2 ON table1.id = table2.table1_id;
```

**Example:**
```sql
SELECT u.username, o.order_id, o.amount
FROM users u
RIGHT JOIN orders o ON u.user_id = o.user_id;
```

**Result:** All orders, with users if they exist

| username | order_id | amount |
|----------|----------|--------|
| Alice    | 101      | 50.00  |
| Bob      | 102      | 75.00  |
| NULL     | 103      | 120.00 |

---

## ⬌ FULL OUTER JOIN

Returns **ALL rows from BOTH tables** (NULL where no match).

**Syntax:**
```sql
SELECT columns
FROM table1
FULL OUTER JOIN table2 ON table1.id = table2.table1_id;
```

**Note:** NOT supported in MySQL. Use UNION of LEFT and RIGHT JOINs.

**Example (SQL Server, PostgreSQL):**
```sql
SELECT u.username, o.order_id, o.amount
FROM users u
FULL OUTER JOIN orders o ON u.user_id = o.user_id;
```

**MySQL Alternative:**
```sql
SELECT u.username, o.order_id, o.amount
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
UNION
SELECT u.username, o.order_id, o.amount
FROM users u
RIGHT JOIN orders o ON u.user_id = o.user_id;
```

**Result:** All users and all orders

| username | order_id | amount |
|----------|----------|--------|
| Alice    | 101      | 50.00  |
| Bob      | 102      | 75.00  |
| Charlie  | NULL     | NULL   |
| NULL     | 103      | 120.00 |

---

## ❌ CROSS JOIN

Returns **Cartesian product** (every row from table1 with every row from table2).

**Syntax:**
```sql
SELECT columns
FROM table1
CROSS JOIN table2;
-- or
SELECT columns
FROM table1, table2;
```

**Example:**
```sql
SELECT u.username, c.category
FROM users u
CROSS JOIN categories c;
```

**Result:** 3 users × 5 categories = 15 rows

---

## 🎯 Multiple JOINs

**Example: Users, Orders, Products**

```sql
SELECT 
    u.username,
    o.order_id,
    p.product_name,
    p.price
FROM users u
INNER JOIN orders o ON u.user_id = o.user_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON oi.product_id = p.product_id
WHERE o.order_date > '2024-01-01';
```

---

## 🔑 Handling NULL Values

When joining and getting NULLs:

```sql
SELECT 
    COALESCE(u.username, 'Unknown') AS username,
    o.order_id,
    COALESCE(o.amount, 0) AS amount
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id;
```

---

## ⚡ Performance Tips

1. **Index join columns** — Create indexes on foreign keys
2. **INNER JOIN is faster than LEFT JOIN** if you don't need unmatched rows
3. **Limit rows early** — Use WHERE clause before JOIN
4. **Avoid FULL OUTER JOIN if possible** — Use UNION of LEFT + RIGHT

```sql
-- ❌ Slow: Full table join then filter
SELECT u.*, o.*
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
WHERE u.status = 'active';

-- ✅ Fast: Filter first
SELECT u.*, o.*
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
WHERE u.status = 'active';
```

---

## ⚠️ Common Interview Questions

1. **What's the difference between INNER and LEFT JOIN?**
   - INNER: Only matching rows
   - LEFT: All left + matching right

2. **Which JOIN is fastest?**
   - INNER JOIN (no NULL handling needed)

3. **When would you use FULL OUTER JOIN?**
   - When you need all rows from both tables
   - Not available in MySQL

4. **How do you handle NULLs from LEFT JOIN?**
   - Use COALESCE() or IFNULL()

---

## Related

- [SQL Index](Java%20Developer/SQL/00%20-%20Index.md)
- [SQL Window Functions](SQL-Window-Functions.md)
- [Java Developer Index](../00%20-%20Index.md)
