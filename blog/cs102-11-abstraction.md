# Episode 11: Modular Design and Abstraction, or How to Make Your Code Less Like a Junk Drawer

By the time you arrive here, you have already wandered through CS 101 with [Episode 1 - What Is CS 101?](https://medium.com/@DaveLumAI/back-to-basics-cs-101-explained-like-youre-holding-the-syllabus-upside-down-554961c6e0b8), [Episode 2 - Programming Fundamentals Part 1: Variables and Conditionals](https://medium.com/@DaveLumAI/programming-fundamentals-part-1-variables-and-conditionals-aka-teaching-a-computer-to-stop-2d94ab24b91a), [Episode 3 - Programming Fundamentals Part 2: Loops and Functions](https://medium.com/@DaveLumAI/episode-3-loops-and-functions-or-how-to-stop-copy-pasting-yourself-into-madness-fac07f2d1bc4), [Episode 4 - Algorithmic Thinking](https://medium.com/@DaveLumAI/algorithmic-thinking-the-superpower-you-already-use-you-just-dont-call-it-that-e7242fa13527), [Episode 5 - Data Structures](https://medium.com/@DaveLumAI/episode-5-data-structures-putting-things-somewhere-so-you-can-find-them-again-51483812ac35), and [Episode 6 - History, Debugging, and Problem Solving](https://medium.com/@DaveLumAI/efe6db927fd3).

Then CS 102 showed up and politely informed you that writing code is not the same thing as building software that survives contact with reality, so the path continued through [Episode 7 - Recursion and Problem Decomposition](https://medium.com/@DaveLumAI/episode-7-recursion-and-problem-decomposition-or-how-to-solve-a-problem-by-making-it-smaller-66f8b6fc19f2), [Episode 8 - Complexity and Efficiency](https://medium.com/@DaveLumAI/episode-8-complexity-and-efficiency-or-why-two-correct-programs-can-have-very-different-regret-f6825b54207a), [Episode 9 - Memory and the Machine](https://medium.com/@DaveLumAI/episode-9-memory-and-the-machine-or-what-the-computer-is-actually-doing-while-you-are-feeling-b7bbabe9548f), and [Episode 10 - Files, Input, and Output](https://medium.com/@DaveLumAI/episode-10-files-input-and-output-or-how-programs-stop-living-entirely-inside-their-own-heads-941dc13d407d).

Now we reach one of the great turning points in programming.

Not the part where you learn a flashy new keyword.

Not the part where a framework arrives wearing sunglasses and pretending it invented organization.

I mean the moment when you realize that a working program can still be structured like a garage full of unlabeled extension cords.

That is Episode 11.

This is modular design and abstraction.

Or, in plain English, this is how you stop making every part of your program know everybody else’s business.

## What is modular design?

Modular design is the idea that software should be split into smaller, focused parts, with each part handling a clear job.

One module deals with users.

Another deals with billing.

Another deals with files.

Another deals with talking to a database.

Another exists because past-you made a bold decision at 2:14 a.m. and present-you is now cleaning it up with the emotional posture of a janitor after a parade.

The point is not just to cut code into pieces for decoration.

The point is to separate responsibilities so the whole system is easier to understand, test, change, and trust.

A module is not magic.

It is just a boundary.

A place where you say, "This part handles this job, and the rest of the program should interact with it in a controlled way instead of rummaging through its internal organs."

That boundary matters more than beginners usually expect.

Because once a program gets past toy size, the hardest part is no longer writing individual lines.

It is managing relationships between parts.

## What is abstraction?

Abstraction is controlled ignorance.

That is not an insult. It is a survival strategy.

Abstraction means you hide unnecessary details so other parts of the program can use something without having to understand every moving piece inside it.

When you call a function like `save_user(user)` you usually do not want to know whether it writes to one table, three tables, a queue, a log, a cache, or a tiny goblin in a server room with a clipboard.

You want to know what it does, not how every screw is tightened.

That is abstraction.

It gives you a clean surface to work with.

It lets you think at the right level.

Without abstraction, every change drags the whole codebase into the room like a family argument at Thanksgiving.

With abstraction, parts can cooperate without turning into one giant nervous blob.

## Is this still relevant?

Absurdly relevant.

In fact, modular design has become more relevant, not less.

Modern software is larger, more integrated, more team-based, more API-driven, more distributed, and more likely to involve several layers of code all pretending to be simple while secretly negotiating with databases, cloud services, auth providers, queues, caches, and whatever "modern observability" is charging by the month.

So yes, it is still relevant.

Wildly.

Even when people move from monoliths to services, from services to packages, from packages to components, from components to plugins, or from "careful engineering" to "we asked AI to scaffold it and now we are all learning something," the same question remains:

Can each part of this system do one clear job without requiring a blood oath from the rest of the codebase?

That is modular design.

The wardrobe changes. The principle does not.

## Where did this idea come from?

The urge to break systems into understandable parts is older than most current buzzwords and probably healthier than all of them.

As software grew in the 1960s and 1970s, people discovered that the real danger was not only bad code. It was tangled code. The kind where changing one thing causes six unrelated things to burst into flames out of professional spite.

So software engineering started emphasizing decomposition, information hiding, interfaces, separation of concerns, and structured design.

That is why people like to talk about modularity as if it were a grand intellectual discovery.

And to be fair, it was.

Not because "small pieces" is a shocking thought.

Because getting teams, systems, and future maintainers to agree on where the boundaries belong is one of the central problems of software design.

## Who invented it?

No single person gets to walk away with the entire trophy.

A lot of the important groundwork came from classic software engineering thinkers, especially people who pushed structured programming, modular programming, information hiding, and interface-based design.

If you want the short version, modular thinking came out of the realization that software complexity had to be managed intentionally or it would manage you instead.

Which, to be honest, remains one of the most reusable lessons in the whole field.

## What is it used for?

Everything serious.

Web apps.

Desktop apps.

Mobile apps.

Games.

Operating systems.

Libraries.

Compilers.

AI pipelines.

Data tools.

Payment systems.

Internal business software.

Build systems.

Developer tools.

Anything large enough that another human might have to read it later.

Which is to say: almost all real software.

A tiny one-file script can get away with being one-file script chaos.

A real system usually cannot.

Once multiple features, multiple people, or multiple months enter the picture, modular design stops being a style preference and starts being a coping mechanism.

## What are the strengths?

The good news first.

Modular design makes code easier to understand because each piece has a smaller mental footprint.

It makes systems easier to change because you can often update one area without performing emergency surgery on the whole application.

It makes testing easier because smaller, more focused parts are easier to isolate.

It makes teamwork easier because multiple people can work in parallel without stepping on the same rake every five minutes.

It improves reuse because a well-defined piece can often serve more than one part of the system.

It also helps debugging because when responsibilities are clear, you have fewer places to look when something goes wrong.

That last one is huge.

There is a special kind of despair reserved for bugs in code where everything talks to everything.

## What are the weaknesses?

Now the fair part.

Modular design is not free.

You can overdo it.

You can create so many layers, wrappers, adapters, factories, managers, controllers, orchestrators, helpers, registries, coordinators, and spiritual consultants that the code becomes a bureaucratic theme park.

Too much abstraction can make simple tasks harder to trace.

Too many modules can make the project feel scattered.

Bad boundaries can be worse than fewer boundaries because now the complexity has paperwork.

And sometimes beginners hear "modular" and decide every six lines of code deserve their own file like a tiny kingdom with diplomatic immunity.

That is not always better.

A healthy module reduces cognitive load.

An unhealthy one turns "find the bug" into a guided tour through twelve folders and an existential crisis.

## Pros and cons in one honest breath

The pro is that modular design helps software stay understandable as it grows.

The con is that it requires judgment.

And judgment is annoying because you cannot install it from a package manager.

There is no universal rule that says, "At 43 lines, separate this into a module, but at 39 lines, leave it alone."

You have to ask:

Does this part have one job?

Does it deserve its own boundary?

Will this separation make the code easier to read and change, or am I just rearranging the furniture while the house is on fire?

That is the real craft.

## How is it similar to other ideas?

It overlaps with separation of concerns, encapsulation, information hiding, component design, layered architecture, and in many cases object-oriented design.

It also gets along very well with procedural design and functional design.

Which is worth saying clearly, because modularity is not owned by one programming religion.

You can have modular procedural code.

You can have modular object-oriented code.

You can have modular functional code.

You can also have a complete mess in any of those styles.

The paradigm does not save you by itself.

The boundary work does.

## Is it the same thing as object-oriented programming?

No.

Related, yes.

Identical, no.

Object-oriented programming is one way people often organize code around objects and behavior.

Modular design is the broader idea of separating a system into coherent parts.

You can use classes to help do that.

You can also use plain functions, packages, namespaces, modules, services, components, or carefully designed APIs.

This is important because a lot of people were taught to treat "put it in a class" as the same thing as "designed it well."

Those are not the same sentence.

A class can help.

A class can also be a decorative filing cabinet full of confusion.

## What are the alternatives?

The honest alternative is not "anti-modular design."

It is just different ways of drawing the lines.

You might lean more procedural, where behavior is organized around functions and data flows.

You might lean more functional, where immutable data and transformations reduce hidden side effects.

You might use event-driven design, plugin systems, pipelines, layered architecture, or service-oriented patterns.

At larger scales, people argue about monoliths versus microservices as though one of them personally insulted their grandparents.

But even there, modularity still matters.

A modular monolith can be excellent.

A badly designed set of microservices can be a distributed parade of regret.

So the real alternative is not whether to have boundaries.

It is where to place them, how strict to make them, and whether you are solving an actual problem or simply buying more diagrams.

## Is it popular?

Yes, in the least dramatic way possible.

Modular design is not trendy in the way that people print it on conference banners and pretend it arrived yesterday.

It is foundational.

That means it is less a fad and more a permanent expectation.

Its popularity is not going down.

If anything, the pressure to write modular systems keeps increasing because software teams are juggling more complexity, more integrations, and more generated code than ever.

If one related thing has cooled a bit, it is blind enthusiasm for splitting everything into tiny networked services just because it sounds enterprise-shaped.

But the underlying desire for clear boundaries, maintainable structure, and local reasoning has not faded at all.

That is still rising.

Because the pain it solves is still rising.

## When was it most popular?

In a sense, right now.

Not because people suddenly discovered it, but because large software systems keep making the same lesson unavoidable.

You can ignore modular design for a while.

Then the codebase gets older, the team gets larger, the features get messier, and modularity comes back into the room carrying a folding chair.

## What companies use it most?

Pretty much all serious software companies.

Banks use it.

Cloud platforms use it.

SaaS companies use it.

Game studios use it.

Retail platforms use it.

AI companies use it.

Operating system teams use it.

Even companies with famously chaotic products are usually trying, somewhere deep inside the repository, to keep responsibilities separated enough that Tuesday's fix does not destroy Friday's revenue.

Nobody scales real software by having every file know everything.

Not for long, anyway.

## Does it work well with AI?

Yes, and this is one of the more interesting modern twists.

AI-assisted coding works much better when the codebase has clear module boundaries, predictable interfaces, explicit responsibilities, and tests that can tell you when the machine has confidently invented nonsense.

If the architecture is clear, AI can be genuinely helpful at filling in parts, refactoring isolated areas, writing tests, generating adapters, or scaffolding features.

If the architecture is mush, AI often becomes a very fast confusion amplifier.

So modular design pairs well with AI not because AI replaces design, but because good design gives AI fewer places to be disastrously creative.

Which, frankly, we should all appreciate.

## What tech stack does it work with?

Almost all of them.

Python, JavaScript, TypeScript, Java, C#, Go, Rust, C++, PHP, Kotlin, Swift, Ruby, and anything else that permits more than one file and at least one opinion.

It works in frontend apps.

It works in backend systems.

It works in libraries.

It works in services.

It works in monoliths.

It works in distributed systems.

The exact mechanisms change. The principle does not.

One language gives you packages.

Another gives you namespaces.

Another gives you modules.

Another gives you crates.

Another gives you a stern lecture and a folder structure.

Fine.

The idea survives all of that.

## What tools help the most?

Testing tools help because boundaries become meaningful when you can verify them.

Linters help because consistent structure reduces accidental chaos.

Type systems help because interfaces are easier to trust when they are explicit.

Package managers and dependency tooling help because modules eventually need civilized ways to talk to one another.

Architecture diagrams help if they remain accurate longer than a banana on a dashboard.

And yes, editors and AI coding tools can help a lot, especially when the project already has sane boundaries.

The tools do not create modularity for you.

But they reward it.

## What does it cost?

At small scale, mostly design time and thought.

At larger scale, also coordination.

You spend time deciding boundaries, naming interfaces, documenting assumptions, testing contracts, and resisting the temptation to let one convenient shortcut quietly become a structural hostage situation.

That is the cost.

The savings show up later in reduced maintenance pain, easier onboarding, faster debugging, safer changes, and fewer moments where someone says, "I changed a label color and now billing is down."

That sentence should never exist.

And yet.

## A beginner-friendly example

Suppose you are building a tiny online store.

The non-modular version might do this:

One giant file reads products, validates users, calculates totals, applies discounts, charges cards, sends emails, writes logs, and updates inventory.

Technically, that is still "organized" in the sense that all the code is somewhere.

The same way a kitchen drawer full of batteries, birthday candles, rubber bands, mystery keys, and one dead pen is technically storage.

A modular version would split that into clearer pieces:

* a product module
* an order module
* a payment module
* an inventory module
* a notification module

Now each part has a clearer job.

The order module does not need to know how email formatting works.

The payment module does not need to know how inventory is stored.

The notification module does not need to know how tax was calculated.

They cooperate through defined interfaces instead of crowding into each other's rooms and touching everything.

That is the difference.

Not elegance for its own sake.

Containment.

## A tiny code example

Here is the broad idea in simple Python.

```python
# pricing.py
def subtotal(items):
    return sum(item["price"] * item["quantity"] for item in items)


def apply_discount(amount, percent):
    return amount * (1 - percent / 100)
```

```python
# checkout.py
from pricing import subtotal, apply_discount

cart = [
    {"price": 20, "quantity": 2},
    {"price": 15, "quantity": 1},
]

base_total = subtotal(cart)
final_total = apply_discount(base_total, 10)

print(final_total)
```

This is not glamorous.

That is part of why it matters.

`checkout.py` does not need to know how the pricing math is implemented. It just uses the pricing module through a simple interface.

That is abstraction doing useful work without demanding applause.

## So what is the real lesson here?

The real lesson is that software organization is part of software correctness.

A program is not well designed just because it produces the right output today.

It also has to be understandable tomorrow.

Changeable next month.

Debbugable when tired people are staring at it on a Thursday.

And survivable when a new feature arrives with the charming sentence, "This should be a quick tweak."

Modular design is how you give software a fighting chance.

Abstraction is how you keep that chance from collapsing under detail.

Neither one makes code perfect.

But both make it less likely to turn into an archaeological site full of sharp edges and old decisions.

## Final thought before we all go reorganize something

At the beginner stage, writing code feels like learning how to make the computer obey.

At the next stage, you realize obedience was the easy part.

The hard part is building systems that stay legible after they grow.

That is why modular design matters.

It is not academic furniture.

It is the difference between a codebase you can reason about and a codebase that makes every bug feel like a scavenger hunt designed by a bitter wizard.

If this one hit home, follow along for the next episode, and drop a comment telling me which piece of software first taught you that "just put it all in one file" was not, in fact, an architectural philosophy.

**[Art Prompt (Ancient Art):](https://lumaiere.com/?gallery=ancient)** A ceremonial black-figure composition on a grand terracotta vessel, showing two poised warriors bent over a small game board in a moment of eerie calm before violence. The figures should be rendered in glossy obsidian silhouettes against warm clay orange, with fine incised lines carving out curls, armor details, shields, spear shafts, and patterned cloaks. Build the scene with strict symmetry and elegant stillness, framed by bands of geometric ornament, stylized palmettes, and rhythmic border motifs. Let the mood feel solemn, mythic, and intensely focused, as if fate itself has paused to watch. Keep the surface richly tactile, slightly weathered, and museum-lit, with the composition feeling both decorative and monumental despite its restraint.

**[Video Prompt:](https://www.tiktok.com/@davelumai/video/7621739012377660702)** A grand terracotta vessel fills the frame in a museum-dark setting as black-figure warriors, geometric borders, and incised details come alive with sharp rhythmic motion. The camera circles the vessel in quick elegant arcs while bands of ornament pulse, spear lines glide, reflections race across glossy black surfaces, and the painted scene subtly animates as if myth has begun breathing inside fired clay. Add dramatic reveals through spinning transitions, close macro passes over etched armor and patterned cloaks, flickers of torchlike light, drifting dust, and a final striking freeze on the tense game-board moment, making the whole sequence feel ancient, precise, hypnotic, and irresistibly watchable.

A couple songs that would fit that video beautifully: **Neverender - Justice & Tame Impala** and **Staralfur - Sigur Ros**.
