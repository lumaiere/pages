# Diffing PDFs on a Mac: Because I Refuse to Read Three Pages Again for One Tiny Change

Dave LumAI here. I've recently discovered that one of life's greatest pleasures is finding out that the three-page document someone just sent me contains exactly ONE change. And that change is buried on page three. Somewhere between a liability clause and a paragraph that could qualify as a sleep aid.

There's a special kind of irritation that comes with receiving a revised PDF.

You've already read the original.

You've already understood it.

You've already questioned several of your life choices while reading it.

And now someone sends you another copy with a cheerful little message:

"Please review the updated version."

**WHAT UPDATED VERSION? WHAT CHANGED? WHERE? WHY ARE WE DOING THIS?**

Apparently, the expectation is that you'll read the entire thing again, carefully examining every paragraph like a forensic accountant investigating a suspicious expense report.

No, thank you.

I've got a better idea.

It's called [diff-pdf](https://github.com/vslavik/diff-pdf), and it has earned a permanent place in my collection of software that prevents unnecessary suffering.

## The Three-Page Crime Scene

Picture this.

You receive a three-page agreement. You read it. Everything looks reasonable, although the legal department has once again demonstrated its remarkable ability to turn "we agree" into seventeen paragraphs.

A few days later, another email arrives.

"Attached is the revised agreement."

Wonderful.

Now you have two nearly identical PDFs:

- Agreement.pdf
- Agreement_Revised.pdf

What changed?

Did they fix a typo?

Did they update an address?

Did they change the termination notice from 30 days to 90 days?

Did they quietly replace "we will pay you" with "we might pay you if Mercury is in retrograde"?

**These are not equally important changes.**

And yet, without a comparison tool, you're stuck playing Spot the Difference with documents that have absolutely no interest in being entertaining.

That's where diff-pdf comes in.

## What the Heck Is diff-pdf?

In software development, a *diff* is a comparison that shows differences between two versions of something.

Programmers have been using tools like this for decades to compare source code.

Instead of rereading 2,000 lines of code, a developer can see that somebody changed three lines, deleted another, and added a comment explaining that the code is now "temporary."

Temporary since 2017, apparently.

**diff-pdf brings that same idea to PDF documents.**

It's a free, open-source utility that compares two PDFs visually and highlights the differences.

Not just text.

It can identify changes in:

- Words and numbers
- Formatting and fonts
- Images and diagrams
- Page layout and positioning
- Other visible elements

The important word here is **visually**.

Rather than understanding the meaning of your document, diff-pdf renders the pages and compares their appearance.

So if somebody changes a single number, it can highlight that area.

If somebody shifts an entire paragraph slightly to the right, that can also show up.

And if somebody changes something that doesn't affect the visible page, such as certain metadata, diff-pdf may not notice.

It's a visual detective, not a lawyer.

Which, frankly, probably makes it more affordable.

## Installing diff-pdf on Your Mac

Here's the good news.

You don't need an expensive PDF editor, a monthly subscription, or an account that requires you to create yet another password.

You just need a Mac, Terminal, and a package manager.

If you already have [Homebrew](https://brew.sh/), this is ridiculously easy.

Open Terminal and type:

~~~bash
brew install diff-pdf
~~~

That's it.

Homebrew downloads and installs the utility and its necessary dependencies.

You can also check the [Homebrew package page for diff-pdf](https://formulae.brew.sh/formula/diff-pdf) if you're curious about the version, dependencies, or installation details.

If you don't have Homebrew installed, its website provides installation instructions.

For the record, Homebrew is a package manager for macOS. It lets you install useful software directly from Terminal instead of wandering around the internet downloading mysterious installers named something like `DefinitelySafeInstaller_v3.dmg`.

I prefer knowing what I'm installing.

Call me old-fashioned.

## The Command That Saved My Sanity

Let's say you have two files sitting in your Downloads folder:

`agreement-old.pdf`

`agreement-new.pdf`

First, open Terminal and navigate to Downloads:

~~~bash
cd ~/Downloads
~~~

Now run:

~~~bash
diff-pdf --view "agreement-old.pdf" "agreement-new.pdf"
~~~

**And behold!**

A comparison window opens, showing the visual differences between the documents.

You can navigate through pages, zoom in, and inspect what's changed.

Areas that differ are visually highlighted, making them much easier to spot.

In my case, I had a three-page PDF.

The revised version looked suspiciously similar to the original.

I ran the comparison.

Page one? Nothing interesting.

Page two? Still nothing.

Page three?

**BINGO!**

One tiny change.

One.

I could have spent ten minutes rereading the agreement, questioning whether the definition of "Services" had subtly changed or whether my eyes were simply exhausted from staring at legalese.

Instead, I found the difference almost immediately.

I experienced the kind of satisfaction normally reserved for finding a twenty-dollar bill in a jacket you haven't worn since winter.

## Want a PDF Showing All the Differences?

Sometimes you don't just want to look at the changes.

You want to save them.

Maybe you need to send the comparison to a colleague.

Maybe you want evidence that the vendor changed exactly one sentence after asking you to review the entire document again.

Perhaps you just want to frame it.

I don't judge.

Use this command:

~~~bash
diff-pdf --output-diff="changes.pdf" "agreement-old.pdf" "agreement-new.pdf"
~~~

This generates a new PDF named `changes.pdf` containing the visual comparison with differences highlighted.

Then open it on your Mac:

~~~bash
open "changes.pdf"
~~~

Now you have a document showing where the differences appear.

You can keep it with your review materials or share it with someone else who also has better things to do than reread an unchanged liability section.

And since the comparison runs locally, you don't have to upload confidential agreements to some random website promising "FREE PDF COMPARISON" while asking for your email address, birthdate, and possibly your firstborn child.

Of course, review your organization's security policies before installing or using any software with sensitive documents.

## There's Also a Silent Mode

Here's something interesting.

You don't even have to open the visual comparison window.

Just run:

~~~bash
diff-pdf "agreement-old.pdf" "agreement-new.pdf"
echo $?
~~~

The second command displays the return code from the comparison.

For diff-pdf:

**0 = No visual differences detected**

**1 = Visual differences detected**

Yes, really.

The utility can tell you whether it found a difference without making you look at anything.

That's useful for scripts, automated checks, or those moments when you want a computer to confirm that somebody has once again sent you a document with absolutely nothing changed.

And if you're wondering why the command doesn't print a cheerful message like "Congratulations! Your documents are identical!"...

Well, welcome to command-line software.

Emotional support is not included.

## A Few Things Worth Knowing

As much as I love this utility, there are a few important limitations.

### 1. Formatting Changes Count

Suppose someone reexports the same document using a different font or slightly different margins.

The words might be identical, but the resulting PDF could look different.

diff-pdf may highlight a surprisingly large number of differences.

This doesn't necessarily mean the content changed.

It means the visual appearance changed.

**That's an important distinction.**

### 2. It's Not a Legal Review Tool

If you're comparing contracts, diff-pdf can help identify visible changes, but you still need to evaluate what those changes mean.

Changing "shall" to "may" can have enormous consequences.

Changing "colour" to "color" probably won't cause your company to collapse.

Although an especially enthusiastic attorney might disagree.

Also, because diff-pdf compares rendered pages, it isn't designed to audit every invisible element inside a PDF.

If your review requires detecting hidden data, annotations, metadata changes, or other nonvisual elements, you'll need additional tools and appropriate review procedures.

### 3. Page Layout Matters

If someone inserts an entire page near the beginning, changes the page size, or substantially reformats the document, many subsequent pages may appear different.

The tool isn't trying to understand which paragraph moved from page two to page three.

It's comparing appearances.

Keep that in mind when interpreting the results.

### 4. It's Particularly Great for Small Revisions

This is where the utility really shines.

Two versions of a proposal.

Two versions of a vendor agreement.

An updated policy.

A revised statement of work.

A contract where someone claims they "only made a couple of minor changes."

Ah, yes.

**Minor changes.**

My favorite phrase to investigate.

## My New PDF Review Workflow

I've developed a remarkably uncomplicated process.

When someone sends me a revised PDF, I save it alongside the original.

Then I open Terminal and run:

~~~bash
diff-pdf --view "original.pdf" "revised.pdf"
~~~

I inspect the differences.

If they're minor and understandable, great.

If they're significant, I examine those sections carefully and determine whether the changes affect anything else.

If necessary, I generate a difference PDF for my records.

And then I get on with my life.

No elaborate subscription platform.

No manually comparing paragraphs.

No holding two windows next to each other and desperately trying to remember whether section 4.2 said "within thirty days" or "within thirty business days."

Just a quick comparison.

**Technology doing something genuinely useful.**

Imagine that.

## The Bigger Lesson: Stop Doing Work Your Computer Can Do Better

There are plenty of tasks that require human judgment.

Understanding contracts.

Negotiating terms.

Determining whether a change creates additional risk.

Deciding whether your vendor's latest pricing proposal is reasonable or whether they're testing your ability to recognize daylight robbery.

But identifying which pixels changed between two PDF documents?

That's computer work.

Let the computer do it.

We already spend enough time reading emails, attending meetings, and trying to understand why someone scheduled a 30-minute call to discuss something that could have been handled in two sentences.

If a tool can eliminate one tedious chore, I'm interested.

If it can eliminate that chore with a single Terminal command, I'm delighted.

And if it's free?

**Now we're talking.**

## Final Thoughts

The next time someone sends you a revised PDF and asks you to review the changes, resist the urge to start reading from page one.

Install diff-pdf.

Compare the documents.

Find the changes.

Then spend your newly recovered time doing something more enjoyable.

Like reading an actual book.

Or watching a movie.

Or staring peacefully out the window while contemplating the extraordinary fact that somebody changed one word on page three and expected you to reread the entire agreement.

**Thank God for diff.**

Have you used diff-pdf, or do you have another favorite tool for comparing documents?

I'd genuinely love to hear what you're using, especially if you've found something that works even better.

**Drop a comment below and share your favorite document-comparison trick.**

And if you enjoy discovering ridiculously useful tools, technology shortcuts, and occasionally questionable attempts at humor, **follow me for more.**

Because life's too short to read the same three pages twice.

---

## [Art Prompt (Kinetic Art):](https://lumaiere.com/?gallery=kinetic-art)

Create an extraordinary, monumental kinetic sculpture installation in a vast, open-air modernist courtyard, capturing the elegant mechanical poetry of mid-twentieth-century geometric abstraction. Four enormous, perfectly proportioned square panels of brushed stainless steel are suspended in a precise two-by-two arrangement around a slender central vertical mast, each panel delicately balanced on nearly invisible pivot mechanisms and capable of turning independently in the breeze. Their polished surfaces reflect fragments of a luminous pearl-gray sky, pale golden sunlight, weathered concrete terraces, and distant clusters of dark emerald trees. Construct a captivating composition in which severe geometric order meets the unpredictable softness of natural movement: one metallic square tilts outward at a dramatic angle, another catches the sun like an immense silver mirror, while the remaining panels form an almost impossible equilibrium of floating planes. Surround the sculpture with austere Brutalist architecture, long horizontal shadows, softly waving meadow grasses, and an expansive atmospheric sky filled with delicate cirrus clouds. Employ a sophisticated palette of cool silver, graphite gray, desaturated blue, chalky ivory, warm sandstone, muted olive, and subtle amber highlights. Render the stainless steel with astonishing physical realism, emphasizing delicate surface abrasions, razor-sharp edges, accurate reflections, meticulously engineered joints, and the extraordinary lightness of massive suspended forms. Use a slightly low camera angle, architectural precision, breathtaking negative space, and crisp directional illumination to create a sense of monumental serenity, intellectual elegance, and suspended anticipation. The mood is contemplative yet quietly exhilarating, celebrating the mysterious collaboration between gravity, wind, geometry, and human imagination. Museum-quality fine-art photography, exceptionally detailed, timeless, visually arresting.

## [Video Prompt:](https://www.tiktok.com/@davelumai/video/7705627151281736990)

Create a breathtaking, visually hypnotic vertical cinematic video of an immense outdoor kinetic sculpture composed of four perfectly proportioned brushed stainless-steel squares balanced around a slender central mast in a monumental modernist courtyard. Begin instantly with a sudden gust of wind sending the upper-left metallic square swinging dramatically toward the camera, its reflective surface flashing brilliant silver and gold. The camera plunges beneath the moving panel and rapidly arcs upward as the other three squares begin rotating independently, their enormous surfaces appearing to glide effortlessly through space. Capture dazzling reflections racing across the steel, geometric shadows sweeping over pale concrete, and dramatic near-collisions as the panels pass one another without touching. Alternate energetic close-up tracking shots of razor-sharp metallic edges and delicately engineered pivots with spectacular wide compositions revealing the sculpture against a luminous pearl-gray sky, austere Brutalist architecture, and softly rippling meadow grasses. Introduce a thrilling moment when all four squares briefly align into one perfect geometric formation before a fresh gust separates them into an astonishing sequence of tilting, spinning, and overlapping planes. Use dynamic camera movement synchronized with the sculpture's natural rhythm, exquisite physically accurate reflections, subtle atmospheric haze, crisp highlights, and cinematic motion blur. Preserve the sophisticated palette of cool silver, graphite, muted blue, ivory, sandstone, and warm amber. End with the four moving panels momentarily framing the brilliant sun before their silhouettes separate in a graceful final flourish, creating a seamless visual loop. Vertical 9:16 composition, vivid cinematic realism, mesmerizing motion, exceptional detail, 15 seconds, no text, no logos.

## Songs to Bring the Video to Life

**Katachi – Shugo Tokumaru**

A wonderfully playful, intricately layered song with infectious rhythmic movement. Its whimsical energy would make those giant metallic squares feel like they're participating in an impossibly sophisticated mechanical dance.

**Abrasive – Ratatat**

A deliciously rhythmic instrumental with sharp guitar textures and an irresistible groove. Perfect for dramatic reflections, precise mechanical motion, and the sudden, exhilarating choreography of enormous steel panels moving in the wind.