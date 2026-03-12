# Episode 7: Recursion and Problem Decomposition, or How to Solve a Problem by Making It Smaller Until It Stops Arguing

By the time you get here, the CS 101 training montage is already doing its job.

You have met [Episode 1 - What Is CS 101?](https://medium.com/@DaveLumAI/back-to-basics-cs-101-explained-like-youre-holding-the-syllabus-upside-down-554961c6e0b8), survived [Episode 2 - Programming Fundamentals Part 1: Variables and Conditionals](https://medium.com/@DaveLumAI/programming-fundamentals-part-1-variables-and-conditionals-aka-teaching-a-computer-to-stop-2d94ab24b91a), learned to stop copy-pasting your soul away in [Episode 3 - Programming Fundamentals Part 2: Loops and Functions](https://medium.com/@DaveLumAI/episode-3-loops-and-functions-or-how-to-stop-copy-pasting-yourself-into-madness-fac07f2d1bc4), started thinking in steps with [Episode 4 - Algorithmic Thinking](https://medium.com/@DaveLumAI/algorithmic-thinking-the-superpower-you-already-use-you-just-dont-call-it-that-e7242fa13527), organized your digital chaos in [Episode 5 - Data Structures](https://medium.com/@DaveLumAI/episode-5-data-structures-putting-things-somewhere-so-you-can-find-them-again-51483812ac35), and developed the thousand-yard stare of someone who has already read [Episode 6 - History, Debugging, and Problem Solving](https://medium.com/@DaveLumAI/efe6db927fd3).

So naturally, the next move is recursion.

Because apparently learning to solve a problem once was not enough. Now we are going to solve it by having the solution ask a slightly smaller version of itself for help.

This sounds ridiculous at first.

Then it becomes elegant.

Then, if you are not careful, it becomes a [stack overflow](https://chatgpt.com/s/t_69b2c2076ea88191a7c7afb5238d33bc) wearing a fake mustache.

## What recursion actually is

Recursion is when a function solves a problem by calling itself on a smaller version of that problem.

That is the whole trick.

Not magic. Not wizardry. Not a secret club for people who own mechanical keyboards and use the phrase elegant solution like it is a personal virtue.

Just this:

1. Break the problem into a smaller version of itself.
2. Keep doing that.
3. Stop at a simple case you already know how to solve.

That stopping point is the **base case**.

Without a base case, recursion is less a programming technique and more a controlled fall down the stairs.

## Why this matters

A lot of problems are naturally recursive whether you notice it or not.

Folders contain folders.

Menus contain submenus.

Comments contain replies.

Trees contain branches, and branches contain smaller branches, and before long nature is out here doing recursion without even filing a ticket.

Recursion is useful because some problems are easier to describe in layers than in a giant flat pile of steps. When a structure contains smaller versions of itself, recursion often fits the shape of the problem like a key fits a lock, or at least like a key fits a lock more reliably than your first three attempts.

## The basic shape

Here is the classic mental template:

```python
def solve(problem):
    if problem is simple enough:
        return simple_answer

    smaller_problem = make_it_smaller(problem)
    smaller_answer = solve(smaller_problem)
    return build_the_final_answer(smaller_answer)
```

That is recursion in a trench coat.

The hard part is not the syntax. The hard part is deciding two things clearly:

* What counts as small enough to stop?
* How exactly does each step make real progress toward that stop?

If either of those is fuzzy, the computer will cheerfully recurse until it falls through the floor.

## A tiny example that does not immediately ruin your afternoon

Let us say you want to compute a factorial.

Factorial is one of those math ideas that sounds dramatic but is really just multiplication with commitment.

5! means:

5 x 4 x 3 x 2 x 1

Recursively, that becomes:

5! = 5 x 4!
4! = 4 x 3!
3! = 3 x 2!
2! = 2 x 1!
1! = 1

So the code looks like this:

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

That is the friendly version.

The less friendly version is forgetting the base case and discovering a new error message at high speed.

## Base case vs infinite sadness

This is the part beginners need tattooed on the inside of their eyelids.

A recursive function must move toward a base case.

Not vaguely.

Not emotionally.

Actually.

If you keep calling yourself with the same problem, or a bigger one, or a smaller one that somehow never reaches the stop condition, you do not have recursion. You have a loop with extra paperwork.

This is why recursion has such a dramatic reputation. When it goes right, it feels crisp and clean. When it goes wrong, it goes wrong repeatedly, enthusiastically, and faster than your confidence can reload.

## Is it still relevant?

Yes. Very.

Recursion is still all over real software, just not always in the flashy look-I-am-being-clever way people imagine.

It shows up in:

* tree traversal
* graph search
* parsing
* divide-and-conquer algorithms
* file systems
* menus and UI hierarchies
* compilers
* interpreters
* backtracking problems
* functional programming

A lot of modern systems still work with nested structures, and nested structures are basically recursion bait.

The trick is that professional code often uses recursion selectively. Engineers do not usually ask, How can I make this more recursive? They ask, What is the clearest and safest way to express this problem without Future Me filing a complaint?

That is a much healthier question.

## What recursion is used for

Recursion is especially good when the problem has one of these personalities:

**Self-similar structure**
A tree node has child nodes, each of which is also a tree node.

**Divide and conquer**
Split the problem in half, solve both halves, combine the result.

**Search and backtracking**
Try a path, see if it works, back up if it does not.

**Nested data**
JSON, folders, comments, syntax trees, component trees, and anything else that keeps hiding little boxes inside bigger boxes.

If you have ever opened a folder, then a folder inside that folder, then another folder, then paused to wonder who created this labyrinth, congratulations: you already understand the shape recursion likes.

## A practical example: counting files in nested folders

Imagine you want to count every file in a directory, including all subdirectories.

You can write that as:

* count the files in this folder
* for every subfolder, count its files too
* add everything together

That is recursion wearing a hard hat.

You can also do this iteratively with a stack or queue. Both are valid. The recursive version often matches the way your brain already describes the problem.

That is one reason recursion survives. It often reads like the idea itself.

## Pros and cons

The pros first, because recursion deserves some compliments before we roast it.

**Strengths**

* It can make complicated problems feel smaller and more organized.
* It mirrors tree-shaped and nested data naturally.
* Some algorithms become dramatically clearer with it.
* It can reduce ugly bookkeeping in code.

Now the part where we stop pretending it is always adorable.

**Weaknesses**

* It can be harder for beginners to trace mentally.
* It may use more stack space.
* Bad base cases create spectacular failure.
* In some languages, deep recursion can hit system limits quickly.
* Sometimes a loop is simply clearer and less dramatic.

So yes, recursion is powerful.

No, it is not automatically better.

Sometimes recursion is elegance.

Sometimes recursion is showing off in public.

The difference is whether it makes the code easier to understand.

## Recursion vs loops

This is the question that always shows up five minutes after the first recursive example.

If loops can repeat, why not just use loops?

Fair.

Loops are often better when:

* the repetition is straightforward
* the state is simple
* you want predictable memory behavior
* you do not need the structure of the problem to call itself

Recursion is often better when:

* the problem is naturally hierarchical
* the steps are defined in terms of smaller copies of the same task
* the recursive version is much easier to read than the iterative one

In other words, loops are great for doing the same kind of thing again and again.

Recursion is great when the problem itself is built out of smaller versions of itself.

Neither is morally superior. This is not a custody battle.

## What is the history here?

The idea behind recursion is older than programming languages. Mathematics and logic were using self-referential and recursively defined ideas long before anyone started arguing about semicolons.

In computer science, recursion became especially famous through early functional thinking and languages like Lisp, where recursive definitions became a very natural way to describe computation.

So who invented it?

Not one single programmer in a garage.

This is one of those ideas that grew out of mathematics, logic, and early computer science together. Programming just gave it a stage and better error messages.

## Is it similar to anything else?

Yes.

Recursion is closely related to:

* loops, because both repeat work
* stacks, because recursive calls are tracked on the call stack
* divide-and-conquer algorithms, because they break problems into smaller pieces
* tree traversal, because trees practically beg for recursive code
* dynamic programming, which sometimes starts from a recursive idea and then becomes more efficient by remembering past results

You can think of recursion as one member of a larger family called ways to stop panicking in front of a big problem.

## Does it work well with AI?

Actually, yes.

AI tools are often pretty good at helping with recursive thinking when the problem has a clear base case and a clear shrinking step. They can help sketch recursive traversals, tree walks, parsers, and classic interview-style problems.

Where AI can still make a mess is the same place humans make a mess:

* weak base cases
* accidental infinite recursion
* combining results incorrectly
* using recursion where iteration would be simpler

So recursion works fine with AI, but it still benefits from human supervision, which is a polite way of saying the machine may confidently hand you a beautiful mistake.

## What tech stack does it fit with?

Almost all of them.

Python, JavaScript, Java, C, C++, C#, Go, Rust, functional languages, scripting languages, database query logic, compilers, search systems, graphics, games, and plenty of backend tooling all have places where recursion is useful.

That does not mean every stack loves deep recursion equally. Some languages and runtimes are more comfortable with it than others. Some make iterative solutions easier to optimize. Some will let you recurse with grace. Others will look at your fifteenth nested call and start coughing.

## What tools work well with it?

The best tools are boring, which is usually a good sign.

* a debugger that lets you step through calls
* a call stack view
* tests for edge cases
* print statements, when you are humble enough to use them
* diagrams for trees and nested structures
* patience, which no package manager can install for you

A recursive bug often becomes much easier once you draw the problem as levels instead of trying to hold the whole thing in your head like a cursed grocery list.

## How much is it going to cost you?

In dollars, basically nothing.

In engineering tradeoffs, possibly quite a bit.

Recursion can cost:

* stack space
* readability if overused
* performance if it recomputes work
* debugging time when the stop condition is wrong

So the real cost is not money. It is whether the clarity you gain is worth the complexity you introduce.

That is the adult version of the conversation.

## Is it popular?

This is where recursion gets funny.

As a buzzword, recursion is not exactly headlining stadium tours.

As a concept, it is permanently relevant.

It is taught constantly, used quietly, and rediscovered by every new wave of programmers the moment they meet trees, parsers, nested data, or backtracking. So it is not really going up or down the way trendy tools do. It is more like gravity. Not always discussed at parties, still very much in effect.

Its most dramatic popularity spikes tend to happen in education, interview prep, algorithm study, and functional programming circles, where it has been a favorite for years.

## Is it famous outside programming?

A little.

Recursion has that rare quality of being both useful and a little weird, so artists, writers, filmmakers, and puzzle-makers have all played with recursive ideas.

You see it in images inside images, stories inside stories, loops of self-reference, impossible spaces, and works that fold back into themselves conceptually. It is not a museum wing by itself, but it absolutely has artistic relatives.

Which is honestly on brand. Recursion has always had the energy of an engineering concept that accidentally wandered into philosophy and stayed for snacks.

## Where companies actually use this kind of thinking

Not in the sense of a billboard saying WE USE RECURSION HERE with a mascot pointing at a tree.

But in practice, any company working with nested structures, compilers, search, graphics, route finding, data parsing, dependency analysis, or UI hierarchies runs into recursive patterns constantly.

Browsers, game engines, developer tools, cloud platforms, search engines, design tools, and database systems all brush up against problems that are recursive in shape even if the final implementation is partly iterative under the hood.

So the better question is not Who uses recursion?

It is Who escaped it entirely?

Very few.

## One good beginner instinct

Here is the instinct worth keeping:

When a problem feels huge, ask whether it can be described as the same problem but smaller.

That is the real lesson.

Recursion is not just a coding trick. It is a way of thinking. Break a monster into manageable copies of itself until the monster is no longer in charge.

This works in programming.

It also works on closets, inboxes, and occasionally life.

Use responsibly.

## Final thought before we all recurse into the comments

Recursion matters because it teaches you one of the deepest moves in computer science: a problem does not always need one giant clever leap. Sometimes it needs a clean definition, a smaller version, and a stopping point.

That is a more general superpower than it first appears.

So yes, recursion can be elegant.

Yes, it can be dangerous.

Yes, it can make your code look smarter than you feel while writing it.

And yes, you should learn it anyway.

If this episode helped, explore more experiments and visuals at [LumAIere.com](https://lumaiere.com) and keep an eye on the broader series over at [blog.lumaiere.com](https://blog.lumaiere.com). Follow along, drop a comment, and tell me which recursive example you want next: trees, mazes, folders, or the classic beginner rite of passage where the function keeps calling itself until everybody needs a walk.

**[Art Prompt (Realism):](https://lumaiere.com/?gallery=realism2)** A weather-beaten fishing vessel battling through a steel-blue Atlantic swell near dusk, with towering waves rising in layered walls around the boat, coarse sea spray caught in cold wind, heavy cloud cover pressing low over the horizon, muted sunlight breaking in pale slashes across wet surfaces, the sailors reduced to small determined figures against the vast force of water, meticulous naturalistic detail in the rigging, foam, and soaked clothing, deep slate, green, and silver tones throughout, dramatic realism emphasizing scale, labor, danger, and the solemn grandeur of the sea.

**[Video Prompt:](https://www.tiktok.com/@davelumai/video/7616363602336845087)** A storm-tossed fishing boat surges through massive steel-blue waves as sea spray lashes across the lens and rigging snaps in the wind, quick cinematic push-ins on foam exploding over the bow, sharp cuts to drenched sailors pulling lines, gulls whipping through the gray sky, and pale light breaking through clouds in sudden flashes, with the water heaving in layered motion and every frame carrying the raw force, danger, and grandeur of the open sea.

**Songs to Pair With It:**

* Dayvan Cowboy – Boards of Canada
* Hoppipolla – Sigur Ros

Follow for more, and leave a comment with the recursion example you want to see next.

