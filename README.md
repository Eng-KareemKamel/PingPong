# PingPong by Python

# 🏓 Python Ping Pong Game (Turtle)

A simple **2-player Ping Pong game built with Python's Turtle graphics module**.
Two players control paddles and try to bounce the ball past their opponent to score points.

This project is a beginner friendly example of using **Python Turtle for game development**, including keyboard input, collision detection, and a basic game loop.

---

## 🎮 Features

* Two player local gameplay
* Real time paddle movement
* Ball physics and wall bouncing
* Paddle collision detection
* Live score tracking
* Simple and clean graphics using Turtle

---

## 🕹 Controls

| Player             | Key         | Action           |
| ------------------ | ----------- | ---------------- |
| Blue Player (Left) | **W**       | Move paddle up   |
| Blue Player (Left) | **S**       | Move paddle down |
| Red Player (Right) | **↑ Arrow** | Move paddle up   |
| Red Player (Right) | **↓ Arrow** | Move paddle down |

---

## 📦 Requirements

* Python 3.x
* `turtle` module (comes with standard Python installation)

No external libraries are required.

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/yourusername/ping-pong-turtle.git
```

2. Navigate to the project folder

```bash
cd ping-pong-turtle
```

3. Run the script

```bash
python pingpong.py
```

---

## 🧠 How It Works

The game uses:

* **Turtle objects** for paddles and the ball
* A **game loop** that constantly updates the screen
* **Keyboard bindings** to control paddle movement
* **Collision detection** for paddles and borders
* **Score tracking** displayed at the top of the screen

The ball direction is controlled using:

```python
ball.dx
ball.dy
```

These values determine the horizontal and vertical movement speed.

---

## 📁 Project Structure

```
ping-pong-turtle
│
├── pingpong.py
└── README.md
```

---

## 🚀 Possible Improvements

Some ideas if you want to extend the project:

* Add sound effects
* Add AI opponent
* Increase ball speed over time
* Add a winning score limit
* Add start and restart screens
* Improve paddle collision physics

---

## 📸 Screenshot

You can add a screenshot like this:

```
![Game Screenshot](screenshot.png)
```

---

## 📜 License

This project is open source and available under the **MIT License**.

---

If you want, I can also show you how to upgrade this project with:

* **AI paddle**
* **ball acceleration**
* **better collision physics**
* **start menu**

which makes it look much more like a real arcade Pong game.
