# Start a Computer

**Source:** AlgoMaster · Low-Level Design Practice · **medium** · **Pattern:** Facade
🔗 [AlgoMaster problem](https://algomaster.io/practice/low-level-design/start-computer)

### Problem

Booting a computer involves a fixed low-level sequence: freeze the CPU, load the boot sector from the
hard drive into memory, jump the CPU to the boot address, and execute. Expose a **facade**
`ComputerFacade.start()` so callers don't orchestrate CPU/memory/disk directly.

### Approach — Facade

- `Cpu`, `Memory`, `HardDrive` are the subsystem classes.
- `ComputerFacade` holds them and exposes a single `start()` that runs the boot sequence.

### Java Solution

```java
class Cpu {
    void freeze()          { System.out.println("CPU freeze"); }
    void jump(long address){ System.out.println("CPU jump to " + address); }
    void execute()         { System.out.println("CPU execute"); }
}
class Memory {
    void load(long address, byte[] data) {
        System.out.println("Memory load " + data.length + " bytes @ " + address);
    }
}
class HardDrive {
    byte[] read(long lba, int size) {
        System.out.println("HardDrive read sector " + lba);
        return new byte[size];
    }
}

class ComputerFacade {
    private static final long BOOT_ADDRESS = 0L;
    private static final int  BOOT_SECTOR  = 512;
    private static final int  SECTOR_SIZE  = 512;

    private final Cpu cpu = new Cpu();
    private final Memory memory = new Memory();
    private final HardDrive hardDrive = new HardDrive();

    void start() {
        cpu.freeze();                                                 // 1
        memory.load(BOOT_ADDRESS, hardDrive.read(BOOT_SECTOR, SECTOR_SIZE));  // 2
        cpu.jump(BOOT_ADDRESS);                                       // 3
        cpu.execute();                                                // 4
    }
}
```

**Usage**
```java
new ComputerFacade().start();
```

### Design points
- **Encapsulated sequence** — the caller invokes one method, not four device calls.
- **Constants hidden** — boot address/sector live inside the facade.
- **Thin facade** — it orders calls; the devices do the work.

**Complexity:** O(1) · Space O(1)

---
#facade #lld #practice