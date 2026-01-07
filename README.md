## TSP Nearest Neighbor + 2-Opt

Quick Python script that solves two 1,000-node TSP instances. It builds a tour with a nearest-neighbor walk, then keeps flipping edges with 2-opt until it runs out of time.

### What’s here
- `919711804.py`: main script that loads distances, runs the heuristic, and writes a tour.
- `TSP_1000_euclidianDistance.txt` and `TSP_1000_randomDistance.txt`: distance data.
- `goodresults/`: sample output from a previous run.
- `solution_*.txt`: saved tour from the last run.

### How to run it
1) Install NumPy if you don’t have it: `pip install numpy`.  
2) From this folder: `python 919711804.py`.  
It will churn for about a minute (hardcoded time limit) and drop `solution_919711804.txt` with the two tours.

### 2-opt
Cut two edges, flip the middle chunk, and reconnect. If that makes the tour shorter, keep it. Repeat until nothing better shows up or the clock says stop.

### Notes
- The script uses a fixed `N = 1000` and expects the distance files to match.
- Start nodes are randomized for the first few runs, then it shuffles the current best tour to explore.

