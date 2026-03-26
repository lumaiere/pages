# **Episode 10: Files, Input, and Output, or How Programs Stop Living Entirely Inside Their Own Heads**

If you are just joining this increasingly suspicious little computer science caravan, the path here began with [Episode 1: What Is CS 101?](https://medium.com/@DaveLumAI/back-to-basics-cs-101-explained-like-youre-holding-the-syllabus-upside-down-554961c6e0b8), continued through [Episode 2: Programming Fundamentals Part 1: Variables and Conditionals](https://medium.com/@DaveLumAI/programming-fundamentals-part-1-variables-and-conditionals-aka-teaching-a-computer-to-stop-2d94ab24b91a), [Episode 3: Loops and Functions](https://medium.com/@DaveLumAI/episode-3-loops-and-functions-or-how-to-stop-copy-pasting-yourself-into-madness-fac07f2d1bc4), [Episode 4: Algorithmic Thinking](https://medium.com/@DaveLumAI/algorithmic-thinking-the-superpower-you-already-use-you-just-dont-call-it-that-e7242fa13527), [Episode 5: Data Structures](https://medium.com/@DaveLumAI/episode-5-data-structures-putting-things-somewhere-so-you-can-find-them-again-51483812ac35), [Episode 6: History, Debugging, and Problem Solving](https://medium.com/@DaveLumAI/efe6db927fd3), [Episode 7: Recursion and Problem Decomposition](https://medium.com/@DaveLumAI/episode-7-recursion-and-problem-decomposition-or-how-to-solve-a-problem-by-making-it-smaller-66f8b6fc19f2), [Episode 8: Complexity and Efficiency](https://medium.com/@DaveLumAI/episode-8-complexity-and-efficiency-or-why-two-correct-programs-can-have-very-different-regret-f6825b54207a), and [Episode 9: Memory and the Machine](https://medium.com/@DaveLumAI/episode-9-memory-and-the-machine-or-what-the-computer-is-actually-doing-while-you-are-feeling-b7bbabe9548f).

Now we arrive at the moment when your program stops talking only to itself and starts interacting with the outside world like a tiny nervous intern with clipboard access.

This episode is about files, input, and output.

Or, to put it more bluntly, this is the chapter where software stops existing entirely on vibes.

A program can do beautiful logic all day long, but if it cannot read anything, accept anything, save anything, display anything, or hand anything off to another system, it is basically a very organized monologue. Impressive in theory. Less helpful in practice.

So let us fix that.

## **What is files, input, and output?**

Input is any information a program receives.

Output is any information a program produces.

A file is one of the most common ways programs keep information around after the program itself has stopped running and gone home emotionally.

That means keyboard input is input. A web form is input. A sensor reading is input. A CSV someone emailed you at 4:52 PM on a Friday is input, although also a cry for help.

Output can be text on a screen, a saved image, a PDF, a database write, a log entry, a network response, or a friendly message explaining why your code has once again declined to cooperate.

And files sit in the middle of this whole arrangement as durable storage. Memory is temporary. Files are what you use when you want your data to survive longer than your current mood.

## **Is it still relevant?**

Painfully, gloriously, permanently yes.

Files, input, and output are not old-fashioned leftovers from the era of floppy disks and beige sadness. They are still everywhere. Programs read configuration files, process uploads, write logs, save images, export reports, cache results, serialize data, and talk to APIs that are basically input and output wearing nicer shoes.

Even modern cloud systems that love pretending they are too sophisticated for ordinary file handling still spend huge amounts of time reading data, writing data, buffering data, streaming data, validating data, and storing data somewhere that had better still exist tomorrow.

In other words, this topic did not age out.

It became the floor.

## **What is it used for?**

Almost everything useful.

Programs use input and output to:

* receive commands from users
* load saved settings
* read spreadsheets, images, text, and JSON
* write reports and exports
* log what happened when everything catches fire
* communicate with databases and web services
* save progress, preferences, uploads, and results

Even a simple calculator app is doing output.

Even a game save is file I/O.

Even an AI system is constantly consuming input and producing output at industrial scale.

So when someone asks what file and I/O concepts are used for, the honest answer is: nearly every moment when software touches reality.

## **What are the strengths and weaknesses?**

The strengths are obvious and wonderful.

Files let data persist.

Input lets software respond.

Output lets software become useful.

Together they let programs stop being sealed containers and start becoming tools.

The weaknesses are also obvious and less wonderful.

The real world is messy.

People type strange things.

Files go missing.

Permissions get weird.

Formats drift.

Encodings become dramatic.

Paths break.

Someone uploads a file called final_report_revised_FINAL_v2_REAL.xlsx and your code has to pretend this is a normal society.

So the strength of I/O is that it connects your program to life.

The weakness of I/O is that life connects back.

## **Pros and cons**

**Pros**

Programs become practical instead of purely academic.

Data can survive after the program exits.

Users can actually interact with the thing you built.

Information can move between systems.

Automation becomes possible.

**Cons**

Now you have to validate everything.

Now failure modes multiply.

Now your code has to care about missing files, malformed input, partial writes, permissions, timing, network hiccups, and the dark art of explaining errors without sounding personally offended.

The machine was simpler before the outside world showed up.

Sadly, the outside world is where all the customers are.

## **What is the history here? Who invented it?**

No one person gets to wear the crown here.

Input and output are older than most of the software vocabulary we casually throw around. Early computing dealt with punched cards, paper tape, printers, terminals, magnetic storage, and later file systems that let programs store and retrieve data with something approaching dignity.

So if you are looking for one grand inventor, you are going to be disappointed in the way history often disappoints people hoping for a clean villain or hero.

File handling and I/O are really a stack of ideas built across hardware, operating systems, programming languages, and user interfaces. Different systems made them friendlier, faster, safer, and less likely to ruin your afternoon, but the core idea has been there from the beginning: computers need a way to receive information and a way to send it back out.

Which is honestly less a feature than the minimum requirement for not being a decorative brick.

## **When was it most popular? Is it going up or down?**

This is like asking when breathing was hottest.

Files and I/O are not fashionable in the way a framework is fashionable. They are foundational. They do not spike because they never really left the building.

If anything, they are more central than ever because software now handles more formats, more devices, more data streams, more integrations, and more distributed systems than before. The surface area expanded. The need did not shrink.

So no, it is not going down in popularity.

It is just so essential that people forget it is a topic until their code has to read a file from a folder it suddenly cannot find.

## **Is it similar to anything else? What are the alternatives?**

Yes.

At a conceptual level, file I/O is just one version of a larger theme: moving information between a program and something outside that program.

Files are one option.

Alternatives include databases, API calls, message queues, in-memory caches, browser storage, standard input and output streams, and direct device communication.

If a file is like putting a letter in a labeled drawer, an API is more like calling another office and asking for the answer live, while a database is like hiring a very fast librarian with trust issues.

You choose based on what you need:

* files for straightforward persistence and exchange
* databases for structured querying and relationships
* APIs for live system-to-system communication
* queues for asynchronous workflows
* caches for speed
* streams for continuous or transient data

So files are not the only game in town.

They are just one of the oldest, most useful, and least glamorous workhorses in software.

## **Can you give me an example?**

Absolutely.

Imagine you are writing a tiny program that reads a list of expenses from a JSON file, totals them, and writes out a short summary.

That is already multiple important ideas at once:

* input from a file
* structured data parsing
* computation in memory
* output back to disk

Here is a simple example in Python:

```python
import json
from pathlib import Path

input_path = Path("expenses.json")
output_path = Path("summary.txt")

with input_path.open("r", encoding="utf-8") as f:
    expenses = json.load(f)

total = sum(item["amount"] for item in expenses)
count = len(expenses)

summary = (
    f"Expense count: {count}\n"
    f"Total amount: ${total:.2f}\n"
)

with output_path.open("w", encoding="utf-8") as f:
    f.write(summary)

print("Summary written to summary.txt")
```

That little script is not flashy, but it is doing real work.

It reads data that already exists, turns it into something usable, and writes a result someone can keep.

That is how a shocking amount of practical software begins.

## **What is serialization, and why does it sound like a legal problem?**

Serialization is the process of converting data in memory into a format that can be stored or transmitted.

If your program has a dictionary, object, record, or some other structured shape in memory, that is great for the program.

It is less great for a file unless you translate it into a format like JSON, CSV, XML, or something binary and specific.

So serialization is just the act of packing your program's data into a form that can travel.

And deserialization is the reverse: opening the suitcase and reconstructing the data on the other end without losing anyone's socks.

## **What are the biggest beginner mistakes here?**

There are several classics.

Trusting input too much.

Assuming files always exist.

Assuming text is always encoded how you think it is.

Forgetting that a program can fail halfway through a read or write.

Treating storage and memory like they are the same place.

They are not.

Memory is where data lives while your program is running.

Storage is where data waits when your program is not.

That difference matters.

If you compute a result and never save it, it vanishes when the program ends. The machine is not being cruel. It is simply refusing to become your unpaid archivist.

## **Does this work well with AI?**

Extremely well.

In fact, AI systems are some of the hungriest I/O creatures we have ever built.

They read training data, checkpoints, prompts, configuration files, embeddings, logs, evaluation outputs, model weights, cached artifacts, and user uploads. Then they produce responses, metrics, images, transcripts, structured data, and enough intermediate files to frighten an organized person.

AI may look futuristic, but underneath the glossy layer it still relies heavily on plain old input and output. The models are fancy. The data plumbing is relentless.

So yes, this topic works very well with AI.

More importantly, AI falls apart without it.

## **What tech stack does it work with? What tools work best?**

Basically all of them.

If you want official examples wearing clean documentation and a responsible haircut, Python covers file reading, writing, and JSON in the [Python input/output tutorial](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) and the [json module docs](https://docs.python.org/3/library/json.html), JavaScript and server-side applications lean heavily on the [Node.js fs module](https://nodejs.org/api/fs.html), browser-side file handling shows up in the [MDN File API](https://developer.mozilla.org/en-US/docs/Web/API/File_API), and if your "file handling" starts growing opinions and relationships, you may find yourself sliding toward something like [SQLite](https://www.sqlite.org/index.html).

As for tools, the useful ones are rarely glamorous:

* text editors
* logging tools
* CSV and JSON parsers
* file watchers
* database browsers
* API clients
* test fixtures
* command-line utilities

The best tools are the ones that help you inspect what actually went in and what actually came out, because I/O bugs love confusion more than they love complexity.

## **What companies use it the most?**

All of them.

Banks, hospitals, game studios, logistics firms, streaming platforms, schools, retailers, AI companies, government agencies, design tools, operating systems, and the app that keeps sending you cheerful notifications while your battery dies.

Once a company uses software that stores, reads, exports, uploads, logs, syncs, or communicates, it is using I/O concepts whether or not anyone in the meeting says the phrase out loud.

So the real answer is not "which companies use it most."

The answer is "which companies are currently pretending they do not."

## **How much is it going to cost me?**

Learning it?

Very little.

Using it?

That depends on scale.

Basic file reading and writing in a local script can cost effectively nothing beyond your time and a faint sense of suspicion.

At larger scale, the costs come from storage, bandwidth, cloud services, databases, backups, monitoring, and the engineering time required to keep data from becoming a pile of contradictory ghosts.

The concept itself is cheap.

Getting it wrong can be wildly expensive.

## **Is it the subject of any famous art?**

Not directly, unless you count every cinematic image of a glowing terminal as modern mythology.

Files and I/O are not exactly the muse of oil painters. No one stands in a museum whispering, "Ah yes, behold the eternal beauty of buffered writes."

But conceptually, there is something strangely artistic about translation, storage, and transfer. You take one form, move it through a system, and reassemble it somewhere else. That is not so far from editing, printing, recording, collage, filmmaking, or music production.

So while file I/O is not the subject of famous art in the tidy literal sense, it absolutely sits underneath a huge amount of digital creativity.

Which is close enough for this classroom.

## **Any other interesting tidbits?**

Yes.

A lot of "software bugs" are really input assumptions wearing fake mustaches.

A program works beautifully with the clean sample data from your tutorial, then collapses when a real human types an apostrophe, uploads a giant file, leaves a field blank, uses an emoji, or saves something in a format last updated during the reign of small dragons.

That is why file and I/O work matters so much. It teaches humility.

Not poetic humility.

Operational humility.

It teaches you that software is not done when the logic is correct. It is done when the logic survives contact with actual people, actual files, and actual systems.

Which is much ruder and therefore much more educational.

## **So what do we do with this?**

We stop thinking of programs as sealed puzzles and start thinking of them as participants in a larger world.

We learn how to read.

We learn how to write.

We learn how to store data in forms that survive.

We learn how to validate what comes in and how to shape what goes out.

And we accept, with the tired dignity of everyone who has ever debugged a path issue at 11:40 PM, that reality is now part of the assignment.

That is Episode 10.

Programs do not live on vibes alone.

They live on input, output, and the tiny miracle of not losing the file you just swore you saved.

If you enjoyed this episode, follow along for the rest of CS 102, leave a comment with the most ridiculous file name or input bug you have ever encountered, and tell me which part of "real-world software" you want this series to tackle next.

**[Art Prompt (Ancient Art):](https://lumaiere.com/?gallery=ancient)** A monumental mosaic scene unfolding with dense, jewel-like tesserae and dramatic diagonals, centered on a moment of violent motion between a charging force and a suddenly recoiling rival. Let the composition feel crowded yet exquisitely ordered, with spears, horse necks, windswept drapery, and flashing eyes all interlocked in a storm of movement across a shallow pictorial space. Use a palette of deep terracotta, dusty gold, obsidian black, oxidized bronze, pale stone, muted cobalt, and sunlit cream, with tiny reflective surfaces creating a subtle shimmer across armor, fabric, and animal forms. The mood should feel heroic, tense, and breathless, as if history has been compressed into one glittering instant. Keep the textures tactile and handcrafted, with slight irregularities in the surface that reveal the labor of countless small pieces locked into one grand image.

**[Video Prompt:](https://www.tiktok.com/@davelumai/video/7621381224396852510)** Begin with an extreme close-up of shimmering mosaic tiles catching light like tiny fragments of metal and stone, then rush laterally across the surface as if the image is waking up from stillness. Let the camera weave through charging horses, angled spears, and sweeping drapery with quick forward motion, parallax shifts, and sudden reframing that makes the ancient scene feel alive and urgent. Add flickers of reflected light across gold and terracotta surfaces, subtle dust in the air, and rhythmic zoom-ins on fierce eyes, tense hands, and cracking motion lines implied by the composition. Keep the movement energetic and elegant, with the image feeling handcrafted yet cinematic, and end on a wide reveal of the full mosaic glowing like a battlefield preserved inside light.

Two songs to pair with it:

- Night Drive - Chromatics
- Sonate Pacifique - L'Impératrice

Follow for more art, code, and cultured computational mischief, and drop a comment: what is the first file, format, or input disaster that ever made you realize software was not built in a peaceful universe?

