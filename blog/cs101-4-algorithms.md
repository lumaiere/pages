# Algorithmic Thinking: The Superpower You Already Use (You Just Don’t Call It That)

Algorithmic thinking sounds like something you need a hoodie, a whiteboard, and a suspicious amount of coffee to achieve.

In reality, you do it constantly.

You do it when you pack for a trip (socks first, then shirts, then the item you forgot twice).

You do it when you cook (do not add pasta after draining the water, no matter how confident you feel).

And you definitely do it when you try to leave the house on time and discover your keys have joined a secret society.

Algorithmic thinking is just this: you stop trying random stuff, and you start deciding what happens first, second, and last.

Not because you’re trying to be fancy.

Because you’re trying to suffer less.

If you want the earlier chapters in this little saga, Episode 2 is right here: **[Programming Fundamentals Part 1: Variables and Conditionals](https://medium.com/@DaveLumAI/programming-fundamentals-part-1-variables-and-conditionals-aka-teaching-a-computer-to-stop-2d94ab24b91a)**

Now let’s talk about the part of CS 101 where your brain learns to stop flailing.

---

## What an Algorithm Really Is (Spoiler: It’s Not a Wizard Spell)

An algorithm is a repeatable set of steps that solves a problem.

That’s it.

It’s not magic.

It’s not “AI.”

It’s not a mystical incantation whispered into the vents of a data center.

It’s just a plan that a computer can follow without improvising.

And that last part matters, because computers do not improvise.

A computer is the coworker who will follow your exact instructions with perfect confidence while heading directly toward disaster.

If you say:

* “Find me the largest number”

It will respond:

* “Sure. How?”
* “From where?”
* “What counts as a number?”
* “If you include NaN, I will personally burn down your weekend.”

Algorithmic thinking is you becoming the person who answers those questions before the computer forces you to.

---

## Brute Force: The Method That Works… Until It Doesn’t

Brute force is the strategy of trying everything.

It’s the programming equivalent of:

* “I don’t know where my phone is, so I’m going to flip every cushion in the house like a raccoon.”

And honestly, brute force is not “bad.” It’s just… enthusiastic.

Sometimes brute force is exactly right:

* Small input
* Time doesn’t matter
* You’re prototyping
* You’re learning
* You’re in a hurry and future-you hasn’t started yelling yet

The problem is that brute force scales like chaos.

If a problem gets 10x bigger, brute force doesn’t get 10x harder.

It often gets “laughs in exponential.”

That’s when your code goes from “works fine” to “why is my laptop making that sound.”

Algorithmic thinking is noticing when a problem is about to cross that line.

---

## Pattern Recognition: The Real Skill Nobody Warns You About

Most beginners think programming is about typing.

It’s not.

It’s about noticing that you keep solving the same shape of problem.

Same vibe, different costume.

Examples:

* “I need to find something” (search)
* “I need to organize things” (sort)
* “I need the best option” (optimize)
* “I need to do this many times” (iterate)
* “I need to stop doing this many times” (cache/memoize)
* “I need to avoid checking the same thing twice” (use a set / map)

Algorithmic thinking is when you stop saying:

* “How do I solve this exact problem?”

…and start saying:

* “What kind of problem is this?”

That shift is where the pain starts decreasing.

---

## Thinking in Processes Instead of Outcomes

A beginner thinks:

* “I want the answer.”

An algorithmic thinker thinks:

* “How do I get the answer, reliably, every time, even when the input changes?”

Because computers don’t want your goal.

They want your steps.

So instead of:

* “I want to sort this list.”

You write down:

* Compare things.
* Swap things.
* Repeat.
* Stop when nothing changes.

It’s not glamorous.

But it’s how everything works.

Your job is to turn “I want” into “Do this, then this, then this.”

That’s algorithmic thinking.

---

## A Concrete Example: Finding the Largest Number

Let’s say you have a list of numbers and you want the biggest one.

A human might glance and say, “Oh, it’s 97.”

A computer will stare at the list like it’s an ancient prophecy.

So you give it a plan:

* Start by assuming the first number is the biggest.
* Look at the next number.
* If the next number is bigger, update your “biggest so far.”
* Repeat until you’ve checked everything.

That’s not just a solution.

That’s a reusable pattern.

And it scales beautifully.

Here’s what that looks like in Python:

```python
def find_max(nums):
    if not nums:
        return None

    biggest = nums[0]
    for n in nums[1:]:
        if n > biggest:
            biggest = n
    return biggest

print(find_max([3, 10, 2, 97, 45]))  # 97
```

Notice what you did there:

* You defined a process.
* You made it deterministic.
* You made it handle different inputs.
* You made it reusable.

Congratulations, you just did algorithmic thinking without needing a motivational poster.

---

## Common “Algorithmic Thinking” Mistakes (And Why They’re Normal)

### 1) Writing code that solves only the one example in your head

If your solution works only for your test case, you didn’t build an algorithm.

You built a coincidence.

### 2) Over-optimizing immediately

Sometimes you don’t need the clever solution.

You need the clear solution that works.

Clever can come later, after you’re sure what “works” even means.

### 3) Forgetting the stopping condition

If your algorithm doesn’t know when to stop, it will continue forever.

Computers are incredibly loyal in this way.

They will loop until the heat death of the universe unless you specifically ask them not to.

---

## The Big Takeaway

Algorithmic thinking is less about typing and more about planning.

It’s the habit of turning vague goals into concrete steps.

It’s the difference between:

* “I hope this works”
  and
* “I know exactly why this works”

And once you start thinking this way, programming stops feeling like guessing and starts feeling like building.

If you’re enjoying the series, follow along, and drop a comment with the most ridiculous “brute force” solution you’ve ever written (or witnessed in the wild).

Also, if you want to see more of my art and projects outside the CS series, you can explore **[LumAIere](https://lumaiere.com/)** and grab prints and merch here: **[LumAIere.com Shop](https://www.redbubble.com/people/DaveLumAI/explore?page=1&sortOrder=recent)**.

---

**[Art Prompt (Bauhaus):](https://lumaiere.com/?gallery=bauhaus)**
A crisp Bauhaus-inspired composition built from flat, confident planes of color and clean geometric architecture. A warm, sunlit palette of sandy ochres, muted terracotta, pale lemon, and cool slate-blue forms a playful yet disciplined balance. Interlocking rectangles and stepped blocks rise like a simplified city of forms, with a bold circular “sun” hovering just off-center, creating a quiet tension between order and whimsy. Edges are razor-sharp, surfaces matte and poster-like, and the whole scene feels both childlike and architecturally precise. Subtle texture resembles aged print paper, with slight grain and gentle fading at the margins. The mood is optimistic, modern, and quietly radiant.

**[Video Prompt:](https://www.tiktok.com/@davelumai/video/7586878419049221407)**
Transform the geometric Bauhaus composition into a lively, rhythmic motion piece. Start with a sharp snap-in of flat color planes assembling themselves like magnetic tiles, locking into place with satisfying precision. Have rectangles slide, rotate 90 degrees, and stack into stepped forms in time with an energetic beat, while the circular “sun” bounces subtly and pulses with soft light. Add quick match cuts between close-up textures (paper grain, ink-like edges) and wide shots of the full composition as it reconfigures into a few different balanced layouts. Introduce playful parallax: foreground blocks drift faster than the background, creating depth without breaking the flat graphic style. Finish with the shapes settling into a final clean arrangement as the “sun” gives one last bright pulse and the grain gently breathes.

**Songs to pair with the video:**

* “Atlas" – Battles
* “Kaleidoscope” – The Japanese House

If you watched this far, you’re officially in it. Follow for more. And in the comments: what’s a problem you used to brute force that you now solve with an actual plan?

