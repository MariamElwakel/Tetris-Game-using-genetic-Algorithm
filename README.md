# Tetris Game Using Genetic Algorithm

This project implements an AI agent to play the classic Tetris game using a Genetic Algorithm (GA).  
The algorithm evolves a population of candidate solutions (chromosomes) to optimize gameplay and achieve a high score.

## Features
- Implements all main GA steps:
  - Population initialization (20 chromosomes with random genes)
  - Fitness evaluation (score / number of pieces played)
  - Parent selection (roulette wheel method)
  - One-point crossover
  - Mutation (rate = 0.2)
- AI evaluates all possible moves for each piece and selects the best one.
- Game continues until either:
  - The player loses, or  
  - The AI reaches the **winning score of 10,000 points**.

## Gameplay Scoring
- 1 line cleared → **+50 points**  
- 2 lines cleared → **+150 points**  
- 3 lines cleared → **+500 points**  
- 4 lines cleared → **+1500 points**

## Fitness Factors
Each chromosome is evaluated using the following factors:
- Removed lines (maximize)  
- Holes (minimize)  
- Blocking blocks (minimize)  
- Wells and maximum height (minimize)  
- Piece sides, floor sides, wall sides (balanced)

## Training
- Population size: **20 chromosomes**  
- Seeds: **25**  
- Iterations: **300–500**  
- Best chromosomes achieved fitness scores of ~32.9 and ~28.8  
- Most impactful factors: **holes** and **piece sides**

## Tech Stack
- **Language:** Python  
- **Algorithm:** Genetic Algorithm
