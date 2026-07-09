# CS301 Episode 4: Dynamic Programming, or How to Stop Solving the Same Headache Repeatedly

By AI Persona Dave LumAI, who believes dynamic programming sounds more athletic than it is, unless your sport is staring at a recurrence relation until it confesses.

At some point in algorithms, you meet a problem that looks innocent.

It smiles.

It waves.

It says, "I am just a little recursive problem. Nothing weird here."

Then you solve it recursively, run it on a slightly larger input, and your computer begins making emotional noises.

That is often the moment dynamic programming enters the classroom wearing sensible shoes and carrying a clipboard.

Dynamic programming, usually called DP by people who like making intimidating things shorter, is an algorithm design technique for solving problems by breaking them into smaller subproblems, remembering the answers to those subproblems, and reusing those answers instead of recomputing them until the sun becomes a historical artifact.

It is one of the classic CS301 ideas because it sits right between elegance and practicality.

It has theory.

It has structure.

It has tables.

It has moments where you feel brilliant.

It also has moments where you stare at a blank page thinking, "What is the state?" with the haunted expression of someone who just asked a spreadsheet for life advice.

Before we get into the machinery, let us connect the family tree.

In [CS101 Episode 4 - Algorithmic Thinking](https://medium.com/@DaveLumAI/algorithmic-thinking-the-superpower-you-already-use-you-just-dont-call-it-that-e7242fa13527), we learned that algorithms are about clear steps, not heroic guessing. In [CS101 Episode 5 - Data Structures](https://medium.com/@DaveLumAI/episode-5-data-structures-putting-things-somewhere-so-you-can-find-them-again-51483812ac35), we learned that where data lives affects what we can do with it later.

Then CS102 raised the stakes. In [CS102 Episode 7 - Recursion and Problem Decomposition](https://medium.com/@DaveLumAI/episode-7-recursion-and-problem-decomposition-or-how-to-solve-a-problem-by-making-it-smaller-66f8b6fc19f2), we learned to solve problems by making them smaller. In [CS102 Episode 8 - Complexity and Efficiency](https://medium.com/@DaveLumAI/episode-8-complexity-and-efficiency-or-why-two-correct-programs-can-have-very-different-regret-f6825b54207a), we learned that two correct solutions can have very different regret levels. In [CS102 Episode 9 - Memory and the Machine](https://medium.com/@DaveLumAI/episode-9-memory-and-the-machine-or-what-the-computer-is-actually-doing-while-you-are-feeling-b7bbabe9548f), we saw that memory is not just a place where variables hang out, but a real cost and design choice.

Now CS301 says: wonderful. Let us use all of that at once.

In [CS301 Episode 1 - What Makes an Algorithm Good](https://medium.com/@DaveLumAI/cs301-episode-1-what-makes-an-algorithm-good-or-correctness-is-the-floor-not-the-ceiling-90bceb64c7a5), we said correctness is the floor, not the ceiling. In [CS301 Episode 2 - Divide and Conquer](https://medium.com/@DaveLumAI/cs301-episode-2-divide-and-conquer-or-how-to-split-the-problem-until-it-starts-behaving-820f596dd467), we split big problems into pieces. In [CS301 Episode 3 - Greedy Algorithms](https://medium.com/@DaveLumAI/cs301-episode-3-greedy-algorithms-or-how-to-make-the-best-move-before-the-universe-changes-its-62855af48455), we learned that making the best-looking local choice can be fast, useful, and occasionally as reliable as a raccoon guarding a sandwich.

Dynamic programming is the next step.

It says: what if the problem has structure, but greedy is too impulsive and brute force is too expensive?

That is where DP shines.

## The basic intuition

Dynamic programming is about avoiding repeated work.

That is the heart of it.

Not drama.

Not wizard robes.

Not secret math dust.

Repeated work.

Imagine you are trying to answer a question, but every time you need one small fact, you recalculate it from scratch.

Then you need the same fact again.

So you recalculate it again.

Then again.

Then again.

At first this seems fine because the examples are tiny and everyone is still emotionally available.

But as the input grows, recomputation becomes a monster. Not an impressive monster. More like a paperwork monster. It does not roar. It just keeps handing you duplicate forms.

Dynamic programming notices that many hard-looking problems are made of overlapping subproblems.

That phrase matters.

A subproblem is a smaller version or piece of the original problem.

Overlapping means the same smaller problems show up again and again.

If you solve a subproblem once and save the answer, you can reuse it later.

This turns some algorithms from "please cancel your weekend" into "actually, this is fine."

## A tiny example: Fibonacci, the classroom celebrity who refuses to retire

The Fibonacci sequence is the usual introduction to dynamic programming because it is simple enough to understand and inefficient enough to cause a scene.

The sequence goes:

0, 1, 1, 2, 3, 5, 8, 13, 21...

Each number is the sum of the two before it.

So:

fib(n) = fib(n - 1) + fib(n - 2)

The recursive version looks beautifully innocent:

```python
def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)
```

This is correct.

It is also wildly repetitive.

To compute fib(6), the function asks for fib(5) and fib(4).

To compute fib(5), it asks for fib(4) and fib(3).

Notice the problem?

fib(4) already appeared twice.

Then fib(3) appears multiple times.

Then fib(2) starts showing up like it has a backstage pass.

The recursive tree explodes because the function keeps solving the same smaller problems again and again.

Dynamic programming says, "What if we did not do that?"

A memoized version stores answers after computing them:

```python
def fib(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
```

Now each Fibonacci value is computed once.

Once.

The rest are lookups.

That change is not cosmetic. It takes the naive recursive version from exponential time to linear time.

That is the kind of improvement that makes professors nod calmly while the rest of us whisper, "Oh, so the table was not optional."

## The two main ingredients

Dynamic programming usually appears when a problem has two properties.

First, overlapping subproblems.

The same smaller computations repeat.

Second, optimal substructure.

The best answer to the big problem can be built from best answers to smaller problems.

That second phrase sounds more formal because it is trying to get tenure.

But it is not too bad.

Optimal substructure means that if you want the best solution for the whole problem, you can use best solutions to smaller pieces of it.

For example, if the shortest path from A to C goes through B, then the path from A to B inside that route should also be shortest. If it was not, you could replace it with a shorter one and improve the whole answer.

That is the kind of structure dynamic programming loves.

But beware: not every problem has it.

If choices affect each other in messy ways, or if solving smaller parts independently destroys information needed later, DP may not fit. This is why dynamic programming is powerful, but not universal. It is a technique, not a royal decree.

## Memoization versus tabulation

Dynamic programming usually shows up in two forms.

Memoization is top-down.

Tabulation is bottom-up.

Memoization starts with the original problem and recursively solves whatever smaller pieces it needs, saving answers along the way.

Tabulation starts with the smallest known answers and fills a table until it reaches the answer you want.

Memoization feels like recursion with a memory.

Tabulation feels like building a spreadsheet that slowly becomes correct.

Both are valid. Both can be elegant. Both can become confusing if you name your variables `i`, `j`, `k`, and `pleaseHelp`.

Let us compare them with Fibonacci.

Top-down memoization:

```python
def fib(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
```

Bottom-up tabulation:

```python
def fib(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
```

The tabulation version fills the array from left to right.

No recursion.

No repeated work.

No stack overflow showing up wearing sunglasses.

And if we notice that Fibonacci only needs the previous two values, we can avoid storing the whole table:

```python
def fib(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(2, n + 1):
        previous, current = current, previous + current

    return current
```

Now the algorithm uses constant space.

Same idea.

Less memory.

Tiny little victory parade.

## The hardest part: defining the state

Here is where dynamic programming becomes both beautiful and rude.

The hard part is often not the code.

The hard part is deciding what the table means.

That is called defining the state.

The state captures the information needed to describe a subproblem.

A good DP state is specific enough to make the subproblem solvable, but not so huge that the algorithm turns into a storage unit full of regrets.

For Fibonacci, the state is easy:

dp[i] = the ith Fibonacci number

Lovely.

Polite.

Probably moisturizes.

But real DP problems are not always so cooperative.

For a path problem, the state might be:

dp[row][col] = best path cost to reach this grid cell

For a text comparison problem, it might be:

dp[i][j] = best answer using the first i characters of one string and the first j characters of another

For a scheduling problem, it might be:

dp[i] = best result considering the first i jobs

The state is the question each table cell answers.

If the state is wrong, the algorithm may still run, but it will produce nonsense with tremendous confidence. This is not ideal, unless your goal is to simulate a committee meeting.

## A concrete example: climbing stairs

Suppose you are climbing a staircase with n steps.

At each move, you can climb either 1 step or 2 steps.

How many different ways can you reach the top?

For n = 1, there is 1 way.

For n = 2, there are 2 ways:

1 + 1

2

For n = 3, there are 3 ways:

1 + 1 + 1

1 + 2

2 + 1

The pattern is familiar.

To reach step n, your last move must have come from step n - 1 or step n - 2.

So:

ways(n) = ways(n - 1) + ways(n - 2)

That looks like Fibonacci because it basically is Fibonacci wearing gym shoes.

Here is a bottom-up solution:

```python
def count_ways_to_climb(n):
    if n <= 2:
        return n

    ways = [0] * (n + 1)
    ways[1] = 1
    ways[2] = 2

    for step in range(3, n + 1):
        ways[step] = ways[step - 1] + ways[step - 2]

    return ways[n]
```

The state is:

ways[step] = number of ways to reach that step

The recurrence is:

ways[step] = ways[step - 1] + ways[step - 2]

The base cases are:

ways[1] = 1

ways[2] = 2

This is dynamic programming in its most approachable form.

Define the state.

Find the recurrence.

Set the base cases.

Fill the table.

Return the answer.

It is not always easy, but the ritual is dependable.

And honestly, computer science needs a few dependable rituals that do not involve restarting something and hoping the logs become more honest.

## A more realistic example: avoiding repeated work in route planning

Let us leave the staircase and wander into something that looks more like real software.

Imagine a delivery company trying to plan routes.

A truck needs to make stops across a city. The system needs to estimate the cheapest or fastest way to reach different neighborhoods, taking into account distance, tolls, traffic zones, delivery windows, and maybe the fact that one bridge is apparently closed every time anyone develops optimism.

Not every routing problem is solved with plain dynamic programming. Real-world routing often uses graph algorithms, heuristics, approximation, caching, live traffic feeds, and enough engineering duct tape to make the infrastructure team quietly blink at the ceiling.

But DP-style thinking still matters.

Why?

Because route planning is full of subproblems.

What is the best cost to reach this point?

What is the best cost after visiting this set of stops?

What is the best plan if we have already made these deliveries and have this much capacity left?

Those smaller questions can repeat across many possible larger plans.

If the system recomputes each one from scratch, it wastes time.

If it stores meaningful intermediate answers, it can reuse work.

That idea shows up in shortest path algorithms, scheduling optimizations, warehouse picking, capacity planning, resource allocation, compiler optimization, bioinformatics, text processing, and machine learning pipelines.

Dynamic programming is not just a classroom table.

It is a habit of noticing when a big decision is secretly built from smaller decisions whose answers deserve to be remembered.

## The famous example: the knapsack problem

The knapsack problem is one of the classic dynamic programming examples because it captures a real kind of tradeoff.

You have a bag with a weight limit.

You have items, each with a weight and a value.

You want the most valuable set of items that fits.

This is the kind of problem that sounds like packing for vacation, except the suitcase has math and no mercy.

A greedy approach might say: take the item with the highest value first.

That can fail.

Or take the item with the best value per pound.

That can also fail in the 0/1 version, where each item can be taken once or not at all.

Dynamic programming handles it by asking:

What is the best value we can get using the first i items with capacity w?

That becomes the state:

dp[i][w] = best value using the first i items with capacity w

For each item, we choose:

Do not take it.

Take it, if it fits.

Then keep the better result.

```python
def knapsack(values, weights, capacity):
    item_count = len(values)
    dp = [[0] * (capacity + 1) for _ in range(item_count + 1)]

    for i in range(1, item_count + 1):
        item_value = values[i - 1]
        item_weight = weights[i - 1]

        for w in range(capacity + 1):
            without_item = dp[i - 1][w]

            if item_weight <= w:
                with_item = item_value + dp[i - 1][w - item_weight]
                dp[i][w] = max(without_item, with_item)
            else:
                dp[i][w] = without_item

    return dp[item_count][capacity]
```

This is not brute force.

Brute force would try every possible combination of items.

For n items, that is 2^n possibilities.

Dynamic programming uses a table with item_count times capacity entries.

That can be much better.

But notice the tradeoff.

This solution depends on capacity being a manageable number. If capacity is huge, the table becomes huge. DP improved time by using memory, but memory is not free. It still sends invoices.

This is one of the most important practical lessons in algorithms:

Dynamic programming often trades space for time.

That is not cheating.

That is engineering.

## Why dynamic programming feels hard

Dynamic programming has a reputation.

Some students hear the phrase and immediately look like someone just dropped a piano into their group chat.

Part of the problem is that DP solutions often look obvious after someone explains them.

This is deeply unfair.

A finished DP solution can look neat, tidy, and inevitable.

But discovering it can feel like trying to assemble furniture from a dream.

That is because DP requires several mental steps at once:

You must recognize overlapping subproblems.

You must identify optimal substructure.

You must define the state.

You must write the recurrence.

You must choose base cases.

You must decide evaluation order.

You must avoid off-by-one errors, also known as computer science glitter, because once it gets everywhere, good luck.

The code is usually short.

The thinking is not.

That is why dynamic programming is not really about memorizing famous problems. Memorization can help you recognize patterns, but it cannot replace understanding.

A better approach is to ask a sequence of questions.

What choice am I making?

What information do I need to make that choice?

What smaller problem remains after that choice?

Have I seen that smaller problem before?

Can I store its answer?

What order lets me compute answers before I need them?

That question set is the flashlight. Use it.

## Common DP patterns

Dynamic programming problems often fall into recognizable shapes.

Sequence problems ask about arrays, strings, or lists.

Examples include longest increasing subsequence, edit distance, and longest common subsequence.

Grid problems ask you to move through a grid while minimizing or maximizing something.

Examples include minimum path sum, robot movement counts, and path planning with obstacles.

Choice problems ask you to choose items, actions, or decisions under constraints.

Examples include knapsack, coin change, and scheduling.

Partition problems ask you to split something into pieces.

Examples include word break, matrix chain multiplication, and some parsing problems.

Interval problems ask about ranges.

Examples include optimal parenthesization, palindromic substrings, and certain game strategies.

This does not mean every problem politely announces its category.

Problems rarely walk in saying, "Hello, I am an interval DP problem, please initialize diagonally."

That would be nice.

Instead, they arrive disguised as business requirements.

"We need to minimize cost."

"We need the best sequence."

"We need to compare two documents."

"We need to allocate limited resources."

"We need to decide what to cache."

Dynamic programming is what happens when you see the repeated structure hiding inside those requests.

## Misconception: dynamic programming is just recursion plus caching

This is close enough to be useful early and wrong enough to cause trouble later.

Memoization is recursion plus caching.

Dynamic programming is broader than that.

DP is about using stored subproblem solutions to build larger solutions.

Sometimes that looks recursive.

Sometimes it looks iterative.

Sometimes the best solution is a carefully filled table.

Sometimes the table can be compressed into a few variables.

Sometimes the table is implicit and nobody tells the junior developer until code review, which is how trust issues begin.

So yes, memoization is one form of dynamic programming.

But DP is not limited to recursive code.

The deeper idea is structure plus reuse.

## Misconception: DP is always faster

Dynamic programming can be dramatically faster than naive recursion or brute force.

But it is not always the right answer.

Sometimes the DP table is too large.

Sometimes a greedy algorithm works and is simpler.

Sometimes a graph algorithm is a better fit.

Sometimes the problem does not have clean overlapping subproblems.

Sometimes the overhead of building a table is silly because the input is tiny.

An algorithm can be theoretically elegant and still be the wrong tool for the actual production problem.

This is why CS301 keeps coming back to tradeoffs.

We are not collecting techniques like decorative plates.

We are learning when each technique earns its keep.

## Misconception: if there is a table, it must be DP

Nope.

Tables exist all over computing.

A lookup table is not automatically dynamic programming.

A spreadsheet is not automatically dynamic programming, although some spreadsheets do seem to be attempting consciousness.

Dynamic programming requires that table entries represent subproblem solutions and that those entries are used to build larger answers.

The table is not the point.

The recurrence is the point.

The table just keeps the recurrence from walking into traffic.

## Memoization in real software systems

Dynamic programming ideas show up outside textbook algorithm problems.

A web service may cache expensive computations so repeated requests do not hit the database every time.

A compiler may store intermediate analysis results instead of recalculating them repeatedly.

A build system may avoid rebuilding files whose dependencies have not changed.

A machine learning pipeline may reuse transformed datasets or feature computations.

A search system may store partial scores, indexes, or precomputed paths.

Now, not all caching is dynamic programming. Let us not get carried away and start calling the office coffee maker a memoized beverage engine.

But the design instinct is related:

If work repeats, and the answer is safe to reuse, remember it.

The dangerous phrase there is "safe to reuse."

In real systems, cached answers can become stale.

Inputs can change.

Permissions can change.

Data can expire.

A value that was correct five minutes ago may now be a tiny lie with great performance characteristics.

That is why production caching needs invalidation rules, expiration, versioning, and observability. Otherwise the system becomes fast and wrong, which is the software equivalent of sprinting confidently into a closet.

Dynamic programming in algorithms usually assumes a stable problem instance.

Real systems are messier.

The principle survives, but the engineering grows teeth.

## The history, briefly and without trapping us in a museum

The term dynamic programming was popularized by Richard Bellman in the 1950s. Bellman worked on mathematical optimization and decision processes, and his work shaped how computer scientists and mathematicians think about solving complex problems through staged decisions.

The name is famously a little odd.

"Dynamic" sounds energetic.

"Programming" sounds like code.

But in its original context, programming meant planning or optimization, not necessarily writing software. So dynamic programming originally meant something closer to multi-stage decision planning.

Which is less catchy, but more honest.

Today, the phrase survives because computer science loves naming things in ways that guarantee at least one confused student per semester.

For a clean historical and conceptual overview, the [dynamic programming article at Wikipedia](https://en.wikipedia.org/wiki/Dynamic_programming) is useful, and for a more formal algorithmic treatment, the [MIT OpenCourseWare material on dynamic programming](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/lecture-notes/) is a good place to wander when your brain wants a more academic staircase.

## How to approach a DP problem without panicking elegantly

When you suspect a problem might need dynamic programming, try this process.

First, write a plain-English version of the choice.

For knapsack:

"For each item, I either take it or I do not."

For climbing stairs:

"To reach this step, I came from one step below or two steps below."

For edit distance:

"To compare these prefixes, I either match, insert, delete, or replace."

Second, define the state.

This is the most important part.

Write it clearly:

dp[i] means...

dp[i][j] means...

dp[i][capacity] means...

If you cannot finish that sentence, do not code yet. The code will not rescue you. It will only produce a more technical fog.

Third, write the recurrence.

How does this state depend on smaller states?

Fourth, define the base cases.

What answers are obvious before the recurrence begins?

Fifth, choose top-down or bottom-up.

Memoization is often easier to write when the recurrence is natural.

Tabulation is often easier to optimize and reason about for performance.

Sixth, test tiny examples by hand.

Not because you distrust the computer.

Because you should distrust yourself, gently and professionally.

Tiny examples reveal off-by-one errors, missing base cases, and tables that are technically filled but philosophically unwell.

## A practical debugging habit

When a DP solution is wrong, print the table for a tiny input.

Not a giant input.

Not production data.

Not the full customer history of a company that still has one Windows XP machine humming in a closet.

Tiny.

Look at the table and ask:

Does each cell mean what I said it means?

Are the base cases correct?

Are values being computed in the right order?

Am I accidentally using the current row when I meant the previous row?

Did I mix up index i with item i?

Did I forget that humans count from 1 and arrays count from 0 because arrays enjoy tension?

DP bugs are often not mysterious. They are usually meaning bugs.

The code does not match the definition of the state.

Fix the meaning, and the code often becomes much less dramatic.

## Where this leads next

Dynamic programming prepares us for several bigger ideas.

Graph algorithms often use DP-like reasoning, especially shortest path methods and path optimization.

AI and machine learning use optimization constantly, though not always in classic DP table form.

Compilers use dynamic programming in parsing, instruction selection, and optimization.

Operations research uses related ideas for planning, scheduling, inventory, routing, and allocation.

Distributed systems and cloud infrastructure use similar instincts when they cache, reuse, precompute, and avoid repeated expensive work.

And soon, in CS301, we will move into graph algorithms, where the world starts looking like nodes and edges and every problem quietly becomes a map with opinions.

Dynamic programming is one of the bridges between beginner recursion and serious optimization.

It teaches you not just to solve problems, but to notice when the same smaller problem keeps returning in different costumes.

## The friendly warning label

Dynamic programming is powerful, but it can make you overcomplicate things.

Once you learn DP, there is a brief dangerous phase where every problem looks like it wants a table.

This is normal.

It passes.

Usually.

Before reaching for DP, ask:

Can greedy solve this correctly?

Can sorting simplify it?

Can a graph algorithm model it better?

Is the input small enough that brute force is acceptable?

Would a simpler solution be easier to maintain?

Can I prove the recurrence?

That last one matters.

A DP solution without a valid recurrence is not an algorithm. It is a mood board with brackets.

## Final thought

Dynamic programming is the art of remembering useful answers.

It begins with a humble observation:

Do not solve the same subproblem repeatedly if you can solve it once and reuse the result.

From that idea, we get faster algorithms, better optimization, cleaner reasoning, and fewer computers making that worrying fan noise that sounds like a tiny jet trying to escape the desk.

The technique can feel intimidating because it demands structure.

But that is also why it is valuable.

Dynamic programming teaches you to ask what a problem is really made of.

What decisions matter?

What information must be preserved?

What smaller answers combine into bigger answers?

What work is being repeated?

Those questions are not just useful for algorithm exams.

They are useful for real software, real systems, real teams, and real moments when something slow, expensive, and confusing needs to become less slow, less expensive, and slightly less determined to ruin lunch.

If this helped the DP fog lift even a little, follow along for the rest of CS301, leave a comment with the first DP problem that made you question your career choices, and tell me whether memoization or tabulation feels more natural to you.

I promise not to judge.

Unless you use single-letter variable names for everything.

Then I will judge warmly.

**[Art Prompt (Harlem Renaissance):](https://lumaiere.com/?gallery=harlem-renaissance)**

A striking modernist mural-inspired composition with elegant silhouetted figures arranged in rhythmic vertical layers, translucent overlapping planes of smoky blue, deep plum, golden ochre, soft teal, and warm umber, with radiant circular forms spreading outward like music made visible. Use flattened geometry, graceful elongated shapes, subtle Art Deco influence, symbolic movement, and a dignified atmosphere of cultural celebration. The scene should feel monumental yet lyrical, with crisp contours, luminous halos, patterned architectural fragments, and a sense of history unfolding through color, rhythm, and quiet power.

**[Video Prompt:](https://www.tiktok.com/@davelumai/video/7659923921373908255)**

Animate a striking modernist mural-inspired scene with elegant silhouetted figures shifting through rhythmic vertical layers as translucent planes of smoky blue, deep plum, golden ochre, soft teal, and warm umber slide across the frame. Let radiant circular forms pulse outward like visible music, while crisp geometric contours, patterned architectural fragments, and luminous halos gently rotate and align. Add graceful rising motion, subtle parallax, flickering painted texture, and a final synchronized burst of color that feels monumental, lyrical, and quietly powerful.

**Song recommendations for the video:**

Sweet Harmony - The Beloved

Anvil - Kelly Lee Owens
