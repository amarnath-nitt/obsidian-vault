# Implement a Secure Report Proxy

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** Proxy
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/implement-secure-report-proxy)

### Problem

A reporting service can generate sensitive reports. Only users with sufficient permission should be
able to fetch them, and every attempt should be audited. Enforce these rules in a **protection
proxy** that sits in front of the real reporting service, so the service itself stays focused on
report generation.

### Approach — Proxy

- **Subject** = `ReportService` (`getReport(name)`).
- **RealSubject** = `RealReportService`.
- **Proxy** = `ReportServiceProxy` — checks the caller's role and logs access before delegating.

### Java Solution

```java
interface ReportService {
    String getReport(String name);
}

class RealReportService implements ReportService {
    @Override public String getReport(String name) {
        return "REPORT[" + name + "]";                 // the real work
    }
}

class User {
    final String name; final String role;              // "ADMIN" or "VIEWER"
    User(String name, String role) { this.name = name; this.role = role; }
}

class ReportServiceProxy implements ReportService {

    private final ReportService real;                  // the real subject
    private final User user;

    ReportServiceProxy(ReportService real, User user) { this.real = real; this.user = user; }

    @Override
    public String getReport(String name) {
        if (!"ADMIN".equals(user.role)) {              // protection
            System.out.println("AUDIT: denied " + user.name + " -> " + name);
            throw new SecurityException("Access denied for role " + user.role);
        }
        System.out.println("AUDIT: granted " + user.name + " -> " + name);
        return real.getReport(name);                   // delegate
    }
}
```

**Usage**
```java
ReportService adminService  = new ReportServiceProxy(new RealReportService(), new User("ana", "ADMIN"));
ReportService viewerService = new ReportServiceProxy(new RealReportService(), new User("bob", "VIEWER"));

System.out.println(adminService.getReport("Q3"));   // allowed
viewerService.getReport("Q3");                      // throws SecurityException
```

### Design points
- **Access control centralised** — the rule lives in the proxy, not scattered across callers.
- **Auditing** — every request is logged, granted or denied.
- **Encapsulated subject** — the proxy is the only way in; the real service is unchanged.

**Complexity:** O(1) overhead · Space O(1)

---
#proxy #security #lld #practice