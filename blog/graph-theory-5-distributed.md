# Graph Theory Episode 5: Distributed Systems, Service Graphs, and the Fine Art of Not Taking Down Production

If you have ever looked at a distributed system diagram and thought, "That seems manageable," there is an excellent chance the diagram was lying to you.

Distributed systems always begin with noble intentions. One service handles users. Another handles payments. Another handles inventory. Another sends email. Another logs events. Another quietly exists because someone made a "temporary" helper service in 2022 and nobody has had the courage to ask what it does.

Soon enough, you are no longer running one application. You are running a neighborhood.

And graph theory is what helps you understand who is talking to whom, what depends on what, what breaks when something fails, and why one innocent-looking timeout can suddenly turn your Tuesday into an incident review.

If you are new to the series, the intro is here: [What Am I Missing About Graph Theory (and Why FAANG Keeps Bringing It Up)?](https://medium.com/@DaveLumAI/what-am-i-missing-about-graph-theory-and-why-faang-keeps-bringing-it-up-e010db2aef7e)

Earlier episodes:
- [Episode 1: Maps, GPS, and Why Your Phone Knows a Shortcut You Don't](https://medium.com/@DaveLumAI/episode-1-maps-gps-and-why-your-phone-knows-a-shortcut-you-dont-1138882c0968)
- [Episode 2: Social Networks - Who Influences Whom (and Why FAANG Cares)](https://medium.com/@DaveLumAI/episode-2-social-networks-who-influences-whom-and-why-faang-cares-c5b7221f075b)
- [Graph Theory and Search Engines: Why Some Pages Matter More Than Others](https://medium.com/@DaveLumAI/graph-theory-and-search-engines-why-some-pages-matter-more-than-others-3c1796593206)
- [Graph Theory and Build Systems: Why Your Code Refuses to Compile in the Wrong Order](https://medium.com/@DaveLumAI/graph-theory-and-build-systems-why-your-code-refuses-to-compile-in-the-wrong-order-738517184e5a)

So let us talk about Episode 5: distributed systems and service communication.

## The core graph theory idea

A distributed system can often be modeled as a directed graph.

Each node is a service:

* API gateway
* auth service
* user service
* payment service
* recommendation service
* notification service
* database proxy
* cache layer
* event processor

Each directed edge means one service calls, depends on, or sends work to another service.

If Service A calls Service B, and Service B calls Service C, then the graph is not just a pretty architecture picture. It is an operational fact. Requests, failures, retries, latency, and load all move along those edges.

That is the important mental shift.

Graph theory turns "our system is kind of complicated" into something more precise:

* What services are reachable from this one?
* What is the shortest dependency path between two services?
* Which services are critical bridges?
* What is the blast radius if one service fails?
* Are there cycles that can create nasty retry storms or feedback loops?
* Can we order startup, shutdown, or deployment safely?

Once you see the service map as a graph, a lot of distributed systems behavior stops feeling mysterious and starts feeling measurable.

## Can you explain this aspect of graph theory in detail?

Yes, and this is one of the most practical uses of graph theory in modern engineering.

There are a few graph concepts doing the heavy lifting here.

### 1. Reachability

Reachability asks a simple question: from Service X, what other services can be reached?

If your checkout service depends on pricing, inventory, fraud, payment authorization, notification, and order persistence, then a failure in one upstream component may affect everything downstream that depends on it.

That means a reachability traversal is a very real way to compute blast radius.

Not "kind of affected."
Actually affected.

### 2. Directed graphs

Direction matters.

Auth calling user-profile is not the same as user-profile calling auth. In a distributed system, who initiates the call changes latency, ownership, retry behavior, security posture, and failure propagation.

Edges are not decorative. They are causality wearing a tiny arrow.

### 3. Cycles

Cycles in service communication are where things start getting spicy.

Suppose:

* Service A calls Service B
* Service B calls Service C
* Service C calls Service A

Now imagine one of them slows down. Retries begin. Queues back up. Threads pile up. Timeouts multiply. Logs turn into modernist poetry.

A cycle in a service graph is not always forbidden, but it is always worth treating with suspicion.

### 4. Centrality and articulation-like importance

Some services are not the biggest, but they are the most dangerous to lose.

A small configuration service, token service, or discovery layer may sit in the middle of many request paths. Remove it, and half your system suddenly forgets how to be alive.

That is a graph-importance question, not just a hardware question.

### 5. Topological ordering for dependency-aware operations

When services have one-way dependencies and the graph is acyclic, you can use topological thinking to reason about startup order, deployment order, or migration order.

You do not want to bring up a service that depends on three things that are still taking a nap.

## How do I apply this to actual distributed systems problems?

Here are some concrete examples.

### Failure blast radius

If Service X is down, which services are impacted?

That is a traversal problem. Start at X, walk the graph, and find everything downstream that depends on it either directly or transitively.

### Safe deployment order

If a new deployment changes a shared dependency, which services should be updated first?

That is often a topological-order or dependency-order question.

### Tracing and debugging

If a request times out, where did it go?

Distributed tracing tools model request flow across services, and that flow is fundamentally graph-shaped. OpenTelemetry's overview explicitly describes traces in terms of span relationships, and the tracing docs are useful references if you want to see that in a formal observability context:
- [OpenTelemetry Overview](https://opentelemetry.io/docs/specs/otel/overview/)
- [OpenTelemetry Traces](https://opentelemetry.io/docs/concepts/signals/traces/)

### Cascading failure analysis

If one service degrades, where does overload spread next?

That becomes a graph-plus-systems question. Failure does not stay politely in one corner. It travels edges, often helped along by retries, queues, and wishful thinking. Google's SRE material on cascading failures is a very good real-world reference here:
[Google SRE: Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/)

### Dependency hygiene

If your service graph has too many edges, hidden cycles, or strange central chokepoints, graph analysis helps you clean it up before production teaches you the lesson more dramatically.

## What is an actual FAANG-style interview question on this topic?

A very believable version is this:

You are given a directed graph of microservice dependencies. An edge A -> B means service A depends on service B. If service B fails, service A is impacted.

Given a starting failed service, return all impacted services in the system.

That is a beautiful interview question because it tests several things at once:

* Do you recognize the graph model quickly?
* Do you get the edge direction right?
* Do you know whether to traverse the original graph or the reversed graph?
* Do you avoid revisiting nodes?
* Do you produce something correct before trying to get fancy?

And yes, this type of question is common enough in interviews that you should absolutely be comfortable with it. Maybe not with the exact words "microservice dependency graph," but the underlying pattern shows up constantly: dependency propagation, failure impact, reachability, graph traversal, transitive closure, topological reasoning.

In other words, if FAANG does not ask this exact question, it will often ask this question wearing a fake mustache.

## How do I solve it?

The key insight is that the dependency graph as stated is:

A -> B means A depends on B

If B fails, we need to find all services that depend on B.

So for propagation of failure, we want the reverse direction:
B -> A

That means the clean solution is:

1. Reverse the graph
2. Start from the failed service
3. Run BFS or DFS
4. Collect every reachable node except the starting one

BFS and DFS both work here because the main task is reachability. If the interviewer asks for distance in hops from the failed service, BFS is especially nice because it naturally gives layers.

## How do I optimize that solution?

First, get the correct traversal working. Heroics can wait.

After that:

### Optimization 1: Build the reverse graph once

If you will answer many failure-impact queries, do not rebuild the reverse graph every time. Precompute it.

### Optimization 2: Use adjacency lists

Distributed systems graphs are usually sparse. Adjacency lists are the right default. Adjacency matrices are a terrific way to spend memory like you are trying to impress it.

### Optimization 3: Cache repeated queries

If the service graph changes infrequently, memoizing impact sets for commonly failed services can save time.

### Optimization 4: Return distances if useful

Sometimes "what breaks?" is less useful than "what breaks first?" or "how many hops away is the impact?" A BFS can return impact depth almost for free.

### Optimization 5: Detect cycles separately

Cycles do not break the traversal if you track visited nodes, but detecting them is useful operationally because cycles often indicate risky architecture.

## Python solution

```python
from collections import defaultdict, deque

def impacted_services(dependencies, failed_service):
    """
    dependencies: dict[str, list[str]]
        A -> [B, C] means A depends on B and C

    failed_service: str
        The service that has failed

    returns: list[str]
        All impacted services, sorted in BFS discovery order
    """

    # Reverse the graph so dependency failure can propagate outward.
    reverse_graph = defaultdict(list)

    # Ensure all services appear even if they have no outgoing edges.
    for service in dependencies:
        reverse_graph[service]

    for service, deps in dependencies.items():
        for dep in deps:
            reverse_graph[dep].append(service)
            reverse_graph[service]  # keep service present

    impacted = []
    visited = set([failed_service])
    queue = deque([failed_service])

    while queue:
        current = queue.popleft()

        for neighbor in reverse_graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                impacted.append(neighbor)
                queue.append(neighbor)

    return impacted


if __name__ == "__main__":
    dependencies = {
        "api-gateway": ["auth-service", "order-service"],
        "order-service": ["payment-service", "inventory-service"],
        "payment-service": ["fraud-service"],
        "inventory-service": [],
        "fraud-service": [],
        "auth-service": ["user-service"],
        "user-service": [],
        "notification-service": ["order-service"]
    }

    failed = "payment-service"
    print(impacted_services(dependencies, failed))
    # Expected:
    # ['order-service', 'api-gateway', 'notification-service']
```

## Can you walk me through how you would manually test it?

Absolutely. This is the part people skip, and then later they are "surprised" that production has opinions.

### Test 1: Simple chain

A depends on B
B depends on C

If C fails, impacted should be:

* B
* A

Input:

* A -> B
* B -> C
* C -> none

Expected output for failed C:

* B, A

### Test 2: Branching dependency

Checkout depends on payment and inventory
Notification depends on checkout

If payment fails, impacted should be:

* checkout
* notification

But inventory should not appear.

That checks that failure only propagates along valid reverse paths.

### Test 3: Isolated service

If logging-service has no dependents and it fails, impacted should be empty.

That checks we do not invent damage for dramatic effect.

### Test 4: Cycle

A depends on B
B depends on C
C depends on A

If A fails, impacted should eventually include B and C, but the traversal must terminate.

That checks visited-set correctness.

### Test 5: Missing leaf in original keys

Suppose A depends on B, but B was not explicitly listed as a top-level key in the dictionary.

The reverse-graph build should still handle B correctly.

That checks graph construction robustness.

### Test 6: Bigger realistic graph

Use a graph with gateway, auth, users, checkout, payment, fraud, notifications, and analytics. Pick several failed services and verify the returned blast radius matches your architecture intuition.

That checks whether the model still behaves when the graph stops being toy-sized and starts resembling your actual life choices.

## What is the Big O for time and space?

Let:

* V = number of services
* E = number of dependency edges

### Building the reverse graph

Time: O(V + E)
Space: O(V + E)

### BFS traversal

Time: O(V + E) in the worst case
Space: O(V) for visited and queue, plus the stored graph

### Total

If you include graph construction:
Time: O(V + E)
Space: O(V + E)

That is about as good as it gets for a full graph traversal. Once the interviewer hears linear in nodes plus edges, they usually stop looking disappointed.

## Can you walk me through how you came up with that?

Yes. This is the reasoning path I would say out loud in an interview.

First, I translate the problem into graph language.

We have services and dependency relationships, so this is a directed graph.

Second, I carefully interpret the edge.

If A depends on B, and B fails, then impact travels from B to A, not from A to B.

That means the traversal direction in the original graph is backwards relative to failure propagation.

Third, I ask what the problem wants.

It wants every impacted service, which means all reachable nodes under the failure-propagation relation.

That is a graph traversal problem.

Fourth, I choose BFS or DFS.

Either works for plain reachability. I would often choose BFS because it is iterative, easy to explain, and naturally supports "distance from failure" extensions.

Fifth, I analyze complexity.

Any traversal that may need to visit every node and edge is going to be O(V + E), which is the expected answer for this class of problem.

That is the whole thought process. No mysticism. Just careful interpretation of direction, then a standard traversal.

## Any other interesting tidbits?

A few.

One, distributed tracing is basically graph storytelling with timestamps.

Two, service dependency maps are often more honest than team documentation.

Three, the most dangerous service in a system is not always the biggest one. Sometimes it is the tiny service nobody thinks about until everything depends on it.

Four, retries are useful right up until they become a coordinated attack on your own infrastructure.

Five, graph theory is one of those topics that seems abstract until you realize it is quietly running half the systems you use every day.

And distributed systems are one of the best examples of that. The services may be spread across machines, regions, queues, caches, and databases, but the structure underneath is still a graph. Once you model it that way, failure paths, dependency chains, critical nodes, and operational risks all become much easier to reason about.

Which is nice, because "it felt haunted" is not usually the postmortem language people are hoping for.

If you enjoyed this episode, follow for more of the series, and drop a comment with the nastiest service dependency problem you have ever seen in the wild. Clean examples are educational. Slightly cursed ones are even better.

## [Art Prompt (Dadaism):](https://lumaiere.com/?gallery=dadaism)

A densely layered abstract-collage composition bursting with torn paper textures, mechanical fragments, bold typographic shards, mismatched diagram pieces, postage-mark graphics, and angular painted interruptions arranged in a restless but deliberate balance. Let the image feel witty, urban, and slightly unruly, with off-kilter geometry, abrupt scale shifts, distressed surfaces, and a palette of muted cream, newsprint gray, rust red, charcoal black, faded teal, and nicotine yellow. Include crisp cut edges, scattered circles, broken grids, and eccentric overlaps that create a sense of improvised intelligence rather than chaos. The mood should feel playful, cerebral, handmade, and faintly rebellious, as if a filing cabinet, a printing press, and a very opinionated poet had collaborated in secret.

## [Video Prompt:](https://www.tiktok.com/@davelumai/video/7623237851978812702)

A fast-moving surreal collage film set inside a world of layered paper, print fragments, mechanical scraps, and sharp geometric forms, with elements sliding, flipping, tearing, rotating, and snapping into strange temporary alignments. Let the camera drift and punch inward through stacked planes of cream, gray, rust red, faded teal, nicotine yellow, and charcoal, with sudden close-ups of distressed textures, cropped letters, circles, broken grids, and diagram pieces that appear and vanish rhythmically. Keep the motion catchy and hypnotic with whip transitions, jittery stop-motion accents, elegant parallax depth, and satisfying visual beats, while the overall mood stays playful, intelligent, and slightly rebellious.

Song suggestions for the video:

* Numb - Men I Trust
* Boadicea - Enya

