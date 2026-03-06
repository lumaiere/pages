# Graph Theory and Search Engines: Why Some Pages Matter More Than Others

If you have ever typed a question into a search engine and gotten an eerily good answer in under a second, you might assume the internet is secretly run by librarians with superpowers.

It is not.

It is run by math.

Specifically, graph theory.

If you are new to this mini-series, the introduction explains why engineers at large tech companies keep bringing up graph theory during interviews and system design conversations:

[https://medium.com/@DaveLumAI/what-am-i-missing-about-graph-theory-and-why-faang-keeps-bringing-it-up-e010db2aef7e](https://medium.com/@DaveLumAI/what-am-i-missing-about-graph-theory-and-why-faang-keeps-bringing-it-up-e010db2aef7e)

In the previous episode we looked at social networks and influence. Today we move to something even bigger: the web itself.

Because the internet is basically a giant graph.

And once you realize that, search engines suddenly make a lot more sense.

---

## The Web Is a Graph

Imagine every web page on the internet as a node.

Every hyperlink from one page to another is an edge.

That alone creates an enormous directed graph.

Page A links to Page B
Page B links to Page C
Page C links to Page A

Now we have a cycle.

Multiply that by billions of pages and trillions of links and you get the web graph.

Search engines must answer one deceptively simple question:

Which pages are the most important?

Not the newest.
Not the longest.
Not the ones with the fanciest fonts.

Important.

This is where graph theory steps in.

---

## The Core Idea: Importance by Association

Early search engines mostly counted keywords.

That worked about as well as you might imagine.

If you searched for "best pizza," the results might include pages that repeated the word pizza 4,000 times and still somehow sold office chairs.

The breakthrough was realizing something simple.

A page becomes important if important pages link to it.

This idea became the foundation of PageRank, one of the algorithms behind early Google.

You can read about the original concept in the research paper:

Lawrence Page, Sergey Brin, Rajeev Motwani, Terry Winograd
"[The PageRank Citation Ranking: Bringing Order to the Web](https://web.archive.org/web/20090126204112/http://ilpubs.stanford.edu:8090/422/1/1999-66.pdf)" (1999)


The key insight:

Links behave like votes.

But not all votes are equal.

A link from a respected site counts far more than a link from a random blog created yesterday about alien gardening techniques.

Graph theory lets us model that mathematically.

---

## The Random Surfer Model

Imagine a person who starts on a random page and begins clicking links forever.

Sometimes they follow a link.

Sometimes they jump somewhere completely different.

The probability that the surfer lands on a particular page becomes its importance score.

Pages that receive lots of links from other high-scoring pages accumulate more probability.

Mathematically, the system becomes a giant network of probability flow.

This can be expressed using matrix operations on the adjacency graph of the web.

In other words:

We repeatedly distribute influence through the graph until the scores stabilize.

That stable distribution is the ranking.

---

## How This Appears in Real Systems

Search engines combine hundreds of signals today.

But the core graph idea still appears everywhere:

* web page ranking
* academic citation ranking
* recommendation engines
* knowledge graphs

Even package managers use similar ideas when evaluating dependencies.

If something is widely depended on by reliable projects, it likely matters.

Graph structure reveals hidden authority.

---

## A Classic FAANG Interview Question

Here is a question that often appears in interviews.

**Problem**

You are given a directed graph representing web pages.

Each node links to several other nodes.

Return the PageRank score for each node after running the algorithm for N iterations.

This tests:

* graph modeling
* probability distribution
* iterative convergence

---

## Step 1: Model the Graph

We represent the graph as an adjacency list.

Example:

```
A → B, C
B → C
C → A
```

---

## Step 2: Initialize Equal Probability

If we have N pages:

```
initial_rank = 1 / N
```

Everyone starts equal.

Democracy at its finest.

---

## Step 3: Update Scores Iteratively

Each page distributes its rank across outgoing links.

With damping factor **d** (usually 0.85):

```
new_rank = (1 - d)/N + d * incoming_contributions
```

The damping factor models the "random jump" behavior.

---

## Python Implementation

```python
def pagerank(graph, iterations=20, d=0.85):
    n = len(graph)
    ranks = {node: 1/n for node in graph}

    for _ in range(iterations):
        new_ranks = {}
        for node in graph:
            new_ranks[node] = (1 - d) / n

        for node in graph:
            links = graph[node]
            if links:
                share = ranks[node] / len(links)
                for target in links:
                    new_ranks[target] += d * share

        ranks = new_ranks

    return ranks


graph = {
    "A": ["B", "C"],
    "B": ["C"],
    "C": ["A"]
}

print(pagerank(graph))
```

---

## Manual Testing Strategy

When testing graph algorithms, start small.

Test case 1:

```
A → B
B → A
```

Expected result:

Both pages receive equal rank.

Test case 2:

```
A → B
B → C
C → A
```

Symmetrical cycle.

Again, equal ranking.

Test case 3:

```
A → B
C → B
```

Page B should accumulate more rank because two pages point to it.

These sanity checks confirm probability flow is working.

---

## Time and Space Complexity

Let:

* V = number of pages
* E = number of links
* k = number of iterations

### Time Complexity

Each iteration processes all edges.

```
O(kE)
```

### Space Complexity

We store rank values and adjacency lists.

```
O(V + E)
```

---

## Why FAANG Likes This Problem

It tests multiple skills at once:

Graph representation
Iterative algorithms
Probability thinking
Optimization

It also opens doors to follow-up questions.

What if the graph has billions of nodes?

How do you distribute the computation?

That conversation quickly moves into distributed systems.

Which happens to be the topic of the next episode.

---

## A Few Fun Graph Theory Tidbits

The web graph has fascinating properties.

It is:

* highly clustered
* scale-free
* power-law distributed

Meaning a small number of pages receive most of the links.

Sound familiar?

That pattern appears in social networks, airline routes, and scientific citations.

Graph theory keeps revealing the same structures in wildly different places.

Which is why engineers keep coming back to it.

---

## Your Turn

If you enjoyed this one:

* follow along for the next episode
* drop a comment with your favorite graph problem
* share how you have used graph theory in real systems

You might be surprised how often it quietly powers the tools we use every day.

---

## [Art Prompt (Realism)](https://lumaiere.com/?gallery=realism)

A windswept shoreline under heavy gray skies, towering ocean waves crashing against dark volcanic rock, thick sea spray suspended in cold coastal air, the water rendered with dramatic physical realism and layered textures, deep green and slate-blue tones rolling through translucent crests, subtle foam patterns catching dim afternoon light, distant horizon blurred by mist and rain, the composition dominated by the raw energy of the ocean, meticulous brushwork emphasizing movement and mass, with naturalistic lighting and atmospheric depth that evokes the rugged majesty of a storm-driven sea.

---

## [Video Prompt](https://www.tiktok.com/@davelumai/video/7613958059370515742)

A cinematic coastal storm scene where enormous waves crash rhythmically against jagged black rocks, mist and sea spray drifting through the air in slow motion, shifting gray clouds racing across the sky while shafts of pale sunlight break through the storm. The camera sweeps low across the turbulent water, then rises above the cliffs revealing endless ocean motion, dramatic lighting changes, swirling fog, and rolling waves that pulse in sync with music.

---

## Song Suggestions

Illusion – Dua Lipa
Too Sweet – Hozier

