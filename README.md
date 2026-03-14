# Wandering in the Woods

An interactive educational simulation game designed to introduce K–8 students to **computational thinking, randomness, and data analysis**.

In this simulation, explorers wander randomly inside a forest represented by a grid until they meet each other.

The project demonstrates how **computer simulations can help students understand algorithms, probability, and experimental analysis.**

---

## 🎮 Features

- **Three educational levels:**
  - **K–2** – Basic visualization
  - **Grades 3–5** – Custom grid and players
  - **Grades 6–8** – Experiment mode with graphs
- Interactive **grid-based simulation**
- **Click-to-place players** in experiment mode
- **Automatic graph generation** for experiments
- **Background music**
- **Pause / Resume controls**
- **Data recording** for simulations

## 📁 Project Structure

```
WanderingInTheWoods/
│
├── Wondering-in-the-woods.exe
├── Wondering-in-the-woods.py
├── Wondering-in-the-woods.spec
├── yakastreams-retro-gaming-271301.mp3
├── scores.txt
├── User manual.docx
├── Final Project Report Software Eng.pdf
└── README.md
```

| File | Description |
|------|-------------|
| Wondering-in-the-woods.exe | Main executable program |
| Wondering-in-the-woods.py | Source code of the simulation |
| Wondering-in-the-woods.spec | PyInstaller build configuration |
| yakastreams-retro-gaming-271301.mp3 | Background music used in the game |
| scores.txt | Stores simulation results |
| User manual.docx | Instructions for running and using the program |
| Final Project Report Software Eng.pdf | Detailed project report |
| README.md | Project documentation |

## ⚙️ System Requirements

### Hardware

- PC or laptop  
- Mouse and keyboard  
- 4 GB RAM recommended  

### Software

- Windows 10 / Windows 11  

No additional installations are required when using the `.exe` file.

---

## ▶️ How to Run the Program

You can obtain the project in two ways.

### Option 1: Clone the Repository (Recommended)

```bash
git clone https://github.com/sairamreddy1/final-project.git
```

Then open the downloaded folder.

### Option 2: Download the Project Folder

1. Click **Code → Download ZIP** from the repository page.
2. Extract the folder if it is compressed.
3. Open the folder.

### Run the Program

#### Option 1: Run the Executable

Double-click:

```
Wondering-in-the-woods.exe
```

#### Option 2: Run with Python

Make sure Python is installed, then run:

```bash
python Wondering-in-the-woods.py
```

The program will launch and display the **main menu**.

## 🏠 Home Screen

The home screen allows users to choose between three levels:

- K–2  
- Grades 3–5  
- Grades 6–8  

Each level offers a different learning experience.

---

## 🧒 K–2 Mode (Basic Simulation)

### Purpose

Introduce young students to the concept of **random movement**.

### Features

- Fixed **10 × 10 grid**
- **Two explorers**
- Start in **opposite corners**
- **Random movement**

### Objective

Students observe how long it takes for the explorers to meet.

When they meet, a **Game Over** screen displays the results.

## 🧑‍🎓 Grades 3–5 Mode (Custom Simulation)

### Purpose

Allow students to explore how grid size affects meeting time.

### Inputs Required

Users must enter:

```
Grid Width
Grid Height
Number of Players (2–4)
```

### Example

```
Grid Width: 10
Grid Height: 10
Players: 3
```

### Simulation Process

1. Explorers are placed randomly on the grid.
2. They move randomly.
3. When explorers meet, they merge.
4. The simulation ends when all explorers are together.

## 🧪 Grades 6–8 Mode (Experiment Mode)

### Purpose

Enable students to perform **data-driven experiments**.

### Inputs Required

Users must enter:

```
Grid Size (example: 10x10)
Number of Players
Number of Simulations
```

### Example

```
Grid Size: 10x10
Players: 3
Simulations: 20
```

### Player Placement

After entering inputs, students click on **grid cells to place players**.

Example:

```
Click grid → Player 1
Click grid → Player 2
Click grid → Player 3
```

### Experiment Execution

The program runs the simulation multiple times and records results.

### Results Generated

After simulations complete:

```
Shortest Run
Longest Run
Average Run
```

A **graph is automatically generated** showing the results of each simulation.

---

## 🎵 Background Music

The game includes background music that:

- Starts automatically when the game launches
- Plays continuously in a loop

Ensure the `.mp3` file is in the same folder as the executable.


## 🎮 Controls

| Button | Function |
|------|-----------|
| Back | Return to the previous screen |
| Pause | Pause the simulation |
| Resume | Continue simulation |
| Home | Return to the main menu |

---

## 📊 Saved Results

Experiment results are automatically saved to:

```
scores.txt
```

Each entry records:

- Shortest run
- Longest run
- Average run

---

## 📚 Educational Goals

This simulation helps students learn:

- Computational thinking
- Random algorithms
- Data collection
- Statistical analysis
- Experimental design

Students progress from **simple observation to advanced experimentation** across the three levels.

---

## 🛠 Technologies Used

- **Python**
- **Pygame** – graphical interface
- **Matplotlib** – graph generation

---

## 📄 License

This project is intended for **educational use**.
