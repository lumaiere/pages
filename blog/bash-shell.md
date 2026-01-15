# Episode 12: Bash and Shell - The Language Youve Been Using While Pretending You Were Not

If programming languages were people at a party, Bash would not be the loud one giving a TED Talk in the kitchen.

Bash is the one quietly refilling the ice, fixing the broken speaker cable, and somehow getting everyone home safely - while the rest of us are still arguing about tabs vs spaces like it is an international incident.

And the wild part?

You have probably used Bash (or at least shell commands) more times this week than half the languages on your resume.

If you are continuing this series from Episode 11, here is the previous stop: **[Episode 11: HTML and CSS](https://medium.com/@DaveLumAI/episode-11-html-and-css-the-two-roommates-who-built-the-internet-and-still-argue-about-where-b81a5482a2e5)**

---

## What it is

At a basic level, a shell is a command interpreter. You type commands. It runs commands. You feel powerful for five minutes.

Then you accidentally delete the wrong folder and suddenly you are Googling how to reverse time.

Bash is a specific shell: the Bourne Again SHell. It became the default on a lot of Linux systems for a long time, and it is still absolutely everywhere in servers, CI pipelines, Docker builds, and the darker corners of production where nobody has touched the scripts since 2017.

The official home base is here: **[GNU Bash](https://www.gnu.org/software/bash/)**

---

## Is it still relevant

Yes. Aggressively yes.

According to the **[Stack Overflow Developer Survey 2025](https://survey.stackoverflow.co/2025/technology)**, Bash/Shell shows up as one of the most commonly used languages (48.7% of respondents). That is not niche. That is not a phase. That is a lifestyle.

Bash is relevant for one simple reason:

Every time two tools need to talk to each other, a shell script appears like a raccoon in a dumpster behind a restaurant.

You did not invite it.

But there it is.

And it works.

---

## What it is used for

Bash is the duct tape of automation, but let us be more respectful than that.

Bash is used for:

* Running repeatable tasks (build, test, deploy, backup, migrate, rotate logs)
* Gluing together command line tools (pipes, redirects, filters, one-liners that look like wizard curses)
* Writing CI steps (the part of your pipeline you fear touching because it is held together by bravery)
* Server administration (where the reward for success is more servers)
* Dev tooling (project scripts, bootstrap installers, environment setup, etc.)

---

## Pros and cons

### Pros

* Installed basically everywhere you care about
* Perfect for orchestrating other tools
* Fast to write for small automation tasks
* Great for text processing and filesystem operations
* Plays nicely with the Unix philosophy: do one thing well, then chain it

### Cons

* Error handling is optional, and Bash will happily accept that invitation
* Quoting rules feel like they were designed by someone who hates joy
* Portability gets messy fast (Bash vs sh vs different OS behaviors)
* Large scripts become fragile spaghetti unless you are disciplined
* Debugging can be painful unless you build guardrails

---

## Strengths and weaknesses

Bash is strongest when it is small, sharp, and focused.

Bash is weakest when it starts cosplaying as a full application.

If your script begins with, "This will only take a minute" and ends with, "I should add classes," you have crossed the line. Back away slowly.

A helpful mental model:

* Bash is a great conductor
* Bash is a terrible orchestra

---

## A quick history bite

Bash first appeared in 1989 as part of the GNU Project and was originally written by Brian Fox, with long-term maintenance by Chet Ramey.

That means Bash has been quietly running modern computing longer than many of us have been pretending we were going to learn Vim properly.

---

## How popular is it, and is it going up or down

It is popular because it is unavoidable.

Is it trending upward like the newest framework of the week?

No.

Is it trending downward like something becoming obsolete?

Also no.

Bash is not trendy. Bash is infrastructure. The same way plumbing is not trending, but you will absolutely notice if it stops working.

---

## Is it similar to anything else

Yes: the POSIX shell world.

There is "shell" as a general category, there is POSIX sh (the standard baseline), and then there are shells with extra features and personality.

If you care about portability, it helps to know what is considered standard behavior. A good reference point for the POSIX side of the universe is the spec hub here: **[The Open Group Base Specifications](https://pubs.opengroup.org/onlinepubs/9799919799/)**

---

## Does it work well with AI

Yes, with a seatbelt.

AI can help you scaffold scripts quickly, explain cryptic one-liners, and generate starter automation.

But shell scripting has sharp edges, and AI has a talent for confidently handing you a sword by the blade.

If you use AI for Bash, do these two things:

1. Keep scripts small and readable.

2. Run a static checker on anything you did not personally type with mild suspicion.

The best tool for that is: **[ShellCheck](https://www.shellcheck.net/)**

---

## What tech stack does it work with

All of them.

Bash does not care if you are running Node, Python, Go, Java, Rust, containers, VMs, or a Raspberry Pi taped under your desk.

If it can run a command, Bash will orchestrate it.

This is why Bash keeps showing up in build pipelines like it pays rent.

---

## Tools that make Bash less terrifying

* Want the "man pages, but useful"? Try: **[tldr pages](https://tldr.sh/)**
* Want the official deep reference? Here is the: **[Bash Reference Manual](https://www.gnu.org/s/bash/manual/bash.html)**

And yes, [explainshell](https://explainshell.com/) exists. It is exactly what it sounds like, and it is exactly why the internet is occasionally wonderful.

---

## Cost

Bash itself is free.

The real cost is:

* The first time you forget quotes and your script breaks on a filename with spaces
* The first time you assume a command exists on every machine (it does not)
* The first time you ship a script that "works on my laptop" but not in CI

So the cost is not money.

The cost is pride.

---

## Example: a practical script that does not try to be a novel

This is a tiny log cleanup script with some basic safety habits:

```bash
#!/usr/bin/env bash
set -euo pipefail

LOG_DIR="${1:-/var/log/myapp}"
DAYS="${2:-14}"

if [[ ! -d "$LOG_DIR" ]]; then
  echo "Log directory not found: $LOG_DIR" >&2
  exit 1
fi

echo "Cleaning logs in: $LOG_DIR (older than $DAYS days)"

find "$LOG_DIR" -type f -name "*.log" -mtime +"$DAYS" -print -delete

echo "Done."
```

Small. Clear. Works. Does not require a committee meeting.

---

## Is it the subject of any famous art

Not directly, unless you count the abstract emotional journey of watching a deployment script fail at 2:00 AM.

But if you want to get poetic: shells show up in art constantly.

Bash, however, shows up in the credits.

---

## One last thing

If this episode made you laugh, wince, or whisper "yeah thats me" at your screen, do me a favor:

Follow me, and drop a comment with your most cursed Bash one-liner.

Bonus points if it worked once and you have no idea why.

---

## [Art Prompt (De Stijl):](https://lumaiere.com/?gallery=de-stijl)

A crisp, geometric abstract composition built from a clean white field structured by thick black horizontal and vertical lines, forming an asymmetrical grid of rectangles and squares. A few select blocks are filled with flat, saturated primary colors - a vivid red rectangle that anchors the visual weight, a bright yellow panel that adds lift, and a deep blue block that cools the balance. The rest remains white, creating spacious negative areas that feel intentional and calm. The edges are razor-sharp, the paint appears smooth and matte, and the overall mood is quietly confident, orderly, and modern. High resolution, museum-quality lighting, perfectly flat planes, no texture, no gradients, minimalist precision.

## [Video Prompt:](https://www.tiktok.com/@davelumai/video/7595054105312136479)

Start with a bold snap-in of black lines drawing themselves onto a bright white background, forming an asymmetrical grid in quick, satisfying strokes. As each rectangle locks into place, blocks of primary color pop into existence with rhythmic pulses - vivid red expands smoothly from the center of its shape, bright yellow flashes on with a soft glow, and deep blue slides in like a clean magnetic plate. Add subtle camera micro-movements that feel like a steady handheld gimbal adjusting for perfect alignment, plus gentle parallax between the line layer and the color blocks to create depth without breaking the flat graphic style. Use crisp, modern motion-graphics timing: quick builds, short holds, then playful rearrangements where a few rectangles shift position and re-lock with clean click-like transitions. Finish on a perfectly balanced final arrangement with a brief, satisfying color pulse and a clean freeze-frame.

Songs to match the vibe:

* The Less I Know the Better - Tame Impala
* K. - Cigarettes After Sex
