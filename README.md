
# Cuenca - coding challenge
### ISC Omar CC

# N Queens Puzzle

## The Problem
Here's the programming problem: [https://en.wikipedia.org/wiki/Eight_queens_puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle)

## Steps Challenge
These are the different aspect of the project you can work on (in order):

1. Determine all possible solutions for a given N where N ≥ 8 (within 10 mins on a laptop). Bonus points for a higher N where N is the size of the board / number of queens

2. Tterate over N and store the solutions in postgres using SQLAlchemy

3. Write basic tests that at least verify the number of solutions for a given N match what's online. I recommend using pytest

4. Docker-ize the solution, so that I can run the code and tests without any assumption of my local setup (including running a postgres instance in docker-compose)

5. Setup Travis CI (or similar) for your public GitHub repo to run the tests automatically

  
## Consideration
You don't need to go through all of the steps, but there should be instructions on how I can run the code. I mainly want to see how you approach a problem and your coding style. There are multiple steps so you have the option to show me different skills. It's up to you.

## Runing the Solution
### Build Docker

    docker build -t n_queens_puzzle .

### Run Docker

    docker run -it --rm --name runing_n_queens_puzzle n_queens_puzzle 

## References
### Program reference
https://solarianprogrammer.com/2017/11/20/eight-queens-puzzle-python/

### Testing Use Cases
http://www.ic-net.or.jp/home/takaken/e/queen/