# Episode 24 (Bonus): Testing in Perl, or “Yes, We Still Ship With This Camel”

We made it.

Twenty-three episodes of [testing frameworks](https://medium.com/stackademic/the-state-of-testing-what-are-we-even-doing-here-1f0bce2fa0d4). Unit tests. Integration tests. E2E tests that flake so hard they deserve their own weather forecast. BDD tools that made us write “Given I have feelings” in a `.feature` file and pretend that was normal.

And now, the grand finale of this beloved series arrives like a mysterious legacy cron job you forgot existed:

**Testing in Perl. Thanks, Steven.**

Because nothing says “final boss” like a language that can parse a log file, summon a regex demon, and still have time to roast your code style.

If you’ve never tested Perl before, don’t worry. Perl testing is actually one of the most civilized corners of the ecosystem, mostly because Perl developers have lived through enough chaos to invent calmness on purpose.

## The Perl Testing Vibe

Perl’s testing culture is built around a simple idea: **your tests speak in TAP** (the Test Anything Protocol). That means your tests output a standardized stream of results like:

* ok 1
* ok 2
* not ok 3 (aka “something is deeply wrong and your coffee is now required”)

Then a runner reads that stream, summarizes it, and tells you whether you’re allowed to deploy or must remain in the shame cave.

The two names you’ll see constantly are:

* **[Test::More](https://metacpan.org/pod/Test%3A%3AMore)** for writing tests
* **[prove](https://perldoc.perl.org/prove)** for running them like you mean it

And if you want the newer, more modular universe (which is especially nice when you’re doing modern-ish Perl things in a modern-ish way), you’ll run into:

* **[Test2::V0](https://metacpan.org/pod/Test2%3A%3AV0)** for a big bundle of recommended tools
* **[Test2::Manual](https://metacpan.org/pod/Test2%3A%3AManual)** when you inevitably ask, “Wait, how does this actually work?”

## Why Perl Testing Still Matters

Because Perl is still out there doing real work.

It’s in build pipelines, text processing, bioinformatics, legacy enterprise code, and those “temporary scripts” that celebrated their 9th birthday last week.

And the punchline is: when Perl sticks around, the tests need to stick around too. Otherwise you end up in that classic situation where the script is mission-critical, nobody remembers how it works, and the only documentation is a comment that says:

`# do not touch`

That is not documentation. That is a curse.

## The Classic Starting Point: Test::More

Here’s the basic shape of a Perl test. This is the “hello world” of proving your code is not lying to you:

```perl
use strict;
use warnings;

use Test::More tests => 4;

sub add {
    my ($a, $b) = @_;
    return $a + $b;
}

is(add(2, 3), 5, "2 + 3 = 5");
is(add(0, 0), 0, "0 + 0 = 0");
is(add(-2, 3), 1, "-2 + 3 = 1");

ok(add(10, 1) == 11, "basic sanity still holds");
```

That `is(...)` assertion is the workhorse. It checks equality and gives you a message that will feel comforting when everything is green and extremely judgmental when it isn’t.

You save that in something like `t/add.t` and run it with:

```bash
prove -lv t
```

* `-l` adds `lib/` to your include path (because you like finding your modules)
* `-v` shows you the full output (because you like knowing what’s happening)

And yes, the command is literally named **prove**, because Perl is emotionally supportive like that. It’s not “run tests.” It’s “prove you’re right.”

## “But Is It Any Good?” (Pros and Cons, Perl Edition)

### Pros

* **Battle-tested culture.** Perl has been doing testing for ages, which means the ecosystem has strong conventions and tons of tooling.
* **TAP plays nicely with everything.** CI systems love predictable output. TAP is predictable. Until your code isn’t.
* **Fast feedback.** For script-heavy codebases, Perl tests can be quick and lightweight.

### Cons

* **Legacy variety.** You may inherit old patterns, old harnesses, and old assumptions that were valid in 2009 but now feel like an archaeological dig.
* **Readability is optional.** Perl gives you the freedom to write clear tests or write tests that look like wizard homework. Choose wisely.
* **Mocking can get spicy.** It’s doable, but depending on what you’re mocking, you may spend time arguing with global state like it owes you money.

## When You Should Use Test2

If you’re doing larger suites, modern workflows, concurrency, or you just want a more structured toolset, **[Test2::V0](https://metacpan.org/pod/Test2%3A%3AV0)** is a great on-ramp.

Think of it as: “I’d like my tests to be powerful, consistent, and less like a personal improv show.”

And if you’re curious how deep the rabbit hole goes, **[Test2::Manual](https://metacpan.org/pod/Test2%3A%3AManual)** is where the real nerd candy lives.

## The Real Secret Sauce: The Harness

People talk about assertions. They talk about fixtures. They talk about mocks.

But in Perl land, the quiet MVP is the harness.

The harness is what takes a pile of `.t` files and turns them into a result you can trust. That’s why **[prove](https://perldoc.perl.org/prove)** is such a big deal: it gives you a consistent way to run tests locally and in CI, and it doesn’t care whether your test is tiny or terrifying.

## Grand Finale Energy

This series has been a long, glorious march through every kind of testing personality:

* the minimalist
* the enterprise bureaucrat
* the browser automation wizard
* the BDD poet
* the “why is this snapshot 9,000 lines” realist

And ending on Perl feels perfect, because Perl is the living reminder that tools don’t die just because the internet stops talking about them. Real tools survive by being useful.

So yes, Steven: you were right to demand this episode. Consider this the official closing credits scene where the camel walks into the sunset, dragging a perfectly formatted TAP report behind it.

If you enjoyed this entire series, do me a favor: **follow me**, and **drop a comment** with your hottest testing take. Are you Team “test everything” or Team “ship it and apologize later”? Also, if you’ve ever inherited a Perl script that ran a company, I need that story.

If you want more writing like this, it lives at **[https://medium.com/@DaveLumAI](https://medium.com/@DaveLumAI)**, and if you want to grab something pretty for your wall (or your shirt, or your mug that judges your sprint velocity), you can browse **[prints and merch here](https://www.redbubble.com/people/DaveLumAI/explore?page=1&sortOrder=recent)** or explore the galleries at **[https://lumaiere.com/](https://lumaiere.com/)**.

---

[Art Prompt (Mannerism):](https://lumaiere.com/?gallery=mannerism) A luminous court portrait scene with elegantly elongated figures posed in a tall, narrow interior, their gestures refined and slightly theatrical. Skin tones are porcelain-pale with cool undertones, and fabrics shimmer with satin highlights in deep emerald, muted rose, pearl white, and inky black. The composition feels polished and slightly uncanny: long necks, delicate hands, and graceful proportions that stretch just beyond realism. Architectural details are crisp and ornate but restrained, with marble columns and a distant niche holding a pale sculpture. Lighting is cool and directional, creating smooth gradients on faces and glossy folds on garments. Mood: aristocratic calm with a faint sense of surreal elegance, as if the air itself is holding its breath.

[Video Prompt:](https://www.tiktok.com/@davelumai/video/7613231929504124190) Start with a slow vertical camera glide from the hem of shimmering satin up to an elongated hand resting lightly on a carved chair. Add subtle motion to the fabrics so they ripple like a soft indoor breeze, with specular highlights traveling across folds. Introduce gentle parallax between the foreground figure, the marble columns, and the distant niche, making the space feel tall and dreamlike. Use slow, elegant micro-zooms on jewelry details and soft rack-focus shifts between faces and hands. Halfway through, let the lighting “breathe” slightly brighter, then return to cool stillness. End on a lingering close-up of a calm face as the background softens into painterly blur.

Two songs to pair with the video:

* I Follow Rivers – Lykke Li
* Tiny Moves – Bleachers

Follow, comment, and tell me what series you want next. And if you’re Steven, congratulations: you got Perl on the main stage.
