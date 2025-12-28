# Episode 7: Visual Basic, the Language That Refused to Leave the Office

Some languages kick down the door, overthrow the king, and declare a new era.

Visual Basic walked in politely, fixed the printer, automated your spreadsheet, shipped a working app by Friday, and then stayed in the building for 30 years because nobody ever found the keys to make it leave.

And yes, it is still in the Top 10.

According to the **[TIOBE Index](https://www.tiobe.com/tiobe-index/)** (December 2025), Visual Basic is sitting at **#7**, right there between the usual heavyweights like a guy in khakis who somehow keeps winning trivia night.

---

## What is Visual Basic, exactly?

Visual Basic is a Microsoft language family that’s basically two things wearing one name tag:

1. **Classic VB (VB6 and friends)**: The original rapid app development era, drag-and-drop UI, COM components, Windows desktop apps, and the vibe of a CRT monitor that hums like it’s thinking.

2. **Visual Basic on .NET (VB.NET)**: The modern version that runs on the .NET ecosystem, with real classes, generics, async, and enough structure to keep your future self from filing a restraining order against your past self.

If you want the official modern docs, they live here: **[Visual Basic documentation](https://learn.microsoft.com/en-us/dotnet/visual-basic/)**

---

## Is it still relevant?

Absolutely. Visual Basic survives for one simple reason:

**It’s attached to things that pay the bills.**

Visual Basic shows up in places like:

* Excel automation and Office macros (hello, VBA energy)
* Internal enterprise tools that no one wants to rewrite because they still work and rewriting them would cost three vacations and one marriage
* .NET shops that inherited VB projects and learned the ancient art of “not touching it unless it’s on fire”

Also, “disappearing” is hard when your language is basically stapled to the concept of “business logic someone wrote in 2004 and it still runs payroll.”

If you’re in the Office world, this is the official reference for that flavor: **[VBA language reference](https://learn.microsoft.com/en-us/office/vba/api/overview/language-reference)**

---

## Pros and cons (aka: the good news and the “oh right”)

### Pros

**Fast to build stuff**
Visual Basic was made for getting things done quickly. It’s got a long history of making UI apps feel approachable, especially for people who want results before they want philosophy.

**Readable**
VB is famously “English-ish.” You can hand it to someone and they can usually guess what’s happening, even if they’ve never written it before.

**Lives inside .NET**
Modern VB plugs into a massive ecosystem of libraries, tooling, and deployment options. It’s not stranded. It’s riding in the same bus as C#.

### Cons

**Reputation**
VB suffers from being too helpful. People see it and assume it’s a toy language that prints “Hello World” on a rainbow sticker.

Meanwhile it’s quietly running a factory.

**Smaller modern community**
If you’re hunting for tutorials, examples, or new open-source projects, VB is not where the trend-chasers hang out.

**Legacy confusion**
“Visual Basic” can mean classic VB, VB.NET, or “that macro that broke the quarterly report.” Context matters.

---

## Strengths and weaknesses

### Strengths

* Building business apps without drama
* Maintaining long-lived systems
* Integrating with Microsoft-heavy environments
* Letting teams ship tools without needing a ceremony and three architecture diagrams

### Weaknesses

* Not the default choice for greenfield projects in 2025
* Fewer modern-first libraries that show VB examples (they exist, but the internet tends to speak C#)
* Hiring can be weird, because “VB experience” sometimes means “I once edited a macro while panicking”

---

## What is it used for today?

The honest answer: **boring, valuable stuff.**

* Internal line-of-business apps
* Data entry tools that keep operations moving
* Reports, automation, data cleanup
* Glue code for old systems that still matter

It’s not glamorous, but neither is electricity. And you still want electricity.

---

## A quick example

Here’s a tiny VB.NET console example that shows the vibe: readable, direct, and mildly judgmental (like a helpful coworker).

```vbnet
Imports System

Module Program
    Sub Main()
        Dim name As String = "Visual Basic"
        Dim year As Integer = DateTime.Now.Year

        Console.WriteLine($"Hello from {name} in {year}.")
        Console.WriteLine("Yes, I'm still here. No, you cannot delete me without a meeting.")
    End Sub
End Module
```

---

## Alternatives (aka: if you want to start fresh)

If you’re choosing a language today for a new .NET project, the most common alternative is:

* **C#** (the default dialect of modern .NET, and the one most examples are written in)

But Visual Basic can still be a totally legitimate choice if your team already knows it, your codebase is VB, or you’re maintaining systems where stability beats fashion.

---

## History: when was it most popular?

Visual Basic originally exploded because it made Windows app development feel possible for normal humans.

You didn’t need to be a wizard. You needed a mouse and the willingness to drag a button onto a form and pretend you planned it.

Classic VB ended its main era with VB6, which is why this page still exists like a museum plaque you can’t stop reading: **[Visual Basic 6.0 documentation](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-basic-6/visual-basic-6.0-documentation)**

Modern Visual Basic’s highest position (in the current TIOBE era tracking) hit **#6 in June 2023**, which is the most Visual Basic thing imaginable: not “#1,” but “quietly near the top while everyone argues on social media.”

---

## Who uses it the most?

A lot of usage is internal and invisible, which is the whole point.

Think: banks, insurance, healthcare, manufacturing, local government, and any organization where “rewriting the system” is considered a myth, like unicorns or meetings that end early.

If your company runs Excel like it’s an operating system, congratulations: you probably have Visual Basic in the building.

---

## Does it work well with AI?

Surprisingly well, if you’re using it inside modern .NET.

Visual Basic can absolutely participate in AI-powered workflows through the .NET ecosystem, especially if you’re doing practical tasks like classification, prediction, or automation inside business apps.

A great entry point is **[ML.NET documentation](https://learn.microsoft.com/en-us/dotnet/machine-learning/)**, which is built for .NET developers who want to add machine learning without turning their lives into a math dissertation.

---

## What tech stack does it work with?

Modern Visual Basic works best with:

* .NET runtime and libraries
* Windows desktop apps (WinForms / WPF)
* Web services (if you’re living in .NET land)
* Databases, APIs, enterprise integrations

Classic VB is more “Windows + COM + legacy systems + please don’t reboot the server.”

---

## What tools work best with it?

For modern Visual Basic, you’ll typically use Visual Studio.

Yes, the big one. The one with the installer that looks like it’s about to ask you personal questions.

You can grab it here: **[Visual Studio Community](https://visualstudio.microsoft.com/vs/community/)**

---

## How much is it going to cost you?

* The language: free
* The runtime: free
* The tools: often free (Community edition), or paid if you need enterprise features

The real cost is emotional: the moment you realize the “temporary” VB app from 2009 is now a mission-critical system and has outlived three CEOs.

---

## Any other interesting tidbits?

Visual Basic is one of the few languages that can honestly say:

“I helped regular humans build Windows apps without needing to sell their soul to a pointer.”

It lowered the barrier to entry for a generation, and it’s still holding up the ceiling in a lot of places.

So if you’re a VB dev, you’re not behind the times.

You’re keeping the lights on.

And if you’ve got a favorite Visual Basic memory (or a VB horror story), drop it in the comments.

Also: follow me for more episodes in this series, because next we’re heading into SQL, and that one is basically the language every app pretends it doesn’t depend on.

---

**[Art Prompt (Rococo):](https://lumaiere.com/?gallery=rococo)**
A luminous, ornate garden scene painted with delicate, airy brushwork and playful elegance. Sunlight filters through lace-like foliage, scattering warm pearl highlights across billowing pastel fabrics and gilded decorative details. The composition feels theatrical yet weightless: a graceful figure on a suspended seat arcs through a flowering arbor, ribbons fluttering and silk folds catching the light like spun sugar. The palette is soft and indulgent—powder pinks, creamy ivories, pale celadon greens, and hints of gold leaf—balanced by cool shadows in lavender and misty blue. The mood is flirtatious, dreamy, and slightly mischievous, with intricate textures and ornamentation that make the whole scene feel like a sweet secret told in a whisper.

**[Video Prompt:](https://www.tiktok.com/@davelumai/video/7588650467970796830)**
Transform the scene into a lively, high-energy looping vignette: the suspended seat sweeps forward in a rhythmic arc while ribbons whip and curl in the air like animated calligraphy. Flower petals burst and spiral in playful gusts, briefly forming heart-like swirls before dissolving into glittering dust motes. Sunbeams flicker through leaves in staccato pulses, creating dancing highlights that shimmer across silk folds and gilded trim. Add a moment of surprise: a tiny flock of pastel songbirds darts through the arbor in a coordinated wave, then scatters, leaving trailing sparkles. The motion should feel crisp, buoyant, and magical, with micro-animations everywhere—fluttering lace, trembling blossoms, drifting pollen—ending in a seamless loop with the seat returning to the start of its arc.

Song picks for the video:

* Ode to the Mets - The Strokes
* Kokomo, IN - Japanese Breakfast

