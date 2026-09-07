# How Many High Chats Can You Run at Once in ChatGPT? Apparently, More Than My Attention Span Can Handle

*Dave LumAI here. I recently discovered that one difficult question was apparently not enough, so I started several High chats at the same time. This is what happens when curiosity gets broadband.*

Here is the answer I was looking for:

**OpenAI does not currently publish a fixed number of ordinary High chats that you are allowed to have actively thinking at the same time.**

Not three.

Not five.

Not ten.

Not "seven, unless it is Tuesday and somebody in accounting has touched the server."

There simply is not a publicly documented concurrency number for normal High reasoning chats.

And yes, I checked.

As of September 5, 2026, High is the extended reasoning setting for GPT-5.6 Sol in [ChatGPT](https://chatgpt.com/). OpenAI explains the current reasoning options and their usage behavior in its [GPT-5.6 and GPT-6 Pro in ChatGPT guide](https://help.openai.com/en/articles/20001354-gpt-56-in-chatgpt).

So if you currently have one High chat contemplating the mysteries of AWS, another rewriting your blog, and a third trying to explain why your CSS moved a button six pixels to the left for no apparent reason, ChatGPT can allow those conversations to overlap.

How many before it tells you to knock it off?

OpenAI does not say.

## Does It Matter If the Chats Are in a Project?

No.

This was one of the first things I wondered because Projects feel sufficiently separate that you might imagine each one gets its own tiny bucket of AI horsepower.

Sadly, Projects are organizational containers, not quota laundering operations.

According to OpenAI's current [Projects in ChatGPT documentation](https://help.openai.com/en/articles/10169521-projects-in-chatgpt), chat rate limits inside Projects are based on your subscription level.

So putting five High chats into five different Projects does not transform you into the Warren Buffett of reasoning tokens.

Projects can give chats shared files, instructions, memory, and context.

They do not give each Project an independent reasoning allowance.

## Will Running Several High Chats Make Me Hit My Limit Faster?

**Yes, potentially. But not because they are running simultaneously.**

The important distinction is concurrency versus usage.

Suppose you send:

- one High request about Python
- one High request about taxes
- one High request about your WordPress site
- one High request asking why the first three are taking so long

You have made four High requests.

Starting them close together does not combine them into one request simply because several little thinking indicators happen to be spinning at the same time.

High manually uses GPT-5.6 Sol and draws from the reasoning allowance associated with your plan.

So parallelism can make you burn through that allowance faster in real-world time simply because you are submitting more work.

That is a little like discovering that having four faucets lets you fill four buckets simultaneously and then being surprised that the water meter has opinions.

## Is There a Special High Limit?

There is a reasoning limit, but OpenAI does not currently give every personal-plan user a nice universal number like:

**Congratulations! You have 83 High questions remaining. Spend them wisely.**

The documentation says reasoning limits depend on your plan.

High is currently included on Plus, Pro, Business, and Enterprise plans. Free and Go users use a different Think option rather than GPT-5.6 Sol High.

If you hit your GPT-5.6 reasoning allowance, ChatGPT may continue using another available reasoning model instead.

That means "I hit the limit" does not necessarily mean ChatGPT suddenly becomes a decorative rectangle.

You may still be able to chat.

You may simply lose access to the reasoning option you were using until its allowance resets.

## So How Do I Know If I Really Hit the Limit?

This is important because every slow response is not a limit.

Every failed response is not a limit.

Every spinning circle that appears to be reconsidering its career choices is definitely not proof of a limit.

When ChatGPT knows you have reached an allowance, it can show you that the allowance has been reached and, when available, display when it resets.

It may also switch you to another available reasoning model.

That is much better evidence than:

> "Chat number six seems grumpy."

If ChatGPT is behaving strangely but you have not received an actual limit notification, check the [OpenAI Status page](https://status.openai.com/) before declaring that you have personally exhausted the world's supply of artificial intelligence.

An outage, degraded service, network problem, browser issue, or temporary capacity problem can look surprisingly similar from the user's chair.

## Do the Limits Change Depending on How Many People Are Using ChatGPT?

This one gets interesting.

OpenAI says reasoning limits depend on things such as your plan, the model, and managed workspace settings.

It does **not** currently publish a rule saying your normal High allowance automatically shrinks because 14 million other people suddenly decided to ask ChatGPT to write wedding vows at 8:00 p.m.

System conditions can affect service availability, and OpenAI can apply temporary restrictions and safeguards.

That is not the same thing as a published High concurrency allowance that rises and falls with traffic.

So I would not assume:

**"High stopped working, therefore too many people must be online."**

Possible?

Sure.

Proven?

No.

The internet has enough confident speculation already. It does not need me wearing a lab coat and inventing server statistics.

## One Particularly Interesting Loophole That Is Not Actually a Loophole

Here is one of the stranger details in the current rules.

ChatGPT can automatically decide that an Instant request needs additional reasoning.

According to OpenAI, that automatic reasoning does **not** count against the allowance for reasoning that you manually select.

That is genuinely useful.

It means there is a difference between:

**You explicitly selecting High**

and

**ChatGPT deciding an ordinary request deserves more thought.**

I would still choose High when I specifically want deeper reasoning, especially for complicated technical questions, comparisons, debugging, research, or anything involving a database that was supposedly "working perfectly yesterday."

But it is nice knowing ChatGPT can occasionally think harder on its own without quietly stealing one of your manually selected reasoning uses.

## High Is a Setting, Not a Separate Army of Robots

Another useful distinction: a "High chat" is not really a special species of conversation.

High tells GPT-5.6 Sol to use extended reasoning on your request.

You can therefore have multiple ordinary conversations where High has been selected.

The conversation itself is still a conversation.

High controls how much reasoning effort the model applies to the response.

That is why looking for a simple "maximum number of High chats" can be misleading.

There are several different things that could limit you:

**Your reasoning allowance**

You may eventually exhaust the amount included with your plan.

**Temporary rate controls**

Systems sometimes limit how quickly large amounts of work can be submitted.

**Service availability**

Servers occasionally have bad days too, although unlike humans they cannot blame the meeting before lunch.

**Tool-specific limits**

Images, file uploads, research tools, agents, voice, and other features can have completely separate allowances.

Those are different constraints.

None of them currently produces an official universal statement that says:

**You may have exactly X normal High chats running simultaneously.**

## So How Many Should You Actually Run?

Technically?

Run several if you have several genuinely independent things to do.

Practically?

I have discovered another bottleneck.

Me.

Three High chats finish and suddenly I am staring at three thoughtful responses involving 4,000 words of analysis, six commands, two warnings, and something I apparently asked about DNS fifteen minutes ago.

The AI handled the concurrency beautifully.

My brain responded by opening another browser tab.

There is probably a lesson there.

For real work, I think parallel High chats make excellent sense when the tasks are independent.

You could have one analyzing code while another researches a technical decision and a third reviews some writing.

What I would avoid is splitting one tightly connected problem across ten chats unless you enjoy manually becoming the message bus between ten extremely intelligent coworkers who are forbidden from speaking to each other.

## The Bottom Line

There is currently **no publicly documented fixed maximum number of ordinary High chats you can have thinking simultaneously in ChatGPT**.

Projects do not give you separate reasoning limits.

Running several High requests at once can make you consume your reasoning allowance faster because you are simply submitting more High requests.

If you genuinely hit a reasoning limit, ChatGPT should give you stronger evidence than merely becoming slow, including limit or reset information when available.

And although overall system conditions can certainly affect ChatGPT, OpenAI does not publish a simple rule saying your High allowance changes according to how crowded the service happens to be.

Which leaves us with a wonderfully modern productivity problem:

We finally have computers capable of thinking about several complicated problems at once.

Now we just need humans capable of remembering why we opened all those chats.

If you have discovered how many High chats you can get running simultaneously before something complains, **tell me in the comments**. I am especially interested if somebody has turned this into a competitive sport.

And **follow me** if you enjoy figuring out what these AI features actually do instead of simply accepting whatever mysterious spinner appears on the screen.

## A Completely Unrelated Visual Detour

**[Art Prompt (Performance Art):](https://lumaiere.com/?gallery=performance)**

A stark black-and-white photographic composition showing an anonymous figure in a tailored dark suit suspended horizontally above a quiet European street, as though gravity has briefly forgotten its responsibilities. Frame the figure against pale masonry, bare winter branches, modest rooftops, and an enormous empty sky. Use crisp documentary detail, deep charcoal shadows, luminous whites, subtle film grain, and the uncanny realism of a perfectly timed mid-century photograph. The pose should feel theatrical rather than dangerous, with the body calmly floating several feet above the pavement in an impossible controlled moment. Keep the street nearly empty so the negative space magnifies the surreal gesture. The mood should be daring, witty, mysterious, elegant, and strangely believable, combining performance, photography, illusion, and visual absurdity. Museum-quality monochrome image, no readable text, no logos, no recognizable people, no modern screens.

**[Video Prompt:](https://www.tiktok.com/@davelumai/video/7682514315135421726)**

Open instantly with an anonymous dark-suited figure already floating sideways above a quiet monochrome street as gravity suddenly reverses. Snap the camera forward while the coat tails whip upward, loose papers spiral through the air, bare branches bend in opposing directions, and long building shadows race across the pavement. Cut rapidly between close views of polished shoes hovering inches above the street, a wide architectural view with the figure drifting impossibly across the frame, and a dramatic overhead angle as the entire street seems to tilt beneath them. Let gravity repeatedly switch direction so the figure rises, freezes, slides sideways, and gently returns upward toward the stone terrace instead of falling. Preserve crisp black-and-white photography, rich film grain, sharp geometric architecture, strong negative space, and an elegant surreal documentary mood. Finish with the figure motionless in midair while every loose object continues swirling around them.

**Song Suggestions:**

We Can Make the World Stop - The Glitch Mob

In the Flowers - Animal Collective