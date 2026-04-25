# Episode 2: Bits, Bytes, and Data Representation, or How Everything Becomes Zeros, Ones, and Increasingly Specific Lies

By the time most people start programming, they already know the machine can store numbers, print text, show images, play music, and occasionally ruin an afternoon with a mysteriously placed comma.

What is less obvious is that the computer does not naturally understand any of those things.

It does not understand numbers the way you understand numbers. It does not understand letters the way you understand letters. It does not understand color, sound, emoji, spreadsheets, cat photos, invoices, or your carefully named file called `final_final_REALLY_final_v3`.

What it understands, at the lowest practical level, is state.

Tiny distinctions. Tiny switches. Tiny yes-or-no conditions.

That is where bits, bytes, and data representation come in.

This is the part of computer science where we stop politely pretending the machine shares our mental model and admit that every value in software is really an agreed-upon encoding scheme wearing a confident smile.

And honestly, that explains a lot.

If you want the earlier stepping stones before we get gloriously binary, the most relevant continuity from **CS101** is [Episode 2 - Programming Fundamentals Part 1: Variables and Conditionals](https://medium.com/@DaveLumAI/programming-fundamentals-part-1-variables-and-conditionals-aka-teaching-a-computer-to-stop-2d94ab24b91a), where values first start behaving like named things instead of ambient wizard dust, and [Episode 5 - Data Structures](https://medium.com/@DaveLumAI/episode-5-data-structures-putting-things-somewhere-so-you-can-find-them-again-51483812ac35), where organization starts mattering. From **CS102**, the best lead-ins are [Episode 8 - Complexity and Efficiency](https://medium.com/@DaveLumAI/episode-8-complexity-and-efficiency-or-why-two-correct-programs-can-have-very-different-regret-f6825b54207a), because representation affects cost more than people expect, and [Episode 9 - Memory and the Machine](https://medium.com/@DaveLumAI/episode-9-memory-and-the-machine-or-what-the-computer-is-actually-doing-while-you-are-feeling-confident-b7bbabe9548f), because data has to live somewhere before it can confuse you.

## What is a bit?

A bit is one binary digit.

It can be 0 or 1.

Off or on.
False or true.
No or yes.
The software equivalent of a tiny intern holding up one of two signs and refusing to elaborate.

That sounds almost insultingly small, and it is. A single bit by itself does not do much. But computer science has built an empire out of taking very small simple things and combining them until they can run a spacecraft, recommend a song, or make your tax software quietly judge you.

If one bit gives you two possibilities, then two bits give you four:

* 00
* 01
* 10
* 11

Three bits give you eight possibilities. Four bits give you sixteen. In general, `n` bits can represent `2^n` distinct patterns.

That is the first big idea: **bits are not valuable because each one says much. They are valuable because patterns of bits can say almost anything, as long as everyone agrees what the pattern means.**

That last part matters more than it first appears.

## Then what is a byte?

A byte is usually 8 bits grouped together.

That means one byte can represent 256 distinct patterns, from `00000000` to `11111111`.

Why 8? Partly convention, partly engineering history, partly the usual tale of technology becoming standard after enough people stop arguing and start shipping hardware.

A byte became the convenient unit for storing small chunks of information. One character of basic text often fits in a byte. Small integers often fit in a byte. File sizes are commonly described in bytes, kilobytes, megabytes, and so on, because eventually someone had to explain why a photo takes more space than the word "photo."

A byte is not magical. It is just a very successful grouping.

But it is a grouping that quietly shaped almost everything.

## Why binary at all?

At this point a reasonable person might ask, "Why did computers choose base 2? Why not base 10, since humans already did all the emotional labor on that one?"

Because hardware likes clear distinctions.

At the physical level, it is much easier to build reliable systems around two stable states than ten. High voltage and low voltage. Current and no current. Charged and not charged. Close enough to one threshold or another that the machine can make a decision without staring into the void.

Binary is not "natural" in the human sense.

Binary is practical in the machine sense.

And computer science is full of moments where reality politely informs human intuition that it is not in charge.

## Binary numbers: counting with only two symbols

You already know positional notation from decimal.

In decimal, the number 507 means:

* 5 hundreds
* 0 tens
* 7 ones

Binary does the same thing, just with powers of 2 instead of powers of 10.

So:

`1011` in binary means:

* 1 x 8
* 0 x 4
* 1 x 2
* 1 x 1

Which gives us 11 in decimal.

That is it. No sorcery. Just place values in a different base.

Here is a tiny example:

```text
Binary   Decimal
0000     0
0001     1
0010     2
0011     3
0100     4
0101     5
0110     6
0111     7
1000     8
```

Once you see it as place value, binary stops looking like alien static and starts looking like arithmetic wearing a simpler outfit.

## Why hexadecimal exists, because humans deserve mercy

Binary is correct.

Binary is also annoying to read at scale.

Once you get past a handful of bits, long binary strings become the visual equivalent of counting grains of rice during a power outage.

So programmers often use **hexadecimal**, or base 16.

Hex uses:

`0 1 2 3 4 5 6 7 8 9 A B C D E F`

That means a single hex digit represents 16 possibilities, which maps perfectly to 4 bits.

So:

* `0000` = `0`
* `1001` = `9`
* `1010` = `A`
* `1111` = `F`

And one byte, which is 8 bits, can be written as two hex digits.

For example:

* `11111111` in binary = `FF` in hex
* `10101100` in binary = `AC` in hex

This is why memory dumps, color values, machine code, and debugging tools often use hex. It is compact enough for humans and close enough to binary for machines.

In other words, hex is what happens when we accept that the machine is right but still want to keep our eyesight.

## Representation is meaning attached to patterns

Now we hit the central idea of the entire episode.

A pattern of bits does not come with built-in meaning.

`01000001` could mean:

* the number 65
* the letter `A` in ASCII
* part of a pixel value
* part of a machine instruction
* one byte of a compressed audio file
* complete nonsense, if interpreted under the wrong rules

The bits are just the pattern.

**Representation is the rulebook.**

This is one of the most important habits in computer science: never ask only "What bits are stored?" Also ask "How are those bits being interpreted?"

Because a shocking amount of software failure is just one system saying, "This byte sequence is text," while another says, "Fantastic, I assumed it was something else entirely."

## Integers: whole numbers with limits and attitude

Let us start with something friendly: integers.

If you use 8 bits to store an **unsigned integer**, you can represent values from 0 to 255.

Why? Because 8 bits gives 256 total patterns.

That is useful, but it leaves out negative numbers, which are inconvenient to ignore because reality keeps inventing them.

So computers usually use **signed integers** for values that might go below zero. The most common representation is **two's complement**.

This is one of those topics that sounds like it belongs in a mildly haunted textbook, but the practical idea is simple:

* positive numbers work mostly as expected
* one bit helps indicate sign
* arithmetic still works efficiently in hardware

With 8 bits in two's complement, the range is typically:

* -128 to 127

Notice the asymmetry. There is one extra negative value. That is not a bug. That is the math of the representation.

### A concrete example

Suppose a game stores player health in an unsigned 8-bit integer.

That means valid values are 0 through 255.

If some bug subtracts 1 from 0 and the language or system allows wraparound, the result might become 255.

So your dead character is suddenly extremely alive.

Which is funny until it is in production.

This is why representation matters in real software. You do not just pick "a number." You pick a range, a storage cost, and a failure mode.

### Tradeoffs for integers

Smaller integer types:

* use less memory
* can improve cache efficiency
* may be fine for huge arrays or tight systems work

Larger integer types:

* handle bigger values
* reduce overflow risk
* may be simpler for application code

So the tradeoff is not "small is better" or "large is better."

The tradeoff is **how much range do you need, how much memory can you spend, and what kind of mistake would hurt most?**

That is engineering, not superstition.

## Floating-point numbers: where decimals go to become complicated

Whole numbers are relatively polite.

Fractions are not.

Humans like to write `3.14`, `0.1`, and `99.95` and assume those numbers exist cleanly inside the machine. Sometimes they do not. Or rather, they do not exist exactly in the format you hoped.

Most systems represent non-integer values using **floating-point** formats, commonly based on the IEEE 754 standard.

A floating-point number is usually stored using pieces that roughly act like:

* a sign
* an exponent
* a significand or mantissa

That allows the machine to represent a huge range of values, from very tiny to very large.

Wonderful.

It also means some decimal values cannot be represented exactly in binary.

And that is where the trouble begins.

### The famous betrayal of 0.1

In many languages, this kind of thing happens:

```python
0.1 + 0.2 == 0.3
```

You might expect `True`.

The machine may very cheerfully hand you `False`.

Not because math broke.
Because **representation** happened.

The binary encoding of `0.1` is not exact in standard floating-point. Same for `0.2`. So the stored approximations add up to something extremely close to `0.3`, but not exactly equal to the stored approximation of `0.3`.

This is not a quirky edge case. This is normal behavior.

If you are writing graphics software, simulations, machine learning code, finance tools, or anything else numeric, this matters.

### Misconception: floating-point means "real numbers"

Not really.

Floating-point means "a finite, standardized approximation system for many real-number-like values."

That is less poetic, but much more accurate.

### Real-world example

Imagine an e-commerce system calculating totals with floating-point values instead of decimal-safe currency logic.

Most of the time it looks fine.
Then one day a report is off by a few cents in enough places to make accounting start breathing through its nose.

This is why finance software often uses decimal types, fixed-point representations, or integer cents rather than plain floating-point. The right representation depends on what kind of error is acceptable.

A tiny approximation error in a physics engine? Often survivable.

A tiny approximation error in payroll? Suddenly everyone is having a meeting.

## Text encoding: how letters become numbers and then become arguments

Text feels obvious until computers get involved.

You type a letter.
The machine stores a number.
Later some software reads the number and turns it back into a symbol.

That means text is representation too.

Early systems often used **ASCII**, where characters like `A`, `B`, and `C` were assigned numeric values. For example, uppercase `A` is 65.

That worked reasonably well for basic English text and basic punctuation.

It worked much less well for the rest of humanity.

So modern systems commonly use **Unicode**, which is a much larger standard designed to represent writing systems, symbols, and characters from across the world. Unicode is not one single storage format so much as a big character standard with multiple encodings, such as UTF-8 and UTF-16.

UTF-8 became especially popular because it is efficient for common text, backward-compatible with ASCII for the lower range, and flexible enough for far more than old-school one-byte text.

### Why this matters in practice

If two systems disagree about text encoding, your nice readable sentence can become visual soup.

You have probably seen this in the wild:

* weird accented characters
* broken quotation marks
* symbols turning into nonsense
* emoji exploding into placeholder boxes like they just lost a licensing dispute

That is not the computer being artistic.
That is encoding mismatch.

### Concrete example

Suppose one system writes text as UTF-8, but another reads the bytes as if they were Latin-1 or some other encoding.

The underlying bytes did not change.
The interpretation did.

Same bits. Different rulebook. Disaster in a collared shirt.

## Images, audio, and everything else: all representation, all the way down

Once you understand that bits need interpretation rules, a lot of digital media becomes less mysterious.

An image might be represented as:

* pixel values
* dimensions
* color channels
* compression metadata

An audio file might be represented as:

* sampled amplitudes over time
* bit depth
* sample rate
* compression format

A video is basically a highly organized conspiracy involving images, audio, timing, compression, and the sort of coordination that makes group projects look easy.

The machine is still storing patterns of bits.

What changes is the format and the decoder.

That is why file extensions matter less than people think, and actual file formats matter more. Renaming `photo.jpg` to `photo.mp3` does not create avant-garde music. It creates confusion.

## Endianness: because even byte order can start drama

Now for one of the great little "of course this matters" details in systems work: **endianness**.

When a multi-byte value is stored, which byte comes first?

* **Big-endian** stores the most significant byte first
* **Little-endian** stores the least significant byte first

If you store the hexadecimal number `12345678`, the byte order in memory may differ depending on the system.

This matters when working close to hardware, parsing binary files, sending data across networks, or debugging low-level systems.

At higher levels, languages and libraries usually shield you from this.

At lower levels, it is very much your problem.

And it is always fun when the same four bytes mean one thing on your machine and another thing on the one across the room.

## Compression, precision, and the price of convenience

Representation choices always come with tradeoffs.

A few common ones:

### More bits vs less memory

More bits let you represent more values, more precision, or larger ranges.
They also consume more storage and bandwidth.

### Exactness vs speed

Floating-point is fast and broadly useful.
Decimal-safe numeric handling may be more exact for money, but can be more specialized.

### Human readability vs machine efficiency

Text formats like JSON are easy to inspect.
Binary formats are often smaller and faster to parse.

### Compatibility vs ideal design

Sometimes the best representation is not the cleanest one.
Sometimes it is the one every tool in your stack already understands.

This is why engineering is full of phrases like "it depends," said with the haunted dignity of people who have deployed things before.

## Common misconceptions that deserve to be gently tackled

### "The computer stores what I mean"

No. It stores what your format specifies.

### "A number is a number"

Also no. An 8-bit signed integer, a 64-bit unsigned integer, a float, and a decimal-safe currency value are all different representation choices with different behaviors.

### "Text is simple"

Text is simple right up until encodings, normalization, international characters, or emojis arrive and start flipping tables.

### "If it displays correctly once, the representation must be fine"

Absolutely not. Sometimes a broken interpretation happens to look correct for a small set of values and then fails spectacularly later.

### "Bits are too low-level to matter in modern software"

They matter whenever systems exchange data, whenever performance matters, whenever correctness matters, and whenever bugs get weird enough that abstractions stop protecting you.

So, yes. Quite often.

## Why this still matters in modern stacks, AI workflows, and cloud systems

You might think all of this belongs to an earlier era of basement servers and suspicious beige hardware.

Not even slightly.

Modern software still depends on representation decisions everywhere:

* APIs serialize data into text or binary formats
* databases choose storage types with real consequences
* cloud systems move encoded data across networks and services
* AI systems depend on numeric precision, tensor formats, quantization, token encoding, and file formats
* frontend apps push strings, bytes, images, JSON payloads, and cached assets around all day long

Even something as modern-sounding as model quantization is, at heart, a data representation story. You are deciding how to store values with fewer bits while preserving enough meaning to remain useful.

Same old computer science. New fashionable jacket.

## Where this leads next

This episode sits in a very important spot in the course.

If Episode 1 of CS201 was about how a program runs through multiple layers, Episode 2 is about what the data actually looks like while moving through those layers.

And from here, the course gets even more physical.

Because once you understand how values are represented, the next obvious question is: how does hardware manipulate those values at all?

That takes us toward logic gates, digital circuits, memory elements, assembly language, and the machine model beneath the polite software surface.

In other words, the floorboards are about to come up.

## The practical takeaway

If I could sneak one durable idea into your brain and leave before security notices, it would be this:

**Data is never just data. It is always data in a representation.**

When you understand the representation, a lot of "weird computer behavior" stops being weird.

Overflow stops being weird.
Encoding bugs stop being weird.
Floating-point surprises stop being weird.
Hex dumps stop looking like encrypted spite.
System boundaries start making more sense.

You do not need to memorize every encoding standard or numeric format on Earth.

But you do want the instinct to ask:

* What is this value supposed to represent?
* How is it actually stored?
* What assumptions is this system making?
* What happens at the edges?

Those questions will save you from an astonishing number of mistakes.

And they will make you much more dangerous in the best possible way.

If this helped untangle the machine a bit, follow along for the rest of the course, drop a comment with the weirdest encoding or number bug you have ever seen, and share this with someone who still thinks text files are just "letters in a file." They are. Until they absolutely are not.

**[Art Prompt (neoclassical):](https://lumaiere.com/?gallery=neoclassical)** A serene neoclassical interior arranged with calm architectural symmetry, where young scholars gather around a polished stone table covered in geometric instruments, folded maps, wax tablets, ribbons, and luminous glass vessels filled with jewel-toned pigments; soft golden daylight pours through high columns and diffused linen curtains, illuminating pale marble floors, muted coral drapery, powder blue accents, antique gold trim, and creamy ivory walls; the composition is balanced and graceful, with poised gestures, refined contours, delicate faces, and a mood of thoughtful dignity mixed with quiet wonder, painted with smooth surfaces, crisp edges, and elegant clarity, evoking intellectual beauty and measured harmony without depicting any modern technology

**[Video Prompt:](https://www.tiktok.com/@davelumai/video/7632139565049990431)** In a luminous neoclassical hall, geometric tools, ribbons, tablets, and glowing pigment vessels spring into rhythmic motion the instant the scene begins; scholars pivot sharply, fabrics ripple in sync, colored light pulses across marble floors, circular arrangements assemble and reassemble like visual math, and the whole composition moves with precise, catchy choreography designed for short-form video, with elegant whip transitions, orbiting objects, and a final satisfying lock into perfect symmetry

A couple songs that fit the video nicely: **Numbers - Daughter** and **Algorithm - Muse**.
