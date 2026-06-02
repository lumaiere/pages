# **CS202 Episode 3: Error Handling and Defensive Programming, or Hope Is Not an Exception Strategy**

Software is not fragile because computers are emotional.

Software is fragile because reality keeps showing up.

A file is missing. A network request times out. A user enters "banana" where your program expected a date. A payment provider says "temporary unavailable," which is corporate poetry for "good luck, little app." A database connection drops. A permissions check fails. A value is null. A service returns something shaped almost like the documentation promised, but with one tiny difference, because apparently chaos has a product roadmap.

Welcome to CS202 Episode 3.

This is error handling and defensive programming.

Or, in plain English: how to write software that does not faint dramatically the first time the universe refuses to cooperate.

In **[CS202 Episode 1 - Version Control and Change Management](https://medium.com/@DaveLumAI/cs202-episode-1-version-control-and-change-management-or-how-teams-remember-what-happened-before-068050d8d334)**, we learned how teams track change so the past does not become a crime scene with branch names. In **[CS202 Episode 2 - APIs and Program Boundaries](https://medium.com/@DaveLumAI/cs202-episode-2-apis-and-program-boundaries-or-how-software-talks-without-everyone-crying-1da7a2f92fe4)**, we learned that software systems talk through contracts, not through vibes and rummaging.

Now we get to the uncomfortable but extremely useful truth:

Every boundary is also a place where things can go wrong.

And professional software is not software that never fails.

Professional software is software that fails in ways someone planned for.

That may sound less glamorous than "move fast and build amazing things," but it is the difference between a system that bends and a system that turns into confetti because one field was empty.

So let us give our programs a little backbone.

Preferably before production does it with a chair.

---

## **What is error handling?**

Error handling is the part of programming where you decide what your software should do when something does not go according to plan.

That is it.

Not magic. Not pessimism. Not the part where you wrap the whole program in `try` and whisper "please."

Error handling means recognizing that a program can encounter abnormal conditions and should respond deliberately.

Sometimes the response is:

* Try again.
* Show a useful message.
* Use a default value.
* Skip one bad record and continue.
* Log the problem for later investigation.
* Ask the user to fix their input.
* Roll back a failed operation.
* Stop immediately because continuing would be dangerous.

The goal is not to avoid all failure.

The goal is to avoid mystery failure.

A mysterious failure is the kind where the system stops working, nobody knows why, the log file contains one heroic line saying "Error," and three people named Kevin are suddenly being investigated.

Good error handling leaves breadcrumbs.

Bad error handling leaves smoke.

---

## **What is defensive programming?**

Defensive programming is the habit of writing code as if inputs, assumptions, dependencies, and future maintainers may occasionally betray you.

Not because everyone is incompetent.

Because software is a contact sport with time.

The code you write today may be called tomorrow with different data, by a different feature, in a different environment, under different load, after someone upgraded a library because it "only changed a minor version," which is how small fires learn ambition.

Defensive programming means you do not assume everything will be perfect.

You check.

You validate.

You limit damage.

You design your code so a small problem does not become a system-wide interpretive dance of regret.

From **CS101**, **[Programming Fundamentals Part 1 - Variables and Conditionals](https://medium.com/@DaveLumAI/programming-fundamentals-part-1-variables-and-conditionals-aka-teaching-a-computer-to-stop-2d94ab24b91a)** gave us the basic machinery: values and decisions. Error handling is where those decisions start protecting the program from incorrect values, missing values, and values wearing fake mustaches.

From **CS102**, **[Files, Input, and Output](https://medium.com/@DaveLumAI/episode-10-files-input-and-output-or-how-programs-stop-living-entirely-inside-their-own-heads-941dc13d407d)** showed us that once a program interacts with the outside world, it has to deal with the outside world being, frankly, outside. Also from **CS102**, **[Testing and Reliability](https://medium.com/@DaveLumAI/episode-12-testing-and-reliability-or-why-it-worked-once-is-not-a-career-strategy-a50f80c8d6dc)** reminded us that "it worked once" is not a binding treaty.

Defensive programming is what happens when those lessons stop being theory and start wearing steel-toed boots.

---

## **The basic shape of failure**

Before we can handle errors well, we need to stop treating all errors as the same blob of sadness.

There are different kinds of failure, and they deserve different responses.

A recoverable error is a problem the program can reasonably respond to and continue.

For example:

* A user enters an invalid email address.
* A file is temporarily locked.
* A network call times out.
* A search returns no results.
* A request is missing a required field.
* A payment attempt is declined.

These are ordinary failures. Annoying, yes. But ordinary.

A fatal error is a problem that means continuing would be unsafe, meaningless, or corrupting.

For example:

* A required configuration file is missing at startup.
* The database schema is incompatible with the application version.
* A security check fails in a way that suggests tampering.
* The program detects corrupted internal state.
* A critical dependency cannot be initialized.

Fatal errors should not be hidden under the rug.

The rug is already lumpy. Everyone can tell.

The job is to stop cleanly, explain what happened, and avoid making the damage worse.

---

## **The beginner mistake: pretending errors are rare**

When students first learn programming, examples are often polite.

The input is valid.

The file exists.

The function receives what it expects.

The user behaves like a cooperative woodland creature.

This is fine for learning syntax. It is terrible preparation for actual systems.

Real users type things like:

```text
blue
```

into a field labeled "Number of guests."

Real files disappear because paths are wrong, permissions changed, disks filled up, or someone dragged a folder into another folder and then went to lunch.

Real APIs return `500`, `429`, `403`, empty arrays, partial results, stale data, weird time zones, and once in a while an error body that is HTML because the server fell backward into a load balancer.

Real systems are messy because reality has never read your syllabus.

So professional programmers learn to ask:

What can go wrong here?

What should happen when it does?

How will we know?

Can the system recover?

If not, can it fail safely?

That last question matters a lot.

Failing safely means the system does not continue in a way that causes worse damage.

A thermostat that cannot read the temperature should not blast heat forever.

A banking system that cannot confirm a transfer should not just shrug and subtract money twice because apparently confidence is a database strategy.

A medical records system that cannot save a note should not tell the user everything is fine while quietly dropping the data into the void.

Safety is not only about dramatic life-or-death systems. Even ordinary business software needs to avoid silent corruption, confusing behavior, and data loss.

Silent failure is especially nasty.

It smiles at you while stealing your weekend.

---

## **A tiny concrete example**

Let us start with something small.

Imagine a program that calculates a discount percentage.

```python
def apply_discount(price, discount_percent):
    return price - (price * discount_percent / 100)
```

Looks fine.

Very innocent.

Wearing tiny shoes.

But what can go wrong?

* `price` might be negative.
* `discount_percent` might be negative.
* `discount_percent` might be greater than 100.
* One or both values might not be numbers.
* The caller might pass `None`.
* The result might need rounding.
* The business rule might say some products cannot be discounted.

A defensive version might begin like this:

```python
def apply_discount(price, discount_percent):
    if price is None:
        raise ValueError("price is required")

    if discount_percent is None:
        raise ValueError("discount_percent is required")

    if price < 0:
        raise ValueError("price cannot be negative")

    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("discount_percent must be between 0 and 100")

    return round(price - (price * discount_percent / 100), 2)
```

This is not glamorous.

No one is making a movie where the hero checks `discount_percent`.

Although, honestly, I would watch it if the trailer had enough fog.

But this code is better because it makes assumptions explicit.

It does not allow nonsense to quietly become official nonsense.

That is one of the core ideas of defensive programming:

Bad input should be rejected near the entrance, not discovered later in the basement wearing your company hoodie.

---

## **Validation: the polite bouncer at the door**

Validation means checking whether data is acceptable before using it.

It can happen in several places:

* In the user interface.
* In the API layer.
* In business logic.
* Before saving to a database.
* When reading from files.
* When consuming messages from queues.
* When accepting data from another system.

One common misconception is that validation in one place is enough.

It usually is not.

User interface validation is nice because it gives fast feedback.

But UI validation is not security.

Someone can bypass your form and call your API directly. Someone can send data from a script. Someone can replay a request. Someone can be your own future code accidentally making a bad call from inside the system like a raccoon with credentials.

So validation belongs at the boundary where trust changes.

When data crosses from outside to inside, validate it.

When data crosses between services, validate it.

When data comes from a file, validate it.

When data comes from a user, validate it twice and maybe offer it a glass of water.

The point is not paranoia.

The point is that boundaries are where assumptions become dangerous.

---

## **Exceptions: useful tool, terrible lifestyle**

Many languages support exceptions.

An exception is a way for code to signal that something unusual happened and normal execution cannot continue in the usual way.

Example:

```python
try:
    data = load_customer_file("customers.csv")
except FileNotFoundError:
    print("The customer file was not found.")
```

That is a good use of an exception.

The code tries something that may fail, then handles a specific failure.

Specific matters.

This is usually better than:

```python
try:
    data = load_customer_file("customers.csv")
except Exception:
    print("Something went wrong.")
```

That catches everything.

Which sounds safe, but often is not.

Catching every exception is like putting a bucket under the ceiling and declaring the entire plumbing system fixed.

Sometimes broad exception handling is useful at the outer edge of a system, where you need to prevent a crash from showing ugly details to users. But inside your code, broad catches can hide programming mistakes, security problems, data corruption, or failures you absolutely should not ignore.

A good rule:

Catch errors you can meaningfully handle.

Log errors you cannot fully handle.

Do not swallow errors just because they make the room uncomfortable.

Software engineering is full of uncomfortable rooms. Bring snacks.

---

## **The difference between handling and hiding**

This is important enough to say directly:

Handling an error does not mean making it disappear.

Handling an error means responding appropriately.

Bad handling:

```python
try:
    save_order(order)
except Exception:
    pass
```

That `pass` is terrifying.

It says: "If saving the order fails, do nothing."

Not "notify the user."

Not "retry."

Not "log the error."

Not "roll back the transaction."

Just silence.

That code is not resilient. It is wearing a fake mustache and pretending the order went to college.

Better:

```python
try:
    save_order(order)
except DatabaseTimeoutError as error:
    log_error("Order save timed out", error)
    notify_user("We could not save your order yet. Please try again.")
except ValidationError as error:
    notify_user(f"Please fix the order details: {error}")
```

Now the program distinguishes between different failures.

A database timeout and invalid order data are not the same problem. One may be temporary infrastructure trouble. The other may require the user to fix something.

Treating all errors the same is easy.

It is also how systems become confusing.

---

## **Graceful degradation: doing less instead of exploding**

Graceful degradation means that when part of a system fails, the system keeps offering reduced but useful functionality.

For example:

* If recommendations fail, still show the product page.
* If avatar images fail, show initials.
* If analytics cannot load, do not block checkout.
* If a search enhancement fails, fall back to basic search.
* If a third-party shipping estimator is down, explain that estimates are temporarily unavailable.

This is a practical design skill.

Not every failure should stop the whole system.

If the weather widget on a travel site fails, users should still be able to book a hotel. Unless the site is literally selling weather, in which case we have other problems.

The hard part is deciding what is essential.

A login system should not gracefully degrade into "everyone is admin now."

That is not graceful. That is a cybersecurity piñata.

So graceful degradation requires judgment.

Ask:

What parts are optional?

What parts are required?

Can we safely continue without this dependency?

What should users see?

What should operators know?

This connects directly to API boundaries. When one service depends on another, you need a plan for what happens when the other service is slow, unavailable, or returns nonsense with confidence.

---

## **Retries: useful, dangerous, and often overconfident**

One common response to failure is retrying.

This can be smart.

Networks hiccup. Temporary failures happen. Cloud services sometimes sneeze. A retry may succeed a moment later.

But retries are not free.

Too many retries can make an outage worse. If a service is already struggling, thousands of clients retrying aggressively can turn a small failure into a stampede wearing logging badges.

Good retry behavior usually includes:

* A limited number of attempts.
* A delay between attempts.
* Backoff, where delays increase after each failure.
* Jitter, where random variation prevents every client from retrying at the same moment.
* Clear logging.
* Knowing which operations are safe to retry.

That last one is a big deal.

Reading data is often safe to retry.

Charging a credit card is not something you casually retry like refreshing a browser tab while muttering at the clouds.

This leads to the concept of idempotency.

An idempotent operation can be performed more than once and still have the same effect as doing it once.

For example, setting a user email address to a specific value can be idempotent.

Adding $10 to an account balance is not idempotent unless carefully designed.

This matters because error handling is not just about the line where the error happens. It is about system behavior over time.

One timeout may leave you uncertain.

Did the operation fail?

Did it succeed but the response got lost?

Should you try again?

Should you check status first?

These are real engineering questions, not small-print trivia.

---

## **A more realistic example: processing uploaded files**

Imagine a web application where users upload CSV files containing customer records.

The system needs to:

1. Accept the file.
2. Validate the format.
3. Parse rows.
4. Save valid customers.
5. Report invalid rows.
6. Avoid importing duplicates.
7. Avoid losing the whole upload because one row contains a birthday written as "Tuesday-ish."

A naive approach might be:

```python
rows = parse_csv(file)

for row in rows:
    customer = create_customer(row)
    save_customer(customer)

show_message("Upload complete")
```

That works beautifully in the imaginary world where every CSV file was raised by librarians.

Now let us think defensively.

What can go wrong?

* The file is missing.
* The file is too large.
* The file is not really a CSV.
* The file encoding is weird.
* A row is missing required fields.
* A date has an invalid format.
* An email is malformed.
* A duplicate customer already exists.
* The database fails halfway through.
* The user uploads the same file twice.
* The process takes too long.
* A later system expects fields this importer forgot to validate.

A better design would separate concerns:

* Validate file type and size before parsing.
* Parse rows carefully and collect row-level errors.
* Validate each record before saving.
* Use transactions where appropriate.
* Avoid saving partial data silently.
* Make duplicate behavior explicit.
* Return a useful import report.
* Log technical details for maintainers.
* Show user-friendly messages for the human who just wants to go home.

The output might say:

```text
Upload processed.

347 customers imported.
12 rows skipped.

Row 18: Missing email address.
Row 44: Invalid date format.
Row 91: Duplicate customer ID.
```

That is much better than:

```text
Error.
```

"Error" is not a message.

It is a shrug with a keyboard.

Good error handling respects both audiences:

The user needs to know what to do next.

The developer or operator needs to know what went wrong.

Those are not always the same message.

Showing a user a raw stack trace is rude. Also unsafe. Also very much the software equivalent of opening the pantry and letting guests see where the chaos lives.

But logging only "user upload failed" is not enough for the person who has to fix it.

Good systems separate public explanation from internal diagnosis.

---

## **Logging: because future you deserves evidence**

A log is a record of what happened.

When errors occur, logs help answer questions like:

* What failed?
* When did it fail?
* Which user or request was involved?
* What input or state was relevant?
* Was this failure isolated or widespread?
* Did it start after a deployment?
* Is a dependency unavailable?
* Is someone doing something suspicious?

Good logs are specific.

Bad logs are theatrical but useless.

This is bad:

```text
Something broke.
```

This is better:

```text
Payment authorization failed: provider timeout, order_id=84722, attempt=2
```

Do not log secrets.

Do not log passwords.

Do not log full credit card numbers.

Do not log private data just because your debugging brain got hungry.

Logging should help investigation without creating a new security problem wearing a tiny detective hat.

Modern systems often use structured logging, where logs include fields like request ID, user ID, service name, error code, and duration. That makes logs searchable and useful across multiple services.

In cloud-era systems, this matters because a single user action might involve:

* A web frontend.
* An API.
* An authentication service.
* A database.
* A queue.
* A background worker.
* A storage bucket.
* A third-party provider.
* A monitoring tool quietly judging everyone.

Without good logging and correlation IDs, debugging distributed systems becomes archaeology, but with more caffeine.

---

## **Defensive design at API boundaries**

Since CS202 just covered APIs, let us connect the dots.

An API boundary should make promises.

But defensive software also knows that promises can be misunderstood, broken, or changed by someone who thought the word "optional" was decorative.

When consuming an API, do not assume:

* Every field is present.
* Every field has the expected type.
* Every response is successful.
* Every failure looks the same.
* Every response arrives quickly.
* Every version behaves forever.
* Documentation and reality are currently speaking.

When exposing an API, do not assume:

* Clients send valid data.
* Clients respect rate limits.
* Clients handle errors correctly.
* Clients understand your response format.
* Clients update when you change things.
* Clients are friendly.

This is why good APIs return clear status codes, useful error messages, stable schemas, and predictable behavior.

For example, if a client submits invalid data, an API should not return:

```json
{
  "success": false
}
```

That is barely a fortune cookie.

Better:

```json
{
  "error": {
    "code": "INVALID_EMAIL",
    "message": "Email address is not valid.",
    "field": "email"
  }
}
```

Now the client can help the user fix the problem.

That is the difference between a system that merely refuses and a system that participates in recovery.

---

## **Failure modes: the shapes trouble likes to wear**

A failure mode is a specific way a system can fail.

Thinking in failure modes helps you design before the problem happens.

For example, in a login system:

* The password is wrong.
* The username does not exist.
* The account is locked.
* The authentication service is down.
* The database is slow.
* The session store fails.
* The user has too many attempts.
* The login succeeds but redirect fails.
* The user exists but lacks permission.

Each failure mode may require a different response.

Security matters here.

For login, you may not want to tell an attacker whether the username exists. So the user-facing message might be intentionally vague:

```text
Invalid username or password.
```

But internally, logs may record a more specific reason.

This is one of the tradeoffs:

Useful errors help real users.

Overly detailed errors can help attackers.

So error handling is not only a programming concern. It is also a product, security, and operations concern.

Congratulations. Your error message has stakeholders.

Try not to cry into the keyboard. It makes the keys weird.

---

## **Misconception: defensive code is just more code**

Defensive programming does add code.

But not all added code is clutter.

Some code expresses business rules.

Some code protects assumptions.

Some code prevents corruption.

Some code makes failure understandable.

The problem is not "more code."

The problem is code that checks the wrong things, hides the wrong errors, duplicates logic everywhere, or turns simple functions into panic bunkers.

Defensive programming should make code clearer, not more paranoid.

For example, this is reasonable:

```python
if quantity <= 0:
    raise ValueError("quantity must be greater than zero")
```

This is less reasonable:

```python
if quantity is not None and quantity != "" and quantity != "banana" and quantity != []:
    try:
        quantity = int(quantity)
    except:
        try:
            quantity = float(quantity)
        except:
            quantity = 1
```

That code is not defensive.

That code is negotiating with soup.

A better approach is to validate input at the boundary, convert it once, and pass clean data inward.

Clean boundaries reduce defensive clutter inside the system.

This is where good design and good error handling support each other.

---

## **Misconception: crashing is always bad**

Crashing is not always bad.

Sometimes stopping is the correct choice.

If a program detects that its configuration is missing, it should probably fail fast at startup. Running with guessed configuration can be worse than not running.

If internal state is corrupted, continuing may spread damage.

If a security invariant is violated, stopping may be safer than improvising.

This is called failing fast.

Fail fast means the program detects unrecoverable problems early and stops clearly, instead of limping onward while making the situation harder to diagnose.

The trick is knowing when to fail fast and when to recover.

A missing optional profile picture? Recover.

A missing database password? Fail fast.

A bad row in a bulk import? Maybe skip the row and report it.

A corrupted transaction ledger? Stop before your accounting system becomes modern art.

There is no universal answer.

There are tradeoffs.

Professional software design is full of tradeoffs.

Anyone who says otherwise is probably selling a framework.

---

## **Misconception: users need technical details**

Users need useful details.

Developers need technical details.

These are different species of information.

Bad user message:

```text
NullReferenceException at CustomerController.cs line 184.
```

The user does not know what that means, and now they are afraid your software is haunted.

Better user message:

```text
We could not load this customer record. Please refresh and try again.
```

Better internal log:

```text
Null customer profile in CustomerController.GetProfile, customer_id=49281, request_id=f6a8
```

The user gets an action.

The developer gets a clue.

Everyone gets a better afternoon.

---

## **Misconception: AI-generated code handles this for you**

Modern AI coding tools can produce useful code quickly.

They can also produce code that looks confident while forgetting edge cases, swallowing exceptions, skipping validation, or assuming the sample data is the universe.

That does not make AI bad.

It means you still need engineering judgment.

When using AI tools, ask for:

* Input validation.
* Error cases.
* Retry behavior.
* Logging strategy.
* Test cases for failure paths.
* Safe handling of missing or malformed data.
* Clear separation between user-facing messages and internal logs.

Do not only ask, "Can you write the function?"

Ask, "What can go wrong with this function, and how should it behave?"

That is a much better prompt.

It turns the tool from a code vending machine into a design assistant with fewer crumbs in the output tray.

---

## **The practical checklist**

When you write or review code, ask these questions:

What assumptions does this code make?

Are those assumptions checked?

What happens if input is missing, malformed, too large, too small, duplicated, late, stale, or hostile?

What happens if a dependency is slow or unavailable?

Can this operation be safely retried?

If this fails halfway through, what state is left behind?

What does the user see?

What does the log record?

Could this expose sensitive information?

Could this error be handled closer to where it occurs?

Could handling it here hide a deeper bug?

Will future maintainers understand what happened?

That last one is not sentimental.

Future maintainers include you.

And future you has less patience than you think.

---

## **How this connects to what comes next**

Error handling and defensive programming are not isolated skills.

They are part of the foundation for everything that follows in CS202.

When we get to refactoring, we will need to preserve behavior while improving structure. Good error handling makes behavior visible.

When we get to build systems and dependency management, failures become more interesting because your software depends on packages, compilers, environments, and configuration files with strong opinions.

When we get to debugging at scale, the difference between useful logs and vague sadness becomes enormous.

When we get to software engineering as a team sport, error handling becomes a shared language. Teams need conventions for exceptions, validation, logging, monitoring, retries, and user-facing messages.

This also connects backward into **CS201**. In **[Processes, Threads, and Concurrency Basics](https://medium.com/@DaveLumAI/episode-6-processes-threads-and-concurrency-basics-or-how-one-machine-does-many-things-at-once-6ef3836f4ebf)**, we saw that multiple things happening at once can create timing failures, race conditions, and state surprises. In **[Operating Systems in Plain English](https://medium.com/@DaveLumAI/episode-7-operating-systems-in-plain-english-or-the-adult-in-the-room-that-keeps-programs-from-a267d108394c)**, we saw that programs depend on the operating system for files, memory, permissions, processes, and hardware access.

All of those layers can fail.

Not because they are bad.

Because systems are made of parts, and parts have edges.

Edges are where engineering happens.

---

## **The big idea**

Error handling is not about being negative.

It is about being honest.

Defensive programming is not about distrusting everyone.

It is about respecting the fact that software lives in a world full of users, networks, files, services, hardware, permissions, timeouts, upgrades, and one person who will paste an entire spreadsheet into the first-name field because no one stopped them.

Your program does not need to predict every disaster.

But it should handle ordinary trouble like it has been outside before.

It should validate what enters.

It should distinguish recoverable errors from fatal ones.

It should fail safely.

It should explain problems clearly.

It should log enough evidence to help someone fix things later.

It should avoid turning one broken assumption into a parade.

Because hope is not an exception strategy.

Hope is fine for birthday candles, weather forecasts, and opening the refrigerator when you know perfectly well there is no pie.

But software needs something sturdier.

Software needs design.

So check your inputs.

Handle your errors.

Write the message.

Log the evidence.

And when the universe hands your program a banana where a date should be, let your code respond like a professional.

Not like a toaster in a thunderstorm.

---

## [**Art Prompt (Lowbrow Art / Pop Surrealism):**](https://lumaiere.com/?gallery=surrealism4)

A whimsical pop surrealist garden scene with a giant glossy-eyed porcelain rabbit resting beneath oversized candy-colored mushrooms, tiny floating teacups, glowing fruit, and delicate vines curling through a dreamlike forest clearing. Use creamy pastels, strawberry reds, pale mint greens, soft ivory highlights, and polished enamel-like surfaces, with an uncanny but charming mood, precise decorative detail, rounded toy-like forms, and a sense of innocent wonder slightly tilted into the strange. Keep it family-friendly, painterly, richly textured, and free of text, logos, modern devices, recognizable faces, or frightening elements.

## [**Video Prompt:**](https://www.tiktok.com/@davelumai/video/7646070478032997663)

Start with a bright snap of motion as the porcelain rabbit blinks, the mushrooms gently bounce like soft drums, and tiny teacups orbit in playful spirals through the glowing garden. Fruit lanterns pulse in rhythm, vines curl and uncurl like animated filigree, and the camera darts between glossy details with energetic short-form timing. Add quick match cuts from mushroom caps to teacup rims to sparkling dew, ending on the rabbit lifting one paw as the whole surreal clearing shimmers warmly.

## **Song Recommendations:**

Walking on Sunshine - Katrina and the Waves

Pump It Up - Elvis Costello & The Attractions

Follow for more art, code, and suspiciously useful computer science. And comment with the weirdest error message you have ever seen, because somewhere out there a program is still saying "unexpected banana" and meaning it.
