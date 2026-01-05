# Episode 9: Perl, the Language That Refuses to Die (And Honestly, Good for It)

Happy New Year 2026.

May your builds be green, your deployments be boring, and your password manager stop asking if you want to "save this one too" like it is collecting them for a scrapbook.

Now, let’s talk about Perl.

Perl is that legendary coworker who has been at the company since before the company existed. You do not remember hiring it. You do not remember onboarding it. But every time something breaks at 2:00 AM, Perl is already in the logs, holding a flashlight, muttering: "I can fix this in one line."

And it can. Which is both inspiring and deeply unsettling.

## What is Perl

Perl is a high-level, general-purpose programming language originally built for text processing, report generation, and the kind of data wrangling that makes other languages stare into the middle distance and whisper, "Nope."

Its unofficial superpower is doing ridiculously practical work with minimal ceremony. Regular expressions, file munging, log slicing, automation, and gluing systems together like a raccoon with a hot glue gun.

The official home base is [https://www.perl.org/](https://www.perl.org/) if you want the straight story without my emotional commentary.

## Is Perl still relevant

Yes.

Not because it is trendy, but because it is useful, and useful things tend to survive. Perl still shows up in system administration scripts, legacy enterprise workflows, bioinformatics pipelines, network tooling, and anywhere there is a suspicious amount of text that needs to become slightly less suspicious.

Also, there is an entire galaxy of reusable modules, and that galaxy is not small. If you want proof that Perl people have been quietly shipping solutions for decades, browse MetaCPAN at [https://metacpan.org/](https://metacpan.org/)

Perl is not the loudest language in the room anymore. But it is absolutely still in the room, and it knows where the bodies are buried (and also where the log files are).

## Who invented it

Larry Wall created Perl, and the world has been both blessed and confused ever since.

Perl’s origin story is basically: "I needed to process text, and existing tools were annoying, so I made a new tool that can do everything."

That is either heroic or chaotic, depending on whether you are reading the code.

## Pros and cons (a.k.a. the deal you make with the Perl gods)

### Pros

* Text handling is excellent. Regex feels like a native language, not a temporary visa.
* You can get from idea to working script very fast.
* Huge ecosystem of modules and battle-tested utilities.
* Fantastic for automation and glue work.

### Cons

* Readability varies wildly. Perl can be crystal clear, or it can be an ancient rune carved into a server rack.
* Perl style is a real thing. If you ignore it, your future self will file a formal complaint.
* Hiring and community momentum are smaller compared to newer favorites.

## Strengths and weaknesses

Perl’s strength is pragmatic power: it is very good at taking messy real-world stuff and producing useful output.

Perl’s weakness is that it gives you many ways to do the same thing, which is great until you inherit someone else’s "creative" solution and realize they wrote it during a thunderstorm while fighting a printer.

## What is it used for

Common Perl use cases include:

* Log analysis and text processing
* Automation scripts for ops and DevOps
* ETL style data cleanup
* Legacy CGI and web systems (yes, they still exist, and yes, they still pay bills)
* Bioinformatics and scientific scripting
* Network tooling and quick utilities

If you want to explore built-in functions without opening five tabs and losing your will to live, the documentation for built-ins is at [https://perldoc.perl.org/perlfunc](https://perldoc.perl.org/perlfunc)

## How popular is it and is it going up or down

If you are measuring popularity like it is a social media contest, Perl is not winning the dance battle right now.

But popularity is not the same as presence.

Perl has shifted from "everyone is learning it" to "the people using it are using it on purpose." That is a quieter kind of success, like a tool that does not need branding because it is too busy working.

Also, when you look at modern language lists like the Stack Overflow survey, you can see how the crowd moves year to year: [https://survey.stackoverflow.co/2025/technology](https://survey.stackoverflow.co/2025/technology)

## Can you give me an example

Here is a tiny Perl example that reads a file and counts how many lines match a pattern. Simple. Practical. Slightly smug.

```perl
use strict;
use warnings;

my $pattern = shift @ARGV or die "Usage: perl count.pl PATTERN FILE\n";
my $file    = shift @ARGV or die "Usage: perl count.pl PATTERN FILE\n";

open my $fh, "<", $file or die "Could not open '$file': $!\n";

my $count = 0;
while (my $line = <$fh>) {
    $count++ if $line =~ /$pattern/;
}

close $fh;

print "Matches: $count\n";
```

That script is the Perl personality in one bite: direct, effective, and absolutely willing to shout at you if you do not provide arguments.

## Alternatives

Depending on what you are doing:

* Python for general scripting and data work
* Bash for quick shell glue
* Ruby for scripting with a different flavor
* Go for compiled tools you want to ship as a single binary
* JavaScript/Node for scripts that live near web stacks

Perl’s main differentiator is still text power plus decades of modules plus "I will finish this task before your linter boots."

## Does it work well with AI

Yes, in a very modern way and a very old-school way.

Modern: you can absolutely use AI tools to generate boilerplate, refactor scripts, and explain mysterious regex spells you wrote in 2014.

Old-school: Perl is great at preprocessing data for AI pipelines, cleaning text, chunking logs, and building little automation pieces that feed bigger systems.

## What tech stack does it work with

Perl is a friendly neighbor. It lives well with Linux, cron, Docker, CI pipelines, and anything that can run a command line tool. It also plays nicely around databases, filesystems, and network services.

If you want the classic module universe, CPAN is still the mothership: [https://www.cpan.org/modules/index.html](https://www.cpan.org/modules/index.html)

## What tools work best with it

* Any decent editor with Perl syntax highlighting
* Perltidy (because formatting is self-care)
* Perlcritic (because sometimes your code needs a therapist)
* A terminal, coffee, and just enough fear to respect production

## How much is it going to cost me

Perl itself is free.

The real cost is emotional: whether you write it clearly, or whether you create a puzzle box that only opens on leap years.

If you want the famous reference book that many people treat like the Perl bible (and also a desk weapon), here is the canonical one: [https://www.amazon.com/Programming-Perl-Tom-Christiansen/dp/1565921496](https://www.amazon.com/Programming-Perl-Tom-Christiansen/dp/1565921496)

## One last thing for 2026

New years are funny. We make big plans. We buy notebooks. We declare we will "finally organize our digital life."

Then January hits, and suddenly you are debugging something that looks like it was written by a raccoon with admin privileges.

So here is my wish for you in 2026:

May your code be readable, your logs be honest, and your automation be so solid you forget it exists.

And if you have Perl stories, I want them.

Did Perl save your day? Did Perl ruin your weekend? Did you inherit a Perl script that turned out to be a sentient being? Drop a comment and tell me what you are building this year.

Also, if you missed the last episode, here is [Episode 8: SQL, the Language Your Data Already Trusts (Plus a Happy 2026)](https://medium.com/@DaveLumAI/episode-8-sql-the-language-your-data-already-trusts-plus-a-happy-2026-425b3c96b7f6).

---

**[Art Prompt (Mannerism):](https://lumaiere.com/?gallery=mannerism)**

A highly stylized, courtly portrait with elegant, elongated proportions and refined, slightly unreal grace. The subject is a regal figure posed front-facing against a dark, velvety backdrop, but the face and hair are composed entirely of meticulously arranged fruits, flowers, leaves, and ripening grains. Each element is rendered with jewel-like precision: glossy grapes, pale figs with translucent flesh, curling citrus peel, delicate blossoms, and crisp vegetables woven into an ornate, symmetrical design. Dramatic, controlled lighting sculpts the forms with subtle highlights and deep shadows, emphasizing texture and botanical detail. The mood is playful but aristocratic, with an uncanny, museum-worthy finish, rich color saturation, and a polished, late-renaissance elegance.

**[Video Prompt:](https://www.tiktok.com/@davelumai/video/7591476066225573150)**

Start with a snappy, rhythmic reveal: floating fruits, blossoms, and leaves assemble themselves mid-air like magnetic puzzle pieces, clicking into place to form a regal portrait. Use quick, elegant motion beats: grapes roll into an eye socket, citrus peel spirals into a curled mustache, petals flutter into a collar, and wheat sheaves fan outward into a crown. Add subtle depth-of-field shifts and crisp rack-focus changes to spotlight different textures, then punctuate transitions with clean whip-zooms and kaleidoscopic mirroring for a moment of surreal flair. Lighting should remain dramatic and sculptural, with highlights gliding across glossy fruit skins. Finish with the completed portrait giving a faint, uncanny blink as a few petals drift down like confetti, then snap to a bold final frame.

**Songs to pair with the video:**
- Digital Witness – St. Vincent
- Let It Happen – Tame Impala

