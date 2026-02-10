# Episode 1: Maps, GPS, and Why Your Phone Knows a Shortcut You Don’t

If you have ever watched your GPS calmly reroute you around traffic like it planned this all along, congratulations: you have already trusted graph theory with your time, your fuel, and your sanity.

This first episode of the mini graph theory series starts with the most familiar setting possible: maps. Streets are edges. Intersections are nodes. Your job is simple. Get from here to there without wasting your life at red lights.

This is the shortest path problem, and it is the gateway drug of graph theory.

For the full context of why FAANG companies keep coming back to this topic, the series intro lives here:
[https://medium.com/@DaveLumAI/what-am-i-missing-about-graph-theory-and-why-faang-keeps-bringing-it-up-e010db2aef7e](https://medium.com/@DaveLumAI/what-am-i-missing-about-graph-theory-and-why-faang-keeps-bringing-it-up-e010db2aef7e)

## What is this aspect of graph theory?

In graph terms, a map is a weighted graph. Each node represents a location. Each edge represents a connection between locations. The weight is the cost of using that edge, which could be distance, time, traffic delay, tolls, or even vibes if you are feeling poetic.

The shortest path problem asks a very practical question: what is the cheapest way to go from one node to another?

Algorithms like Dijkstra’s and A* exist for one reason only: nobody wants to explore every possible route just to find the best one.

## Applying this to real problems

GPS routing is the obvious example, but the same idea shows up everywhere:

Routing packets across the internet
Finding the fastest dependency resolution order in build systems
Optimizing delivery routes
Planning robot movement in physical space

Anytime you hear “minimum cost,” “fastest route,” or “least number of hops,” a shortest path problem is quietly clearing its throat.

## A real FAANG-style interview question

You are given a grid representing a city. Each cell has a cost to enter. Starting from the top-left corner, find the minimum cost path to the bottom-right corner. You can move up, down, left, or right.

This looks innocent. It is not.

## How do you solve it?

You model the grid as a graph. Each cell is a node. Each move is an edge with a weight equal to the destination cell’s cost.

Then you run Dijkstra’s algorithm starting from the top-left node. You always expand the cheapest known path first, updating neighbors when you find a better route.

The moment the destination node is finalized, you have your answer.

## How do you optimize it?

You do not need to store the entire graph explicitly. You generate neighbors on the fly.

You use a priority queue to always pull the lowest-cost node next.

Here is solid pseudocode for the “Maps and GPS shortest path” solution (Dijkstra with a min-priority queue), including path reconstruction.

```text
# DijkstraShortestPath(G, start, goal)
# G: graph with adjacency list G.neighbors(u) -> list of (v, weight)
# weight must be non-negative

function DijkstraShortestPath(G, start, goal):
    dist = map with default value Infinity
    prev = map with default value null
    visited = empty set

    dist[start] = 0

    # Min-priority queue of (distance, node)
    pq = new MinPriorityQueue()
    pq.push((0, start))

    while pq is not empty:
        (d, u) = pq.popMin()

        # Skip stale entries
        if d != dist[u]:
            continue

        if u == goal:
            break

        if u in visited:
            continue
        visited.add(u)

        for each (v, w) in G.neighbors(u):
            if w < 0:
                error "Dijkstra requires non-negative weights"

            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                pq.push((alt, v))

    if dist[goal] == Infinity:
        return (Infinity, empty list)

    path = ReconstructPath(prev, start, goal)
    return (dist[goal], path)


function ReconstructPath(prev, start, goal):
    path = empty list
    cur = goal

    while cur is not null:
        path.prepend(cur)
        if cur == start:
            return path
        cur = prev[cur]

    # If we fell off the chain without hitting start, no valid path
    return empty list
```

If the grid is large and you have a heuristic, you switch to A* and guide the search toward the goal instead of wandering politely in all directions.

This version assumes a **non-negative cost graph** and an **admissible heuristic** (it never overestimates the remaining cost).

```text
# AStarShortestPath(G, start, goal, h)
# G: graph with adjacency list G.neighbors(u) -> list of (v, weight)
# h(n): heuristic estimate from node n to goal

function AStarShortestPath(G, start, goal, h):
    gScore = map with default value Infinity   # cost from start to node
    fScore = map with default value Infinity   # gScore + heuristic
    prev = map with default value null

    gScore[start] = 0
    fScore[start] = h(start)

    # Min-priority queue ordered by fScore
    openSet = new MinPriorityQueue()
    openSet.push((fScore[start], start))

    closedSet = empty set

    while openSet is not empty:
        (currentF, current) = openSet.popMin()

        # Skip stale entries
        if currentF != fScore[current]:
            continue

        if current == goal:
            path = ReconstructPath(prev, start, goal)
            return (gScore[goal], path)

        closedSet.add(current)

        for each (neighbor, cost) in G.neighbors(current):
            if neighbor in closedSet:
                continue

            if cost < 0:
                error "A* requires non-negative weights"

            tentativeG = gScore[current] + cost

            if tentativeG < gScore[neighbor]:
                prev[neighbor] = current
                gScore[neighbor] = tentativeG
                fScore[neighbor] = tentativeG + h(neighbor)
                openSet.push((fScore[neighbor], neighbor))

    return (Infinity, empty list)


function ReconstructPath(prev, start, goal):
    path = empty list
    cur = goal

    while cur is not null:
        path.prepend(cur)
        if cur == start:
            return path
        cur = prev[cur]

    return empty list
```

### Notes interviewers silently care about

* If `h(n) = 0` for all nodes, A* becomes Dijkstra.
* If `h(n)` is admissible and consistent, A* is optimal.
* In grid problems:

  * Manhattan distance is common for 4-direction movement.
  * Euclidean distance works for free movement.

## Big O time and space

Using Dijkstra’s with a priority queue:

Time complexity: O(E log V)
Space complexity: O(V)

On a grid, that usually becomes O(n log n), which is acceptable enough that your interviewer will stop frowning.

Let’s walk through the Big O for **A*** slowly, the same way an interviewer expects you to explain it out loud without panicking or over-optimizing too early.

I’ll start from the data structures, then build up to time and space.

---

## First, define the symbols

We need these before Big O means anything:

* **V** = number of vertices (nodes)
* **E** = number of edges
* **b** = branching factor (average neighbors per node)
* **d** = depth of the optimal solution (how many steps to the goal)

In grid problems:

* V is usually number of cells
* E is roughly 4V (up, down, left, right)

---

## What operations does A* actually do?

Inside the main loop, A* repeatedly:

1. Pops the lowest-priority node from a min-priority queue
2. Iterates over that node’s neighbors
3. Updates scores and pushes neighbors back into the queue

So Big O is dominated by:

* Priority queue operations
* Edge relaxations

---

## Priority queue cost

A* uses a **min-heap** (priority queue).

### Push

* Cost: **O(log V)**

### Pop minimum

* Cost: **O(log V)**

Each node can be pushed multiple times, but only the best version matters (stale entries are skipped).

In the worst case:

* Each edge causes a push
* Total pushes ≈ **E**

So priority queue cost is:

```
O(E log V)
```

---

## Neighbor processing cost

Each edge is examined at most once when relaxing neighbors.

* Total neighbor checks: **O(E)**
* Each check is constant time

This part is cheaper than the heap operations, so it does not dominate.

---

## Total time complexity (general graph)

Putting it together:

```
Time = O(E log V)
```

This is **the same upper bound as Dijkstra**, because A* is Dijkstra plus a heuristic.

---

## But doesn’t the heuristic help?

Yes — but **Big O is worst case**, not best case.

### Worst case

If the heuristic is bad (or zero):

* A* explores almost everything
* Behaves exactly like Dijkstra

So worst-case time remains:

```
O(E log V)
```

### Practical case

With a good heuristic:

* A* explores far fewer nodes
* Runtime is often much closer to O(b^d) in practice
* But interviewers will not let you claim that as Big O

---

## Space complexity

A* stores:

* gScore for each visited node → O(V)
* fScore for each visited node → O(V)
* prev pointers for path reconstruction → O(V)
* Priority queue entries → up to O(V)

So space complexity is:

```
O(V)
```

---

## Grid-specific simplification (very common interview follow-up)

For an N x N grid:

* V = N²
* E ≈ 4N²

Substitute:

```
Time: O(N² log N²)
Space: O(N²)
```

Since log N² = 2 log N:

```
Time: O(N² log N)
Space: O(N²)
```

This is the answer interviewers expect you to say smoothly.

---

## One subtle detail interviewers love

Why do we allow multiple pushes of the same node?

Because:

* Decrease-key is awkward or slow in many heap implementations
* Pushing duplicates and skipping stale entries keeps the code simple
* It does **not** change Big O

If you mention this, you sound very prepared.

---

## The clean interview summary

If you need a one-breath answer:

> A* with a binary heap runs in O(E log V) time and O(V) space.
> In grid problems, this simplifies to O(N² log N) time and O(N²) space.

## How common is this in FAANG interviews?

Very.

Sometimes it is dressed up as maps. Sometimes it is matrices. Sometimes it pretends to be a game board or a maze.

But if you can confidently solve shortest path problems, you are covering a large percentage of graph questions without even knowing their real names.

## Interesting tidbits

Dijkstra’s algorithm fails if you allow negative weights. This is not a bug. It is a reminder that assumptions matter.

Your GPS recalculates routes constantly because edge weights change in real time.

If you ever wondered why interviews love this problem, it is because it tests modeling, algorithm choice, optimization, and calm thinking under pressure in one neat package.

If this clicked, follow along for the next episode and drop a comment with the worst reroute your GPS has ever suggested.

---

[Art Prompt (Constructivism): ](https://lumaiere.com/?gallery=constructivism)
A bold, geometric composition built from sharp angles and overlapping planes, dominated by strong diagonals that suggest motion and direction. A limited palette of deep reds, charcoal blacks, and muted creams creates visual tension, while flat blocks of color collide and interlock. The composition feels architectural and purposeful, with an industrial rhythm that conveys momentum and precision rather than emotion.

[Video Prompt:](https://www.tiktok.com/@davelumai/video/7604668949703314718)
Animate the geometric forms so they slide, rotate, and snap into alignment with mechanical precision. Diagonal shapes sweep across the frame in rhythmic pulses, while subtle camera pans reveal new layers of intersecting planes. Motion feels deliberate and engineered, creating a hypnotic sense of forward progress.

Song suggestions for the video:
- Vector Drift – Aural Systems
- Silent Geometry – North Atlas

Follow for more deep dives and leave a comment if graph theory finally stopped feeling abstract.
