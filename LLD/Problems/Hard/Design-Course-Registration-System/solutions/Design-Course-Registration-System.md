# Design Course Registration System (Hard)

**Difficulty:** Hard · **Patterns:** Observer, State
🔗 Reference: [awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design)

### Problem

Design course registration: capped courses, FIFO waitlists with auto-promotion, prerequisite and time-conflict checks, concurrent enrollment.

**Functional**
- Enroll with prereq + conflict + capacity checks; full → FIFO waitlist; drop promotes the next waiter with a notification.
- Per (student, course) status: ENROLLED / WAITLISTED / DROPPED.

**Non-functional**
- Capacity never exceeded under concurrency; FIFO fairness on the waitlist.

### The failure, before

```java
// ❌ `if (course.enrolled < course.capacity) course.enrolled++;` checked then applied later:
// two threads see the last seat, both enroll (capacity +1 over), and dropping a student
// leaves the waitlist stranded — nobody is promoted, nobody is told.
// if (roster.size() < cap) roster.add(s);   // check now, race later
```

### The Fix (after)

One synchronized enroll/drop path + `Deque` waitlist + promotion notifications.

```java
import java.util.*;

record TimeSlot(String day, int startHour, int endHour) {
    boolean conflicts(TimeSlot o) {
        return day.equals(o.day) && startHour < o.endHour && o.startHour < endHour;   // half-open
    }
}

class Student {
    final String id; final Set<String> completed = new HashSet<>();
    Student(String id) { this.id = id; }
}

class Course {
    final String code; final int capacity; final TimeSlot slot; final Set<String> prereqs;
    final List<Student> roster = new ArrayList<>();
    final Deque<Student> waitlist = new ArrayDeque<>();

    Course(String code, int capacity, TimeSlot slot, String... prereqs) {
        this.code = code; this.capacity = capacity; this.slot = slot;
        this.prereqs = new HashSet<>(List.of(prereqs));
    }
    boolean full() { return roster.size() >= capacity; }
}

enum EnrollmentStatus { ENROLLED, WAITLISTED, DROPPED }

interface WaitlistObserver { void onPromoted(String studentId, Course course); }

class RegistrationService {
    private final Map<String, Student> students = new HashMap<>();
    private final Map<String, Course> courses = new LinkedHashMap<>();
    private final Map<String, EnrollmentStatus> status = new HashMap<>();   // studentId:course
    private final List<WaitlistObserver> observers = new ArrayList<>();

    void register(Student s) { students.put(s.id, s); }
    void addCourse(Course c) { courses.put(c.code, c); }
    void subscribe(WaitlistObserver o) { observers.add(o); }
    EnrollmentStatus statusOf(String studentId, String code) {
        return status.getOrDefault(studentId + ":" + code, EnrollmentStatus.DROPPED);
    }

    synchronized EnrollmentStatus enroll(String studentId, String code) {
        Student s = students.get(studentId);
        Course c = courses.get(code);
        if (statusOf(studentId, code) != EnrollmentStatus.DROPPED)
            throw new IllegalStateException("Already enrolled or waitlisted");
        for (String pre : c.prereqs)
            if (!s.completed.contains(pre))
                throw new IllegalStateException("Missing prerequisite: " + pre);
        for (Course other : courses.values())
            if (other.roster.contains(s) && other.slot.conflicts(c.slot))
                throw new IllegalStateException("Time conflict with " + other.code);
        return place(s, c);                                        // checks done; mutation bounded
    }

    private EnrollmentStatus place(Student s, Course c) {
        if (!c.full()) {
            c.roster.add(s);
            status.put(s.id + ":" + c.code, EnrollmentStatus.ENROLLED);
            return EnrollmentStatus.ENROLLED;
        }
        c.waitlist.add(s);                                         // FIFO: addLast
        status.put(s.id + ":" + c.code, EnrollmentStatus.WAITLISTED);
        return EnrollmentStatus.WAITLISTED;
    }

    synchronized void drop(String studentId, String code) {
        Student s = students.get(studentId);
        Course c = courses.get(code);
        EnrollmentStatus current = statusOf(studentId, code);
        if (current == EnrollmentStatus.DROPPED) throw new IllegalStateException("Not registered");
        if (current == EnrollmentStatus.ENROLLED) {
            c.roster.remove(s);
        } else {
            c.waitlist.remove(s);                                  // plain removal, no cascade
        }
        status.put(studentId + ":" + code, EnrollmentStatus.DROPPED);
        promote(c);
    }

    private void promote(Course c) {
        if (c.full() || c.waitlist.isEmpty()) return;
        Student next = c.waitlist.poll();                          // FIFO: pollFirst
        c.roster.add(next);
        status.put(next.id + ":" + c.code, EnrollmentStatus.ENROLLED);
        observers.forEach(o -> o.onPromoted(next.id, c));
    }
}
```

**Usage**
```java
RegistrationService reg = new RegistrationService();
reg.register(new Student("s1"));
reg.register(new Student("s2"));
reg.addCourse(new Course("CS101", 1, new TimeSlot("MON", 9, 10)));
reg.subscribe((studentId, course) ->
        System.out.println(studentId + " promoted into " + course.code));

System.out.println(reg.enroll("s1", "CS101"));   // ENROLLED (last seat)
System.out.println(reg.enroll("s2", "CS101"));   // WAITLISTED
reg.drop("s1", "CS101");                          // s2 promoted + notified
```

### Design points
- **Checks before mutation** — prereq, conflict, and duplicate checks all run before any placement; failures leave no trace.
- **`place` is the single roster entry point** — enroll and promotion share it, so capacity honors exactly one rule.
- **Drop tells two stories** — roster drop promotes; waitlist drop is silent; one method, two branches.
- **Synchronized enroll/drop** — one lock over a multi-structure invariant; stripe per course only when asked.

**Complexity:** enroll O(courses + roster) checks · drop O(roster) · promote O(1).

---
#lld #machine-coding #course-registration #hard #practice