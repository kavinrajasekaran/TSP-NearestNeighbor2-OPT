## TSP Nearest Neighbor + 2-Opt

Quick Python script that solves two 1,000-node TSP instances. It builds a tour with a nearest-neighbor walk, then keeps flipping edges with 2-opt until it runs out of time.

### What’s here
- `919711804.py`: main script that loads distances, runs the heuristic, and writes a tour.
- `TSP_1000_euclidianDistance.txt` and `TSP_1000_randomDistance.txt`: distance data.
- `goodresults/`: sample output from a previous run.
- `solution_*.txt`: saved tour from the last run.


### 2-opt described
Cut two edges, flip the middle chunk, and reconnect. If that makes the tour shorter, keep it. Repeat until nothing better shows up or the clock says stop.

