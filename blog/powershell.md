# Episode 14: PowerShell - The Command Line That Wears a Suit but Still Breaks Your Stuff

There are two kinds of people in this world:

1. People who love PowerShell.
2. People who have only used PowerShell once, typed `Remove-Item` with way too much confidence, and now whisper the words "test environment" like a prayer.

PowerShell is the rare technology that can be both a gentle productivity boost and a laser-guided chaos cannon. It is incredibly capable, occasionally misunderstood, and still very relevant. Which is impressive for something that most folks first encounter while trying to figure out why a Windows service is "Running" but also somehow "Not Running."

If you have ever stared at a terminal and thought, "I wish my commands returned actual structured objects instead of a text soup I have to strain through regex cheesecloth," PowerShell was made for you.

To go deep on the official basics, start here: **[PowerShell Documentation](https://learn.microsoft.com/en-us/powershell/)**

---

## What is it?

PowerShell is both:

* A command-line shell you can drive like a stolen rental car
* A scripting language designed for automation and configuration

The big twist is that PowerShell is object-based. Commands produce objects, not just strings. That means you can filter, sort, group, format, and export with way less screaming.

Also, PowerShell is cross-platform now. It runs on Windows, Linux, and macOS, which is the sort of plot twist that would have sounded like fan fiction in 2009.

If you like looking under the hood (or arguing with the hood), the main project lives here: **[PowerShell on GitHub](https://github.com/PowerShell/PowerShell)**

---

## Is it still relevant?

Absolutely.

PowerShell is still a go-to for:

* Windows administration
* Cloud automation (Azure, AWS, Microsoft 365)
* CI/CD scripting
* Endpoint management
* Bulk operations across fleets of machines
* Glue code between "tools that refuse to talk to each other"

And it still shows up as a widely used language in modern developer tooling surveys. For example, it appears in the 2025 results here: **[Stack Overflow Top Languages](https://survey.stackoverflow.co/2025/technology)**

PowerShell has basically become the language of "I need to do the thing, and I need to do it to 400 machines, and I needed it done yesterday."

---

## Pros and cons

### Pros

**It works with objects**
You pipeline real data instead of string confetti.

**It is ridiculously productive**
When you know the idioms, you can do in 3 lines what takes 60 lines elsewhere.

**It is built for automation**
Scheduling, remoting, modules, and scripting are first-class citizens.

**It plays well with modern formats**
JSON, CSV, XML, REST APIs, logs, you name it.

### Cons

**The learning curve is weird at first**
You think you are learning a shell, but you are also learning a language, an object model, a module ecosystem, and a philosophy. It is like adopting a puppy that comes with a tax code.

**Compatibility quirks**
Different versions behave differently, and Windows-only cmdlets can make cross-platform scripts feel like trying to teach a cat to swim.

**It is powerful enough to ruin your day**
PowerShell does not ask, "Are you sure?" as much as it silently asks, "How sure were you, really?"

---

## Strengths and weaknesses

**Strengths**

* Bulk administration and automation
* Working with system info, services, processes, users, files, and registries
* Tooling ecosystems and modules
* Clean data transformations in the pipeline

**Weaknesses**

* Writing large applications is possible, but it is not where it shines
* Some scripts become "clever" instead of maintainable
* Performance is fine for most admin tasks, but not your best choice for heavy compute

---

## What is it used for?

PowerShell is used for:

* Server setup and configuration
* Account provisioning
* Scheduled maintenance
* Log collection and parsing
* Deploying and updating software
* Orchestrating cloud resources
* Querying APIs and stitching results together

In plain English: it is the language of "stop clicking the same buttons every day."

---

## Can you give me an example?

Here is a small example that shows the core vibe: fetch objects, filter them, format them, and export the results.

```powershell
# Find stopped services that are set to start automatically
$problemServices = Get-Service |
  Where-Object { $_.Status -eq "Stopped" } |
  ForEach-Object {
    $svc = Get-CimInstance Win32_Service -Filter ("Name='" + $_.Name + "'")
    [PSCustomObject]@{
      Name      = $_.Name
      Display   = $_.DisplayName
      StartMode = $svc.StartMode
      Status    = $_.Status
    }
  } |
  Where-Object { $_.StartMode -eq "Auto" } |
  Sort-Object Display

$problemServices | Format-Table -AutoSize

# Export for later blame assignment
$problemServices | Export-Csv -NoTypeInformation -Path ".\\stopped-auto-services.csv"
```

That is PowerShell in a nutshell: discover, filter, shape, export, repeat.

---

## What are the alternatives?

It depends what you are doing.

* **Bash / Shell**: great everywhere, but text-based by default
* **Python**: incredible for automation and scripting, especially cross-platform
* **Ruby**: still a strong scripting language in many environments
* **Node.js**: useful when automation is living in a JavaScript world
* **Go**: great for shipping a single binary tool
* **Ansible / Terraform**: if your "script" is really infrastructure management

PowerShell shines when the environment is Windows-heavy, object-friendly, or requires deep system hooks.

---

## Is it similar to anything else?

It feels like a mashup of:

* A Unix-style shell pipeline
* A scripting language
* A .NET object playground
* An admin toolkit that wants to be your best friend

If Bash is a pocketknife and Python is a workshop, PowerShell is a rolling tool chest that sometimes falls down the stairs if you forget a single quote.

---

## Does it work well with AI?

Yes, and for a simple reason: PowerShell is explicit.

Cmdlets are verb-noun, objects are structured, and scripts tend to be readable. That makes it easier for AI tools to generate useful starting points and for humans to review them without needing an archeological dig.

The best workflow is still the same: let AI draft, then you verify, test, and avoid running it in production like you are speedrunning a catastrophe.

---

## What tech stack does it work with?

PowerShell fits nicely with:

* Windows Server and Active Directory
* Azure and Microsoft 365 tooling
* REST APIs across basically everything
* CI/CD systems (GitHub Actions, Azure DevOps, Jenkins, etc.)
* Docker and container workflows
* Logging and monitoring pipelines

---

## What tools work best with it?

If you want the smoothest experience, use Visual Studio Code with the PowerShell extension here: **[PowerShell for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode.PowerShell)**

That setup gives you debugging, linting, completions, and fewer moments of staring at your screen like it owes you money.

---

## How much is it going to cost me?

PowerShell itself is free.

The real cost is time:

* Learning the pipeline mindset
* Building a module habit
* Writing scripts you will not hate in six months
* Testing before you deploy, unless you enjoy performance art starring your pager

---

## Any other interesting tidbits?

* The "verb-noun" naming convention is not just cute. It makes scripts read like instructions instead of hieroglyphics.
* PowerShell’s superpower is turning repetitive work into reusable tools.
* The fastest way to level up is to automate one annoying task per week. Your future self will thank you. Your mouse will throw a retirement party.

---

If you enjoyed this, hit follow and tell me in the comments:

What is the first thing you would automate with PowerShell if you had a magic wand and absolutely no fear?

---

**[Art Prompt (Pointillism):](https://lumaiere.com/?gallery=pointillism)**
A luminous coastal harbor scene rendered entirely in crisp, jewel-like dots of color, where the surface of the water shimmers with countless specks of cobalt, turquoise, and soft pearl, reflecting a sky built from pale lemon and powder blue. Slender sailboats cluster near a sunlit quay, their masts forming delicate vertical rhythms against the horizon. The shoreline is alive with warm terracotta buildings and muted green trees, all suggested through precise stippling rather than hard outlines. The composition balances calm geometry with sparkling motion, as if the air itself is vibrating with light. The mood is buoyant and serene, with a bright midday clarity and a gentle sense of breezy optimism, museum-quality lighting, high resolution, no text.

**[Video Prompt:](https://www.tiktok.com/@davelumai/video/7596177545075248414)**
A vibrant pointillist harbor comes alive in a looping sequence where thousands of tiny color-dots subtly pulse and rearrange like living pixels. Sunlight glitters across the water in rhythmic sparkles, sailboats gently bob with playful micro-movements, and the sky breathes with soft, shifting dot patterns that feel musical. The camera glides forward in short, energetic pushes and tiny lateral snaps, syncing with the flicker of reflected light, while occasional gust-like ripples sweep across the scene as waves of brighter color. Crisp, mesmerizing motion, bright midday atmosphere, endlessly rewatchable.

For the vibe, pair it with:

* **Feather – Nujabes (feat. Cise Starr & Akin)**
* **Window Seat – Erykah Badu**
