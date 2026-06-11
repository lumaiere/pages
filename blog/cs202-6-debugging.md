# **CS202 Episode 6: Debugging at Scale, or When the Bug Is Not in One Line but in the Relationship Between Eight Ideas**

There is a beautiful beginner fantasy that debugging means finding the broken line.

A missing semicolon. A backwards comparison. A variable named `total` that is secretly holding the emotional weight of an entire accounting department.

And yes, sometimes debugging is that simple.

Sometimes the bug really is sitting there in one file, waving politely, wearing a little hat that says, "I am the problem."

But as software gets bigger, stranger, more distributed, more concurrent, more configurable, more dependent on other people, other services, other environments, and the mysterious weather system known as "production," debugging changes.

The bug stops being a broken line.

It becomes a broken relationship.

One module assumes the date is local time. Another module sends UTC. A queue retries three times. A cache remembers the old answer. A database migration changed a nullable field. A background worker silently skipped one record. The UI says "saved" because the API said "accepted," but accepted did not mean completed.

Nobody lied.

Everybody just told a different tiny truth.

That is debugging at scale.

And welcome to the part of CS202 where the software is no longer politely sitting in one chair. It is wandering through the building with a clipboard, asking other systems for favors, and occasionally locking itself in a supply closet.

## **Where we are in the course**

CS202 is the course where programming becomes software engineering.

In [CS101 Episode 6 - History, Debugging, and Problem Solving](https://medium.com/@DaveLumAI/episode-6-history-debugging-and-problem-solving-you-are-not-bad-at-this-this-is-just-how-it-efe6db927fd3), debugging was introduced as part of the basic craft: observe, test, reason, adjust, repeat, and try not to take the bug personally.

Then CS102 made the world larger. [CS102 Episode 11 - Modular Design and Abstraction](https://medium.com/@DaveLumAI/episode-11-modular-design-and-abstraction-or-how-to-make-your-code-less-like-a-junk-drawer-9b6273bc3721) taught us that software should be divided into meaningful parts. [CS102 Episode 12 - Testing and Reliability](https://medium.com/@DaveLumAI/episode-12-testing-and-reliability-or-why-it-worked-once-is-not-a-career-strategy-a50f80c8d6dc) explained why working once is not the same thing as being dependable. [CS102 Episode 13 - State, Bugs, and Program Behavior](https://medium.com/@DaveLumAI/episode-13-state-bugs-and-program-behavior-or-why-the-same-code-acts-different-after-lunch-91aeea89011d) introduced the extremely rude fact that the same code can behave differently depending on what happened before.

Then CS201 pulled the curtain back on the machine. In [CS201 Episode 6 - Processes, Threads, and Concurrency Basics](https://medium.com/@DaveLumAI/episode-6-processes-threads-and-concurrency-basics-or-how-one-machine-does-many-things-at-once-6ef3836f4ebf), we saw how one computer can do many things at once, which is wonderful until two of those things reach for the same data and suddenly everyone is in a tiny courtroom.

Now CS202 takes all of that and asks:

How do we debug software when the failure is spread across modules, services, logs, data, timing, configuration, and assumptions?

That is the job today.

## **The old debugging model**

When you first learn to program, the debugging loop is usually small.

You write a function.

You run it.

It fails.

You look at the function.

You fix the function.

You feel briefly like a genius.

Something like this:

```python
def apply_discount(price, discount):
    return price - discount
```

If `price` is `100` and `discount` is `10`, this works.

But then someone passes `discount` as `0.10`, expecting a percentage.

Now the result is `99.9`, which is technically a number and spiritually nonsense.

The bug is not really arithmetic. It is a contract problem.

One part of the code thinks `discount` means dollars.

Another part thinks `discount` means percent.

The function did exactly what it was told. Unfortunately, what it was told came from a misunderstanding wearing business-casual shoes.

This is the first hint that larger debugging is not just about syntax or logic.

It is about assumptions.

## **The real unit of failure is often the path**

In small programs, you can often debug by looking at a line.

In larger systems, you debug by following a path.

A request comes in.

It gets authenticated.

It gets validated.

It calls an API.

The API calls another service.

That service reads from a cache.

The cache misses.

The database returns a record.

The service transforms it.

Another service enriches it.

The response returns to the first service.

The UI renders it.

The user says, "Why is the total wrong?"

Ah yes.

The ancient technical diagnosis: the total is wrong.

Helpful as a smoke alarm in a fog machine factory.

At scale, the first question is rarely "Which line is broken?"

The better question is:

Where did the program's understanding of reality first become wrong?

That is a very different hunt.

## **A concrete example: the case of the missing shipping fee**

Imagine an online store.

The user places an order.

The checkout page shows:

```text
Subtotal: $50.00
Shipping: $7.00
Total: $57.00
```

But the confirmation email says:

```text
Subtotal: $50.00
Shipping: $0.00
Total: $50.00
```

The customer is delighted.

Accounting is not.

Where is the bug?

Maybe the UI calculated shipping differently.

Maybe the backend did not receive the shipping method.

Maybe the order service accepted the order before shipping was finalized.

Maybe the email service used an old template.

Maybe the database stored the value correctly, but the email worker read the wrong field.

Maybe someone named a field `shipping_cost`, another system expected `shippingFee`, and now two small pieces of software are glaring at each other across the cafeteria.

A beginner might search the email template.

A more experienced engineer follows the data.

At checkout, what was the shipping fee?

When the request hit the API, was shipping included?

When the order was saved, what value was stored?

When the email worker read the order, what value did it receive?

When the email was rendered, which field did it use?

This is debugging as investigation.

Not guessing.

Not poking random files until the bug gets tired.

Investigation.

## **Tracing across modules**

Tracing means following the journey of one piece of work through the system.

In a simple application, this might mean following one function call into another.

In a larger codebase, it might mean following one user action across controllers, services, repositories, jobs, caches, and event handlers.

In a distributed system, it might mean following one request across multiple services.

The key idea is this:

A bug has a life story.

Your job is to reconstruct it.

One common technique is to add an identifier that travels with the request. This is often called a request ID, correlation ID, or trace ID.

For example:

```text
request_id=abc123 user_id=42 action=checkout step=cart_loaded
request_id=abc123 user_id=42 action=checkout step=shipping_calculated shipping=7.00
request_id=abc123 user_id=42 action=checkout step=order_created order_id=9001 shipping=7.00
request_id=abc123 user_id=42 action=email step=confirmation_rendered shipping=0.00
```

Now we have a clue.

The shipping fee survived order creation but disappeared during email rendering.

That does not solve the bug, but it narrows the battlefield. And narrowing the battlefield is half the job.

Without tracing, debugging can become a treasure hunt where the treasure is embarrassment and the map was drawn by a raccoon.

With tracing, you at least know where to start digging.

Modern observability tools formalize this idea. The [OpenTelemetry observability primer](https://opentelemetry.io/docs/concepts/observability-primer/) is a useful introduction to how traces, metrics, and logs work together in real systems.

## **Logging: the system's diary, if the system had terrible handwriting**

Logging is one of the most useful debugging tools ever created, and also one of the easiest to ruin.

A good log answers questions.

A bad log creates new ones.

Compare this:

```text
Error occurred
```

Marvelous. Poetry. A tiny fortune cookie of uselessness.

Now compare this:

```text
level=error request_id=abc123 order_id=9001 service=email-worker message="missing shipping_cost while rendering confirmation email"
```

That log tells us what failed, where it failed, which order was involved, and how to connect it to the rest of the request.

A useful log usually includes context:

* What happened?
* Where did it happen?
* Which user, order, job, file, or request was involved?
* What decision did the system make?
* What values mattered?
* Was the error expected, recoverable, or catastrophic?

But logging has tradeoffs.

Too little logging and you are debugging in the dark with a decorative candle.

Too much logging and you create a landfill of text where the important clue is buried between "started process" and "still doing process" seventeen thousand times.

Logs can also leak sensitive information if you are careless. Never casually log passwords, tokens, full credit card numbers, private messages, or anything you would not want projected onto a wall during a very awkward meeting.

Good logging is intentional.

It is not screaming everything.

It is leaving a trail.

## **Instrumentation: making invisible behavior visible**

Instrumentation is the practice of adding measurement points inside software so you can see what it is doing.

Logs tell stories.

Metrics count things.

Traces show paths.

Together, they help you answer different questions.

A log might say:

```text
order creation failed because payment authorization timed out
```

A metric might say:

```text
payment_timeout_count increased from 3 per hour to 300 per hour
```

A trace might show:

```text
checkout-service -> payment-service -> external-payment-provider
```

Now you know not only that one order failed, but that many orders are failing, and the slowdown is probably outside your checkout code.

That matters because debugging at scale is often less about proving that code is wrong and more about locating the part of the system where reality changed.

Was there a deployment?

A database slowdown?

A traffic spike?

A new dependency version?

A configuration change?

A vendor outage?

A cache eviction storm?

A clock drift?

A DNS issue?

A timeout that was set optimistically by someone who believed deeply in vibes?

Instrumentation gives you evidence.

And evidence is what separates debugging from ritual clicking.

## **Narrowing failure scope**

When a large system fails, your first job is not to fix it.

Your first job is to make the problem smaller.

This is one of the most important habits in debugging.

A vague bug sounds like this:

"The app is broken."

A narrower bug sounds like this:

"Checkout confirmation emails show zero shipping for orders created through the mobile app when the customer chooses expedited shipping."

That is a completely different problem.

It has shape.

It has boundaries.

It tells us where to look.

Good narrowing questions include:

* Is it happening for all users or some users?
* Did it start after a deployment?
* Does it happen in production, staging, or both?
* Is it tied to one browser, device, region, account type, or feature flag?
* Is the data wrong when stored, or only wrong when displayed?
* Is the failure consistent or intermittent?
* Can we reproduce it?
* What changed recently?

That last question deserves its own chair at the table.

Software does not usually wake up one morning and decide to be weird for personal reasons.

Something changed.

Code changed.

Data changed.

Traffic changed.

Infrastructure changed.

Dependencies changed.

Configuration changed.

User behavior changed.

A system that worked yesterday and fails today is trying to tell you a story about change.

Listen before you start swinging a wrench.

## **The villain known as "works on my machine"**

"Works on my machine" is not a conclusion.

It is a clue.

It means your machine and the failing environment are different in some important way.

Different operating system.

Different dependency version.

Different environment variables.

Different database contents.

Different permissions.

Different time zone.

Different CPU architecture.

Different cache state.

Different network rules.

Different feature flags.

Different secrets.

Different build artifact.

Different Tuesday.

This is why Episode 5 on build systems and dependency management matters so much. If you cannot reliably recreate the software, you cannot reliably investigate the software.

Debugging at scale depends on reproducibility. Not perfect reproducibility every time, because life is not always that generous, but enough control that you can compare environments and isolate differences.

"Works on my machine" should become:

"What is different between my machine and the machine where it fails?"

That is engineering.

The original phrase is mostly a bumper sticker for future regret.

## **Misconception: more tests mean no debugging**

Tests are wonderful.

Tests are necessary.

Tests are not magic bug repellent.

A good test suite catches known classes of mistakes. It protects behavior you have thought to specify. It gives you confidence when changing code. It prevents old monsters from climbing back through the window wearing a fake mustache.

But tests do not catch everything.

They may miss interactions between services.

They may not cover production data.

They may not simulate timing issues.

They may not include expired tokens, partial outages, weird encodings, old mobile clients, corrupted cache entries, or the one enterprise customer whose account has settings last touched during the Bronze Age of your product.

Debugging is what happens when the system teaches you about a case your tests did not imagine yet.

And then, ideally, you turn that discovery into a new test.

That is the loop:

Bug appears.

You investigate.

You understand it.

You fix it.

You add a test or monitor so it does not sneak back in wearing sunglasses.

This is how teams turn pain into infrastructure.

Which is almost noble, in a slightly haunted way.

## **Misconception: the stack trace tells the whole truth**

A stack trace tells you where the program finally fell down.

It does not always tell you where the floor first became slippery.

Suppose you see this:

```text
NullReferenceError: cannot read property "email" of null
```

The crash happened when code tried to read `email`.

But why was the user null?

Was the ID invalid?

Was the database query wrong?

Was the account deleted?

Did an authorization service return no user?

Did a cache store a negative result?

Did a previous step swallow an error and keep going?

The stack trace is useful, but it is not the entire investigation.

It is the chalk outline.

You still need the detective work.

## **A realistic real-world example: the intermittent timeout**

Now let us make the problem more realistic and more irritating, as software enjoys doing.

A company has a reporting dashboard.

Most of the time, it loads in two seconds.

Sometimes it takes thirty seconds and fails.

Only for some customers.

Only in the morning.

Only on weekdays.

Only after a new analytics feature launched.

This is the kind of bug that makes people start saying things like "flaky" and "probably network" and "maybe retry it," which are all valid words but not yet a diagnosis.

A systematic approach might look like this:

First, define the failure.

Reports timeout for large customer accounts between 8:00 and 10:00 AM on weekdays.

Second, compare successful and failed requests.

The failed ones query more rows, hit a slower database path, and call a new aggregation service.

Third, inspect traces.

The dashboard service is fast.

The aggregation service is slow.

Inside the aggregation service, most time is spent waiting on a database query.

Fourth, inspect the query.

The new feature added a filter that prevents an index from being used.

Fifth, confirm with real data.

Large customers have enough rows to expose the problem. Small customers do not.

Sixth, fix the root cause.

Rewrite the query, add the right index, or precompute the aggregation depending on the tradeoff.

Seventh, prevent recurrence.

Add a performance test, a dashboard metric for query duration, and an alert when latency crosses a threshold.

Notice what did not happen.

Nobody just stared at the dashboard controller and hoped the bug would confess.

They followed the system.

## **Debugging AI-assisted code**

Modern development has added a new character to the debugging drama: AI-generated code.

AI tools can be extremely helpful. They can explain error messages, suggest hypotheses, generate test cases, summarize logs, and help you notice patterns you might have missed while you were busy becoming one with the chair.

But AI can also produce code that looks confident while misunderstanding the system.

That means debugging AI-assisted code requires the same discipline as debugging human-written code.

Maybe more.

Do not ask, "Does this look reasonable?"

Ask:

* What assumption is this code making?
* What inputs does it expect?
* What happens when the dependency fails?
* What state does it modify?
* What contract does it rely on?
* Does the generated code match our architecture?
* Do the logs and tests prove the behavior?

AI can accelerate investigation.

It should not replace investigation.

The machine can hand you a flashlight. You still need to look in the closet.

## **Debugging as a team sport**

At scale, debugging is rarely a solo heroic moment.

It often involves multiple people who understand different parts of the system.

The frontend engineer knows how the browser request is shaped.

The backend engineer knows how the API validates it.

The database person knows why the query plan looks like it was assembled during a thunderstorm.

The operations person knows a deployment happened twelve minutes before everything became soup.

The support person knows customers started reporting the issue after using one specific workflow.

The best debugging teams share context quickly.

They do not hoard clues.

They do not treat every bug as a blame festival.

They write down what they know, what they tried, what changed, and what remains uncertain.

This is where documentation becomes a debugging tool, not just a place where old diagrams go to become archaeology.

A good incident note might say:

```text
Symptom:
Checkout confirmation emails show shipping as $0.00.

Scope:
Only expedited shipping orders created from mobile clients after version 4.8.2.

Known:
Order records contain correct shipping_cost.
Email worker receives shippingFee as null.
Mobile API sends shipping_cost, but email renderer expects shippingFee.

Likely cause:
Field naming mismatch introduced during mobile checkout refactor.

Next:
Normalize field mapping in email worker and add contract test.
```

That is not glamorous.

It is better than glamorous.

It is useful.

## **Failure modes in large-system debugging**

Large-system debugging has its own traps.

One trap is confirmation bias.

You think the cache is the problem, so every clue becomes cache-shaped. This is how engineers spend six hours interrogating Redis while the real issue sits in a config file eating crackers.

Another trap is changing too many things at once.

If you update a dependency, clear the cache, restart the service, change the timeout, and deploy a patch all at once, you might fix the symptom while learning absolutely nothing.

That feels good for fifteen minutes.

Then the bug returns with luggage.

Another trap is treating symptoms as causes.

A timeout is not always the cause. It may be the visible effect of a slow query, overloaded service, bad retry loop, network issue, or lock contention.

A null value is not always the cause. It may be the result of missing validation, an unexpected API response, deleted data, or a race condition.

A 500 error is not a root cause. It is the system yelling from another room.

Go find the room.

## **The practical debugging loop**

Here is a healthier loop for debugging at scale:

1. State the symptom clearly.

2. Determine scope.

3. Reproduce or capture evidence.

4. Follow the path of data or control.

5. Compare good and bad cases.

6. Form a hypothesis.

7. Test the hypothesis with the smallest safe change or observation.

8. Fix the root cause.

9. Add protection: tests, logs, metrics, validation, documentation, or alerts.

10. Share what was learned.

The goal is not just to make the red light stop blinking.

The goal is to understand why the red light blinked, why nobody noticed earlier, and how to make future blinking more informative.

That is the difference between patching software and improving software.

## **The tradeoffs**

Debugging tools are not free.

More logging can increase storage costs and expose sensitive data if handled badly.

More tracing can add overhead and require discipline across services.

More metrics can create alert fatigue if every tiny wiggle becomes a siren.

More tests can slow builds if the test suite is poorly designed.

More abstraction can make systems cleaner, but it can also make control flow harder to follow if the architecture becomes a maze with inspirational naming.

The answer is not "instrument everything forever."

The answer is to instrument what matters.

Critical paths.

Expensive operations.

External calls.

State transitions.

Retries.

Failures.

Security-sensitive decisions.

Data transformations.

Places where the system crosses a boundary and says, "Trust me."

Because those are the places where bugs like to rent office space.

## **What students should take away**

Debugging at scale is not about being clever enough to guess the bug.

It is about building enough visibility, discipline, and shared understanding that the system can be investigated.

Small-program debugging teaches you to inspect code.

Large-system debugging teaches you to inspect relationships.

Between modules.

Between services.

Between data and assumptions.

Between expected behavior and observed behavior.

Between what the code says and what the system actually does at 9:04 AM with real users and a database that has seen things.

This is why debugging is not a side skill.

It is software engineering in concentrated form.

It requires technical knowledge, patience, humility, communication, and a willingness to follow evidence even when your favorite theory looked extremely handsome in the beginning.

So the next time a bug is spread across eight ideas, do not panic.

Name the symptom.

Shrink the scope.

Follow the path.

Collect evidence.

Respect the weirdness.

And remember: the system is not haunted.

Probably.

It is just insufficiently observed.

Follow for more CS202 episodes, and drop a comment with the strangest bug you have ever chased. Bonus points if the bug only happened on one machine, one Tuesday, or after somebody said, "This should be a quick fix."

**[Art Prompt (Symbolism):](https://lumaiere.com/?gallery=symbolism)**

A dreamlike Symbolist landscape inspired by late nineteenth-century visionary painting, featuring a moonlit garden of oversized blue flowers, soft violet hills, glowing amber clouds, and a mysterious gentle eye-like form emerging from the horizon as if the landscape itself is quietly awake. Use velvety pastel textures, luminous blues, smoky purples, pale gold highlights, delicate botanical shapes, and a hushed theatrical mood. The composition should feel enchanted, strange, serene, and poetic, with rounded organic forms, misty depth, and a sense of private wonder. Keep it family-friendly, refined, and free of readable text, logos, brands, modern objects, or recognizable people.

**[Video Prompt:](https://www.tiktok.com/@davelumai/video/7649935850465185055)**

Animate the Symbolist dream garden as a catchy short-form video: the oversized blue flowers pulse gently to the beat, golden clouds curl and unfurl like painted smoke, tiny sparks of light drift upward from the petals, and the distant horizon slowly opens with a soft luminous blink before dissolving into violet mist. Add rhythmic camera pushes, subtle parallax between flowers and hills, glowing particles that sync with musical accents, and a final upward burst of moonlit color. Keep the motion elegant, hypnotic, family-friendly, and free of readable text, logos, brands, or recognizable people.

Song recommendations:

Rez - Underworld

Halcyon On and On - Orbital
