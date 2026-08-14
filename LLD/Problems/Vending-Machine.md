# 📠 LLD Problem: Design a Vending Machine

#### Problem Statement
Design a simple vending machine that sells a few items (e.g., Coke, Pepsi, Soda) and accepts coins (e.g., Quarter, Dime, Nickel, Penny). The machine should allow users to select an item, insert money, and dispense the item along with any change.

#### Core Requirements
- Select item.
- Insert coins.
- Dispense item.
- Return change.
- Handle insufficient funds.
- Handle out-of-stock items.
- Reset functionality.

#### High-Level Components
- **VendingMachine**: Orchestrates the process.
- **Inventory**: Manages items and their stock.
- **CoinHandler**: Manages accepted coins and calculates change.
- **Item**: Represents a product.
- **Coin**: Represents a type of coin.

#### LLD - Class Diagram (Conceptual)

```mermaid
classDiagram
    class VendingMachine {
        -Inventory inventory
        -CoinHandler coinHandler
        -State currentState
        +selectItem(Item item)
        +insertCoin(Coin coin)
        +dispenseItemAndChange()
        +refundMoney()
        +reset()
        +setState(State state)
    }

    class Inventory {
        -Map<Item, Integer> itemStock
        -Map<Item, Double> itemPrices
        +addItem(Item item, int quantity, double price)
        +getItemPrice(Item item)
        +hasItem(Item item)
        +deductItem(Item item)
        +addStock(Item item, int quantity)
    }

    class CoinHandler {
        -Map<Coin, Integer> coinStock
        -double currentBalance
        +acceptCoin(Coin coin)
        +getChange(double amount)
        +refundBalance()
        +addCoinStock(Coin coin, int quantity)
        +deductCoinStock(Coin coin, int quantity)
        +getCurrentBalance()
    }

    class Item {
        -String name
        -double price
        +getName()
        +getPrice()
    }

    class Coin {
        -String name
        -double value
        +getValue()
        +getName()
    }

    VendingMachine "1" -- "1" Inventory : uses >
    VendingMachine "1" -- "1" CoinHandler : uses >
    Inventory "1" -- "*" Item : manages >
    CoinHandler "1" -- "*" Coin : manages >

    interface State {
        +selectItem(Item item)
        +insertCoin(Coin coin)
        +dispenseItemAndChange()
        +refundMoney()
    }

    class IdleState {
        +selectItem(Item item)
        +insertCoin(Coin coin)
        +dispenseItemAndChange()
        +refundMoney()
    }
    class HasSelectionState {
        +selectItem(Item item)
        +insertCoin(Coin coin)
        +dispenseItemAndChange()
        +refundMoney()
    }
    class HasMoneyState {
        +selectItem(Item item)
        +insertCoin(Coin coin)
        +dispenseItemAndChange()
        +refundMoney()
    }
    class DispenseState {
        +selectItem(Item item)
        +insertCoin(Coin coin)
        +dispenseItemAndChange()
        +refundMoney()
    }

    VendingMachine "1" *-- "1" State : has current >
    State <|.. IdleState
    State <|.. HasSelectionState
    State <|.. HasMoneyState
    State <|.. DispenseState
```

#### Key Design Decisions & Patterns
- **State Pattern**: The `VendingMachine` can be in different states (Idle, HasSelection, HasMoney, Dispense). Using the State pattern allows the machine's behavior to change based on its internal state, making the state transitions explicit and managing state-specific logic cleanly.
- **Singleton (Optional)**: `Inventory` and `CoinHandler` could potentially be Singletons if there's only one instance of each globally, but often they are injected into the `VendingMachine`.
- **Enums**: `Item` and `Coin` can be represented as Enums for fixed types, or classes if they need more complex attributes/behaviors. For simplicity, Enums are often a good start.
- **Dependency Injection**: The `VendingMachine` can receive `Inventory` and `CoinHandler` instances through its constructor, promoting loose coupling and testability.

#### Example Code Snippets (Illustrative)

```java
// Item Enum
public enum Item {
    COKE("Coke", 1.25),
    PEPSI("Pepsi", 1.50),
    SODA("Soda", 1.00);

    private String name;
    private double price;

    Item(String name, double price) {
        this.name = name;
        this.price = price;
    }

    public String getName() { return name; }
    public double getPrice() { return price; }
}

// Coin Enum
public enum Coin {
    QUARTER("Quarter", 0.25),
    DIME("Dime", 0.10),
    NICKEL("Nickel", 0.05),
    PENNY("Penny", 0.01);

    private String name;
    private double value;

    Coin(String name, double value) {
        this.name = name;
        this.value = value;
    }

    public double getValue() { return value; }
    public String getName() { return name; }
}

// Inventory Class
import java.util.HashMap;
import java.util.Map;

public class Inventory {
    private Map<Item, Integer> itemStock;

    public Inventory() {
        itemStock = new HashMap<>();
        // Initialize with some stock
        itemStock.put(Item.COKE, 5);
        itemStock.put(Item.PEPSI, 3);
        itemStock.put(Item.SODA, 10);
    }

    public int getQuantity(Item item) {
        return itemStock.getOrDefault(item, 0);
    }

    public void deductItem(Item item) {
        if (itemStock.containsKey(item) && itemStock.get(item) > 0) {
            itemStock.put(item, itemStock.get(item) - 1);
        } else {
            throw new IllegalArgumentException("Item " + item.getName() + " is out of stock.");
        }
    }

    public void addItem(Item item, int quantity) {
        itemStock.put(item, itemStock.getOrDefault(item, 0) + quantity);
    }

    public boolean hasItem(Item item) {
        return getQuantity(item) > 0;
    }
}

// CoinHandler Class
import java.util.HashMap;
import java.util.Map;

public class CoinHandler {
    private Map<Coin, Integer> coinStock;
    private double currentBalance;

    public CoinHandler() {
        coinStock = new HashMap<>();
        // Initialize with some coins for change
        coinStock.put(Coin.QUARTER, 10);
        coinStock.put(Coin.DIME, 10);
        coinStock.put(Coin.NICKEL, 10);
        currentBalance = 0.0;
    }

    public void acceptCoin(Coin coin) {
        currentBalance += coin.getValue();
        coinStock.put(coin, coinStock.getOrDefault(coin, 0) + 1);
    }

    public double getCurrentBalance() {
        return currentBalance;
    }

    public Map<Coin, Integer> getChange(double amount) {
        Map<Coin, Integer> change = new HashMap<>();
        double remainingChange = amount;

        // Prioritize larger denominations
        Coin[] denominations = {Coin.QUARTER, Coin.DIME, Coin.NICKEL, Coin.PENNY};
        for (Coin coin : denominations) {
            while (remainingChange >= coin.getValue() && coinStock.getOrDefault(coin, 0) > 0) {
                remainingChange -= coin.getValue();
                change.put(coin, change.getOrDefault(coin, 0) + 1);
                coinStock.put(coin, coinStock.get(coin) - 1);
                remainingChange = Math.round(remainingChange * 100.0) / 100.0; // Avoid floating point issues
            }
        }

        if (remainingChange > 0) {
            // If exact change cannot be given, revert coin stock and throw exception
            // (In a real system, this would be handled more gracefully, e.g., by not accepting the last coin)
            throw new RuntimeException("Cannot provide exact change.");
        }
        currentBalance = 0.0; // Reset balance after dispensing change
        return change;
    }

    public void refundBalance() {
        // Logic to return currentBalance in coins
        currentBalance = 0.0;
    }

    public void reset() {
        currentBalance = 0.0;
    }
}

// VendingMachine (Simplified, without State Pattern for brevity)
public class VendingMachine {
    private Inventory inventory;
    private CoinHandler coinHandler;
    private Item selectedItem;

    public VendingMachine(Inventory inventory, CoinHandler coinHandler) {
        this.inventory = inventory;
        this.coinHandler = coinHandler;
        this.selectedItem = null;
    }

    public void selectItem(Item item) {
        if (!inventory.hasItem(item)) {
            throw new IllegalArgumentException("Item " + item.getName() + " is out of stock.");
        }
        this.selectedItem = item;
        System.out.println("Selected: " + item.getName() + ". Price: $" + item.getPrice());
    }

    public void insertCoin(Coin coin) {
        if (selectedItem == null) {
            throw new IllegalStateException("Please select an item first.");
        }
        coinHandler.acceptCoin(coin);
        System.out.println("Current balance: $" + coinHandler.getCurrentBalance());
    }

    public void dispenseItemAndChange() {
        if (selectedItem == null) {
            throw new IllegalStateException("No item selected.");
        }
        double itemPrice = selectedItem.getPrice();
        double currentBalance = coinHandler.getCurrentBalance();

        if (currentBalance < itemPrice) {
            throw new IllegalStateException("Insufficient funds. Please insert $" + (itemPrice - currentBalance) + " more.");
        }

        inventory.deductItem(selectedItem);
        System.out.println("Dispensing " + selectedItem.getName());

        double changeAmount = currentBalance - itemPrice;
        if (changeAmount > 0) {
            Map<Coin, Integer> change = coinHandler.getChange(changeAmount);
            System.out.println("Dispensing change: " + change);
        }
        reset();
    }

    public void refundMoney() {
        System.out.println("Refunding: $" + coinHandler.getCurrentBalance());
        coinHandler.refundBalance();
        reset();
    }

    public void reset() {
        selectedItem = null;
        coinHandler.reset();
        System.out.println("Vending machine reset.");
    }
}
```

---
## 🔗 Related
- [[00 - Roadmap]]