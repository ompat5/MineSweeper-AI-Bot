# MineSweeper-AI-Bot

A computer bot that plays Minesweeper using different agents. This project implements an intelligent Minesweeper agent that solves the game using advanced AI techniques. It leverages data collection and inference to inform its actions, balancing safe cell exploration with efficient decision-making in uncertain environments.

## Key Features
- Constraint Satisfaction Problem (CSP): The agent models the game board as a CSP, using constraint equations to deduce safe and mine-containing cells.

### Three-Phase Solver:
- Basic Solver: Flags obvious mines and opens safe cells based on simple equations.
- Subset Solver: Deduces additional information by solving subsets of constraints, improving the agent's ability to make inferences.
- Random Solver: Uses heuristics for random cell selection when no further inferences are possible. (Heuristic-Based Exploration: The agent minimizes risk by using probability heuristics when selecting unknown cells.)

# Demo
