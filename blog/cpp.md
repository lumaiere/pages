C++: The Overachieving Middle Child of Programming Languages

You know that feeling when you clean your desk, feel extremely accomplished… and then notice the *entire closet* hasn’t been touched in three years?

That’s what realizing we’ve talked about Web3 languages, whole testing frameworks, and even kicked off this “top languages” tour with Python in [this earlier Python deep dive](https://medium.com/@DaveLumAI/python-the-language-that-looked-at-pseudocode-and-said-move-over-847c87c09f9a)… but hadn’t yet given C++ its own episode feels like.

So let’s fix that.

Welcome to Episode 3: C++ — the language that never quite left the 80s, but somehow runs half the world and still shows up to work in a tailored blazer.

## What Is C++, Really?

C++ is a high-level, general-purpose programming language that grew out of C with extra powers: classes, objects, templates, exceptions, RAII, the whole multi-paradigm buffet. It’s procedural, object-oriented, generic, and even somewhat functional, depending on how weird you decide to get.

It was originally designed to give you:

* Direct control over hardware and memory
* Abstractions that don’t slow you down
* Enough features to make both systems programmers and library designers happy

At heart, C++ is:

> “C, but with tools so you can build skyscrapers instead of just tents.”

You still get pointers, manual memory control (if you want), and bare-metal performance — but you also get `std::vector`, `std::unique_ptr`, templates, lambdas, and a standard library that keeps growing like a very nerdy forest.

## A Tiny Taste: C++ in the Wild

Here’s a small example that shows off modern-style C++ without immediately traumatizing you with templates and metaprogramming:

```cpp
#include <iostream>
#include <vector>
#include <string>

struct TodoItem {
    std::string text;
    bool done = false;
};

int main() {
    std::vector<TodoItem> list = {
        {"Finish Episode 3 blog on C++", true},
        {"Refactor that mysterious legacy service", false},
        {"Finally learn modern C++ (for real this time)", false}
    };

    for (const auto& item : list) {
        std::cout << (item.done ? "[x] " : "[ ] ") << item.text << '\n';
    }
}
```

This tiny program already shows you:

* `struct` with default member initializers
* `std::vector` instead of C-style arrays
* Range-based `for` loop
* No manual `new` / `delete` anywhere

Modern C++ is very much “you *can* use raw pointers, but also… maybe don’t unless you’re doing something very specific.”

## Who Invented C++ and Why?

C++ was created by Bjarne Stroustrup at Bell Labs, starting in 1979. It began as “C with Classes,” then got renamed to C++ in the early 80s. The goal: combine the blazing speed and portability of C with the organizational power of Simula-style object orientation. ([Wikipedia][1])

Key milestones:

* 1979: “C with Classes” experiment begins
* 1983: Officially named “C++” (a nerdy joke on the `++` increment operator)
* 1985: First commercial release
* 1998: First ISO C++ standard (C++98)
* Then: C++03, C++11, C++14, C++17, C++20, C++23… with C++26 on the way

If you want the source straight from the architect, his own site is a great rabbit hole: [Bjarne Stroustrup’s homepage](https://www.stroustrup.com).

## Is C++ Still Relevant in 2025?

Short answer: yes. Longer answer: *very* yes.

C++ is still one of the top languages in the world by popularity indexes like TIOBE, where it’s reached as high as #2 overall and has been named “Language of the Year” more than once. ([TIOBE][2])

Why it refuses to fade:

* It dominates in performance-critical domains
* There’s a huge base of existing C++ code that isn’t going anywhere
* The standard keeps evolving (C++23 just landed; C++26 is in progress) ([Wikipedia][1])

If you’re in systems, games, finance, embedded, or high-performance computing, C++ is still very much not optional.

## What Is C++ Used For?

You’ve almost certainly touched C++ indirectly today, whether you know it or not. Common use cases include:

* **Operating systems and core infrastructure**

  * Parts of Windows, macOS, Linux components, drivers, and tools use C++ under the hood ([Wikipedia][1])

* **Game engines and graphics**

  * Unreal Engine, AAA games, physics engines, real-time rendering — C++ territory all day

* **Browsers and runtime engines**

  * Major browsers use C++ in their layout engines, JavaScript runtimes, and networking stacks

* **Finance and trading**

  * Low-latency trading systems, risk engines, quote systems, and pricing models

* **Embedded systems and devices**

  * Automotive software, IoT, robotics, aerospace, telecom switches

* **AI and high-performance libraries**

  * Many AI frameworks expose Python on top but rely heavily on C++ underneath for performance, GPU access, and memory control ([Conan Blog][3])

It’s the language behind the curtain of a lot of the shiny stuff.

## Who Uses C++ the Most?

Some household-name companies with hefty C++ codebases:

* Microsoft (Windows, Office, game tooling)
* Google (Chrome, search infrastructure, internal libraries)
* Adobe (Photoshop, Premiere, etc.)
* Amazon, Apple, Meta, Tesla, NVIDIA, and plenty more ([GeeksforGeeks][4])

Add to that a huge number of hedge funds, game studios, chip manufacturers, defense contractors, and simulation companies. If you can think of an industry where performance matters, there’s probably C++ inside it somewhere.

## Strengths and Weaknesses (a.k.a. Why It’s Loved and Feared)

### Strengths / Pros

* **Performance**
  Compiles to native machine code with aggressive optimization. Great for low-latency, real-time, or resource-constrained systems.

* **Control**
  You can manage memory, layout, and lifetime explicitly when you need to — or lean on modern abstractions when you don’t.

* **Multi-paradigm**
  Supports procedural, OO, generic, and functional patterns. You can pick the style that fits the problem.

* **Zero-cost abstractions**
  The design goal is that abstractions like `std::vector`, iterators, and templates don’t cost more at runtime than handwritten low-level code.

* **Massive ecosystem**
  Libraries for almost everything: graphics, numerics, networking, game engines, GUI frameworks, scientific computing.

* **Longevity and backward compatibility**
  Old C++ code often still builds (with some nudging), which matters a lot to businesses sitting on 20+ years of investment. ([Wikipedia][1])

### Weaknesses / Cons

* **Complexity**
  The language is big. Very big. Multiple paradigms, template metaprogramming, and decades of added features create a steep learning curve.

* **Footguns**
  Manual memory management, undefined behavior, dangling references, data races, and security holes are possible when you’re careless.

* **Compile times**
  Large modern C++ codebases can have brutal build times, although modules and better build systems are helping.

* **Inconsistency**
  Legacy APIs live alongside modern ones. You can write very beautiful C++ or absolutely cursed C++ in the same file.

So if Python is a friendly bicycle with a little bell, C++ is a high-performance motorcycle that absolutely requires you to respect the throttle.

## How Popular Is C++, and Is It Going Up or Down?

C++ has had a long life near the top of popularity rankings. It’s not the trendy new kid, but it’s stubbornly near the front of the pack:

* Consistently top 5 in TIOBE and similar indexes over many years
* Recently climbed higher again as performance and systems work became more central in AI and cloud infrastructure ([Reddit][5])

Peak popularity by some metrics is right now or very close to it — particularly in 2023–2025, where it’s reached #2 in some rankings. That’s wild for a language that predates most of today’s developers. ([TIOBE][2])

## What Tech Stacks Does C++ Work With?

C++ doesn’t really live in isolation. Common stacks:

* **Desktop / GUI apps**

  * C++ + Qt or wxWidgets
  * C++ back end + platform-specific front end

* **Game development**

  * C++ + Unreal Engine
  * C++ engines with scripting layers (Lua, Python, proprietary languages)

* **Scientific / numeric computing**

  * C++ + Eigen / Blaze / Armadillo
  * C++ libraries wrapped for Python (NumPy, parts of SciPy, and plenty of ML libs rely on C/C++ cores) ([GeeksforGeeks][6])

* **Backend / systems**

  * C++ microservices with gRPC / REST
  * C++ services behind language-agnostic gateways

* **AI / GPU-heavy work**

  * C++ cores with Python frontends
  * C++ code calling CUDA, ROCm, or other accelerator APIs

It plays nicely wherever there’s a need for speed and control.

## Does C++ Work Well with AI?

Yes — just maybe not in the way social media makes it look.

Most demos and tutorials are written in Python, but:

* Many core machine learning libraries and frameworks are implemented in C or C++
* Performance-critical kernels, GPU bindings, and tensor ops often live in C++
* Frameworks like TensorFlow Lite, ONNX Runtime, and Dlib expose C++ APIs and can be consumed via modern C++ build tools ([GeeksforGeeks][6])

So if Python is how you *talk* to AI, C++ is a big part of how AI actually *moves*.

## What Tools Work Best with C++?

There’s a rich toolchain around C++. A (very abridged) shortlist:

* **Compilers**

  * GCC
  * Clang/LLVM
  * MSVC

* **Build systems**

  * CMake (love it or tolerate it, it’s everywhere)
  * Meson, Ninja, and others

* **Package managers**

  * Conan
  * vcpkg

* **IDEs and editors**

  * Visual Studio
  * CLion
  * VS Code with C++ extensions

The [Standard C++ Foundation site](https://isocpp.org) has a ton of up-to-date information on compilers, tools, core guidelines, and events if you want to go deeper. 

## What Are the Alternatives?

If you’re considering C++ today, you’re probably also looking at:

* **[C](https://medium.com/@DaveLumAI/c-the-low-level-legend-that-refuses-to-retire-a85d268cdc5b)**

  * Simpler language; less abstraction, more manual everything
  * Great for very small or extremely constrained systems

* **Rust**

  * Memory-safe by design, with a strict borrow checker
  * Great replacement candidate for some new C++-ish projects, especially where safety and concurrency are key

* **Java / C#**

  * Managed runtimes (JVM / .NET), garbage-collected, large ecosystems
  * Great for business apps, enterprise systems, and large teams

* **Go**

  * Simple language with built-in concurrency and a batteries-included toolchain
  * Strong in cloud services and tooling

* **[Python](https://medium.com/@DaveLumAI/python-the-language-that-looked-at-pseudocode-and-said-move-over-847c87c09f9a)**

  * Great for glue code, AI, scripting, and rapid development
  * Often paired with C++ under the hood for performance-heavy sections

C++ sits in that niche where you want fine-grained control, raw performance, and don’t mind investing in learning the language deeply.

## How Much Does C++ Cost?

The language itself is free.

* Compilers like GCC and Clang are open-source
* Toolchains and libraries often have permissive licenses
* IDEs like Visual Studio Community, VS Code, and some others are free for many use cases

You may pay for:

* Commercial IDEs (e.g., some editions of CLion, Visual Studio, or specialized analysis tools)

* High-quality static analysis tools or code quality platforms

* Training and developer time (which is the *real* cost — good C++ developers are not cheap, and for good reason)

## Is C++ the Subject of Any Famous Art?

There isn’t a famous oil painting titled “Still Life with Pointer and Segfault,” but code — including C++ — definitely shows up in:

* Digital art and generative visuals
* The demoscene (real-time visual demos, many coded in C/C++)
* Gallery installations featuring projected code, compilation visuals, or glitch aesthetics

Most of the “famous art” around C++ is more cultural than literal — think legendary open-source projects, iconic game engines, and mind-bending conference talks that people still reference years later.

## Any Other Interesting Tidbits?

* C++ keeps evolving on a regular release schedule (roughly every 3 years now), with C++23 already standardized and C++26 in progress. ([Wikipedia][1])
* It has a massive conference ecosystem (CppCon, Meeting C++, C++ on Sea, and many more). ([ISO C++][7])
* Many of the guidelines used to teach modern C++ are maintained as living documents, like the C++ Core Guidelines hosted by the Standard C++ Foundation. ([ISO C++][7])

And despite its reputation, modern C++ really is much friendlier than the horror stories from the 90s — as long as you follow current best practices instead of copy-pasting code from 1997.

## So… Should You Learn C++?

If you:

* Care about performance
* Want to build engines, not just apps
* Love understanding “how the machine actually works”
* Or just want to read the source of half the tools you already use

…then yes, C++ is absolutely worth your time.

If you’re already on this “top languages” journey from Episode 1’s Python through to C and now C++, you’re building a very solid mental map of how modern software stacks fit together.

If you’d like more episodes like this, drop a comment, tell me your favorite C++ horror story or feature, and hit follow so you don’t miss Episode 4.

**[Art Prompt (Futurism)](https://lumaiere.com/?gallery=futurism):**

A dynamic city street at night, viewed from a low angle, filled with overlapping, elongated figures that seem to sprint through space, their bodies sliced into sweeping metallic planes that blur into motion trails. Streetlights explode into radiant halos, fractured into sharp geometric shards that radiate outward like shockwaves of energy. Buildings lean forward as if being pulled by speed itself, their facades reduced to intersecting diagonals and mirrored surfaces. The color palette pulses with deep cobalt blues, hot electric oranges, and burnished golds, layered in semi-transparent strokes that suggest vibration and turbulence. Gentle gradients melt into sudden hard edges, creating a sense of unstoppable acceleration, as if time and space are being compressed into a single, glowing, aerodynamic moment.

**[Video Prompt:](https://www.tiktok.com/@davelumai/video/7583150602616589598)**

A short vertical video opens with the city already in motion: streaks of light carving through a night skyline as elongated, faceted figures sprint along a futuristic street, their limbs stretching into shimmering metallic planes. The camera darts and snaps rather than glides, cutting between low-angle shots of leaning skyscrapers and close-ups of faces dissolving into glowing geometric fragments. Streetlights burst into radiant halos that fracture into shards, scattering across the frame like neon confetti before rapidly reassembling into new patterns of energy. The palette pulses between deep cobalt blues and electric oranges, with sudden flashes of gold whenever motion peaks, as if speed itself ignites the scene. Buildings warp and tilt as the perspective shifts, creating the feeling that the entire city is being dragged forward by momentum. In the final seconds, the figures merge into a single streak of light racing toward the horizon, leaving behind a vibrating echo of shapes and reflections that flicker and fade in sync with the beat.

**Song Recommendations for the Video:**

* Reckoner – Radiohead
* Young Blood – The Naked and the Famous


[1]: https://en.wikipedia.org/wiki/C%2B%2B?utm_source=chatgpt.com "C++"
[2]: https://www.tiobe.com/tiobe-index/cplusplus/?utm_source=chatgpt.com "The C++ Programming Language"
[3]: https://blog.conan.io/2024/12/23/You-can-do-AI-with-cpp.html?utm_source=chatgpt.com "Yes, You Can Do AI with C++!"
[4]: https://www.geeksforgeeks.org/cpp/companies-that-use-cpp/?utm_source=chatgpt.com "Companies That Use C++"
[5]: https://www.reddit.com/r/programming/comments/1noqut1/the_top_programming_languages_2025/?utm_source=chatgpt.com "The Top Programming Languages 2025 : r/programming"
[6]: https://www.geeksforgeeks.org/machine-learning/c-libraries-for-machine-learning/?utm_source=chatgpt.com "C++ Libraries for Machine Learning"
[7]: https://isocpp.org/ "
            Standard C++
    "
