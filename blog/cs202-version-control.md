# **CS202 Episode 1: Version Control and Change Management, or How Teams Remember What Happened Before Everyone Starts Blaming Kevin**

Software does not usually fail because one person typed one bad line while lightning struck a keyboard and a raccoon screamed in the hallway.

That can happen, obviously. The universe has range.

But most software trouble is slower, quieter, and more human. A feature worked yesterday. Someone changed something. Someone else changed something nearby. A third person pulled an old copy from their desktop called `final-final-real-final-v3-fixed`, which is how civilizations collapse. Now the app is coughing into a napkin and nobody knows what happened.

Welcome to CS202.

In CS101, we learned how to make programs do things. From CS101, [Programming Fundamentals Part 2: Loops and Functions](https://medium.com/@DaveLumAI/episode-3-loops-and-functions-or-how-to-stop-copy-pasting-yourself-into-madness-fac07f2d1bc4) taught us how to stop repeating ourselves like a haunted printer. In CS102, [Modular Design and Abstraction](https://medium.com/@DaveLumAI/episode-11-modular-design-and-abstraction-or-how-to-make-your-code-less-like-a-junk-drawer-9b6273bc3721) taught us that working code can still be organized like a garage full of unlabeled extension cords. Also from CS102, [Testing and Reliability](https://medium.com/@DaveLumAI/episode-12-testing-and-reliability-or-why-it-worked-once-is-not-a-career-strategy-a50f80c8d6dc) reminded us that "it worked once" is not exactly an engineering department.

Now CS202 asks a different question:

How do people build software together without losing the history, the intent, the evidence, and occasionally the will to continue?

That is version control.

And version control is not just "saving your files."

It is the memory system for a software project.

It is the black box flight recorder.

It is the team diary, except instead of "Dear diary, today I felt misunderstood," it says "Fixed null customer ID during invoice export," which is less romantic but much more useful during production outages.

## **The Basic Problem: Software Changes Constantly**

Beginners often imagine programming like writing an essay.

You sit down. You create the thing. You polish it. You submit it. You are done.

Real software is not like that.

Real software is more like maintaining a restaurant where the menu changes daily, the kitchen has hidden pipes from 1998, customers keep asking for gluten-free blockchain, and someone just discovered the freezer door has been held shut with optimism.

Software is changed more often than it is written fresh.

A useful program accumulates changes:

A bug fix here.

A new feature there.

A config update because the payment provider changed something.

A security patch because the internet remains a public zoo with keyboards.

A performance improvement.

A rollback.

A hotfix.

A tiny "temporary" workaround that celebrates its seventh birthday.

Without a system to track these changes, your project becomes a folder full of vibes.

Version control gives changes structure.

It lets you answer questions that matter:

Who changed this?

When did it change?

Why did it change?

What exactly changed?

Can we undo it?

Can we compare this version with that version?

Can two people work at the same time without stapling their work together at random?

Those are not academic questions. Those are Tuesday.

## **Backup Is Not Version Control**

This is the first misconception we must gently escort out of the building.

A backup copies your files.

Version control records the history of your project.

A backup says:

"Here is a copy of the folder from last night."

Version control says:

"Here are all the meaningful changes, in order, with messages, authors, timestamps, branches, comparisons, and a trail of breadcrumbs so the team can understand how the software evolved."

A backup is useful when your laptop falls into a fountain.

Version control is useful when your teammate changes `calculateDiscount()` and now every customer gets 700 percent off, which is popular but financially spicy.

You need both.

Backups protect against loss.

Version control protects against confusion.

That difference matters.

Copying your project folder and naming it `project_old` is not a strategy. It is a cry for help with a timestamp.

The official [Git book explains version control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) as a system that records changes over time so you can recall specific versions later. That is the heart of it. Version control is not just storage. It is controlled memory.

## **The Central Idea: Commits**

A commit is a saved snapshot of meaningful project change.

Not just "the files at some random moment."

A meaningful change.

That word matters.

A good commit says:

"I changed this piece of the system for this reason."

It has a few important parts:

The files that changed.

The exact lines that changed.

The person who made the change.

The time it happened.

A unique identifier.

A message explaining the intent.

Think of a commit as a sealed envelope containing a small piece of project history.

You can open it later and say, "Ah yes, this is where we changed the login validation."

Or, less joyfully, "Ah yes, this is where the raccoon entered payroll."

The command might look like this:

```bash
git add login.js
git commit -m "Validate empty login form before authentication"
```

That command does not merely save the file. It creates a named moment in the project's history.

A bad commit message says:

```bash
git commit -m "fix stuff"
```

This is technically a message in the same way a smoke alarm is technically a musical instrument.

A better message says:

```bash
git commit -m "Fix invoice total rounding for tax calculation"
```

Now the future team has a clue.

And future team includes you.

Tomorrow you is not magically smarter than today you. Tomorrow you is often tired, holding coffee, and wondering why past you treated documentation like a tax audit.

Help tomorrow you.

## **A Tiny Example: The Calculator That Grew Teeth**

Suppose you are building a tiny calculator app.

At first it only adds two numbers:

```python
def add(a, b):
    return a + b
```

You commit it:

```bash
git add calculator.py
git commit -m "Add basic addition function"
```

Then you add subtraction:

```python
def subtract(a, b):
    return a - b
```

Another commit:

```bash
git add calculator.py
git commit -m "Add subtraction function"
```

Then you discover division crashes when someone divides by zero, because mathematics has boundaries and computers are very willing to faceplant into them.

So you add defensive handling:

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

Commit:

```bash
git add calculator.py
git commit -m "Handle division by zero"
```

Now your project history tells a story.

Not a glamorous story. Nobody is optioning it for streaming. But it is a useful story:

First we added addition.

Then subtraction.

Then division safety.

If a bug appears in division, you can inspect the exact commit where division changed. If subtraction starts behaving oddly after another update, you can compare the current file with the older version.

Version control turns "something broke" into "something changed."

That is a very big upgrade.

## **Branches: Parallel Universes With Better Paperwork**

A branch is a separate line of development.

That sounds fancy, but the intuition is simple.

You have the main version of the project. It is supposed to stay stable.

But you want to try a new feature.

You could change the main code directly, which is exciting in the way juggling knives on a trampoline is exciting.

Or you could create a branch.

```bash
git checkout -b add-coupon-codes
```

Now you can work on coupon codes without disturbing the main version.

The main branch keeps existing.

Your feature branch moves forward separately.

Eventually, if the work is good, you merge it back.

```bash
git checkout main
git merge add-coupon-codes
```

This is one of the most powerful ideas in software teamwork.

Branches allow experimentation without immediate damage.

They allow features, bug fixes, releases, and experiments to move at different speeds.

They also allow chaos, because every powerful tool comes with the possibility that someone will use it like a leaf blower indoors.

Good branch names help:

```bash
feature/customer-search
bugfix/null-invoice-total
hotfix/payment-timeout
experiment/new-dashboard-layout
```

Bad branch names include:

```bash
stuff
newstuff
daves-thing
please-work
real-one
```

That last one is how you summon an outage goblin.

## **Merges: Bringing Work Back Together**

A merge combines changes from one branch into another.

Sometimes this is easy.

If one person changed `login.js` and another changed `styles.css`, Git can usually combine them without drama.

But sometimes two people change the same part of the same file.

Then Git stops and says, in its own gentle machine way:

"I am not your therapist. You decide."

This is a merge conflict.

A merge conflict does not mean Git failed.

It means Git found two competing edits and refused to guess.

That is good.

You do not want the tool randomly deciding whether the checkout button should charge customers once or eighteen times.

A conflict might look like this:

```text
<<<<<<< HEAD
return calculateTotal(cart)
=======
return calculateTotal(cart, couponCode)
>>>>>>> feature/coupon-support
```

This means the current branch has one version, and the incoming branch has another.

A human must decide what the correct result should be.

Maybe the answer is:

```javascript
return calculateTotal(cart, couponCode)
```

Or maybe both branches misunderstood something and the correct answer is:

```javascript
return calculateTotal(cart, couponCode, taxRegion)
```

Merge conflicts are not just mechanical problems. They are communication problems made visible.

They often mean two people were working near the same idea and need to coordinate.

That is why version control is not only a technical tool. It is also a social tool wearing a hoodie.

## **History: The Project Remembers So You Do Not Have To**

One of the greatest gifts version control gives you is history.

You can inspect the timeline:

```bash
git log
```

You can see what changed:

```bash
git diff
```

You can ask who last changed a line:

```bash
git blame filename.py
```

Now, before we continue, `git blame` has one of the least emotionally healthy names in computing.

The point is not to stand in a circle and chant "Kevin" until morale improves.

The point is to understand context.

Who changed this line?

What commit introduced it?

What was the reason?

What else changed at the same time?

History helps you debug.

It helps you review.

It helps you onboard new team members.

It helps you understand why the system is shaped the way it is.

This connects nicely to CS101's [History, Debugging, and Problem Solving](https://medium.com/@DaveLumAI/efe6db927fd3), where we treated debugging as a disciplined investigation instead of a panic ritual. Version control gives that investigation evidence.

Without history, debugging often becomes folklore.

"Do not touch that function."

"Why?"

"Greg touched it once and the printer caught fire."

Version control lets you replace folklore with facts.

That is better for software and, frankly, for Greg.

## **Change Management: Version Control With Adult Supervision**

Version control tracks changes.

Change management decides how changes should happen.

That includes questions like:

Who reviews code before it enters the main branch?

When do we release?

How do we test changes?

How do we roll back bad releases?

How do we handle urgent fixes?

How do we avoid breaking work other teams depend on?

This is where software engineering becomes less about heroic typing and more about controlled movement.

A small student project might use a very simple workflow:

Work on `main`.

Commit often.

Push to a remote repository.

Try not to trip over your own shoelaces.

A professional team usually needs more structure:

Create a branch for each feature or bug fix.

Open a pull request or merge request.

Run automated tests.

Ask another developer to review the change.

Merge only after checks pass.

Deploy through a controlled pipeline.

Monitor the result.

That may sound like bureaucracy, but good process is not paperwork for its own sake.

Good process prevents "I changed one button and accidentally deployed a cursed invoice demon to production."

The goal is not to slow everyone down.

The goal is to make change safe enough that the team can move faster without needing a ceremonial apology meeting every Thursday.

## **Remote Repositories: Collaboration Without Emailing Zip Files Like It Is 2004**

A local repository lives on your machine.

A remote repository lives somewhere shared, usually on a service such as GitHub, GitLab, Bitbucket, Azure DevOps, or an internal company server.

The remote is where collaboration becomes practical.

You push your commits:

```bash
git push origin feature/customer-search
```

Your teammate pulls changes:

```bash
git pull
```

The team reviews branches, discusses changes, runs automated checks, and keeps the shared project history synchronized.

This is where version control becomes team memory instead of personal memory.

It also reduces the ancient horror of emailing zip files around:

"Here is my latest copy."

"No, use this copy."

"Wait, I made changes to the other copy."

"Which one has the database migration?"

"I think Sarah has it."

"Sarah is on vacation."

And that is how a software team becomes a ghost story.

## **Pull Requests: A Conversation Around Change**

A pull request is a request to merge one branch into another.

But it is more than a button.

It is a conversation around a proposed change.

A good pull request explains:

What changed?

Why did it change?

How was it tested?

What risks exist?

What should reviewers pay attention to?

For example:

```text
Summary:
Adds coupon code validation during checkout.

Why:
Marketing needs limited-time discount codes for seasonal campaigns.

Testing:
- Added unit tests for valid, expired, and unknown coupon codes.
- Manually tested checkout with and without a coupon.

Risk:
Coupon validation touches checkout totals, so reviewers should inspect rounding and tax behavior carefully.
```

This is beautiful because it gives reviewers context.

Nobody wants to review 800 lines of code with the description "updates."

That is not a pull request. That is a fog machine.

Pull requests also connect version control to team learning. Junior developers learn by seeing how experienced developers reason about tradeoffs. Experienced developers catch assumptions before they harden into production bugs. The team builds shared standards.

This is the social layer of software engineering, and we will return to it later in this course when we reach software engineering as a team sport.

## **The Practical Consequences of Bad Version Control**

When version control is used badly, the project starts collecting little disasters.

Here are some classics.

One giant commit with two weeks of unrelated changes.

This makes review painful, rollback dangerous, and debugging miserable. If the commit touches login, billing, CSS, database migrations, and a mysterious file named `temporary2.js`, nobody knows what is actually being approved.

Unclear commit messages.

"Fixed bug" is not enough. Which bug? How? Why? Did the bug have a name? Was it wearing a hat?

Long-running branches.

A branch that lives too long drifts away from the main codebase. The eventual merge becomes painful because the world changed while the branch was napping in a cave.

Committing generated files or secrets.

Do not commit passwords, API keys, private certificates, or production credentials. Version control remembers. That is the point. Unfortunately, it remembers your mistakes too, with the calm confidence of an elephant that learned cybersecurity.

Using version control as a backup dump.

If you commit random files without meaning, the history becomes noisy. You can still recover files, but the project story becomes harder to read.

Never pulling changes.

If you work for days without syncing with the team, you may be building on an outdated version of reality. This is also how some family arguments begin, but we will stay with software.

## **Tradeoffs: There Is No One Perfect Workflow**

You will hear many strong opinions about version control workflows.

Some teams use trunk-based development, where developers integrate small changes into the main branch frequently.

Some teams use feature branches, where each change is isolated until reviewed and merged.

Some teams use release branches.

Some teams use GitFlow.

Some teams use something homegrown that began as a diagram and became a lifestyle.

There is no universal winner.

The tradeoff is between speed, safety, coordination, and complexity.

Frequent integration reduces painful merges but requires strong tests and discipline.

Long feature branches provide isolation but increase merge risk.

Strict review improves quality but can slow urgent changes.

Loose review moves quickly but can let bugs stroll into production wearing sunglasses.

Small teams can often use simpler workflows.

Large teams need more structure because coordination cost grows. Once many people touch the same codebase, "just be careful" is not a process. It is a wish with a keyboard.

The right workflow depends on the project, team size, risk level, deployment style, and tooling.

A hobby website and a banking system should not have the same change process, unless the banking system is operated by raccoons, in which case we have larger concerns.

## **Version Control in the Cloud and AI Era**

Version control has become even more important in modern development, not less.

Cloud systems are often defined by configuration files, infrastructure templates, deployment scripts, container files, environment settings, and CI/CD pipelines.

That means the codebase is no longer only application code.

It may include:

Dockerfiles.

Kubernetes manifests.

Terraform or CloudFormation templates.

Database migrations.

GitHub Actions or GitLab CI files.

Security policies.

Documentation.

Feature flags.

Release notes.

The repository becomes the source of truth for how the system exists.

This is sometimes called infrastructure as code. The idea is simple: if infrastructure can be described in files, those files should be reviewed, versioned, tested, and changed with care.

AI coding tools make this even more important.

An AI assistant can generate useful code quickly. It can also generate confident nonsense quickly, which is a special flavor of productivity theater. Version control gives you a safety net.

You can try generated changes on a branch.

You can inspect the diff.

You can run tests.

You can review what changed before merging.

The faster you can produce code, the more important it becomes to manage change carefully.

Speed without history is just chaos wearing sneakers.

## **A More Realistic Example: The Checkout Bug**

Imagine a small ecommerce team.

They have a checkout service.

A developer adds coupon codes on a feature branch.

Another developer changes tax calculation for a new region.

A third developer updates the UI to show estimated shipping earlier.

All three changes touch checkout behavior.

Without version control, this becomes a terrifying group project where everyone edits the same files and hopes friendship survives.

With version control, each developer works separately.

The coupon branch adds validation and discount logic.

The tax branch updates regional tax rules.

The shipping branch updates the checkout display.

Each branch has commits.

Each branch has a pull request.

Tests run automatically.

Reviewers inspect the changes.

Maybe a merge conflict appears because coupon logic and tax logic both changed total calculation.

Good.

The conflict forces the team to decide the correct order:

Subtotal.

Discount.

Tax.

Shipping.

Final total.

That is not merely a code issue. It is a business rule.

Version control exposes the collision before customers discover it with their credit cards.

This is the difference between controlled change and public embarrassment.

## **What Students Should Practice**

For this episode, the goal is not to memorize every Git command ever invented.

Git has enough commands to make a small civilization nervous.

The goal is to understand the model:

A repository stores project history.

A commit records a meaningful change.

A branch lets work happen separately.

A merge combines work.

A remote repository supports collaboration.

A pull request creates review and discussion.

A good workflow makes change safer.

Start with the basics:

```bash
git status
git add
git commit
git log
git diff
git branch
git checkout
git merge
git pull
git push
```

Then build habits:

Commit small, coherent changes.

Write messages that explain intent.

Pull before starting work.

Use branches for nontrivial changes.

Review diffs before committing.

Do not commit secrets.

Do not treat the main branch like a sandbox full of fireworks.

And perhaps most importantly:

Do not be afraid of version control.

At first, Git feels like it was designed by a time-traveling locksmith who communicates through riddles. But underneath the weird command names is a clear idea:

Track change carefully.

That is it.

The rest is practice.

## **The Big Takeaway**

Version control is how software projects remember.

It lets individuals experiment safely.

It lets teams collaborate without turning every file into a custody dispute.

It lets you inspect the past, understand the present, and recover from mistakes without performing a midnight ritual over a broken laptop.

More importantly, version control changes how you think.

You stop seeing software as one big fragile object.

You start seeing it as a sequence of deliberate changes.

That mindset is the beginning of real software engineering.

Not just "Can I make this work?"

But:

Can I change it safely?

Can someone else understand what I changed?

Can we recover if I am wrong?

Can the team move forward without losing the trail?

That is why CS202 starts here.

Because real software is changed more often than it is written fresh.

And if your team cannot manage change, the codebase will still change anyway.

It will just do so in the dark, wearing tap shoes, knocking things over.

## **[Art Prompt (Contemporary Art):](https://lumaiere.com/?gallery=contemporary)**

A dazzling contemporary installation-inspired scene of a mirrored room filled with floating glowing spheres, dense fields of repeating dots, reflective black floors, and endless optical repetition that seems to stretch beyond the walls. Use luminous reds, electric yellows, deep violet shadows, glossy black reflections, and crisp high-contrast patterning. The composition should feel playful, hypnotic, immersive, and slightly unreal, as if the viewer has stepped inside a joyful infinite machine made of light, mirrors, and polka-dot constellations. Avoid depicting computers, code, office work, keyboards, screens, or any direct reference to software; keep the image abstract, vibrant, family-friendly, and visually magnetic.

## **[Video Prompt:](https://www.tiktok.com/@davelumai/video/7643475309634784542)**

Start with a burst of glowing spheres popping into view in sync with the beat, each one reflecting a different dotted pattern as the camera darts through a mirrored room. Let the dots ripple across the walls like animated constellations, then have the floor reflections pulse outward in waves while the spheres gently bob, rotate, and multiply. Add quick rhythmic cuts, shimmering light flashes, and a final moment where the room appears to expand infinitely in every direction before snapping back into a bright centered composition perfect for a short-form loop.

Song recommendations for the video:

"Electric Relaxation - A Tribe Called Quest"

"Sweet Talk - Saint Motel"

Follow along for more art, code, weirdly useful explanations, and the occasional software goblin. If this helped, made you laugh, or reminded you of a folder named `final-final-actually-final`, leave a comment and tell me your best version control horror story.
