# Design Course Registry (Association)

**Source:** AlgoMaster · Low-Level Design Practice · **easy** · **Relationship:** Association
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/design-course-registry)

### Problem

Design a course registry where **students** enrol in **courses**. A student and a course are each
independently meaningful — neither owns the other. The registry links them and answers questions like
"which courses is this student taking?" and "who is enrolled in this course?".

### Approach — Association

- `Student` and `Course` are standalone classes.
- An `Enrollment` (or a registry map) **associates** the two.
- Both objects exist independently of the other.

### Java Solution

```java
import java.util.*;

public record Student(String id, String name) {}
public record Course(String code, String title) {}

public class CourseRegistry {

    private final Map<String, Course> courses = new LinkedHashMap<>();
    private final Map<Student, Set<Course>> enrollments = new LinkedHashMap<>();

    public void addCourse(Course course) { courses.put(course.code(), course); }

    /** Associates a student with a course (both already exist independently). */
    public void enroll(Student student, String courseCode) {
        Course course = courses.get(courseCode);
        if (course == null) throw new IllegalArgumentException("Unknown course: " + courseCode);
        enrollments.computeIfAbsent(student, k -> new LinkedHashSet<>()).add(course);
    }

    public Set<Course> coursesOf(Student student) {
        return enrollments.getOrDefault(student, Set.of());
    }

    public Set<Student> studentsIn(String courseCode) {
        Set<Student> result = new LinkedHashSet<>();
        enrollments.forEach((student, cs) -> {
            for (Course c : cs) if (c.code().equals(courseCode)) { result.add(student); break; }
        });
        return result;
    }
}
```

**Usage**
```java
CourseRegistry registry = new CourseRegistry();
registry.addCourse(new Course("CS101", "Intro to CS"));

Student alice = new Student("S1", "Alice");
Student bob   = new Student("S2", "Bob");
registry.enroll(alice, "CS101");
registry.enroll(bob, "CS101");

registry.coursesOf(alice).size();       // 1
registry.studentsIn("CS101").size();    // 2
```

### Why Association
- **Independent lifetimes** — deleting the registry does not delete students or courses.
- **No ownership** — a student can be in many courses; a course has many students (many-to-many).
- **The registry is a coordination point**, not an owner.

**Complexity:** O(1) enrol, O(enrollments) lookup · Space O(enrollments)

---
#oop #association #lld #practice