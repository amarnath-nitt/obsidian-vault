# Design a Turn-Based Game Lobby

**Source:** AlgoMaster · Low-Level Design Practice · **hard (premium)** · **Pattern:** Mediator
🔗 [AlgoMaster index](https://algomaster.io/practice/low-level-design)

### Problem

In a turn-based game lobby, several players must be coordinated: joining, readying up, taking turns,
and starting the match only when everyone is ready. If players coordinated directly the logic would be
scattered. Centralise it in a **lobby mediator** that players talk to.

### Approach — Mediator

- **Mediator** = `GameLobby` — tracks players, readiness, and whose turn it is.
- **Colleague** = `Player` — reports ready / plays a turn through the mediator.
- The mediator owns all coordination rules (start conditions, turn order).

### Java Solution

```java
import java.util.*;

interface LobbyMediator {
    void join(Player player);
    void setReady(Player player);
    void playTurn(Player player, String move);
}

abstract class Player {
    protected final LobbyMediator lobby;
    protected final String name;
    protected Player(LobbyMediator lobby, String name) { this.lobby = lobby; this.name = name; }

    void join()                       { lobby.join(this); }
    void ready()                      { lobby.setReady(this); }
    void move(String action)          { lobby.playTurn(this, action); }
    abstract void notify(String event);
    String name() { return name; }
}

class HumanPlayer extends Player {
    HumanPlayer(LobbyMediator lobby, String name) { super(lobby, name); }
    @Override void notify(String event) { System.out.println("  " + name + " notified: " + event); }
}

class GameLobby implements LobbyMediator {                  // Mediator
    private final List<Player> players = new ArrayList<>();
    private final Set<Player> ready = new HashSet<>();
    private boolean started = false;
    private int turn = 0;
    private final int requiredPlayers;

    GameLobby(int requiredPlayers) { this.requiredPlayers = requiredPlayers; }

    public void join(Player player) {
        players.add(player);
        broadcast(player.name() + " joined (" + players.size() + "/" + requiredPlayers + ")");
    }

    public void setReady(Player player) {
        ready.add(player);
        broadcast(player.name() + " is ready (" + ready.size() + "/" + requiredPlayers + ")");
        if (players.size() == requiredPlayers && ready.size() == requiredPlayers) {
            started = true;
            broadcast("All ready — match starting!");
        }
    }

    public void playTurn(Player player, String move) {
        if (!started) { player.notify("Cannot move: match not started"); return; }
        if (players.get(turn % players.size()) != player) {
            player.notify("Not your turn"); return;
        }
        broadcast(player.name() + " played: " + move);
        turn++;
        broadcast("Next turn: " + players.get(turn % players.size()).name());
    }

    private void broadcast(String event) { players.forEach(p -> p.notify(event)); }
}
```

**Usage**
```java
GameLobby lobby = new GameLobby(2);
Player p1 = new HumanPlayer(lobby, "Ana");
Player p2 = new HumanPlayer(lobby, "Ben");

p1.join(); p2.join();
p1.move("attack");     // not started yet
p1.ready(); p2.ready();// lobby starts the match
p1.move("attack");     // valid turn
p2.move("defend");     // next turn
```

### Design points
- **Centralised coordination** — start conditions and turn order live only in the lobby.
- **Players are peers that never reference each other** — they only call the mediator.
- **Broadcast helpers** — the lobby notifies all players of state changes.

**Complexity:** O(players) per broadcast · Space O(players)

---
#mediator #games #lld #practice