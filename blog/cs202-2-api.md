# CS202 Episode 2: APIs and Program Boundaries, or How Software Talks Without Everyone Crying

At some point, your program has to stop living alone.

In CS101, it was mostly you and the code. A variable here. A loop there. A function bravely trying to keep the place tidy. Then CS102 arrived and said, “Wonderful, now let us talk about decomposition, abstraction, testing, state, files, and all the ways your program can behave differently after lunch.”

Now we are in CS202, which is where software begins to look less like a single assignment and more like a neighborhood.

And neighborhoods need boundaries.

Not walls, exactly. More like doors. Mailboxes. Street signs. Agreements. A polite little system of “you can ask me for this, but please do not climb through my window holding raw JSON and vibes.”

That is what APIs are about.

An API, or Application Programming Interface, is a boundary where one piece of software offers a controlled way for another piece of software to interact with it. Not by rummaging through its private drawers. Not by guessing how its internal organs are arranged. But through a defined interface: a promise about what you can ask for, what you must provide, and what you can expect back.

This is one of the great turning points in software design.

Because once programs begin talking to other programs, the problem is no longer just “does my code work?”

Now the problem is:

Can other people use it?

Can future me understand it?

Can another system depend on it without developing a twitch?

Can we change the inside without breaking everyone standing outside with a clipboard and production traffic?

Lovely. The village has formed. Someone immediately opened a ticket.

## The Smallest Useful Idea: A Boundary

Let us start with the simplest possible version.

Imagine you write a function:

```python
def calculate_total(price, tax_rate):
    return price + (price * tax_rate)
```

That function has a boundary.

The outside world knows:

* It is called `calculate_total`
* It needs a `price`
* It needs a `tax_rate`
* It returns a total

The outside world does not need to know whether the calculation happens in one line, three lines, or with a tiny committee of arithmetic goblins wearing visors.

That is the point.

A boundary separates what something does from how it does it.

This connects directly back to CS102, especially [Episode 11 - Modular Design and Abstraction](https://medium.com/@DaveLumAI/episode-11-modular-design-and-abstraction-or-how-to-make-your-code-less-like-a-junk-drawer-9b6273bc3721), where we talked about splitting programs into understandable parts. APIs are what make those parts usable from the outside.

A module without a clear interface is just a room full of furniture with no doors.

Technically it exists.

Emotionally, no thank you.

## API Does Not Always Mean Web API

One common beginner mistake is thinking “API” automatically means “some URL on the internet that returns curly braces.”

That is one kind of API, and a very important one.

But the broader idea is older and bigger.

A function can have an API.

A class can have an API.

A library can have an API.

An operating system has APIs.

A database driver has an API.

A browser has APIs.

A payment processor has APIs.

A cloud service has APIs.

Your toaster probably has an API now, because apparently the appliances union lost a bet.

The MDN glossary gives a useful general definition of an API as a set of features and rules that allow interaction with software through code rather than through a human interface: [API - MDN Web Docs](https://developer.mozilla.org/en-US/docs/Glossary/API).

That definition matters because it keeps us from shrinking the idea too much.

An API is not “a website endpoint.”

An API is a contract.

And once you see it as a contract, the whole topic becomes much more interesting.

Also slightly more legally haunted, but only in spirit.

## Contracts: The Heart of the Whole Thing

A good API says:

Give me this kind of input.

I will give you this kind of output.

Here are the rules.

Here is what happens when things go wrong.

Here is what you should not assume.

That last one is where many disasters are born.

Let us use a tiny example.

Suppose we have a function:

```python
def get_student_grade(student_id):
    ...
```

What does this function promise?

At minimum, we need to know:

* What type is `student_id`?
* Can it be a number?
* Can it be a string?
* What happens if the student does not exist?
* Does the function return a letter grade, a percentage, or a full grade object?
* Can it return `None`?
* Can it throw an exception?
* Does it read from a database?
* Is it slow?
* Is it safe to call repeatedly?

The function name helps, but the function name is not the whole contract.

Names are wonderful. Names are not legally binding enough to protect production.

A weak contract says:

```python
grade = get_student_grade(id)
```

Good luck, little developer. May your assumptions be less terrible than usual.

A stronger contract says:

```python
def get_student_grade(student_id: str) -> dict:
    """
    Returns a grade record for an existing student.

    Raises StudentNotFoundError if no student exists.
    Returns:
        {
            "student_id": str,
            "course_id": str,
            "letter": str,
            "percentage": float
        }
    """
```

Now we are getting somewhere.

The code has not magically become perfect, but the boundary is less foggy.

And fog is where bugs wear tiny sneakers.

## Inputs, Outputs, and Assumptions

Every API lives on three things:

Input.

Output.

Assumptions.

Inputs are what the caller must provide.

Outputs are what the API gives back.

Assumptions are the invisible rules that will ruin your afternoon if nobody writes them down.

For example, consider this API:

```python
create_user(email, password)
```

Looks simple.

But what are the assumptions?

Is the email already validated?

Can the password be empty?

Is the email case-sensitive?

Does this send a welcome email?

Does it create a billing profile too?

Does it return the new user?

Does it return only an ID?

Does it fail if the email already exists?

Does it hash the password?

Please say yes.

Does it log anything?

Does it trigger analytics?

Does it behave differently in development and production?

A beginner often thinks the function name is enough.

An experienced developer knows the name is the beginning of the negotiation.

This is why API design is not just syntax. It is communication. It is software architecture with manners.

## A Concrete Example: Weather, But Small

Let us say we want to build a little weather app.

The user interface needs to show the current temperature.

Somewhere else, we have a weather service that knows how to get that information.

Without a clean boundary, the UI might do everything directly:

```javascript
// Not great
const apiKey = "secret-key";
const response = await fetch(
  "https://weather.example.com/data?city=Tampa&units=imperial&key=" + apiKey
);
const raw = await response.json();
document.querySelector("#temperature").textContent = raw.current.temp_f + " F";
```

This works.

That is the dangerous part.

Working code can still be badly shaped code. A raccoon can open a trash can, but we should not make it the facilities manager.

Here the UI knows too much:

* It knows the weather provider URL
* It knows the API key exists
* It knows the provider’s raw response format
* It knows where temperature lives inside that response
* It knows the units
* It knows how to fetch and display at the same time

Now imagine the weather provider changes `temp_f` to `temperatureFahrenheit`.

Congratulations. Your UI just got punched by a detail it should never have met.

A cleaner design puts a boundary between the UI and the weather service:

```javascript
async function getCurrentTemperature(city) {
  const response = await fetch(`/api/weather/current?city=${encodeURIComponent(city)}`);

  if (!response.ok) {
    throw new Error("Could not load weather");
  }

  const data = await response.json();

  return {
    city: data.city,
    temperature: data.temperature,
    unit: data.unit
  };
}
```

Now the UI can say:

```javascript
const weather = await getCurrentTemperature("Tampa");
document.querySelector("#temperature").textContent =
  `${weather.temperature} ${weather.unit}`;
```

Much better.

The UI now depends on our local boundary, not the entire messy universe beyond it.

This is one of the deep reasons APIs matter: they control dependency.

And dependency is where software relationships go from “cute” to “we need a meeting.”

## Function APIs vs Service APIs

A function API is usually inside a program or library.

A service API is usually across a process, machine, or network boundary.

That difference matters.

A function call might look like this:

```python
total = calculate_total(19.99, 0.07)
```

A service call might look like this:

```http
GET /orders/12345
```

Or:

```http
POST /users
Content-Type: application/json

{
  "email": "student@example.com",
  "name": "Ada"
}
```

The ideas are related, but the consequences are different.

A function call is usually fast, local, and controlled by the same codebase.

A service call may cross the network. It may fail because the other service is down. It may time out because the internet is having one of its little emotional weather events. It may be rejected because the caller is not authorized. It may return old data because caching exists. It may succeed but take long enough for the user to wonder if the button has entered witness protection.

That is why service APIs require more design around failure.

This connects nicely to CS202 Episode 3, which comes next: Error Handling and Defensive Programming. APIs and error handling are dance partners, though one of them is always stepping on the other’s foot.

## The Network Is Not a Hallway

When code calls another service, beginners often imagine it like walking down the hall and asking a coworker a question.

It is not that.

It is more like sealing a request in a bottle, throwing it into the ocean, and hoping a different building reads it, understands it, has permission to answer it, answers it correctly, and throws the bottle back before your user starts clicking the button repeatedly like a woodpecker with billing anxiety.

Network calls introduce problems that local function calls usually do not:

* Latency
* Timeouts
* Partial failure
* Authentication
* Authorization
* Rate limits
* Version mismatches
* Serialization and deserialization
* Security concerns
* Observability problems
* Backward compatibility

This is why service APIs need more explicit contracts than ordinary functions.

If you are calling a function inside your own program and something is unclear, you can inspect the code. Maybe complain gently. Maybe complain loudly. Depends on the day.

If you are calling a third-party payment API, you do not get to rummage through their source code and “just see what happens.”

You get documentation.

You get request formats.

You get response formats.

You get error codes.

You get terms of service.

You get a sandbox environment.

And if you are lucky, you get examples that are not from the Bronze Age of JavaScript.

## REST, GraphQL, RPC, and the Shape of Asking

There are several common styles for service APIs.

REST is one of the most common web API styles. It usually organizes the world around resources like users, orders, products, and invoices. A helpful starting point is [What is REST?](https://restfulapi.net/).

A REST-like API might say:

```http
GET /users/42
```

That means:

Please retrieve user 42.

Or:

```http
POST /users
```

That means:

Please create a new user using the data in this request.

This style works well when your system naturally looks like resources.

GraphQL takes a different approach. Instead of hitting many resource endpoints, the client describes the shape of the data it wants. The official introduction is here: [GraphQL Learn](https://graphql.org/learn/).

A GraphQL query might ask for:

```graphql
{
  user(id: "42") {
    name
    email
    recentOrders {
      id
      total
    }
  }
}
```

This can be powerful when clients need flexible data shapes, especially in front-end applications.

RPC-style APIs are more action-oriented. Instead of focusing on resources, they often look like calling named operations:

```http
POST /calculateShipping
```

or

```http
POST /sendPasswordResetEmail
```

None of these styles is automatically “the one true way.”

REST can be simple and cache-friendly, but can become awkward when the client needs many related things at once.

GraphQL can reduce over-fetching and under-fetching, but it adds its own complexity around schemas, performance, authorization, caching, and query control.

RPC can feel direct and natural for actions, but it can become a grab bag of verbs if nobody maintains discipline.

The grown-up answer is not “always use X.”

The grown-up answer is “what boundary are we designing, who will call it, what will change, and what failure modes are we willing to manage?”

Software engineering: where “it depends” is not a dodge, it is the weather report.

## A More Realistic Example: The Online Store

Let us imagine a small online store.

At first, everything is in one application:

* Product catalog
* Shopping cart
* Checkout
* Payment
* Shipping
* Email receipts
* Admin dashboard

This is fine early on.

One codebase. One database. One deployment. One place to stare when things combust.

But as the store grows, boundaries start to matter.

Maybe payment processing should be isolated because it has security and compliance concerns.

Maybe inventory should be its own service because warehouses and storefronts both need it.

Maybe email sending should be handled asynchronously because nobody wants checkout to fail because the receipt service sneezed.

Eventually you might have APIs like:

```http
GET /products/abc123
```

```http
POST /cart/items
```

```http
POST /checkout
```

```http
POST /payments/authorize
```

```http
POST /shipments
```

Each boundary is a design choice.

And each choice creates tradeoffs.

Separating payment from checkout can make the system safer and easier to reason about. It can also introduce network failures, retries, monitoring needs, and versioning problems.

Keeping everything together is simpler. Until it is not.

Splitting everything apart is flexible. Until your system becomes a parade of tiny services yelling across the network while the user waits for a spinner to finish reconsidering its life.

The goal is not maximum separation.

The goal is useful separation.

Boundaries should reduce confusion more than they create coordination cost.

That sentence is worth taping to a monitor, preferably the one currently displaying 47 microservices named things like `core-common-shared-utils-service`.

## The Boundary Is Also a Security Line

APIs are not only about organization.

They are also about control.

A good API decides what callers are allowed to do.

For example, a user profile API might allow this:

```http
PATCH /users/me
```

with:

```json
{
  "displayName": "Ada"
}
```

But it should not allow this:

```json
{
  "isAdmin": true
}
```

Unless your business model is “accidentally appoint strangers to management.”

The API boundary must enforce rules.

Never trust the client just because the front end hid a button.

The front end is not a security boundary. It is a suggestion with CSS.

Anyone can send a request directly if they know how. That means the API must check:

* Who is making the request?
* Are they authenticated?
* Are they allowed to do this?
* Is the input valid?
* Is the requested operation safe?
* Is the output leaking anything private?

Security lives at the boundary because the boundary is where the outside world arrives wearing shoes.

## Versioning: Because Someone Is Already Depending on You

The moment another system depends on your API, change becomes harder.

Inside a private function, you can sometimes rename a parameter or change a return value and update all callers at once.

But with a public service API, callers may be:

* Mobile apps that users have not updated
* Partner systems
* Internal teams on different release schedules
* Scripts nobody remembers until they fail loudly
* A dashboard built by someone who left three reorganizations ago

Changing an API without warning can break all of them.

This is why API versioning exists.

You might see URLs like:

```http
GET /v1/orders/12345
```

Then later:

```http
GET /v2/orders/12345
```

Versioning gives teams a way to improve an API without immediately breaking everyone who depends on the old contract.

But versioning has a cost. Supporting old versions means more code, more tests, more documentation, and more chances for inconsistency.

So the best API change is often the one that preserves compatibility:

Add a new optional field.

Do not remove an old field too soon.

Do not change the meaning of existing fields casually.

Do not turn a string into an object unless you enjoy surprise meetings.

If you must break compatibility, announce it clearly, provide migration time, and document the change like you care about the people reading it.

Because you should.

They are probably you in six months with worse sleep.

## Documentation Is Part of the API

Documentation is not a decorative brochure.

Documentation is part of the interface.

If the code behaves one way and the docs describe another, your API now has two contracts and both are suspicious.

For service APIs, specifications like the [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) can describe endpoints, parameters, request bodies, response formats, authentication rules, and error responses in a structured way.

That helps humans understand the API.

It also helps tools generate clients, documentation, tests, mocks, and validation.

This is especially relevant in modern software teams where APIs are often consumed by front-end developers, mobile developers, back-end developers, QA engineers, cloud workflows, integration partners, and increasingly AI-assisted tools.

Clear API documentation gives both humans and tools a safer surface to work with.

Bad documentation, on the other hand, gives everyone a scavenger hunt and a mood disorder.

## AI Workflows Make API Design More Important, Not Less

Modern AI coding tools can generate client code, server stubs, tests, documentation, and examples very quickly.

That is useful.

It also means unclear boundaries can turn into unclear code at thrilling speed.

An AI assistant can help you call an API, but it still needs a contract to work from.

If your API has consistent naming, explicit schemas, examples, clear error behavior, and stable versioning, AI-assisted development becomes much more reliable.

If your API returns `status: "ok"` for success, `status: "OK"` on Tuesdays, and `status: 1` when the moon is judgmental, the model may still produce code.

The code may even look confident.

Confidence is not correctness. Computers taught us that. Repeatedly. With enthusiasm.

Good APIs are legible to humans, machines, tests, documentation generators, and future maintainers who have not yet had coffee.

That is not a small achievement.

## Common API Failure Modes

Let us talk about the classic traps.

The first trap is exposing too much.

If outside callers depend on your internal structure, you lose the freedom to change it. This is why APIs should reveal what callers need, not everything the system happens to know.

The second trap is hiding too much.

If the API is so vague that callers must guess what happened, they will guess. Then they will build logic around the guess. Then everyone will pretend this was a requirement.

The third trap is inconsistent naming.

If one endpoint says `userId`, another says `user_id`, and a third says `customerNumber`, someone will eventually build a translation layer that looks like a haunted dictionary.

The fourth trap is unclear errors.

Bad:

```json
{
  "error": "Something went wrong"
}
```

Better:

```json
{
  "error": "INVALID_EMAIL",
  "message": "Email address is not valid."
}
```

Best depends on the audience, but the principle is simple: callers need enough information to respond intelligently without exposing sensitive internals.

The fifth trap is pretending the happy path is the whole path.

APIs need to define what happens when:

* Input is missing
* Input is malformed
* A resource does not exist
* The caller is not logged in
* The caller lacks permission
* The system is temporarily unavailable
* The request is duplicated
* A timeout happens after partial work

If your API only makes sense when everything goes perfectly, it is not designed yet. It is merely optimistic.

And optimism is not a retry strategy.

## The Deep Theory Beneath the Practical Stuff

Underneath all this is one of the most important ideas in computing:

Abstraction.

An abstraction hides unnecessary detail behind a useful interface.

In CS101, [Episode 3 - Programming Fundamentals Part 2: Loops and Functions](https://medium.com/@DaveLumAI/episode-3-loops-and-functions-or-how-to-stop-copy-pasting-yourself-into-madness-fac07f2d1bc4) introduced functions as reusable chunks of behavior. That was the beginner version of this idea.

In CS102, [Episode 14 - Intro to Object-Oriented and Alternative Design Styles](https://medium.com/@DaveLumAI/episode-14-intro-to-object-oriented-and-alternative-design-styles-or-why-not-every-problem-needs-60bd09afa968) expanded the conversation into different ways of organizing responsibilities.

Now CS202 asks a sharper question:

How do we design boundaries so people can build large systems without needing to understand every internal detail at once?

That is the intellectual core of APIs.

A good API reduces cognitive load.

It lets one developer think about checkout without also thinking about the internal table structure of the inventory database.

It lets one team change how shipping rates are calculated without forcing the front end to rewrite half its soul.

It lets systems evolve.

And software that cannot evolve eventually becomes archaeology with a login screen.

## A Tiny Design Checklist

When designing an API, ask these questions:

What is the caller trying to accomplish?

What inputs are required?

What inputs are optional?

What output will be returned?

What errors can happen?

Who is allowed to call this?

What assumptions must be true?

What should remain hidden?

What might change later?

How will callers know what changed?

That checklist applies to a function, a class, a library, a service, a cloud endpoint, or a command-line tool.

Different scale. Same discipline.

The boundary is where your design becomes visible.

Make it kind.

Make it boring in the best way.

Make it predictable enough that nobody has to read your mind, because mind-reading does not compile reliably.

## Where This Fits in the Course

CS202 Episode 1 covered version control and change management: how teams remember what changed and who invited the raccoon into the ventilation system.

Episode 2 is the next natural step because teams do not just share code history. They share responsibilities.

APIs are how one part of a system says to another:

Here is what I do.

Here is how to ask.

Here is what I promise.

Here is what I refuse to let you touch.

Next, Episode 3 will move into error handling and defensive programming, because every boundary must decide what happens when the other side sends nonsense, arrives late, lacks permission, or asks for a student record using a sandwich.

Later, refactoring will teach us how to improve boundaries after they already exist.

Build systems will teach us how all these parts become runnable software.

Debugging at scale will teach us what happens when the bug is not inside one component but between several components all technically doing what they were told.

And team software engineering will remind us that APIs are not only technical artifacts. They are collaboration tools.

They are where one team’s clarity becomes another team’s productivity.

Or one team’s chaos becomes another team’s calendar invite.

Choose wisely.

## The Big Takeaway

An API is not just a way to call code.

It is a boundary.

It is a contract.

It is a design decision about what one part of a system is allowed to know about another.

Good APIs make software easier to change, easier to test, easier to secure, easier to document, and easier to use.

Bad APIs make everyone whisper, “Just don’t touch that part,” which is how codebases become haunted real estate.

So when you design an API, do not merely ask:

Can I make this work?

Ask:

Can someone else use this correctly?

Can they recover when it fails?

Can I change the inside later without breaking the outside?

Can the contract survive contact with real software, real people, real teams, and real deadlines?

That is where software design begins to grow up.

Not because it becomes less weird.

It absolutely does not.

But because the weirdness gets boundaries.

And boundaries, dear reader, are how we keep the chaos from wandering into the kitchen and renaming all the variables.

Follow along for the rest of CS202, comment with the worst API naming crime you have personally survived, and if you know someone who thinks “the API is obvious” counts as documentation, please send them this before they hurt themselves or a junior developer.

**[Art Prompt (Hudson River School):](https://lumaiere.com/?gallery=hudson-river)**

A sweeping nineteenth-century American landscape with a high overlook above a winding river valley after a passing storm, one side filled with dark receding clouds, rain-washed forest, and rugged shadowed hills, the other side opening into golden sunlight, cultivated fields, and a bright bend of water stretching toward the horizon. Use luminous greens, deep browns, pearl grays, warm ochres, pale blue sky, and radiant late-afternoon highlights. The composition should feel grand, contemplative, and balanced between wilderness and settlement, with crisp atmospheric depth, dramatic cloud architecture, tiny distant details, and a sense of nature recovering its breath. Keep it painterly, majestic, family-friendly, and richly textured, with no modern buildings, no text, and no recognizable people.

**[Video Prompt:](https://www.tiktok.com/@davelumai/video/7644381017997839646)**

Create a short-form vertical video based on the sweeping river valley landscape. Start with fast-moving storm clouds breaking apart over the dark forested hills, then have sunlight race across the valley like a golden ribbon, lighting the river bend, fields, treetops, and distant horizon in quick dramatic pulses. Add drifting mist, shimmering water reflections, small birds lifting from the trees, and a final bright reveal where the whole valley glows between storm and calm. Keep the motion cinematic, rhythmic, painterly, and eye-catching, with no text, no modern elements, and no recognizable people.

Song recommendations for the video:

Mountain at My Gates – Foals

Safe and Sound – Capital Cities
