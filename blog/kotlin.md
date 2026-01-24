# Episode 18: Kotlin, the Language That Politely Fixes Java Without Starting a Family Argument

Some languages show up to the party wearing a leather jacket and yelling, "We are rewriting everything from scratch!"

Kotlin walks in, smiles, and quietly rearranges the furniture so nobody trips, then asks Java if it would like a cup of tea.

If you have ever thought, "I like the JVM ecosystem, but I do not enjoy writing a novel every time I declare a variable," Kotlin is basically your emotional support language. It keeps the stuff you already paid for (libraries, tooling, battle-tested platforms) and removes a lot of the daily paper cuts. Not by being loud. By being practical.

And yes, it is still very relevant. Kotlin is not a "remember when we all tried that" language. It is a "why did we not do this earlier" language.

---

## What Kotlin is

Kotlin is a modern, statically typed programming language designed to run beautifully in the same world Java built: the JVM. It also targets other places (JavaScript and native platforms), but its superpower is how well it plays with existing Java code.

Kotlin is the friend who can join your group chat, read the entire history, and somehow not get weird about it.

If you want the official home base, it lives here: [https://kotlinlang.org/](https://kotlinlang.org/)

---

## A quick history lesson (with minimal suffering)

JetBrains announced Kotlin publicly in 2011, and the first stable 1.0 release landed in 2016. It was created because JetBrains wanted something more expressive than Java, without the "hope you enjoy waiting for your compiler" vibe that can come with some alternatives.

If you want the fun name trivia: Kotlin is named after Kotlin Island near St. Petersburg. Java has an island name too (long story, coffee got involved). Developers love themes.

---

## Is it still relevant?

Yes. Kotlin is still relevant in the way electricity is still relevant.

Google has been publicly Kotlin-first for Android for years, and their official guidance keeps pushing Kotlin as the recommended starting point for modern Android work: [https://developer.android.com/kotlin/first](https://developer.android.com/kotlin/first)

Also, Kotlin continues to show up strongly in developer surveys (and in real-world job postings), especially anywhere Android or JVM backends exist. The Stack Overflow Developer Survey tech page you referenced is right here: [https://survey.stackoverflow.co/2025/technology](https://survey.stackoverflow.co/2025/technology)

---

## Pros and cons (the honest menu)

### Pros

**Less boilerplate, more meaning**
Kotlin reduces the "ceremony tax." You write what you mean, not what the compiler wants as proof of life.

**Null safety (aka fewer surprise explosions)**
Kotlin makes you acknowledge nulls instead of pretending they do not exist until your app meets a real user.

**Interoperability with Java**
You can adopt Kotlin gradually. You do not have to burn the building down to remodel the kitchen.

**Coroutines for concurrency**
Kotlin gives you a clean way to write async code that still looks readable, and the official coroutine guide is genuinely helpful: [https://kotlinlang.org/docs/coroutines-guide.html](https://kotlinlang.org/docs/coroutines-guide.html)

**Tooling is excellent**
JetBrains built Kotlin and also builds the IDE most Kotlin devs use. That is like the car manufacturer also building the roads and somehow making it work.

### Cons

**Build complexity can creep in**
Multiplatform projects and big Gradle builds can turn into a small ecosystem of plugins, settings, and feelings.

**Learning curve for "Kotlin-isms"**
The basics are approachable, but writing idiomatic Kotlin (without accidentally creating a tiny abstract art museum of scope functions) takes practice.

**Interoperability is a double-edged sword**
You can mix Java and Kotlin, but you also inherit Java realities. Sometimes you are still negotiating with nulls from the Java side like a hostage negotiator with snacks.

---

## Strengths and weaknesses

Kotlin is strongest when you want:

* Android apps that feel modern without being painful
* JVM backends that stay readable as they grow
* Safer codebases where refactoring does not feel like defusing a bomb
* Teams who want productivity wins without platform drama

Kotlin is weaker when:

* You need the absolute simplest toolchain possible (hello, tiny scripts)
* You are in an environment where the JVM is a non-starter
* Your organization treats "new language" like it is a suspicious package

---

## What is it used for?

**Android development** is the obvious headline.

But Kotlin also thrives in:

* **Backend services** (especially JVM shops already using Spring, Ktor, etc.)
* **Shared mobile business logic** via Kotlin Multiplatform: [https://kotlinlang.org/multiplatform/](https://kotlinlang.org/multiplatform/)
* **Cross-platform apps** where you want to share code but keep native performance and native UI where needed
* **Tooling and internal platforms** (Kotlin is great for building developer tooling because it is expressive and refactor-friendly)

---

## How popular is it? Up or down?

Kotlin is popular in the places that matter most for Kotlin: Android and JVM-heavy companies.

Its popularity is not the kind of "everyone is learning it this weekend" spike. It is the steadier kind: teams adopting it, keeping it, and slowly converting their codebase because life got better. Kotlin has had swings in broad indexes (because those measure different things), but in Android and JVM ecosystems it remains a serious, long-term player.

---

## When was it most popular?

Kotlin adoption surged hard in the late 2010s into the early 2020s as Android development went Kotlin-first, and it has continued as the default modern option in that space. The more Compose and modern Android patterns become standard, the more Kotlin stays glued to the center of the conversation.

---

## Who invented it?

Kotlin was developed by JetBrains, with Andrey Breslav as the original lead designer. JetBrains also maintains the language and ecosystem in the open, including the Kotlin compiler and standard tooling.

If you like seeing the engine room, the main Kotlin repo is here: [https://github.com/JetBrains/kotlin](https://github.com/JetBrains/kotlin)

---

## What companies use it the most?

Any company building Android apps at scale is likely using Kotlin somewhere, even if they still have Java in the basement holding up the house.

Also, many JVM backend teams adopt Kotlin because it modernizes their developer experience while keeping their existing libraries and infrastructure.

Translation: Kotlin shows up wherever people say, "We like money, uptime, and fewer bugs."

---

## Is it similar to anything else?

Kotlin often gets compared to Java (obviously), but it also shares some DNA with modern languages that value expressiveness and safety.

The difference is Kotlin is not trying to replace your entire ecosystem. It is trying to upgrade your daily life.

---

## Does it work well with AI?

Yes, especially in practical ways:

* Kotlin is great for building **AI-powered applications** on Android (on-device features, UI, API clients, background work).
* Kotlin is solid for **server-side AI integrations** (calling LLM APIs, orchestrating workflows, handling streaming responses).
* Kotlin codebases are often **refactor-friendly**, which matters when AI tools generate drafts and you need to shape them safely.

Kotlin also benefits from the same AI dev tooling wave as other mainstream languages: code completion, refactor suggestions, test generation, and linting improvements land nicely in Kotlin-first IDEs.

---

## What tech stack does it work with?

Kotlin fits smoothly into:

* JVM stacks (Gradle, Maven, Spring ecosystems)
* Android stacks (Jetpack, Compose, coroutines, Flow)
* Multiplatform stacks (shared logic across iOS, Android, desktop, web)

If your infrastructure already speaks Java, Kotlin is basically bilingual.

---

## What tools work best with it?

* IntelliJ IDEA and Android Studio are the classic pairing for Kotlin development
* Gradle is the common build tool in Kotlin-heavy projects
* Kotlin Playground is a quick way to run and share snippets in a browser: [https://play.kotlinlang.org/](https://play.kotlinlang.org/)

---

## How much is it going to cost me?

Kotlin itself is free to use.

Your costs are the same kind you already have:

* Developer time
* CI minutes
* Optional paid IDE licenses if your team prefers premium tooling

The language will not invoice you. Your ambitions might.

---

## A Kotlin example (small, useful, and not cursed)

Here is a tiny example that shows Kotlin being Kotlin: data classes, null safety, and coroutines for async work.

```kotlin
import kotlinx.coroutines.*

data class User(val id: Int, val name: String?, val email: String?)

fun User.displayName(): String = name?.trim().takeUnless { it.isNullOrBlank() } ?: "Mysterious Person"

suspend fun fetchUser(id: Int): User {
    delay(150) // pretend network
    return User(id = id, name = "  Ada  ", email = null)
}

fun main() = runBlocking {
    val user = fetchUser(42)
    println("Hello, ${user.displayName()}!")

    val emailLength = user.email?.length ?: 0
    println("Email length: $emailLength")
}
```

Notice what is not here:

* Twelve getters
* A three-page builder
* A ritual circle of curly braces

---

## Alternatives (depending on what you are trying to do)

If you want a modern JVM language but different vibes:

* Java (modern Java is better than its reputation, but Kotlin is still usually less verbose)
* Scala (powerful, but can be heavier)
* Groovy (dynamic, often used for scripting and Gradle, different tradeoffs)

If you want cross-platform mobile, Kotlin Multiplatform competes with other approaches, but it stands out when you want shared logic while keeping native performance and native control.

---

## Is Kotlin the subject of famous art?

Not directly, unless you count the modern masterpiece titled "Screenshot of a build error at 2:13 AM."

But the name comes from an actual island, and that island has history, forts, and nautical drama. So in a roundabout way, Kotlin is at least adjacent to the kind of place painters would absolutely put stormy skies over.

---

## Final thoughts

Kotlin is what happens when someone looks at Java and says, "We can keep the ecosystem and still stop hurting people."

It is not trying to be flashy. It is trying to be the language you can live in for years without developing a thousand-yard stare.

If you are already in Android or JVM land, Kotlin is one of the best upgrades you can make without rewriting your identity.

If you are using Kotlin today, drop a comment with your favorite feature (and your least favorite Gradle moment). And if you are just Kotlin-curious, follow along for the next episode in the series.

---

**[Art Prompt (Bauhaus):](https://lumaiere.com/?gallery=bauhaus)**
A crisp, geometric abstract painting built from nested, perfectly aligned squares that seem to hover on a flat surface. The composition is centered and calm, with hard-edged boundaries and immaculate transitions between color planes. Use a restrained, harmonious palette of warm ochres, muted terracotta, soft teal, and smoky charcoal, arranged so that each square subtly changes temperature and depth without any visible texture. The mood is meditative and architectural, like a visual breathing exercise. Ultra-clean lines, matte paint, no gradients, no brush marks, museum lighting, high resolution, minimalist precision.

---

**[Video Prompt:](https://www.tiktok.com/@davelumai/video/7598385502403693855)**
Transform a centered composition of nested geometric squares into a hypnotic motion design loop. The squares gently expand and contract in rhythmic pulses, occasionally snapping into slightly offset alignments like a perfectly timed mechanical calibration. Colors softly swap positions between layers with quick, satisfying transitions, while the whole stack subtly tilts in perspective for a moment and then locks back into perfect symmetry. Add clean, minimal light sweeps that glide across edges, plus micro-vibrations on the borders for tactile energy. Include a few bold beat-synced moments where two layers rotate a few degrees in opposite directions, then click back into place. Keep it crisp, matte, and high-contrast with museum-like lighting, seamless looping, and visually addictive motion.

---

**Songs that pair well with that video vibe:**

* Cherry Blossom Girl – Air
* Angel – Massive Attack
