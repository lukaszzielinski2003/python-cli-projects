# 🛡️ CLI RPG Game

A simple **turn-based battle game** played in the command line.

---

## 🎮 Features

- Choose between 3 enemies: **Troll**, **Knight**, **Dragon**
- Turn-based combat: **Attack** or **Heal**
- Enemy fights back after your turn
- Health points reset after each battle

---

## 🛠️ How to Run

1. Clone the repo or download the files
2. Make sure you have **Python 3.10+** installed
3. Run the game:

```bash
python main.py
```

---

## 🕹️ How to Play

1. Choose your opponent by entering **1, 2, or 3**
2. In each turn, choose your action:
   - `1` to **Attack**
   - `2` to **Heal**
3. Battle until you or the enemy is defeated
4. After the battle, choose if you want to play again

---

## 🧪 Sample Gameplay

```
+---------------------------+
|     Welcome to CLI RPG    |
+---------------------------+
|     Available Enemies:    |
+---------------------------+
| 1. Troll (easy)           |
| 2. Knight (medium)        |
| 3. Dragon (hard)          |
+---------------------------+
| Press Ctrl + C to exit    |
+---------------------------+
Choose your opponent (1–3): 1

==================================================================
The battle has started between Zeril (HP: 100) and Troll (HP: 80)
==================================================================

1. Attack | 2. Heal
Choose your action: 1

===============================================
                  Turn: 1
-----------------------------------------------
Zeril hit for 20 damage
Troll now has 60 HP left
-----------------------------------------------
Troll hit for 25 damage
Zeril now has 75 HP left
===============================================

1. Attack | 2. Heal
Choose your action:
```

---

## 🧾 License

This project is licensed under the MIT License.  
See the [LICENSE](./LICENSE) file for details.
