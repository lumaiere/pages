# Graph Theory Episode 6: Databases, Query Plans, and Why Your SQL Sometimes Takes the Scenic Route

If you have ever written a query that looked perfectly innocent, hit Enter, and then watched the database respond like you had just asked it to reorganize civilization, welcome. You have arrived at one of graph theory's sneakiest habitats.

This episode is about databases, query planning, and relationships, which sounds very official until you realize it mostly means this: the database has to decide what depends on what, what should happen first, what can be joined later, and how to avoid doing something gloriously expensive by accident.

If you are just joining this lightly caffeinated graph parade, start with the intro here: [https://medium.com/@DaveLumAI/what-am-i-missing-about-graph-theory-and-why-faang-keeps-bringing-it-up-e010db2aef7e](https://medium.com/@DaveLumAI/what-am-i-missing-about-graph-theory-and-why-faang-keeps-bringing-it-up-e010db2aef7e)

Earlier stops on the road:

* Episode 1 - Maps and GPS: [https://medium.com/@DaveLumAI/episode-1-maps-gps-and-why-your-phone-knows-a-shortcut-you-dont-1138882c0968](https://medium.com/@DaveLumAI/episode-1-maps-gps-and-why-your-phone-knows-a-shortcut-you-dont-1138882c0968)
* Episode 2 - Social networks: [https://medium.com/@DaveLumAI/episode-2-social-networks-who-influences-whom-and-why-faang-cares-c5b7221f075b](https://medium.com/@DaveLumAI/episode-2-social-networks-who-influences-whom-and-why-faang-cares-c5b7221f075b)
* Episode 3 - Search engines: [https://medium.com/@DaveLumAI/graph-theory-and-search-engines-why-some-pages-matter-more-than-others-3c1796593206](https://medium.com/@DaveLumAI/graph-theory-and-search-engines-why-some-pages-matter-more-than-others-3c1796593206)
* Episode 4 - Build systems: [https://medium.com/@DaveLumAI/graph-theory-and-build-systems-why-your-code-refuses-to-compile-in-the-wrong-order-738517184e5a](https://medium.com/@DaveLumAI/graph-theory-and-build-systems-why-your-code-refuses-to-compile-in-the-wrong-order-738517184e5a)
* Episode 5 - Distributed systems: [https://medium.com/@DaveLumAI/graph-theory-episode-5-distributed-systems-service-graphs-and-the-fine-art-of-not-taking-down-ea5840e7b7a3](https://medium.com/@DaveLumAI/graph-theory-episode-5-distributed-systems-service-graphs-and-the-fine-art-of-not-taking-down-ea5840e7b7a3)

## What is this aspect of graph theory?

Databases are full of relationships, and graph theory is what lets you reason about them without staring at your schema until your soul leaves your body.

At the modeling level, tables, views, foreign keys, joins, indexes, and materialized views all create structure. One thing points to another. One object depends on another. One path through the data is cheaper than another. That is graph territory.

Now, to be fair, an execution plan often shows up as a tree. The database eventually has to pick one concrete plan, so what you see in `EXPLAIN` is usually tree-shaped. But the planner gets there by reasoning over a larger web of possible relationships: join choices, dependency order, access paths, filters, and costs. So the final answer may look like a tidy tree, while the thinking that produced it had much stronger graph energy.

The two big graph ideas here are:

1. **Dependency graphs**
   If `revenue_dashboard` depends on `daily_sales_summary`, and that depends on `orders_clean`, and that depends on raw `orders`, you cannot refresh things in random order and expect the universe to cooperate.

2. **Cost-aware traversal of choices**
   A planner has multiple possible routes through the data. Different join orders and access methods have different costs. The database is not just asking, "Can I do this?" It is asking, "Can I do this without setting fire to the CPU budget?"

So yes, databases may wear a neat shirt and carry a clipboard, but under the surface they are still doing graph-flavored problem solving.

## How do I apply this to actual database problems?

More often than people think.

A few very real examples:

**Refreshing dependent views**
If `revenue_dashboard` depends on `daily_sales_summary`, and that depends on `orders_clean`, and that depends on raw `orders`, there is a correct order and several incorrect orders. The incorrect ones tend to introduce sadness.

**Running ETL pipelines**
In data engineering, jobs often depend on earlier jobs. Parse first. Clean second. Aggregate third. Publish fourth. That is just a dependency graph in a respectable jacket.

**Database migrations**
Adding tables, backfilling data, creating indexes, updating views, and dropping old structures all have ordering constraints. If you do step 7 before step 3, your rollout turns into performance art.

**Query optimization**
When the planner chooses whether to scan a table first, use an index, push down a filter, or join in a different order, it is navigating a structured search space. The final plan is one chosen path through many possibilities.

**Relationship-heavy data**
Foreign keys, self-references, hierarchies, and many-to-many joins all become easier to reason about when you stop thinking "rows" and start thinking "connected things."

That last mental shift matters more than it first appears. Rows are storage. Relationships are behavior.

## What is a FAANG-style interview question on this topic?

A classic version is this:

You are given a list of database views and a list of dependencies between them. Each dependency means one view must be refreshed before another. Return a valid refresh order. If no valid order exists because of a cycle, return an empty list.

That is the database costume.

Underneath, this is a topological sort on a directed graph.

If that phrase sounds dramatic, do not worry. It just means: produce an order where every prerequisite appears before the thing that depends on it.

## How do I solve it?

Use **Kahn's algorithm**, which is one of those rare algorithms that sounds slightly grand and behaves very politely.

The idea:

1. Build a graph where an edge goes from prerequisite to dependent view.
2. Count the indegree of each node, meaning how many prerequisites it still has.
3. Put every node with indegree 0 into a queue. Those are ready right now.
4. Repeatedly remove one ready node, add it to the answer, and reduce the indegree of anything that depended on it.
5. If a dependent node reaches indegree 0, it becomes ready and joins the queue.
6. If you process all nodes, great. If some are left over, you found a cycle.

That cycle is the database equivalent of three people each insisting they can only start once the other two are done.

## How do I optimize that solution?

For the standard interview version, the clean solution is already optimal: adjacency list plus indegree map plus queue.

A few practical upgrades:

* Use an adjacency list, not an adjacency matrix. Real dependency graphs are usually sparse, and a full matrix burns memory like it has a grudge.
* Use `collections.deque` for the queue in Python because popping from the left stays efficient.
* If the interviewer wants a deterministic smallest-first answer when several views are ready at once, replace the queue with a min-heap using `heapq`.
* Normalize input carefully. Interviewers love sneaking in nodes that only appear inside the dependency list.
* In real systems, do not stop at "cycle detected." Surface which objects are involved so the humans can go have the necessary uncomfortable conversation.

## Python solution

```python
from collections import defaultdict, deque

def refresh_order(views, dependencies):
    """
    views: iterable of view names
    dependencies: iterable of (dependent, prerequisite) pairs
                  meaning prerequisite must come before dependent

    returns:
        list of view names in a valid refresh order,
        or [] if no valid order exists
    """
    all_views = set(views)
    for dependent, prerequisite in dependencies:
        all_views.add(dependent)
        all_views.add(prerequisite)

    graph = defaultdict(list)
    indegree = {view: 0 for view in all_views}

    for dependent, prerequisite in dependencies:
        graph[prerequisite].append(dependent)
        indegree[dependent] += 1

    ready = deque(sorted(view for view, degree in indegree.items() if degree == 0))
    order = []

    while ready:
        current = ready.popleft()
        order.append(current)

        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                ready.append(neighbor)

    return order if len(order) == len(all_views) else []
```

## How would I manually test it?

I would test it like I test most things that can embarrass me later: with small cases that each prove one specific point.

**Test 1: Simple chain**
Views: `orders_raw`, `orders_clean`, `daily_sales`, `revenue_dashboard`
Dependencies:

* `orders_clean` depends on `orders_raw`
* `daily_sales` depends on `orders_clean`
* `revenue_dashboard` depends on `daily_sales`

Expected result: one obvious order from raw to dashboard.

**Test 2: Multiple valid answers**
Views: `customers_dim`, `products_dim`, `orders_fact`
Dependencies:

* `orders_fact` depends on `customers_dim`
* `orders_fact` depends on `products_dim`

Expected result: both dimension tables appear before `orders_fact`, but the two dimension tables can swap places.

**Test 3: Disconnected graph**
Views: `billing_rollup`, `inventory_rollup`, `email_metrics`
Dependencies: none

Expected result: all three appear, in any order.

**Test 4: Diamond shape**
Views: `raw_orders`, `clean_orders`, `refunds_clean`, `net_revenue`
Dependencies:

* `clean_orders` depends on `raw_orders`
* `refunds_clean` depends on `raw_orders`
* `net_revenue` depends on `clean_orders`
* `net_revenue` depends on `refunds_clean`

Expected result: `raw_orders` first, `net_revenue` last.

**Test 5: Cycle**
Views: `a`, `b`, `c`
Dependencies:

* `a` depends on `b`
* `b` depends on `c`
* `c` depends on `a`

Expected result: empty list.

**Test 6: Hidden nodes**
Give a dependency that mentions a view not listed in the original `views` input.

Expected result: the function still includes it safely, because production systems love surprise guests.

## What is the time and space complexity?

Let:

* `V` = number of views
* `E` = number of dependencies

Then:

* **Time:** `O(V + E)`
* **Space:** `O(V + E)`

Why?

Building the graph touches each dependency once. Initializing indegrees touches each view once. The queue processing visits each node once, and across the full run each edge gets considered once when we reduce indegrees.

Nothing mysterious is hiding here. If your graph doubles in nodes and edges, your work grows proportionally.

If you switch to a min-heap for deterministic ordering, the runtime becomes roughly `O((V + E) + V log V)` in the interview-sized version, because queue operations are no longer plain constant-time pops.

## How did I come up with that solution?

I start by translating the English into graph language.

"Must happen before" means a directed edge.
"Return a valid order" means topological sort.
"Detect impossible cases" means cycle detection.

Once the problem says all three of those things, the shortlist gets very small very quickly.

Then I ask one practical question: what makes something ready?

Answer: it has no unmet prerequisites.

That answer becomes the indegree count.

And once you have a way to identify "ready now," the queue basically writes itself. From there the algorithm is just bookkeeping with better branding.

## How common is this in FAANG interviews?

Very common as a pattern.

The exact database costume may vary, but the underlying problem shows up constantly as:

* course scheduling
* build order
* package installation
* job execution order
* alien dictionary
* dependency resolution
* view refresh order

So the database-flavored wording is only one skin for a very standard graph question. Interviewers like it because it tests modeling, not just memorization. You have to notice that the problem is a DAG problem before the coding gets easy.

## Any other interesting tidbits?

A few:

* Query planners often expose their final choice as a plan tree, but that should not fool you into thinking the search was simple. The planner compared alternatives and chose a path with estimated cost.
* In PostgreSQL, `EXPLAIN` lets you inspect that chosen plan, which is one of the most useful reality checks in software. It is hard to stay attached to a bad assumption when the database prints its reasoning in public.
* Topological sorts are usually **not unique**. If two things are ready at the same time, multiple answers can be valid.
* Cycles in dependency graphs are not just algorithm failures. They are often design smells wearing fake glasses.

If this made database planning feel a little less like sorcery and a little more like structured decision-making, tell me in the comments. And if you have ever written a query that somehow turned one coffee break into a medieval season change, I would love to hear that too.

Follow along for the next stop in the series. Graph theory keeps hiding in ordinary systems, and frankly it is getting a little too good at it.

## References

* Python `deque`: [https://docs.python.org/3/library/collections.html#collections.deque](https://docs.python.org/3/library/collections.html#collections.deque)
* Python `heapq`: [https://docs.python.org/3/library/heapq.html](https://docs.python.org/3/library/heapq.html)
* PostgreSQL `EXPLAIN`: [https://www.postgresql.org/docs/current/using-explain.html](https://www.postgresql.org/docs/current/using-explain.html)
* NetworkX topological sort: [https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.dag.topological_sort.html](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.dag.topological_sort.html)

[Art Prompt (Ancient Art):](https://lumaiere.com/?gallery=ancient) A taut, elegant scene rendered in the look of a finely painted ancient vessel, with burnished terracotta tones, deep glossy black figures, and exquisitely incised contour lines that feel both severe and alive. Two poised figures lean toward a tiny central game board with concentrated stillness, while long spears rise like vertical accents and patterned borders lock the composition into disciplined symmetry. The surface should feel smooth, mineral, and timeworn, with restrained ornament, profile faces, sharp silhouettes, and a quiet psychological tension. Keep the image balanced, ceremonial, and strangely intimate, with a mood that feels intelligent, competitive, formal, and hushed.

[Video Prompt:](https://www.tiktok.com/@davelumai/video/7625441503090969887) Begin with a close drifting pass across a curved terracotta surface under warm museum light, then let the black-figure forms subtly awaken. Fine incised lines shimmer into visibility, the two figures lean forward by a fraction, fingers hover over the tiny game board, and the long spears tilt with rhythmic precision. Add slow rotational movement as if the vessel itself is turning in space, with crisp shadow play, glints on polished glaze, and delicate dust motes crossing the frame. Use measured, hypnotic motion, sharp profile silhouettes, and elegant pauses so the whole scene feels ancient, tense, and unexpectedly alive.

Songs to Pair With the Video:

* Petrichor - Ben Lukas Boysen
* Portal One - Floating Points
