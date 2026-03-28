# Episode 12: Testing and Reliability, or Why "It Worked Once" Is Not a Career Strategy

By the time you get to this part of the series, you have already survived the **CS 101** portion of the climb with [Episode 1: What Is CS 101?](https://medium.com/@DaveLumAI/back-to-basics-cs-101-explained-like-youre-holding-the-syllabus-upside-down-554961c6e0b8), [Episode 2: Programming Fundamentals Part 1: Variables and Conditionals](https://medium.com/@DaveLumAI/programming-fundamentals-part-1-variables-and-conditionals-aka-teaching-a-computer-to-stop-2d94ab24b91a), [Episode 3: Loops and Functions](https://medium.com/@DaveLumAI/episode-3-loops-and-functions-or-how-to-stop-copy-pasting-yourself-into-madness-fac07f2d1bc4), [Episode 4: Algorithmic Thinking](https://medium.com/@DaveLumAI/algorithmic-thinking-the-superpower-you-already-use-you-just-dont-call-it-that-e7242fa13527), [Episode 5: Data Structures](https://medium.com/@DaveLumAI/episode-5-data-structures-putting-things-somewhere-so-you-can-find-them-again-51483812ac35), and [Episode 6: History, Debugging, and Problem Solving](https://medium.com/@DaveLumAI/efe6db927fd3).

Then the **CS 102** stretch started getting a little more real, with [Episode 7: Recursion and Problem Decomposition](https://medium.com/@DaveLumAI/episode-7-recursion-and-problem-decomposition-or-how-to-solve-a-problem-by-making-it-smaller-66f8b6fc19f2), [Episode 8: Complexity and Efficiency](https://medium.com/@DaveLumAI/episode-8-complexity-and-efficiency-or-why-two-correct-programs-can-have-very-different-regret-f6825b54207a), [Episode 9: Memory and the Machine](https://medium.com/@DaveLumAI/episode-9-memory-and-the-machine-or-what-the-computer-is-actually-doing-while-you-are-feeling-b7bbabe9548f), and [Episode 10: Files, Input, and Output](https://medium.com/@DaveLumAI/episode-10-files-input-and-output-or-how-programs-stop-living-entirely-inside-their-own-heads-941dc13d407d). Episode 11 gave us modular design and abstraction, which is where code stops looking like a panicked attic and starts looking like a place other humans might enter without protective gear.

And now we arrive at Episode 12.

Testing.

The discipline of looking at your code and saying, "I love you, but I do not trust you unsupervised."

That is not cynicism. That is engineering.

## What testing actually is

Testing is the process of checking whether your software behaves the way you think it behaves, especially after you have changed it, refactored it, optimized it, or lightly kicked it down the stairs and hoped for the best.

A lot of beginners think testing is about proving that code works.

It is not.

It is about catching the many exciting ways code does **not** work before those ways become your personality.

A test is just a small, focused piece of code that sets up a situation, runs something, and checks the result. That is the whole magic trick. No choir. No thunderbolt. Just a tiny automated skeptic.

And honestly, that skeptic is one of the best friends you will ever have in programming.

## Is testing still relevant?

More than ever.

In the early days, a lot of code was smaller, simpler, more isolated, and often maintained by fewer people. Today, software is glued to databases, APIs, browsers, cloud services, queues, file systems, payment systems, authentication systems, and at least one thing nobody wants to touch because "it somehow works and we should respect its privacy."

Modern software changes constantly.

That means reliability is no longer a luxury item. It is not decorative parsley. It is the plate.

When AI is helping generate code faster, testing becomes even more important, not less. A machine can help you write ten functions before lunch. It can also help you create ten new opportunities for chaos before dessert. Fast code generation without testing is just accelerated confidence.

## A tiny history of testing, because every useful idea had to be invented by someone who got tired of avoidable pain

Early programmers tested mostly by running programs manually and seeing whether the output looked cursed.

Then software grew up, got complicated, and started requiring more discipline than "well, it seemed fine on Gary's laptop."

Over time, automated testing became a core part of sane development. Unit testing gained a real cultural identity when frameworks like xUnit and later JUnit made it easier to express tests clearly and run them often. The broader idea behind all of this was simple: if code matters, checking it should not depend entirely on memory, luck, or one heroic person squinting at logs at 2:14 a.m.

That is why testing stuck.

Not because developers enjoy extra work.

Because they enjoy preventable disasters even less.

## What is testing used for?

Testing is used for several very practical reasons:

* to catch bugs before users do
* to keep old features from breaking when new features arrive
* to make refactoring less terrifying
* to document expected behavior in a machine-checkable way
* to build confidence when deploying changes
* to keep teams from arguing entirely from vibes

A good test suite says, "Here is what this code is supposed to do."

A bad test suite says, "Something failed somewhere. Good luck, detective."

## The main kinds of testing, translated into human language

### Unit tests

Unit tests check one small piece of logic at a time.

Think: one function, one method, one class, one rule.

You give it controlled input and ask whether it returns the right result.

This is where beginners should usually start, because unit tests are small, understandable, and very good at catching the kind of bugs that sneak in when you are certain you are being clever.

Example:

```python
def is_free_shipping(total):
    return total >= 50

def test_free_shipping_threshold():
    assert is_free_shipping(50) is True
    assert is_free_shipping(49.99) is False
```

That is a test.

No orchestra. No smoke machine. Just a tiny truth-serum injection for your logic.

### Integration tests

Integration tests check whether multiple parts work together properly.

Maybe your app saves something to a database.
Maybe it calls an API.
Maybe it reads a file, transforms the data, and sends the result somewhere else.

Unit tests are great for the individual musicians.

Integration tests tell you whether the band can get through one song without fighting.

### End-to-end tests

These simulate the full user journey.

Click the button.
Fill in the form.
Submit the order.
Confirm the result.

They are useful, but they are heavier, slower, and usually more fragile than smaller tests. They are important, but if you rely only on these, you are basically checking the whole house by repeatedly ringing the front doorbell and hoping that tells you something about the plumbing.

## Pros and cons

### What testing is good at

Testing gives you confidence.

It makes change cheaper.

It catches regressions.

It helps teams move faster because people are not forced to re-check every old feature by hand each time somebody changes a comma and wakes the database.

It also acts like living documentation. A good test often explains expected behavior more clearly than a comment that was written three jobs ago by someone named Trent who no longer answers email.

### What testing is bad at

Testing takes time.

Bad tests create false confidence.

Poorly designed tests become brittle and annoying.

Some teams over-test trivia and under-test risk, which is like buying seventeen locks for the shed while leaving the front door wide open.

And testing cannot prove the total absence of bugs. It can only increase your odds of catching the important ones before they start making calendar invitations.

## Strengths and weaknesses

The greatest strength of testing is that it turns software reliability from a feeling into a repeatable process.

The greatest weakness is that people sometimes treat the existence of tests as more important than the quality of tests.

A test suite full of shallow nonsense is just bureaucracy in sneakers.

You do not want tests because tests are fashionable.

You want tests because software is slippery, stateful, interconnected, and deeply capable of humiliating confident people.

## What are edge cases, and why do they keep ruining everyone's afternoon?

An edge case is a situation that sits near the boundary of what your code is expected to handle.

Empty input.

Very large input.

Weird characters.

Zero.

Negative values.

The exact number where one rule becomes another rule.

These are where bugs like to rent beachfront property.

If your code works for the obvious case and collapses the second someone enters an apostrophe, an emoji, or the number 0, your code is not done. It is just wearing a clean shirt.

## A more realistic example

Suppose you are writing code that applies a discount.

You might think:

"Easy. If the total is over 100, subtract 10 percent."

Then life happens.

What about exactly 100?

What about a negative total because of a refund?

What about a value that is a string because a form behaved like a goblin?

What about a currency rounding issue?

Suddenly your cute little pricing rule has become a tiny legal thriller.

That is exactly why testing matters.

```python
def apply_discount(total):
    if total < 0:
        raise ValueError("total cannot be negative")
    if total >= 100:
        return round(total * 0.9, 2)
    return total

def test_discount_rules():
    assert apply_discount(100) == 90.00
    assert apply_discount(80) == 80
```

Then you add more tests for negative values, decimals, and whatever else your future self is about to accidentally break.

## What are the alternatives to testing?

Technically, the alternatives are:

* manual testing
* code reviews
* monitoring in production
* user complaints
* prayer
* luck
* pretending not to see the error report

To be fair, some of those help.

Manual testing is useful.
Code reviews are valuable.
Monitoring is essential.

But none of them replace testing.

Manual testing is slow and inconsistent.

Code reviews are excellent at catching bad ideas, but not every broken condition.

Monitoring tells you something went wrong after reality has already started throwing chairs.

Testing is the thing that quietly checks the floorboards before the guests arrive.

## Does testing work well with AI?

Yes, incredibly well, if you stay awake.

AI is good at helping generate test cases, boilerplate, edge-case ideas, and even starter test files. It can help you think through scenarios you forgot, especially when you ask it to be adversarial instead of flattering.

But AI also loves confidence.

It will happily generate tests that look official while checking almost nothing.

So the winning combination is this:

* use AI to brainstorm tests faster
* use human judgment to decide what actually matters
* test the behavior, not the fantasy
* make sure the tests fail when the code is wrong

That last point matters more than people think. A test that never meaningfully fails is just a decorative coaster.

## What tech stack does testing belong to?

Basically all of them.

Python has `pytest` and `unittest`.

JavaScript and TypeScript live happily with Jest, Vitest, Playwright, and Cypress.

Java has JUnit.

C# has xUnit and NUnit.

Go has built-in testing that is almost aggressively straightforward.

Rust has first-class testing built right into the culture, which feels very on-brand.

Backend systems use tests.
Frontend apps use tests.
Mobile apps use tests.
Data pipelines use tests.
APIs use tests.
Infrastructure code uses tests.

If software exists, testing has probably shown up with a clipboard.

## What tools work best?

That depends on the layer.

For pure logic, lightweight unit-test tools are wonderful.

For APIs, test clients and mock servers help.

For browser flows, end-to-end tools earn their keep.

For reliability over time, continuous integration is where the real magic happens. Every code change gets checked automatically. That means the computer is now helping prevent computer problems, which feels only fair.

A very practical beginner stack might be:

* unit tests for core logic
* integration tests for important boundaries
* one or two end-to-end tests for the critical user path
* automated runs on every pull request

Not because that sounds impressive.

Because it dramatically reduces the number of surprises wearing fake mustaches.

## How much is this going to cost me?

Usually less than the bugs.

Most test frameworks are free.

The real cost is time, attention, and discipline.

You will spend extra time writing tests.

You will also save time not manually re-checking everything, not shipping obvious regressions, not debugging avoidable failures, and not composing apology messages to your users with the emotional tone of a hostage note.

So yes, testing costs something.

But not testing has a very exciting way of sending the invoice later.

## Is testing similar to anything else?

It is similar to proofreading, rehearsal, preflight checklists, and quality control.

You do not test because you assume disaster.

You test because reality has texture.

People mistype things.
Systems fail.
Assumptions drift.
Requirements change.
Yesterday's harmless shortcut becomes tomorrow's incident report.

Testing is how you stay honest in a profession where being almost right can still destroy an afternoon.

## Is testing the subject of any famous art?

Not directly, unless somewhere there is a giant oil painting called *Engineer Looking Tired Beside Build Pipeline*.

But spiritually, testing belongs to the same tradition as all art about order versus chaos, confidence versus consequence, and humans trying to create structure in a universe that keeps dropping bananas on the staircase.

Which, if we are being honest, is most of civilization.

## Is testing popular? Going up or down?

Testing is one of those rare topics that becomes more important the larger, faster, and more automated software gets.

The exact style of testing changes.

Tools change.
Fashion changes.
People argue online with theatrical commitment.

But the core idea keeps getting stronger: software that matters must be checked in repeatable ways.

So no, testing is not fading away.

If anything, the growth of cloud systems, CI pipelines, and AI-assisted coding has made it harder to ignore.

## Famous companies and real-world use

Big companies test because big companies enjoy outages even less than small companies do.

If you are shipping finance, commerce, healthcare, logistics, communications, infrastructure, or anything user-facing at scale, reliability stops being philosophical and becomes budget-shaped.

That does not mean every company tests perfectly.

Far from it.

But the larger the blast radius, the less "we clicked around a little and it seemed okay" sounds like a strategy.

## So what is the real lesson here?

Testing is not a side quest.

It is part of how software becomes trustworthy.

You do not write tests because your code is bad.

You write tests because your code matters, because systems evolve, because memory is unreliable, and because Future You deserves at least one ally in the room.

A beginner often asks, "When should I start testing?"

The honest answer is: earlier than you think, smaller than you fear, and more regularly than your inner chaos goblin prefers.

Start with the logic that would hurt if it broke.

Start with the rules that are easiest to misunderstand.

Start with the edge cases that look boring until they cost you Saturday.

Then build from there.

Because "it worked once" is a moment.

Reliable software is a habit.

## One last thing before you go

If this episode saved you from trusting a suspiciously cheerful function a little too much, follow along for the rest of the series, and drop a comment with the bug that taught you the hardest lesson. I always enjoy a good story where confidence went in one direction and reality went in another.

And if you want to see more of my work beyond the coding chaos, you can wander over to [LumAIere.com](https://lumaiere.com).

**[Art Prompt (Neoclassicism):](https://lumaiere.com/?gallery=neoclassical)** A grand, luminous interior arranged with calm architectural dignity, where pale marble columns, soft rose drapery, and warm ivory stone frame a stately gathering of elegantly posed figures. The composition should feel balanced and ceremonial, with one serene central woman standing in quiet authority while younger figures cluster near her in graceful triangular rhythms. Use a refined palette of creamy whites, muted coral, antique gold, dusty blue, and soft terracotta, with satin-smooth skin tones and fabric that falls in sculptural folds. Let the lighting be clear, noble, and evenly diffused, emphasizing polished surfaces, moral gravity, and poised restraint rather than spectacle. The mood should feel elevated, harmonious, and emotionally sincere, as if virtue itself has been staged with impeccable taste and classical confidence.

**[Video Prompt:](https://www.tiktok.com/@davelumai/video/7622132044507761950)** A stately neoclassical hall comes alive in crisp, elegant motion as soft morning light glides across marble columns and rose-toned drapery. The central figure turns slightly while surrounding figures shift in graceful, choreographed gestures, creating flowing triangular movement through the frame. Fabric ripples with delicate weight, golden highlights bloom across polished stone, and the camera circles with measured confidence before pushing inward for a dramatic reveal of the full balanced composition. Dust motes shimmer in the light, shadows stretch gently across the floor, and the final moment lands on a tableau of perfect classical harmony with just enough motion to feel luxurious, dramatic, and hypnotic.

**Recommended Songs for the Video:**
- A Gallant Gentleman - We Lost the Sea
- The Last One - This Will Destroy You

If this one hit home, follow me for more, and tell me in the comments whether you are a "write tests first" person, a "write tests after the bug bites me" person, or a "I meant to write tests and then life happened" person.
