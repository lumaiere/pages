# Episode 5: Data Structures - Putting Things Somewhere So You Can Find Them Again

If [Episode 4](https://medium.com/@DaveLumAI/algorithmic-thinking-the-superpower-you-already-use-you-just-dont-call-it-that-e7242fa13527) was about thinking smarter, Episode 5 is about storing smarter.

Because at some point, every program turns into the same little panic:
"Cool. I have data. Now where do I put it so Future Me can find it without screaming?"

That is the entire point of data structures. They are the choices you make about how information should live in memory, based on how you plan to use it.

And yes, they are still wildly relevant. In fact, they are more relevant now, because modern apps are basically giant data-moving machines wearing a friendly UI as a disguise.

---

## What a data structure actually is

A data structure is just a method for organizing information so common actions are predictable:

* Add an item
* Remove an item
* Find an item
* Check what is next
* Loop through everything without losing your place or your will to live

The trick is: different structures make different actions fast, and different actions annoying.

So the real lesson is not memorizing definitions.
The real lesson is learning to ask: "What am I going to do to this data most often?"

---

## Arrays and lists: the default that gets you pretty far

Arrays and lists are the "put things in order" option.

They are great when:

* You want to keep items in sequence
* You want to access something by position
* You are mostly adding to the end and iterating through everything

They are less great when:

* You keep inserting and removing from the beginning or the middle
* You need to search constantly in a huge list
* You are trying to treat the list like a magic teleportation device

In most beginner projects, lists are the workhorse.
And in most real projects, lists remain the workhorse.
They just get backed by more specialized helpers once the data grows up and becomes a problem.

---

## Stacks: last in, first out, like your browser tabs

A stack is what happens when you want the most recent thing first.

You push items onto the top.
You pop items off the top.

Perfect for:

* Undo features
* Backtracking
* Keeping track of nested stuff (like function calls or parsing)

The strength is simplicity.
The weakness is also simplicity.

If you need the middle item, the stack politely refuses and tells you to take it up with management.

---

## Queues: first in, first out, like sanity

A queue is the polite opposite of a stack.

First item in is the first item out.

Perfect for:

* Job processing
* Task scheduling
* Anything that should be handled in order

Queues are how you keep systems fair.
They are also how you keep systems from exploding when ten things arrive at once and you pretend you will "just handle them real quick."

---

## Hash maps: fast lookups with tradeoffs

Hash maps (often called dictionaries or maps) are what you use when you want this:

"Given a key, give me the value right now."

Not "in a second."
Not "after I loop through 80,000 items."
Now.

Perfect for:

* User profiles by user ID
* Caches
* Counting things
* Any situation where you keep asking "have I seen this before?"

Tradeoffs:

* They do not naturally preserve order in the way beginners expect
* Collisions exist (you do not need to fear them, just respect them)
* Keys must be something hashable, which is basically the computers way of saying "I need to be able to uniquely label this in a reliable way"

When you choose a hash map, you are choosing speed for direct access, and giving up the idea that the items are arranged in a meaningful sequence.

---

## How to choose without overthinking yourself into paralysis

Pick based on your dominant action:

* Need to keep order and iterate? Use a list.
* Need last thing first? Use a stack.
* Need first thing first? Use a queue.
* Need instant lookup by key? Use a hash map.

This is not the full world of data structures. Trees and graphs are waiting in the next hallway like a sequel you are not emotionally ready for.

But for now, these four are enough to build a surprising amount of real software.

---

## A quick example that actually feels real

Here is a tiny example showing how these choices change your code. Same problem: handle incoming support requests and keep a quick lookup by ticket ID.

```python
from collections import deque

# Queue: handle requests in the order they arrive
request_queue = deque()

# Hash map: instant lookup by ticket id
tickets = {}

# Stack: quick "undo" of the last action (toy example, but the idea is real)
undo_stack = []

def add_ticket(ticket_id, message):
    request_queue.append(ticket_id)
    tickets[ticket_id] = message
    undo_stack.append(("add", ticket_id))

def process_next():
    if not request_queue:
        return None
    ticket_id = request_queue.popleft()
    msg = tickets.get(ticket_id)
    undo_stack.append(("process", ticket_id))
    return ticket_id, msg

def undo_last():
    if not undo_stack:
        return None
    action, ticket_id = undo_stack.pop()
    return action, ticket_id
```

Notice the vibe:

* The queue keeps the system fair.
* The hash map makes lookups instant.
* The stack keeps your last move close, like a rewind button.

Same data. Different behavior. That is the whole game.

---

## Do data structures work well with AI?

Yes. Actually, they work extremely well with AI because AI systems are obsessed with organizing information:

* Retrieval systems depend on fast lookups and indexing
* Caches are everywhere
* Tokenization pipelines are basically data structure decisions wearing a lab coat
* Even prompts are structured information once you start saving templates, versions, and parameters

If you are building anything AI-adjacent, your data choices become your performance choices.

---

## Wrap up

Data structures sound dramatic until you realize they are just "storage rules."

And once you start noticing the rules, you start writing code that feels calmer:
less searching, less guessing, less brute forcing your way through life.

If you want to start this series from the beginning, Episode 1 is right here: [https://medium.com/@DaveLumAI/back-to-basics-cs-101-explained-like-youre-holding-the-syllabus-upside-down-554961c6e0b8](https://medium.com/@DaveLumAI/back-to-basics-cs-101-explained-like-youre-holding-the-syllabus-upside-down-554961c6e0b8)

If you enjoyed this, drop a comment with the data structure that finally clicked for you, and follow along for the next episode. More projects and art live at [https://lumaiere.com](https://lumaiere.com) and you can grab new work in the shop at [https://www.redbubble.com/people/DaveLumAI/explore?page=1&sortOrder=recent](https://www.redbubble.com/people/DaveLumAI/explore?page=1&sortOrder=recent)

---

[Art Prompt (Realism):](https://lumaiere.com/?gallery=realism)
A large, candid winter village scene rendered with grounded realism and earthy restraint, like an unposed moment captured on a wide horizontal canvas. The sky is a cold pewter gray and the snow is packed and slightly dirty near the road edges, reflecting muted daylight. Townspeople in heavy wool coats and worn boots gather in small clusters, their faces individualized with subtle expressions and imperfect features, as if each person has a story. Holiday garlands and simple red ribbons hang sparingly from a wooden fence and a few storefronts, never glossy, always practical. A small group of carolers stands near the foreground, breath visible in the air, while a distant church spire and low stone buildings anchor the background. The palette is subdued: umbers, slate blues, charcoal, and soft off-whites, with restrained pops of deep cranberry and evergreen. Lighting is natural and overcast, with gentle tonal transitions and confident, textured brushwork that emphasizes fabric, snow, and weathered wood. The mood is quietly festive and human, more honest than sparkly, with a sense of communal warmth inside a cold day.

[Video Prompt:](https://www.tiktok.com/@davelumai/video/7587543802580127007)
Start with a quick, energetic reveal: a burst of swirling snow fills the frame, then clears to a wide winter village scene with townspeople gathered in layered depth. Use dynamic push-ins and gentle handheld drift to feel present in the crowd, with occasional snap zooms to expressive faces, boots crunching snow, and mittened hands holding song sheets. Add subtle parallax by moving past foreground coats and scarves while the church spire stays centered in the distance. Let breath vapor pulse in the cold air, lantern light flicker softly, and garlands sway in a light wind. Include a few quick match cuts: ribbons fluttering to carolers mouths singing, then to boots stepping in rhythm, then to falling snow landing on dark wool. Keep the color grade muted and realistic with restrained cranberry and evergreen accents. End with a satisfying slow-down moment: the carolers hold a final note as snow drifts past the lens and the village scene settles into a calm, honest holiday stillness.

Song picks for the video:

* Christmas Lights – Coldplay
* Carol of the Bells – Lindsey Stirling
