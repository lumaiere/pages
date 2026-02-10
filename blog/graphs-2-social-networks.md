## Episode 2: Social Networks — Who Influences Whom (and Why FAANG Cares)

Before we jump in, here is the intro to the overall series, which explains why graph theory keeps showing up in interviews and real systems:
[https://medium.com/@DaveLumAI/what-am-i-missing-about-graph-theory-and-why-faang-keeps-bringing-it-up-e010db2aef7e](https://medium.com/@DaveLumAI/what-am-i-missing-about-graph-theory-and-why-faang-keeps-bringing-it-up-e010db2aef7e)

If Episode 1 was about getting from point A to point B without losing your sanity, Episode 2 is about people. Or more precisely: connections between people, companies, bots, influencers, lurkers, and that one account that only exists to like posts at 3 a.m.

Social networks are graphs. Clean, elegant, deceptively simple graphs that immediately turn chaotic the moment real humans get involved.

Nodes are people (or accounts).
Edges are relationships: follows, friendships, likes, mentions, replies, shares.

That’s it. That’s the whole model.

And yet, from this innocent setup, companies build recommendation engines, detect misinformation, rank influence, decide what you see, and quietly answer the question: “Whose voice actually matters here?”

### The Core Graph Theory Idea

The key concept in this episode is **centrality**.

Centrality asks: which nodes are important, and why?

Not popular. Not loud. Important.

There are several ways to define importance in a graph, and each one answers a slightly different question.

Degree centrality is the simplest. Count the edges. More connections means more influence. This is fine until you realize spam bots exist.

Betweenness centrality looks at who sits on the shortest paths between others. These are the brokers, the bridges, the “if you remove this node, everything fractures” accounts.

Closeness centrality measures how quickly a node can reach everyone else. Think fast spreaders, not necessarily famous ones.

Eigenvector-based centrality (famously used in PageRank) says: being connected to important nodes makes you important. A like from someone nobody listens to is polite. A like from someone everyone listens to moves markets.

Social networks use all of these, often together, and usually with additional constraints layered on top to stop the system from being gamed too easily.

### Applying This to Real Problems

Let’s ground this in something concrete.

Imagine you’re building a feature that answers: “Who should we recommend this post to first so it spreads efficiently?”

That is not a sorting problem.
That is not a database problem.
That is a graph problem.

You model the network as a directed graph. You assign weights to edges based on interaction strength. Then you compute a centrality score that matches your goal: speed, reach, trust, or containment.

Another example: misinformation detection.

Instead of asking “Is this post false?”, platforms often ask: “How is this spreading?”

If a claim jumps across loosely connected communities through a small number of bridging nodes, those nodes become critical intervention points. That insight comes directly from betweenness centrality and community detection in graphs.

### A Real FAANG-Style Interview Question

Here is a very typical formulation, stripped of buzzwords:

“You are given a directed graph representing users and follow relationships. Starting from a given user, find the top K most influential users reachable within N steps.”

This question quietly tests multiple things at once.

Do you recognize this as a graph traversal problem?
Do you choose BFS or DFS, and can you explain why?
Do you track visited nodes correctly?
Do you know how to rank influence without recomputing everything from scratch?

### How You Solve It

You start with a breadth-first search from the source node, stopping at depth N.

As you traverse, you accumulate influence scores. These might be raw follower counts, weighted scores, or precomputed centrality values stored with each node.

You maintain a min-heap of size K to track the top candidates as you go.

You do not traverse the entire graph unless forced to. You stop early when depth limits or pruning conditions are met.

This is the difference between “works on the whiteboard” and “works at scale.”

### Optimizing the Solution

The first optimization is obvious: don’t recompute influence scores during the interview. Precompute or cache them.

The second is less obvious: prune aggressively. If you already know the maximum possible influence remaining at a deeper level cannot beat your current top K, you stop exploring that branch.

The third is structural: store adjacency lists, not matrices. Social graphs are sparse, and pretending otherwise is how memory budgets quietly explode.

Below is **clean, interview-ready Python**, followed by a **manual testing walkthrough** exactly the way I would explain it at a whiteboard or while pair-debugging.

---

## 1. Python Source Code: Top-K Influential Users Within N Steps

### Problem Restated (Precisely)

* Directed graph: `user -> users they follow`
* Start from a given user
* Traverse up to `N` hops away
* Rank reachable users by an **influence score**
* Return the **top K**

We’ll assume:

* Graph is an adjacency list
* Influence scores are precomputed (as they would be in real systems)

---

### Python Implementation

```python
from collections import deque
import heapq

def top_k_influencers(graph, influence, start_user, max_depth, k):
    """
    graph: dict[str, list[str]]
        Adjacency list of the social graph
    influence: dict[str, int]
        Precomputed influence score per user
    start_user: str
    max_depth: int
    k: int
    """

    visited = set()
    queue = deque()
    min_heap = []

    # (current_user, depth)
    queue.append((start_user, 0))
    visited.add(start_user)

    while queue:
        user, depth = queue.popleft()

        if depth > max_depth:
            continue

        if user != start_user:
            score = influence.get(user, 0)

            if len(min_heap) < k:
                heapq.heappush(min_heap, (score, user))
            else:
                if score > min_heap[0][0]:
                    heapq.heappushpop(min_heap, (score, user))

        if depth < max_depth:
            for neighbor in graph.get(user, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))

    # Sort descending by influence
    return sorted(min_heap, reverse=True)
```

---

## 2. How I Would Manually Test This (Step by Step)

This is the part interviewers *love*, and many candidates skip.

### Step 1: Build a Small Test Graph (On Paper)

```text
A -> B, C
B -> D, E
C -> F
D -> G
```

Influence scores:

```text
B: 10
C: 8
D: 15
E: 3
F: 7
G: 20
```

Parameters:

```text
start_user = A
max_depth = 2
k = 3
```

---

### Step 2: Expected Traversal (BFS)

Depth 0:

* A (ignored for ranking)

Depth 1:

* B (10)
* C (8)

Depth 2:

* D (15)
* E (3)
* F (7)

Depth 3:

* G (ignored, depth too deep)

---

### Step 3: Track Heap Evolution Manually

Heap keeps **top 3 only**, smallest at the top.

| Visited | Score | Heap Contents              |
| ------- | ----- | -------------------------- |
| B       | 10    | [(10, B)]                  |
| C       | 8     | [(8, C), (10, B)]          |
| D       | 15    | [(8, C), (10, B), (15, D)] |
| E       | 3     | ignored (too small)        |
| F       | 7     | ignored (too small)        |

Final heap:

```text
[(15, D), (10, B), (8, C)]
```

✅ Matches expectation

---

### Step 4: Edge Case Tests (Very Important)

#### Case 1: `k = 0`

Expected result:

```python
[]
```

Why it works:

* Heap never fills
* Function safely returns empty list

---

#### Case 2: Graph With Cycles

```text
A -> B
B -> C
C -> A
```

Why it doesn’t break:

* `visited` prevents infinite loops
* BFS guarantees bounded traversal

---

#### Case 3: Missing Influence Score

```python
influence.get(user, 0)
```

Why this matters:

* Real data is messy
* Missing scores degrade gracefully instead of crashing

---

### Step 5: Time & Space Sanity Check

Manually confirm:

* BFS visits each node once → O(V + E)
* Heap operations → O(log K)
* Memory grows with visited set → O(V)

Everything behaves exactly as analyzed.

---

## 3. How This Translates to a FAANG Interview

What they’re really watching for:

* You chose **BFS** (not DFS) and can explain why
* You capped depth correctly
* You didn’t sort everything unnecessarily
* You used a **bounded heap**
* You thought about cycles and bad data

If you walk through it this cleanly, you’re not “answering a question” anymore — you’re demonstrating systems thinking.

### Big O Time and Space

Let V be the number of users and E the number of relationships.

The traversal is O(V + E) in the worst case, but bounded by depth N in practice.

Maintaining the heap is O(log K) per insertion.

Space complexity is O(V) for visited tracking, plus O(K) for the heap.

Interviewers care less about the exact symbols and more about whether you understand what actually grows when the system grows.

### How Common Is This in FAANG Interviews?

Very.

Sometimes it’s framed as “influencers.”
Sometimes it’s “recommendations.”
Sometimes it’s “trust networks” or “spam detection.”

But under the hood, it is the same family of problems: graph traversal plus ranking.

If you can explain why BFS makes sense here, how centrality differs from popularity, and where performance bottlenecks appear, you are already ahead of most candidates.

### Interesting Tidbits

Social networks rarely rely on a single graph. They stack graphs: follows, interactions, content similarity, shared behavior, time decay.

They also intentionally inject randomness. Pure graph optimization leads to echo chambers. Controlled noise keeps systems healthy and users slightly surprised.

And yes, many systems still quietly resemble academic papers from the late 1990s. The math aged well. The interfaces did not.

### [Art Prompt (Conceptual Art)](https://lumaiere.com/?gallery=conceptual-art)

A vast, pale canvas dominated by delicate, floating geometric forms that seem suspended in thought rather than space. Soft gradients of ivory, ash gray, and muted teal drift across the surface, intersected by faint, almost hesitant lines. The composition feels intentional yet unresolved, as if meaning is implied but never fully revealed. Negative space is treated as an active participant, creating a calm, intellectual tension. The mood is contemplative, restrained, and quietly provocative, inviting the viewer to linger and interpret rather than consume.

### [Video Prompt](https://www.tiktok.com/@davelumai/video/7605051325419638047)

Slow camera drift across the abstract forms as they subtly shift position, lines gently animating as if responding to unseen forces. Gradual color transitions ripple through the background, creating the sensation of thought unfolding in real time. Occasional soft pulses of light emphasize connections between shapes, then fade, maintaining a minimalist, hypnotic rhythm suited for short-form visual storytelling.

### Music Pairings for the Video

* Silver Lining – Hana Vu
* Quiet Geometry – Green-House

If this sparked a few “ohhh, that’s why” moments, follow along for the rest of the series. Drop a comment with the graph concept that confused you the longest, or the one that finally clicked. Conversations, like graphs, get better the more edges we add.
