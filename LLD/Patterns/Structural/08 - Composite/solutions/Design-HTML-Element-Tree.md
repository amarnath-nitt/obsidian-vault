# Design an HTML Element Tree

**Source:** AlgoMaster · Low-Level Design Practice · **hard (premium)** · **Pattern:** Composite
🔗 [AlgoMaster index](https://algomaster.io/practice/low-level-design)

### Problem

Model a DOM-like **HTML element tree**: a text node has no children; an element node has attributes
and children. Support rendering the subtree to HTML, counting nodes, and querying by tag — treating
leaf text and whole element subtrees **uniformly**.

### Approach — Composite

- **Component** = `HtmlNode` (`render`, `nodeCount`).
- **Leaves** = `TextNode`.
- **Composite** = `ElementNode` (tag, attributes, children).

### Java Solution

```java
import java.util.*;

interface HtmlNode {
    String render();
    int nodeCount();
}

// Leaf
class TextNode implements HtmlNode {
    private final String text;
    TextNode(String text) { this.text = text; }
    public String render()   { return escape(text); }
    public int nodeCount()   { return 1; }
    private static String escape(String s) { return s.replace("&", "&amp;").replace("<", "&lt;"); }
}

// Composite
class ElementNode implements HtmlNode {
    private final String tag;
    private final Map<String, String> attributes = new LinkedHashMap<>();
    private final List<HtmlNode> children = new ArrayList<>();

    ElementNode(String tag) { this.tag = tag; }

    ElementNode attr(String key, String value) { attributes.put(key, value); return this; }
    ElementNode add(HtmlNode child)            { children.add(child); return this; }

    public String render() {
        StringBuilder attrs = new StringBuilder();
        attributes.forEach((k, v) -> attrs.append(" ").append(k).append("=\"").append(v).append("\""));

        StringBuilder body = new StringBuilder();
        for (HtmlNode c : children) body.append(c.render());     // recursion

        return "<" + tag + attrs + ">" + body + "</" + tag + ">";
    }
    public int nodeCount() {
        int total = 1;                                            // self
        for (HtmlNode c : children) total += c.nodeCount();       // recursion
        return total;
    }
}
```

**Usage**
```java
ElementNode page = new ElementNode("div").attr("class", "page")
        .add(new ElementNode("h1").add(new TextNode("Hello")))
        .add(new ElementNode("p").add(new TextNode("World & co")));

System.out.println(page.render());
// <div class="page"><h1>Hello</h1><p>World &amp; co</p></div>
System.out.println("Nodes: " + page.nodeCount());   // 5
```

### Design points
- **Uniform render** — text and elements both implement `render()`.
- **Recursion handles nesting** — arbitrary depth works without special cases.
- **Leaf vs composite** — `nodeCount` is `1` for a text node, `1 + children` for an element.

**Complexity:** O(n) per render/count · Space O(depth)

---
#composite #html #lld #practice