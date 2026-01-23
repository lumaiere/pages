# Episode 17: Rust - The Language That Treats Your Memory Like A VIP Guest

[Rust](https://medium.com/block-magnates/web3-languages-episode-4-rust-the-borrow-checker-with-biceps-a82465b3d6e4) is what happens when a programming language looks at your typical app crash and says, "No. Absolutely not. Not on my watch."

If [C](https://medium.com/@DaveLumAI/c-the-low-level-legend-that-refuses-to-retire-a85d268cdc5b) and [C++](https://medium.com/@DaveLumAI/c-the-overachieving-middle-child-of-programming-languages-940eb75291f4) are the high-powered motorcycles of the programming world (fast, thrilling, occasionally trying to throw you into a ditch), Rust is the same machine with a helmet, airbags, a defensive driving course, and a stern friend in the passenger seat whispering, "Do you really need to dereference that?"

Rust is a systems programming language built for performance, reliability, and safety. And yes, it wants you to be happy. It just also wants your code to stop doing crimes.

---

## What is it?

Rust is a compiled language designed for low-level control without the usual low-level regret.

Its greatest party trick is **memory safety without a garbage collector**. That means:

* You get speed that feels like C/C++ territory
* You get guardrails that stop a whole category of bugs
* You also get a compiler that reads your code like a disappointed professor with three degrees and unlimited time

If you want the official front door, here it is: **[rust-lang.org](https://rust-lang.org/)**

---

## Is it still relevant?

Very.

Rust has moved past "cool niche language" and into "this is showing up in serious places" territory. It's firmly in the modern working set of languages developers actually use and want to use, including in the **[Stack Overflow Top Languages list](https://survey.stackoverflow.co/2025/technology?utm_source=substack&utm_medium=email#1-programming-scripting-and-markup-languages)**.

Rust is not a fad. It is a lifestyle choice. Like meal prepping.

---

## Why people love it (Pros)

**Pros:**

* **Memory safety baked in** (fewer segfaults, fewer midnight incident calls)
* **Fast** and close to the metal
* **Fearless concurrency** (it tries very hard to stop you from creating a thread-powered disaster)
* **Cargo** is one of the nicest build + dependency tools out there, and it makes other ecosystems look like they still fax packages to each other
* **Tooling is excellent** (formatter, linter, analyzer, docs)

---

## Why people sometimes scream into a pillow (Cons)

**Cons:**

* The learning curve is real. The borrow checker is not "mean" - it is "honest."
* You will spend time negotiating with the compiler like youre in couples therapy
* Compile times can get spicy as projects grow
* Some patterns that feel casual in other languages require more explicit thinking in Rust

Rust isn't hard because it's trying to hurt you.

Rust is hard because it refuses to let you ship bugs with confidence.

---

## Strengths and weaknesses

**Strengths:**

* High performance + strong correctness guarantees
* Great for building robust libraries and critical infrastructure
* Excellent for long-lived codebases where "future you" should not be punished

**Weaknesses:**

* Steeper onboarding for teams used to garbage collection
* Some domains require picking the right crates and patterns early (you can do anything, but you must choose wisely)
* You may not want Rust for quick throwaway scripts unless you enjoy bringing a full tool belt to butter toast

---

## What is it used for?

Rust shows up when you want speed, safety, and control:

* Backend services where performance and reliability matter
* Systems programming, networking, embedded, CLI tools
* Game engines and performance-heavy tooling
* Security-sensitive components
* WebAssembly projects

If you're looking for a friendly starting path, **[The Rust Programming Language book](https://doc.rust-lang.org/book/)** is the classic.

If you want bite-sized experiments, **[Rust Playground](https://play.rust-lang.org/)** is where you go to test ideas without installing anything.

And when you do want to install: **[rustup](https://rustup.rs/)**

---

## Who invented it?

Rust started as a personal project by Graydon Hoare and grew into a full ecosystem with a large community and long-term stewardship. Today it is maintained by the Rust project community, and the larger ecosystem is supported by the **[Rust Foundation](https://rustfoundation.org/)**.

---

## How popular is it, and is it going up or down?

Rust has been steadily climbing from "cult favorite" to "mainstream tool you actually see at work."

A bunch of developers try Rust, then do the thing that surprises everyone: they actually want to keep using it.

That is rare in tech.

---

## When was it most popular?

Rust has had multiple waves, but the last several years have been a long sustained climb as companies keep adopting it for performance and security reasons.

It didn't peak and vanish.

It just kept showing up, getting better, and quietly taking jobs that used to belong to C++.

---

## What are the alternatives?

It depends on what you want:

* Want low-level control and maximum maturity? C and C++
* Want modern systems language vibes with a different flavor? Zig
* Want high performance with GC and simpler ergonomics? Go
* Want safety and runtime productivity? Java, C#, Kotlin

Rust is the one that says: "Sure, you can have speed. But you also have to be responsible."

---

## Is it similar to anything else?

Rust feels like a mashup of ideas:

* C/C++ performance goals
* Functional-style patterns (enums, pattern matching, iterators)
* Type system muscle
* A compiler that acts like a very strict but genuinely helpful coach

---

## Does it work well with AI?

Honestly, yes - with a catch.

AI tools can help you draft code quickly, but Rust is where vague code goes to get interrogated.

The upside: the compiler forces clarity. The borrow checker catches entire categories of mistakes that AI-generated code might accidentally introduce.

The downside: your AI assistant might feel personally attacked by the compiler.

This is normal. Offer it snacks.

---

## What tech stack does it work with?

Rust plays nicely with a lot:

* Backend services and APIs
* Docker and Kubernetes deployments
* WebAssembly workflows
* Data pipelines and high-performance tooling

Rust also integrates with existing code through FFI, meaning it can coexist with C/C++ in the same universe without summoning a portal demon.

---

## What tools work best with it?

* Cargo for building, dependencies, and running
* rustfmt for formatting
* Clippy for linting
* rust-analyzer for IDE superpowers

Also: docs in Rust are absurdly good. You will actually read them. By choice.

---

## How much is it going to cost me?

Money: basically nothing. Rust is free.

Cost in time: you will pay an upfront learning tax, and then you will earn it back because your software stops waking you up at 3 AM.

This is the rare language where "strict" pays you back.

---

## Can you give me an example?

Here is a small example that shows a very Rust-y pattern: ownership-aware string building, plus clean iteration.

```rust
fn main() {
    let names = vec!["Ada", "Linus", "Grace", "Margaret"];

    let shout = names
        .iter()
        .map(|n| format!("HELLO, {}!", n.to_uppercase()))
        .collect::<Vec<_>>()
        .join(" ");

    println!("{}", shout);
}
```

Simple, readable, and no one can accidentally free the string early and summon chaos.

Rust will not allow it.

Rust will stand in the doorway like a bouncer and say, "Not tonight."

---

## Is Rust the subject of any famous art?

Not in the "museum label says Rust" sense.

But oxidation is basically natures collaboration with metal, so any sculpture that ages, any shipwreck photograph, any industrial cityscape painting with time baked into it - thats Rust-adjacent energy.

Rust is the aesthetic of "time happened here."

Which is also how production bugs feel, so its kind of perfect.

---

## One last thing

If youve been curious about Rust, dont wait until you need it. Try it when youre calm, caffeinated, and not on call.

Then when the day comes that you need speed plus safety, youll already have the skills - and your future self will high-five you so hard it triggers a compiler warning.

---

## [Art Prompt (Bauhaus):](https://lumaiere.com/?gallery=bauhaus)

A crisp Bauhaus-inspired abstract composition with disciplined geometry and playful balance: a field of warm off-white with clean, precise lines forming interlocking rectangles, circles, and arcs. A bold primary palette of red, yellow, and blue is tempered by charcoal black and soft gray, arranged in a dynamic but orderly grid. The forms feel engineered yet lyrical, like a blueprint for a modern dream. Edges are razor-sharp, surfaces matte and flat, with a subtle sense of rhythm created by repeated shapes and carefully spaced negative areas. The mood is optimistic, efficient, and quietly joyful, like design that believes the future will be tidy.

---

## [Video Prompt:](https://www.tiktok.com/@davelumai/video/7598006391432858910)

Animate the Bauhaus composition as a lively, modern motion-graphic loop. Geometric shapes slide into place with crisp, satisfying snaps, then gently counter-shift as if responding to invisible beats. Circles rotate a quarter-turn, rectangles glide along clean paths, and thin lines draw themselves on-screen like a drafting pen in motion. Add quick, punchy transitions between balanced layouts, with occasional playful rebounds that feel precise rather than bouncy. Keep movement clean and intentional, with a seamless looping ending where the final arrangement re-assembles into the opening frame.

---

## Suggested songs:

* "Genesis" - Justice
* "Sea of Voices" - Porter Robinson

---

**Follow me** for more episodes in the language series, more creative chaos, and more code that behaves.

**Comment below**: Have you tried Rust yet, or are you still emotionally recovering from C++ templates?

