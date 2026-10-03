# Design a Document Visitor

**Source:** AlgoMaster · Low-Level Design Practice · **hard (premium)** · **Pattern:** Visitor
🔗 [AlgoMaster index](https://algomaster.io/practice/low-level-design)

### Problem

A document is composed of heterogeneous elements — **paragraphs**, **images**, **tables**. You need
to run many operations over a document: render to HTML, export to plain text, count words, or
compute statistics. The element classes are stable, but operations keep being added — a perfect fit
for **Visitor**.

### Approach — Visitor (double dispatch)

- **Element** = `DocElement` with `accept(visitor)` — `Paragraph`, `Image`, `Table`.
- **Visitor** = `DocVisitor<R>` with one `visit` per element type.
- Operations = concrete visitors (HTML render, word count, plain text).

### Java Solution

```java
interface DocVisitor<R> {
    R visit(Paragraph p);
    R visit(ImageElement i);
    R visit(Table t);
}

interface DocElement {
    <R> R accept(DocVisitor<R> visitor);
}

class Paragraph implements DocElement {
    final String text;
    Paragraph(String text) { this.text = text; }
    public <R> R accept(DocVisitor<R> v) { return v.visit(this); }
}
class ImageElement implements DocElement {
    final String src; final String alt;
    ImageElement(String src, String alt) { this.src = src; this.alt = alt; }
    public <R> R accept(DocVisitor<R> v) { return v.visit(this); }
}
class Table implements DocElement {
    final List<List<String>> rows;
    Table(List<List<String>> rows) { this.rows = rows; }
    public <R> R accept(DocVisitor<R> v) { return v.visit(this); }
}

// Operation 1 — render HTML
class HtmlRenderVisitor implements DocVisitor<String> {
    public String visit(Paragraph p)      { return "<p>" + p.text + "</p>"; }
    public String visit(ImageElement i)   { return "<img src=\"" + i.src + "\" alt=\"" + i.alt + "\">"; }
    public String visit(Table t) {
        StringBuilder sb = new StringBuilder("<table>");
        t.rows.forEach(row -> {
            sb.append("<tr>");
            row.forEach(cell -> sb.append("<td>").append(cell).append("</td>"));
            sb.append("</tr>");
        });
        return sb.append("</table>").toString();
    }
}

// Operation 2 — count words
class WordCountVisitor implements DocVisitor<Integer> {
    public Integer visit(Paragraph p)    { return p.text.isBlank() ? 0 : p.text.trim().split("\\s+").length; }
    public Integer visit(ImageElement i) { return 0; }
    public Integer visit(Table t) {
        int words = 0;
        for (List<String> row : t.rows) for (String cell : row) words += cell.isBlank() ? 0 : cell.trim().split("\\s+").length;
        return words;
    }
}

// Operation 3 — plain text
class PlainTextVisitor implements DocVisitor<String> {
    public String visit(Paragraph p)    { return p.text; }
    public String visit(ImageElement i) { return "[" + i.alt + "]"; }
    public String visit(Table t)        { return t.rows.toString(); }
}
```

**Usage**
```java
List<DocElement> doc = List.of(
        new Paragraph("Hello world"),
        new ImageElement("a.png", "diagram"),
        new Table(List.of(List.of("A", "B"), List.of("1", "2"))));

HtmlRenderVisitor html = new HtmlRenderVisitor();
WordCountVisitor words = new WordCountVisitor();

int total = 0;
for (DocElement e : doc) { System.out.println(e.accept(html)); total += e.accept(words); }
System.out.println("Words: " + total);
```

### Design points
- **New operation, no element changes** — add a `MarkdownVisitor` without touching `Paragraph` etc.
- **Double dispatch** — `accept` → `visitX(this)` selects behaviour by element **and** visitor.
- **Trade-off** — a new element type would require a new `visit` method on every visitor.

**Complexity:** O(n) over the document per operation · Space O(1) (O(output) for renders)

---
#visitor #lld #practice