# Calling Stored Procedures in Java

**Concept tested**: Spring Data JPA `@Procedure` vs `EntityManager`.

## Scenario
Fetch a list of employees using a stored procedure named `GET_EMPLOYEE_LIST`.

## 1. Using Spring Data JPA (@Procedure)
```java
@Repository
public interface EmployeeRepository extends JpaRepository<Employee, Long> {
    
    @Procedure(name = "GET_EMPLOYEE_LIST")
    List<Employee> getEmployeeList();
}
```
*Note: The entity must be mapped with `@NamedStoredProcedureQuery`.*

## 2. Using EntityManager (More Flexible)
```java
@Service
public class EmployeeService {

    @PersistenceContext
    private EntityManager entityManager;

    public List<Employee> fetchEmployees() {
        StoredProcedureQuery query = entityManager
            .createStoredProcedureQuery("GET_EMPLOYEE_LIST", Employee.class);
        
        return query.getResultList();
    }
}
```

## 3. SQL Side (MySQL Example)
```sql
DELIMITER //
CREATE PROCEDURE GET_EMPLOYEE_LIST()
BEGIN
    SELECT * FROM employees;
END //
DELIMITER ;
```

## Interview Explanation
In modern Spring Boot applications, we use the `@Procedure` annotation for simple calls. For more complex procedures involving multiple output parameters or dynamic cursor mapping, I prefer using `EntityManager.createStoredProcedureQuery()` as it provides finer control over the execution context.

## Key Takeaway
- `@Procedure` is declarative and cleaner.
- Ensure `ReadOnly = true` for procedures that only fetch data to optimize transaction overhead.