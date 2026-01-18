# Episode 15: PHP, the Language That Paid Your Bills While Everyone Made Fun of It

PHP is that friend who shows up to help you move, brings a truck, actually lifts the couch, and then gets roasted in the group chat for wearing cargo shorts.

And yet somehow, the couch gets moved. Every time.

If you are continuing this series from the **[Stack Overflow Top languages](https://survey.stackoverflow.co/2025/technology?utm_source=substack&utm_medium=email#1-programming-scripting-and-markup-languages)** list, PHP is the one that quietly waves from the back like, “Yeah, I am still here. Yes, I still run your stuff. No, I do not need applause. But I will accept it.”

So let’s talk about PHP: what it is, why it refuses to die, and why (plot twist) that is actually a compliment.

## What is it?

PHP is a server-side scripting language designed for web development.

Translated into human terms: it is the thing that sits behind a website and turns requests into pages, logins, shopping carts, dashboards, and that one admin panel nobody wants to touch because it was built in 2011 and still has a “Coming Soon” banner.

PHP runs on the server, generates HTML (and JSON, and whatever else you need), talks to databases, and generally does the unglamorous but extremely profitable job of making websites function.

It is also the language that gave us a whole era of “view source and learn” web development. For better and for “oh no.”

## Is it still relevant?

Yes. Loud yes.

Not “relevant like a trend” relevant. Relevant like electricity. You do not throw a party for your breaker panel, but you definitely notice when it stops working.

PHP is still heavily used because:

* Legacy codebases exist, and they are not going anywhere without a budget and a team.
* Modern PHP got dramatically better.
* The web is not one app. It is a billion apps, and most of them want something boring and reliable.

Also: **[WordPress](https://wordpress.org/)** is powered by PHP. And WordPress powers a very large chunk of the web. If PHP disappeared tomorrow, the internet would make a sound like a thousand marketing teams screaming in unison.

## Quick history: how did we get here?

PHP started in 1994 as a set of CGI scripts created by Rasmus Lerdorf. It was originally called “Personal Home Page” tools, which sounds like something you would download from a floppy disk right before your computer caught a cold.

Then it evolved into a full language, got renamed to the famously recursive “PHP: Hypertext Preprocessor,” and became the default engine of early dynamic websites.

For a while, PHP had a reputation for being easy to start and easy to… accidentally create an international incident with.

But modern PHP is not the same beast. The language matured. The ecosystem matured. And developers discovered a secret: if you write PHP like a professional adult, it behaves like a professional adult.

## How popular is it? Going up or down?

It is not the shiny new star at the prom, but it is still in the yearbook.

On the popularity chart, PHP has generally trended downward compared to its peak dominance years, mostly because the industry exploded into many more choices.

But “down” is not the same as “gone.”

It is more like: PHP went from being the only restaurant in town to being one of the busiest restaurants in a city full of options. Still packed. Still serving food. Still paying rent.

## When was it most popular?

PHP’s cultural peak was the 2000s into the early-to-mid 2010s, when dynamic websites were the main event and the tech world had not yet invented seventeen thousand JavaScript frameworks.

Back then, if you built for the web, you probably touched PHP at some point. Sometimes willingly. Sometimes like you touched a hot pan.

## Pros and cons (the honest version)

**Pros**

* Cheap to run, easy to deploy, runs basically everywhere.
* Massive ecosystem and community.
* Great for web apps, APIs, and content-driven sites.
* Modern tooling is strong and improving fast.
* Mature frameworks make serious apps straightforward.

**Cons**

* Legacy PHP is still out there, haunting servers like a polite ghost with terrible code style.
* Inconsistent historical quirks mean you occasionally mutter “why is it like this” at your monitor.
* The ease of entry means you will meet code written by someone who learned PHP yesterday at 2 AM.

So yes: PHP lets beginners build quickly, and that is a gift. It also means you will eventually inherit a codebase that looks like it was assembled by raccoons with keyboard access.

## Strengths and weaknesses

**Strengths**

* Web-first DNA. It is built for request/response life.
* Excellent server-side rendering, APIs, and traditional web workflows.
* Strong modern type features (still not perfect, but way better than the old days).
* Fantastic frameworks and libraries.

**Weaknesses**

* Some developers refuse to update their mental model, and then blame the language for their time travel.
* The ecosystem is wide, and quality varies. You need standards and linting, or chaos will volunteer itself.

## What is PHP used for?

* Websites (small, medium, gigantic)
* APIs
* CMS platforms
* E-commerce stores
* Internal tools and admin panels
* Anything that needs to talk to a database and return something useful

Basically: the internet’s back office.

## Who uses it the most?

PHP is everywhere, but a few gravitational centers matter:

* Sites and businesses built on **[WordPress](https://wordpress.org/)**
* Web apps built with **[Laravel](https://laravel.com/)**
* Projects using the broader PHP ecosystem powered by **[Composer](https://getcomposer.org/)**

And yes, serious companies run serious PHP in production. They just do not brag about it at parties because nobody wants to be the person yelling “OUR MONOLITH IS STABLE” over the music.

## Alternatives (and when you might choose them)

* JavaScript/TypeScript on the server (Node) if you want one language everywhere and your team lives in npm.
* Python if you are doing lots of data work or AI-adjacent tooling and want that ecosystem.
* Ruby if you love conventions and want the “cozy framework” vibe.
* Java, C#, Go, Rust if you are building large-scale services with different performance and concurrency goals.

But PHP’s advantage is simple: it is incredibly practical for building web apps quickly and running them cheaply.

## Does it work well with AI?

Yes, especially in the “AI is a service I call” sense.

Most real-world AI integration is:

* call an API
* send text
* receive text
* store result
* show it to users
* add guardrails because users are users

PHP is perfectly suited for that. You can wire in AI features in a web app without rewriting your stack.

If you want a starting point for learning the modern language itself, **[php.net](https://www.php.net/)** is the official home base, and the **[PHP manual](https://www.php.net/manual/en/)** is still one of the best docs on the internet.

## What tech stack does it work with?

PHP plays nicely with:

* MySQL/MariaDB/PostgreSQL
* Redis
* Nginx/Apache
* Docker
* Linux, macOS, Windows (yes, Windows, calm down)
* Most cloud providers, shared hosting, and that one mystery VPS you inherited

It is the language equivalent of “I can make this work” energy.

## Tools that work best with it

If you want PHP to feel modern and clean, use modern tools:

* Composer for dependencies: **[Composer](https://getcomposer.org/)**
* A real framework when appropriate: **[Laravel](https://laravel.com/)**
* A debugger like Xdebug
* Static analysis (PHPStan/Psalm)
* Automated formatting and code standards
* Tests (PHPUnit or Pest)

In other words: treat it like a real language, and it behaves like one.

## How much is it going to cost you?

The language itself is free.

Hosting can be extremely cheap, especially compared to stacks that require more moving parts. You can run a PHP site on budget hosting, or you can run it at scale with all the modern infrastructure bells and whistles.

The real “cost” is maintenance discipline: keep versions updated, use tooling, and avoid building a museum exhibit.

## A quick example (because we are not here to only vibe)

Here is a tiny PHP script that returns JSON like a polite little API:

```php
<?php
declare(strict_types=1);

header('Content-Type: application/json');

$response = [
    'message' => 'Hello from PHP',
    'timestamp' => gmdate('c'),
    'randomNumber' => random_int(1, 100),
];

echo json_encode($response, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
```

That is it. No drama. No ritual. Just a server doing its job.

## Is it the subject of any famous art?

Not in the museum sense, but PHP does have an unofficial mascot: the elephant.

Which feels right.

PHP is basically the elephant of web development: not flashy, not trying to be trendy, but strong, memorable, and somehow still holding the whole parade together while everyone else argues about fonts.

## One last interesting tidbit

PHP is one of the best examples of a technology that survived its own reputation.

It got clowned for years, improved anyway, and kept shipping value the entire time.

That is not a failure story.

That is a glow-up with receipts.

## [Art Prompt (Bauhaus):](https://lumaiere.com/?gallery=bauhaus)

A crisp, geometric abstract painting composed of nested squares centered on the canvas, each layer slightly offset to create a subtle push-pull tension. The palette is warm and restrained: sunbaked ochres, muted terracotta, creamy off-white, and a quiet charcoal that anchors the composition without overpowering it. Edges are razor clean, with perfectly flat planes of color and no visible brush texture. The surface feels matte and carefully measured, like design turned into meditation. The mood is calm, deliberate, and quietly radiant, inviting the viewer to linger on proportion, balance, and the gentle vibration between adjacent tones. High resolution, gallery lighting, minimal background distractions, precise alignment, modernist clarity.

## [Video Prompt:](https://www.tiktok.com/@davelumai/video/7596375063050325278)

Animate a centered composition of nested squares that subtly shift and breathe with rhythmic precision. The inner squares gently expand and contract like a heartbeat, while each color plane softly slides a few pixels in alternating directions, creating hypnotic parallax tension without breaking the clean geometry. Add crisp, timed “snap” moments where the layers align perfectly for an instant, then drift again. Introduce delicate lighting changes: a faint bloom of warmth across the terracotta, a brief deepening of charcoal, and a soft glow along the edges as if the shapes are emitting quiet energy. Use sharp cuts synced to the beat, with occasional quick zoom-ins that land on perfect symmetry before popping back out. Keep everything ultra-clean and modern, with mesmerizing motion that feels engineered, soothing, and addictive.

Songs to pair with the video:

- Halcyon Days – Lissom
Minimal, warm, quietly hypnotic. Subtle pulse, great for geometric motion.

- Still Life – Rival Consoles
Restrained, textural, and meditative with just enough movement to feel alive.

If you have ever built something in PHP (or inherited something in PHP and survived), tell me your best story in the comments.

And if you want the rest of this language series, hit follow so you do not miss the next episode.
