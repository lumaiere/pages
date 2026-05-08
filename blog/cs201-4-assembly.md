# **Episode 4: Assembly Language and the Machine Model, or Programming With Fewer Comforts and More Consequences**

Welcome back to CS201, the course where we keep pulling up the floorboards under your code and finding smaller, stranger machines underneath.

In **[CS201 Episode 1 - How a Computer Actually Runs a Program](https://medium.com/@DaveLumAI/how-a-computer-actually-runs-a-program-or-why-your-code-does-not-levitate-into-reality-by-positive-2c0127117462)**, we watched source code become something the machine can execute. In **[CS201 Episode 2 - Bits, Bytes, and Data Representation](https://medium.com/@DaveLumAI/episode-2-bits-bytes-and-data-representation-or-how-everything-becomes-zeros-ones-and-88e98577be19)**, we admitted that numbers, text, images, and your suspiciously named `final_final_REAL_final` file all become patterns of bits. In **[CS201 Episode 3 - Logic, Gates, and Digital Circuits](https://medium.com/@DaveLumAI/episode-3-logic-gates-and-digital-circuits-or-tiny-electrical-decisions-all-the-way-down-683a8043c6fc)**, we dropped even lower and saw that hardware is built from tiny electrical decisions that somehow grew up, got jobs, and now run civilization.

Now we arrive at assembly language.

Assembly is the place where programming stops wearing a nice jacket.

It is not quite raw machine code, because raw machine code is mostly numbers and sadness. But it is much closer to what the processor actually does than Python, JavaScript, C++, Java, or any other language that lets you pretend memory is a friendly neighborhood and not a warehouse full of numbered boxes guarded by a raccoon with a clipboard.

Assembly language is not usually where you want to build your next web app.

But it is one of the best places to understand what your code eventually becomes.

And once you see that, a lot of higher-level programming starts making more sense.

## **The big idea: assembly is a readable form of machine instructions**

At the lowest practical level, a CPU executes instructions.

Not “ideas.”

Not “features.”

Not “business logic.”

Instructions.

An instruction might say:

Move this value.

Add these two values.

Compare these two values.

Jump somewhere else if the comparison went a certain way.

Load something from memory.

Store something into memory.

That is the machine’s daily routine. Very disciplined. Very literal. Not big on vibes.

Assembly language gives human-readable names to those machine instructions. Instead of writing raw binary numbers like a haunted accountant, you write short symbolic instructions such as:

```asm
mov eax, 5
add eax, 3
```

That is not a complete program, and different processors use different assembly languages, but the idea is simple enough:

Put 5 into a register named `eax`.

Add 3 to it.

The CPU is not thinking, “Ah yes, arithmetic.”

It is performing a tiny mechanical action defined by its instruction set.

Assembly lets us talk to that machine model almost directly.

## **Wait, what is the machine model?**

A machine model is the simplified picture of how a computer appears to a programmer at a certain level.

At the assembly level, the machine usually looks like this:

A CPU has registers.

Memory holds bytes at addresses.

Instructions operate on registers and memory.

The program counter tracks which instruction runs next.

Condition flags remember certain results from recent operations.

The stack helps manage function calls and temporary data.

That is the basic mental model.

It is not the entire truth of modern processors, because modern processors are doing all kinds of wizardry under the floor: pipelining, caching, prediction, reordering, speculation, and other behaviors that sound like the CPU has been reading productivity books.

But assembly gives us the first honest working model.

It says: here is the CPU, here are the instructions, here is memory, and here is how control moves.

That is enough to start seeing what your high-level code is standing on.

## **Registers: the CPU's tiny workbench**

Memory is large.

Registers are small.

Memory is where a program keeps lots of data. Registers are where the CPU keeps the data it is actively working with right now.

Think of memory as the storage room and registers as the items currently on the workbench.

A CPU cannot do most operations directly on everything in memory all at once. It usually needs values loaded into registers first, operated on there, then stored back if needed.

A rough assembly-style flow might look like:

```asm
mov eax, [x]
add eax, [y]
mov [result], eax
```

In plain English:

Load `x` into a register.

Add `y`.

Store the result.

The exact syntax varies by architecture, but the machine-level idea is steady: values move between memory and registers, and instructions manipulate those values.

This is why registers matter.

They are fast, limited, and central to the CPU’s actual work.

In high-level programming, you might write:

```c
result = x + y;
```

That feels like one idea.

Underneath, it may become several smaller actions involving loading, adding, and storing.

That does not mean you should panic every time you write a plus sign. Please do not start apologizing to the compiler. It has enough going on.

It means the simple line of code is backed by a machine-level choreography.

## **Memory: the giant numbered cabinet**

In earlier work, especially **CS102 Episode 9 - Memory and the Machine**, we looked at memory as one of the key reasons programs behave the way they do. That episode is worth revisiting here: **[CS102 Episode 9 - Memory and the Machine](https://medium.com/@DaveLumAI/episode-9-memory-and-the-machine-or-what-the-computer-is-actually-doing-while-you-are-feeling-confident-b7bbabe9548f)**.

At the assembly level, memory is mostly seen as addresses.

An address is a location.

The CPU does not care that you lovingly named your variable `customerTotal`.

By the time the program runs, that name has usually been replaced with a location, offset, register, or some other lower-level representation.

A high-level variable feels like a labeled container.

At the machine level, it is more like:

Go to this address.

Read this many bytes.

Interpret them according to the instruction and context.

Try not to ruin anything important.

This is one reason bugs involving memory can be so spectacular. If your program reads or writes the wrong address, it may not get a polite error message. It may corrupt data, crash, expose security weaknesses, or quietly produce nonsense while looking very confident.

Computers are extremely obedient.

That is not always the same thing as being helpful.

## **Instructions: small steps, big consequences**

Assembly instructions are generally simple.

That simplicity is powerful, but it also means the programmer has to be explicit.

A high-level language might let you write:

```python
if count > 10:
    print("Too many")
```

That looks friendly.

At a lower level, the machine needs a comparison and a decision about where to go next.

Very roughly, this turns into a pattern like:

```asm
cmp count, 10
jle skip_message
; code to print the message
skip_message:
```

Again, syntax varies, but the concept is the important part.

Compare `count` to 10.

If it is less than or equal, jump over the message-printing code.

Otherwise, continue into the code that prints the message.

This is how conditionals become machine behavior.

Not magic.

Not emotional judgment.

Comparison and jump.

Your elegant `if` statement is really a polite mask over a tiny traffic controller.

## **Jumps: how programs stop walking in a straight line**

Without jumps, programs would just execute one instruction after another until they ran out of road.

Jumps allow loops, conditionals, function calls, error handling, and most of the interesting parts of execution.

A loop in a high-level language might look like this:

```c
while (i < 10) {
    i++;
}
```

At the assembly level, the shape is closer to:

```asm
loop_start:
    cmp i, 10
    jge loop_end
    add i, 1
    jmp loop_start

loop_end:
```

That is the loop’s skeleton.

Check the condition.

If done, leave.

Otherwise do the body.

Jump back.

This is the machine-level version of repetition.

In **CS101 Episode 3 - Programming Fundamentals Part 2: Loops and Functions**, loops may have looked like a friendly way to avoid copying yourself into madness. At this layer, you can see that a loop is really controlled movement through instruction addresses: **[CS101 Episode 3 - Programming Fundamentals Part 2: Loops and Functions](https://medium.com/@DaveLumAI/episode-3-loops-and-functions-or-how-to-stop-copy-pasting-yourself-into-madness-fac07f2d1bc4)**.

That is a nice little moment in computer science.

The thing that felt abstract becomes physical-ish.

Your loop is not “looping” because the universe enjoys repetition.

It is jumping backward.

## **The program counter: the tiny bookmark of destiny**

The CPU needs to know which instruction comes next.

That job belongs to the program counter, sometimes called the instruction pointer.

It holds the address of the next instruction to execute.

Most of the time, after an instruction runs, the program counter advances to the next instruction.

But jumps, branches, calls, returns, and interrupts can change it.

That is control flow.

At a high level, control flow is the path your program takes.

At a machine level, control flow is the changing value of the instruction pointer.

This matters because many serious bugs and security problems involve control flow going somewhere it should not.

If an attacker can influence where the program counter goes, the program may begin executing unintended instructions.

That is not a small problem.

That is the software equivalent of handing the steering wheel to a raccoon and then acting surprised when the car visits a pond.

## **The stack: where function calls leave their shoes**

The stack is a region of memory used to manage temporary data, especially function calls.

When one function calls another, the program needs to remember where to return afterward. It may also need to pass arguments, store local variables, and save register values.

The stack helps with that.

A simplified function call involves:

Saving return information.

Giving the called function what it needs.

Letting the function run.

Returning to the correct place.

Cleaning up afterward.

In high-level code, this looks innocent:

```c
int square(int x) {
    return x * x;
}

int y = square(5);
```

At the machine level, a function call involves instructions that move values, update the stack, jump to the function, and return.

This is why recursion, which you met in **CS102 Episode 7 - Recursion and Problem Decomposition**, has a real memory cost. Each call needs its own little stack frame unless the compiler can optimize it away: **[CS102 Episode 7 - Recursion and Problem Decomposition](https://medium.com/@DaveLumAI/episode-7-recursion-and-problem-decomposition-or-how-to-solve-a-problem-by-making-it-smaller-66f8b6fc19f2)**.

Recursion is not just a beautiful idea.

It also rents space.

And the stack is not infinite.

If you recurse too deeply, you can run out of stack space. Then the program falls over with the dramatic flair of a folding chair at a family reunion.

## **A concrete example: adding two numbers**

Let us start small.

High-level code:

```c
int a = 7;
int b = 4;
int c = a + b;
```

The programmer sees:

Make `a`.

Make `b`.

Add them.

Store the result in `c`.

The assembly-level idea may be:

```asm
mov eax, 7
mov ebx, 4
add eax, ebx
mov [c], eax
```

This says:

Put 7 in one register.

Put 4 in another.

Add them.

Store the result.

The actual assembly generated by a compiler may differ depending on the processor, compiler settings, optimization level, calling convention, and whether the compiler decided your code was so simple it could remove half of it before breakfast.

But the basic concept stands.

High-level operations become lower-level operations.

The lower-level operations work with registers, memory, and instructions.

This is why assembly is educational even when you do not plan to write it every day.

It shows you the cost and shape of computation.

## **A more realistic example: why performance is not just "the code looks short"**

Suppose you have two versions of a program.

One uses a tight loop over an array.

Another jumps around through a linked structure in memory.

At the high level, both might look clean.

But the CPU may treat them very differently.

Arrays often place data close together in memory. That can help caching, because modern processors fetch memory in chunks. If you access one element, nearby elements may already be pulled closer to the CPU.

Linked structures may require following pointers from one memory location to another. That can cause more cache misses, because the next piece of data might be somewhere else entirely, living its best life in a distant memory neighborhood.

Assembly helps you see why.

The program is not just “doing an algorithm.”

It is loading addresses, reading memory, branching, comparing, and waiting on data.

This connects directly to **CS102 Episode 8 - Complexity and Efficiency**, where two correct programs can have very different performance behavior: **[CS102 Episode 8 - Complexity and Efficiency](https://medium.com/@DaveLumAI/episode-8-complexity-and-efficiency-or-why-two-correct-programs-can-have-very-different-regret-f6825b54207a)**.

Big-O notation gives you a broad model.

The machine model gives you another layer: locality, instruction count, branching behavior, memory access patterns, and CPU architecture.

Both matter.

One tells you the shape of the problem.

The other tells you what the machine is actually being asked to do.

## **Why high-level code does not map perfectly to assembly**

A beginner might imagine each line of high-level code turns neatly into a few lines of assembly.

Sometimes it does.

Often it does not.

Compilers are not simple translators. They are aggressive little optimization goblins.

They may remove code.

Reorder operations.

Inline functions.

Use different registers.

Avoid memory entirely.

Replace multiplication with shifts or additions when appropriate.

Unroll loops.

Vectorize operations.

Move calculations out of loops.

Make your assembly output look nothing like what you emotionally prepared for.

This is not betrayal.

This is optimization.

The compiler’s job is not to preserve your source code’s visual poetry. Its job is to produce correct machine code, preferably faster than what a tired human would write at 1:17 AM while muttering at a debugger.

This creates an important lesson:

High-level code describes behavior.

Assembly reveals one possible implementation of that behavior.

The exact implementation depends on the compiler, target architecture, optimization settings, and surrounding context.

That is why assembly teaches humility.

A very useful, slightly annoying humility.

## **Different processors, different assembly languages**

Assembly is not one universal language.

x86-64 assembly is different from ARM assembly.

RISC-V assembly is different again.

Even syntax can vary depending on assembler conventions.

This is because assembly language is closely tied to the instruction set architecture, or ISA.

An ISA defines the machine-level instructions a processor understands, the registers available, how memory is addressed, and the rules for executing instructions.

Common examples include:

x86-64, widely used in desktops, laptops, and servers.

ARM, widely used in phones, tablets, embedded systems, and increasingly laptops and cloud servers.

RISC-V, an open instruction set used in education, research, embedded systems, and growing commercial work.

The ISA is the contract between software and hardware.

Hardware says, “I can execute these instructions.”

Software says, “Fine, I will compile to those instructions.”

Then they shake hands and immediately start arguing about performance.

## **CISC, RISC, and the tiny history goblin**

Historically, processor designs have often been discussed through the lens of CISC and RISC.

CISC stands for Complex Instruction Set Computer.

RISC stands for Reduced Instruction Set Computer.

The classic idea is that CISC processors offer more complex instructions, while RISC processors favor simpler instructions that can be executed efficiently and composed into larger behavior.

That historical distinction still matters, but modern processors are more complicated than the old textbook battle makes it sound.

Modern x86-64 processors may expose a complex instruction set but internally break instructions into smaller operations. Modern ARM processors are not magically simple just because they come from a RISC tradition. Everyone has been learning tricks from everyone else for decades.

The lesson is not “one good, one bad.”

The lesson is tradeoffs.

Complex instructions can make some operations compact and preserve compatibility with older software.

Simpler instruction sets can make hardware design, pipelining, power efficiency, and compiler targeting cleaner in certain ways.

Modern systems are full of compromises because reality refuses to fit into a tidy lecture slide.

Rude, but educational.

## **Why assembly still matters when you almost never write it**

Most developers do not spend their day writing assembly.

That is good.

Civilization has endured enough.

But assembly still matters because it explains several things that higher-level programmers run into constantly.

It explains why integer overflow can happen.

It explains why memory layout affects performance.

It explains why function calls have overhead.

It explains why recursion can run out of stack.

It explains why compiled code may behave differently under optimization.

It explains why security bugs involving buffers and control flow can be so dangerous.

It explains why different CPU architectures can require different builds.

It explains why low-level debugging sometimes involves reading disassembly.

It explains why performance work cannot always stop at “but the code looks clean.”

Clean code is wonderful.

But clean code still becomes instructions.

And the machine has opinions.

## **Assembly and debugging: when the polite layers fail**

Most of the time, you debug in your source language.

You use logs, tests, stack traces, breakpoints, and the noble ritual of staring at a line of code until it confesses.

But sometimes the bug lives at a lower layer.

Maybe optimized code behaves unexpectedly.

Maybe a crash happens in native code.

Maybe a pointer is corrupted.

Maybe a library compiled for one architecture is being used on another.

Maybe a security investigation requires understanding where execution went.

Maybe you are working in embedded systems, operating systems, compilers, game engines, drivers, performance-critical services, or native C++ code where the machine is less politely hidden.

Then assembly becomes less of a historical curiosity and more of a flashlight.

You do not need to love it.

But you should know what room you are standing in.

## **Assembly and AI-era development**

In modern AI-assisted coding, assembly might seem even further away.

After all, if an AI tool can generate application code, why think about registers and jumps?

Because abstraction did not disappear.

It multiplied.

AI can help generate code, explain code, write tests, and accelerate workflows. But the generated code still runs on machines. It still consumes memory. It still branches. It still calls functions. It still depends on libraries compiled for particular architectures. It still has performance characteristics. It can still contain unsafe assumptions.

AI can make you faster.

It does not repeal computer architecture.

In fact, the better your machine model, the better you can judge AI-generated answers when the question touches performance, memory, native code, build targets, cloud deployment, or low-level behavior.

If a tool suggests something that is elegant but cache-hostile, unsafe, architecture-specific, or wildly inefficient, your understanding of the machine model gives you a fighting chance to notice before production becomes a fireworks exhibit.

Not the fun kind.

The incident-report kind.

## **Common misconception: assembly is "what the computer really thinks"**

The computer does not think in assembly.

Assembly is still for humans.

The actual CPU executes encoded machine instructions: binary patterns interpreted according to the processor’s instruction set.

Assembly is a readable notation for those instructions.

That distinction matters.

Assembly is lower-level than C or Python, but it is still an abstraction.

Below assembly are machine code, microarchitecture, logic circuits, transistors, electrical behavior, and physics quietly carrying the whole parade while asking for no applause.

This is a pattern in computer science:

Every layer feels like “the real one” until you look underneath it.

Then you find another layer wearing work boots.

## **Common misconception: assembly is always faster**

Handwritten assembly can be faster in some cases.

It can also be worse.

Modern compilers are extremely good at optimization. They know instruction scheduling, register allocation, calling conventions, vectorization opportunities, and architecture-specific details that most humans do not want to keep in their heads unless they have made certain life choices.

Handwritten assembly may be useful for:

Tiny performance-critical kernels.

Embedded systems.

Special hardware instructions.

Cryptographic routines.

Operating system kernels.

Boot code.

Reverse engineering.

Highly constrained environments.

But for normal application development, writing assembly manually is usually not the best tradeoff.

It can make code harder to read, harder to maintain, harder to port, and easier to break in creative new ways.

Performance is not just about making the machine happy today.

It is also about letting future humans understand what you did without quietly placing a curse on your name.

## **Common misconception: high-level programmers do not need this**

You do not need assembly every day.

But you benefit from understanding it.

If you understand assembly and the machine model, even lightly, then several things become clearer:

Why values have sizes.

Why memory addresses matter.

Why arrays and pointers are powerful.

Why compiled programs are architecture-specific.

Why stack traces exist.

Why crashes are sometimes not random.

Why some bugs appear only under optimization.

Why performance can depend on data layout.

Why systems programming demands respect.

Why “it works on my machine” is not a deployment strategy so much as a tiny autobiography.

This is also where earlier CS101 material grows up. In **CS101 Episode 2 - Programming Fundamentals Part 1: Variables and Conditionals**, variables and conditionals were the user-friendly concepts. Here, we see their machine-level shadows: storage locations, comparisons, jumps, and state changes: **[CS101 Episode 2 - Programming Fundamentals Part 1: Variables and Conditionals](https://medium.com/@DaveLumAI/programming-fundamentals-part-1-variables-and-conditionals-aka-teaching-a-computer-to-stop-2d94ab24b91a)**.

That continuity matters.

Computer science is not a pile of disconnected topics.

It is a stack.

And today we are standing closer to the metal.

## **A practical example: reading disassembly without panic**

Suppose you compile this simple C function:

```c
int add_one(int x) {
    return x + 1;
}
```

A compiler might produce assembly with a simple add instruction and return.

A readable pseudo-assembly version might look like:

```asm
add argument_register, 1
return
```

The exact register name depends on the architecture and calling convention.

The important thing is the pattern:

The input arrives somewhere expected.

The CPU adds 1.

The result is returned according to the platform’s rules.

Now imagine a more complex function:

```c
int max(int a, int b) {
    if (a > b) {
        return a;
    }

    return b;
}
```

The assembly-level version involves comparison and control flow.

Something like:

```asm
cmp a, b
jle return_b
return_a:
    return a
return_b:
    return b
```

That is the machine model showing through the curtain.

Comparison.

Conditional jump.

Return one value or another.

Once you see this, high-level code feels less magical and more grounded.

Still elegant, hopefully.

Just less haunted.

## **Assembly, portability, and why your build has a target**

When you compile a program, you compile it for a target.

That target includes an operating system, architecture, binary format, and calling conventions.

A program built for x86-64 Linux is not automatically the same as a program built for ARM macOS or ARM Linux.

This is one reason cloud infrastructure, containers, native dependencies, and deployment pipelines care about architecture.

If you build an image for the wrong CPU architecture, your program may not run.

If a native library is missing the right binary, your app may fail at startup.

If you mix architecture assumptions, you can end up with errors that feel absurd until you remember that machine code is not universal poetry. It is very specific instructions for very specific hardware contracts.

This is especially relevant now that ARM-based cloud servers and laptops are common. Developers increasingly build, test, and deploy across mixed environments.

The machine model is not ancient lore.

It is still sitting in the meeting, quietly waiting for someone to notice.

## **Tradeoffs: why we do not program everything this way**

Assembly gives control.

Assembly gives visibility.

Assembly gives precision.

Assembly also gives you many new ways to ruin your afternoon.

High-level languages exist because humans are better at reasoning with bigger concepts.

Variables.

Functions.

Objects.

Modules.

Tests.

Interfaces.

Data structures.

Algorithms.

These abstractions let us build larger systems without manually managing every register and jump.

That connects beautifully to **CS102 Episode 11 - Modular Design and Abstraction**, where the goal was to build programs that do not become junk drawers with login screens: **[CS102 Episode 11 - Modular Design and Abstraction](https://medium.com/@DaveLumAI/episode-11-modular-design-and-abstraction-or-how-to-make-your-code-less-like-a-junk-drawer-9b6273bc3721)**.

Abstraction is not dishonesty.

It is compression.

It lets humans work at the right level most of the time.

The danger is forgetting that lower levels still exist.

Good programmers use abstraction.

Great programmers respect what abstraction is hiding.

## **Where assembly shows up in real work**

You may encounter assembly directly or indirectly in many places:

Compiler output when investigating performance.

Debugger disassembly when source-level debugging is not enough.

Crash dumps and stack traces.

Embedded systems.

Operating system kernels.

Device drivers.

Reverse engineering.

Security research.

Game engines.

Cryptography.

High-performance computing.

Native mobile code.

C and C++ build problems.

Cloud deployments involving mixed CPU architectures.

Even if you mostly write high-level code, the machine model can help you understand why certain tools, errors, and performance problems exist.

It gives you a second map.

And when the first map says “everything should work,” the second map can sometimes point at the smoking crater.

## **What you should remember**

Assembly language is a human-readable representation of machine instructions.

The machine model includes registers, memory, instructions, the program counter, condition flags, and the stack.

High-level code becomes lower-level instructions, but the mapping is not always simple because compilers optimize aggressively.

Conditionals become comparisons and jumps.

Loops become repeated control flow.

Function calls involve stack and calling convention machinery.

Memory access patterns can matter enormously for performance.

Different processors use different instruction set architectures.

Assembly is not something every developer writes daily, but understanding it makes you a stronger programmer.

Not because it turns you into a wizard.

Because it removes one layer of fog.

And computer science has plenty of fog already. Some of it has tenure.

## **The real lesson**

Assembly language is not here to make you abandon high-level programming.

It is here to make high-level programming more real.

When you write a variable, there is storage.

When you write a loop, there is control flow.

When you call a function, there is machinery.

When you access data, there is memory.

When you optimize code, there is a processor with habits.

The point is not to live at the assembly level forever.

The point is to visit long enough that the rest of programming becomes less mysterious.

Your code does not float above the machine.

It lands.

It gets translated.

It moves through registers.

It reads and writes memory.

It jumps.

It returns.

It succeeds, fails, crashes, or performs beautifully depending on how well all the layers cooperate.

And now, when someone says “the computer runs your program,” you know that sentence is doing a heroic amount of laundry.

## **Follow along**

If this helped the machine feel a little less like a glowing oracle and a little more like a very fast, very literal coworker, follow along for the rest of CS201.

Next we move into CPU architecture and performance basics, where processors get faster, weirder, and somehow more judgmental.

Drop a comment with the first low-level concept that made programming click for you, or the one that still feels like it is hiding in the basement with a flashlight.

## **[Art Prompt (Arts and Crafts):](https://lumaiere.com/?gallery=artscrafts)**

A richly ornamental Arts and Crafts style botanical scene inspired by a repeating tapestry design, featuring elegant birds nestled among curling strawberry vines, layered leaves, pale blossoms, and deep blue-green foliage arranged in a rhythmic mirrored pattern; use warm indigo, muted crimson, soft cream, moss green, and earthy ochre tones, with flattened decorative forms, crisp outlines, intricate natural detail, and a handcrafted textile feeling; the mood should be lush, balanced, intimate, and quietly enchanted, like a garden transformed into a living pattern of movement and order.

## **[Video Prompt:](https://www.tiktok.com/@davelumai/video/7636932093683059999)**

Begin with a quick burst of fluttering wings as the patterned birds snap into motion inside the ornamental vines, then have strawberries glow one by one like tiny lanterns while leaves unfurl in rhythmic waves across the frame; the whole design should pulse like an animated tapestry, with mirrored vines curling inward, blossoms opening on beat, birds hopping between branches, and the background subtly shifting between indigo, moss green, and warm cream; keep the motion catchy, loopable, elegant, and suitable for short-form video platforms, ending with the birds returning to their starting positions so the pattern can repeat seamlessly.

## **Songs for the video**

Bibo no Aozora - Ryuichi Sakamoto

Little Fluffy Clouds - The Orb
