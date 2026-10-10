# ChatGPT Plugins: How to Survive December 11 Without Giving Away the Secret Recipe

December 11, 2026 is getting closer.

Custom GPTs are scheduled to retire, and the replacement path is ChatGPT plugins.

I already covered the basic migration story in [Custom GPTs Are Retiring: What Plugins Are, What Migration Actually Does, and Why December 11 Just Became Homework](https://medium.com/@DaveLumAI/custom-gpts-are-retiring-what-plugins-are-what-migration-actually-does-and-why-december-11-just-349f390799e4?sharedUserId=DaveLumAI).

That answered the first question:

**What am I supposed to do with my GPT?**

Migrate it.

Wonderful.

Then I thought about the second question.

**Wait. My GPT contains proprietary instructions. How do I turn those into a plugin without effectively stapling my secret recipe to the front door?**

Ah.

There is the fun part.

Because migrating a GPT and building a *secure* plugin are not necessarily the same project.

And suddenly December 11 has become less of a deadline and more of a small figure standing on the horizon, pointing at a calendar and laughing.

## First, What Exactly Is Inside a ChatGPT Plugin?

The [official OpenAI plugin documentation](https://developers.openai.com/plugins) describes plugins as packages that can combine several pieces.

The two particularly important ones are:

- **Skills**
- **MCP servers**

A [skill](https://developers.openai.com/plugins/concepts/skills) contains instructions and resources that teach ChatGPT how to perform a particular workflow.

An [MCP server](https://developers.openai.com/plugins/concepts/mcp-server) provides tools that ChatGPT can call to retrieve information or perform actions.

That distinction matters enormously.

Think of a skill as:

"Here is how I want you to do the job."

Think of an MCP server as:

"Call me when you need the machinery that actually does the job."

And if part of your machinery happens to be something you do not want wandering around the Internet wearing a name tag, the second option becomes very interesting.

## Here Is the Security Problem

When you migrate a custom GPT, OpenAI says the GPT's instructions become a skill in the new plugin.

That sounds wonderfully convenient.

It also caused me to stare suspiciously at the word "instructions."

Because those instructions may contain things like:

- Specialized workflows
- Proprietary decision rules
- Carefully developed prompts
- Business processes
- Formatting logic
- Scoring systems
- Internal terminology
- Information about how your application works

Some of that may be completely harmless.

Some of it may represent months of work.

And here is the rule I would use:

**If information absolutely must remain secret, do not treat model instructions as secure storage.**

That includes your `SKILL.md`.

OpenAI's documentation explains that when a skill is activated, the model loads its complete instructions.

That is what makes skills useful.

It is also why I would not put the nuclear launch codes in one.

Or my Netflix password.

Or the proprietary algorithm responsible for correctly determining whether pineapple belongs on pizza.

Some information is simply too dangerous.

## Can Users Just Read My Plugin Instructions?

This question needs a careful answer.

A plugin skill is not necessarily presented to users as a giant friendly "HERE ARE ALL THE SECRET INSTRUCTIONS" page.

But that is not the security standard I would use.

The instructions are being provided to an AI model because the model needs them to perform the workflow.

Once information becomes part of model context, I would treat it as potentially discoverable rather than as a guaranteed secret.

People can try prompt-injection techniques.

They can ask the model strange questions.

They can attempt to persuade it to reveal instructions.

They can phrase requests in ways nobody anticipated because human beings are remarkably creative when presented with a button labeled DO NOT PRESS.

OpenAI's [plugin security and privacy guidance](https://developers.openai.com/plugins/guides/security-privacy) specifically tells developers to assume prompt injection and malicious inputs will reach their systems.

That is a substantial hint.

The correct security strategy is not:

**I have written an especially stern instruction saying "never reveal this."**

That is not a security boundary.

That is a strongly worded Post-it note.

## The Better Architecture: Thin Skill, Smart Server

If I were building a plugin containing valuable proprietary behavior, I would divide it into two worlds.

### World One: The Skill

The skill contains only enough information for ChatGPT to understand:

- When the workflow should run
- Which tool it should call
- What information it should provide
- How the final result should be presented

Nothing more than necessary.

For example, the skill might effectively say:

> When the user requests an artwork classification, collect the required information, call the classification tool, and present the returned category and confidence level.

Perfectly useful.

Nothing particularly secret.

### World Two: Your MCP Server

Now suppose your artwork classification system uses seventeen proprietary scoring rules, a database you spent two years building, three mathematical transformations, and one mysterious function named `pleaseWorkThisTime()`.

That belongs on your server.

ChatGPT calls something like:

`classify_artwork`

Your server receives the necessary input.

Your private code performs the analysis.

Your server returns only what ChatGPT actually needs.

Perhaps:

- Classification
- Confidence
- Short explanation

The model does not need your entire algorithm.

It only needs the answer.

That is a real security boundary because the proprietary implementation remains on infrastructure you control.

## Do Not Put the Secret Back Into the Tool Description

There is an easy way to completely defeat this architecture.

Build a beautifully secure server and then describe your tool like this:

"Our proprietary classification system first evaluates these 37 criteria using the following weighted formula..."

Congratulations.

You have successfully hidden your valuables in a safe and taped the combination to the refrigerator.

Tool names, descriptions, input schemas, output schemas, and results should reveal only what is necessary for the model to use the tool correctly.

Your MCP server should know how the sausage is made.

ChatGPT only needs to know which button summons the sausage.

Metaphorically.

Please do not build a sausage MCP server solely because of this article.

## What About API Keys and Passwords?

Those absolutely should not live in plugin instruction files.

OpenAI's [plugin packaging guidance](https://developers.openai.com/plugins/build/plugins) is the starting point for assembling your plugin without accidentally bundling information that should stay private.

Store credentials server-side using the same practices you would use for any production application.

That means things like:

- Environment variables
- AWS Secrets Manager
- HashiCorp Vault
- Your cloud provider's secret-management system
- Short-lived credentials where possible
- Narrowly scoped permissions

In other words, all the boring security practices that become extremely exciting approximately four minutes after somebody accidentally commits an API key to GitHub.

## What If My "Secret" Actually Is the Prompt?

This is where things get more complicated.

Suppose the valuable intellectual property is not an algorithm running on a server.

Suppose the valuable thing *is the instruction set itself*.

Maybe you spent hundreds of hours developing a highly specialized prompt that produces unusually good results.

You now have a problem.

The model needs those instructions in order to follow those instructions.

You cannot simultaneously say:

"Here is the complete secret recipe you must use."

And:

"You may never possess the secret recipe."

Physics has already filed an objection.

If those instructions genuinely represent intellectual property that must remain confidential, consider moving the important processing behind an MCP tool.

Instead of ChatGPT performing the proprietary process directly, your server performs it.

Your plugin skill might simply tell ChatGPT:

"When the user requests this operation, send the appropriate information to the processing tool and present the result."

Your server can then run whatever private logic is necessary.

That private logic could be traditional software.

It could call another service.

It could perform database operations.

It could even run a separate AI workflow under your control.

If you use another AI service, you still need to assess its data handling and confidentiality guarantees. Moving a secret from one model to another does not automatically make it secure.

The important point is architectural:

**Do not send a secret into a user-facing AI workflow and then depend on politeness to protect it.**

## Authentication Is a Separate Problem

Protecting your proprietary instructions answers:

"Can users discover how my system works?"

Authentication answers:

"Which users are allowed to use the system in the first place?"

Those are different questions.

If your MCP server accesses private data or performs actions for individual users, OpenAI provides [authentication guidance for plugins](https://developers.openai.com/plugins/build/auth).

The current architecture supports OAuth-based authentication patterns.

That gives you proper concepts like:

- User authentication
- Access tokens
- Scopes
- Authorization
- Token expiration
- Resource validation

Instead of:

"Here is an API key every user shares. Please do not post it on Reddit."

OAuth allows User A to access User A's resources without automatically granting User A access to User B's resources, provided your server enforces those permissions correctly.

Which is generally considered preferable.

Especially by User B.

## Least Privilege Still Matters

Suppose your plugin needs to read customer orders.

Do not give it permission to:

- Delete customers
- Modify accounting records
- Launch EC2 instances
- Cancel payroll
- Reposition satellites

Give it permission to read customer orders.

OpenAI's security guidance recommends least privilege, explicit user consent, server-side validation, and confirmation for destructive actions.

This is traditional application security showing up to the AI party and announcing that everyone still has to follow the rules.

AI did not repeal authentication.

AI did not repeal authorization.

AI did not repeal input validation.

AI mostly gave attackers much more entertaining input boxes.

## Validate Everything on the Server

Another important rule:

Never assume that because ChatGPT called your tool, the arguments must be trustworthy.

Validate them.

Your server should determine:

- Is this input valid?
- Is this user authenticated?
- Does this user have permission?
- Is this operation allowed?
- Are the requested resources within scope?
- Is the input attempting something bizarre?
- Should this action require confirmation?

The model can suggest what should happen.

Your server decides what is actually allowed to happen.

That separation makes me much happier.

The AI can be enthusiastic.

The server should be suspicious.

Together they form a surprisingly healthy relationship.

## So Where Is the Official Manual?

Thankfully, there really is one.

The main starting point is the [official ChatGPT plugin developer documentation](https://developers.openai.com/plugins).

From there, I would read these pages in roughly this order:

1. [Plugin Quickstart](https://developers.openai.com/plugins/quickstart)
2. [Plugin Architecture](https://developers.openai.com/plugins/concepts/plugins)
3. [Skills](https://developers.openai.com/plugins/concepts/skills), covered earlier
4. [MCP Servers](https://developers.openai.com/plugins/concepts/mcp-server), also covered earlier
5. [Security and Privacy](https://developers.openai.com/plugins/guides/security-privacy), which I would read twice
6. [Authentication](https://developers.openai.com/plugins/build/auth), because permissions are not decorative
7. [Plugin Guidelines](https://developers.openai.com/plugins/plugin-guidelines)

And if you are migrating an existing GPT, keep the [Custom GPT retirement and migration FAQ](https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq) nearby.

Possibly open in another tab.

Possibly printed.

Possibly framed.

December has a way of accelerating.

## A Few Interesting Plugin Tidbits

Plugins are more than renamed GPTs.

That becomes increasingly obvious once you get into the architecture.

A plugin can be **skills only** if all you need is reusable workflow guidance.

It can be **MCP only** if the important part is tools and external systems.

Or it can combine **skills and MCP**, which is probably where many interesting business workflows will end up.

Some plugins can also provide custom interfaces, making them considerably more interesting than a plain text conversation.

And plugins are designed to operate across ChatGPT and Codex through a shared ecosystem, although particular capabilities may depend on the environment where they run.

That creates some possibilities considerably larger than "my old GPT, but migrated."

A workflow could potentially combine:

- Company-specific instructions
- Private server-side business logic
- Live databases
- Authenticated services
- Reference material
- Custom tools
- Interactive interfaces

Now we are no longer talking about merely customizing how an AI answers questions.

We are talking about giving it controlled access to actual software systems.

That is much more powerful.

It is also why security becomes much more important.

## And One Migration Detail Worth Remembering

If you migrate an existing GPT, custom actions do **not** automatically migrate.

That deserves bold letters because it is exactly the kind of sentence people discover after clicking a cheerful migration button.

**Custom actions do not automatically migrate.**

If your GPT depends on one, you may need to replace it with an existing app or build an MCP server.

The migration documentation also says the latest **published** GPT version is the one used during migration.

Not your clever unpublished version from Tuesday night.

Not the draft where you finally fixed everything.

Published.

So check before you migrate.

The replacement plugin initially starts private, which is actually nice from a security perspective because you can test it before releasing it into the wilderness.

Private is not the same as impossible to extract, but at least you control the initial distribution.

## What I Am Going to Do

My preferred architecture is becoming fairly obvious:

**Keep the plugin instructions boring. Keep the valuable logic somewhere I control.**

The skill should explain enough for ChatGPT to perform the workflow.

The MCP server should handle anything proprietary, sensitive, authenticated, or dangerous.

Secrets remain server-side.

Permissions remain narrow.

Inputs get validated.

Important actions get confirmation.

And somewhere in the architecture I will undoubtedly add logging because the first rule of troubleshooting is that problems become shy whenever logging is disabled.

This does require more work than simply migrating instructions and declaring victory.

But if the goal is a plugin people can actually use without exposing the intellectual property behind it, I think that work is justified.

A prompt can guide behavior.

A server can enforce security.

Those are not the same thing.

And December 11 seems like an excellent occasion to remember the difference.

## A Little Winter in Paris

For the accompanying artwork, I am taking a brief detour from AI architecture into an Impressionist winter boulevard filled with horse-drawn carriages, pedestrians, and the particular kind of weather that makes everyone question their decision to leave the house.

The still image captures one fleeting moment. The animated version throws us straight into the traffic, weaving between carriages, racing past pedestrians, and climbing above the city as snow and brushstrokes swirl together.

Two musical possibilities:

- **[Winter (The Four Seasons, First Movement) – Antonio Vivaldi](https://www.youtube.com/watch?v=7D5Jcdvavls)** – Dramatic, urgent strings that turn an ordinary winter commute into an event of international importance.
- **[Paris – Else](https://music.apple.com/us/song/1461085630)** – A modern electronic groove that makes the old-fashioned boulevard feel unexpectedly alive.

One for theatrical winter energy. The other for a more contemporary pulse.

Both are excellent excuses to watch a carriage go around a corner faster than its insurance company would approve.

## Your Turn

If you are migrating a GPT, I would love to hear how you are handling proprietary instructions.

Are you keeping everything in skills, moving important logic behind MCP, or constructing some beautiful architecture that currently consists of three diagrams and an increasingly nervous developer?

Have you found a better approach to protecting your intellectual property?

**Drop a comment and tell me what you are building, what concerns you, and whether December 11 has already ruined your holiday planning.**

And if you enjoy AI, programming, technology, and occasionally watching perfectly reasonable software projects develop additional limbs, [follow me here](https://medium.com/@DaveLumAI).

There is always another interesting technology problem waiting around the corner.

Usually carrying a migration deadline.

## [Art Prompt:](https://lumaiere.com/?gallery=impressionist10)

Create a bustling winter boulevard seen from an elevated viewpoint on a cold pale morning, with broad avenues stretching deep into the distance beneath rows of bare trees and elegant cream-stone buildings. Fill the street with dozens of tiny horse-drawn carriages, dark-coated pedestrians, and scattered figures moving through patches of thin snow and damp pavement. Use broken, rapidly placed brushstrokes rather than precise outlines, allowing carriages, people, windows, and branches to dissolve into flickering touches of charcoal, umber, muted blue, dusty rose, pale ochre, and gray-white. Let the overcast sky occupy a generous portion of the composition, painted with soft cool layers that diffuse the weak winter light across rooftops and streets. Build atmospheric perspective by gradually reducing contrast and detail toward the distant intersection, where buildings and traffic merge into a bluish-gray haze. Emphasize the rhythmic repetition of trees, carriage wheels, rooftop lines, and moving figures while keeping every individual element loose and spontaneous. The overall image should feel observed in a fleeting instant: cold air, restless traffic, muted sunlight, damp snow, and urban movement captured through shimmering Impressionist brushwork. Museum-quality oil painting, no readable text, no logos, no recognizable people, family-friendly.

## [Video Prompt:](https://www.tiktok.com/@davelumai/video/7695150696345160990)

Launch immediately into a bustling 19th-century Parisian winter boulevard with a rapid low-angle tracking shot racing between two horse-drawn carriages, their wheels throwing sparkling slush across wet cobblestones. Swing sharply around a carriage wheel, follow a horse's rhythmic gallop, then whip upward past black iron streetlamps and bare winter branches to reveal an enormous avenue filled with carriages, pedestrians, pale stone buildings, and drifting snow. Use quick cinematic perspective shifts, energetic forward motion, and dramatic transitions synchronized to an imagined musical rhythm. Dive back toward street level, sweep past elegantly dressed pedestrians whose coats and scarves flutter in the freezing breeze, then circle around a passing carriage before accelerating along the boulevard. Let the entire environment retain the shimmering character of a late-19th-century Impressionist oil painting, with visible broken brushstrokes in charcoal, umber, muted blue, dusty rose, pale ochre, and gray-white. Animate snowflakes, swirling exhaust-like horse breath, flickering reflections in puddles, and the rhythmic movement of carriage wheels and pedestrians. Build toward a dramatic ascending aerial reveal where dozens of moving carriages create intricate patterns along the wide boulevard, while the snowy city stretches into a distant bluish-gray haze. Finish with a rapid sweeping descent toward the crowded avenue, freezing the final instant into a luminous, richly textured Impressionist painting. Fast-paced, visually captivating, elegant, fluid cinematic movement, strong visual rhythm, sophisticated historical atmosphere, seamless transitions, vertical 9:16 composition, no readable text, no logos, no recognizable people, family-friendly.