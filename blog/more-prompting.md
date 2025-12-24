# The Patience of Working With AI (and How to Make It Behave)

Working with AI for coding and DevOps is a bit like working with a very eager intern who never gets tired, never blinks, and will happily hand you a 20 step plan before you have finished typing “hi.” It is powerful, impressive, and occasionally exhausting if you do not slow it down or speed it up on your terms.

I learned this the hard way while configuring a brand new site and spinning up infrastructure. What should have been a mildly annoying weekend project turned into a master class in patience, prompting, and learning how to tell an AI to chill for five seconds.

At first, I made the classic mistake: I asked for help, and it responded by unloading an entire encyclopedia on my screen. Twenty steps. Commands I had not run yet. Decisions I had not made yet. Step four failed immediately, which made steps five through twenty beautifully useless. They just sat there, staring at me, judging my choices and wasting my screen space.

That was the moment I realized something important. The problem was not the AI. The problem was how I was driving it.

Once I told it to go step by step and wait for my response before continuing, everything changed. Suddenly, it felt like pair programming instead of being shouted at by a very fast lecturer. I could run a command, see what broke, fix it, then move on. Debugging became calm instead of chaotic.

Then the opposite problem appeared. After the big issue was solved, continuing one step at a time felt painfully slow. Waiting for permission to move forward when nothing was breaking was like stopping at every green light just to admire the paint on the traffic signal.

So I changed the instructions again. I asked for blocks of steps instead of single steps. Three to five at a time. Enough momentum to move forward, but not so much that a failure would invalidate an entire novel of instructions. That balance worked like a charm, and I was able to finish the deploy at exactly the speed my brain wanted.

This is the first real lesson of working with AI: you control the pacing. You can tell it to slow down, speed up, or shift gears entirely. Phrases like “wait for my confirmation before continuing,” “give me the next step only,” or “give me the remaining steps in small batches” are not politeness. They are steering commands.

Another underrated trick is narrating what you are doing. When you say things like “I am SSH’d into the server now” or “I just ran the command and got this error,” you save yourself from re-prompting from scratch. The AI does not magically see your terminal, but it does keep context, and good context is half the battle.

Some tools are starting to blur that line even further. Editors like **[Cursor](https://www.cursor.sh/)** can read your code as you type and suggest changes without you constantly explaining what file you are in or what function you are touching. Models with multimodal abilities can even reason over screenshots, which means you can literally show an error instead of describing it like you are on tech support in 1998.

If you want help configuring a server while you are SSH’d in, the best approach is brutally simple: copy and paste. Paste the command you ran, paste the error output, and say what you expected to happen. That last part matters. The AI is very good at fixing things once it knows what “correct” looks like in your head.

As for prompting techniques that consistently work, a few rules stand out. Tell it what role you want it to play. Tell it how verbose you want it to be. Tell it whether you want explanations or just commands. And when something changes, say so. AI does not get offended when you change your mind. It gets better.

One interesting side effect of all this is that patience goes both ways. The more deliberate you are with instructions, the less cleanup you have to do later. You trade a few extra words up front for fewer headaches down the line. That is a bargain any developer should take.

If you have your own tricks, horror stories, or magical phrases that make AI behave, drop them in the comments. And if you want more experiments, art, and mildly opinionated writing about tech and creativity, follow along. The machines are fast. You do not have to be.

---

**[Art Prompt (Constructivism):](https://lumaiere.com/?gallery=constructivism)**
A bold geometric composition built from intersecting rectangles, circles, and diagonal planes arranged with precise tension and balance. A restrained palette of deep reds, industrial blacks, warm creams, and muted grays dominates the canvas, with sharp contrasts between solid blocks and thin linear accents. The surface feels architectural and purposeful, as if designed for both function and visual rhythm. Strong directional lines create a sense of motion and structure, while negative space is used deliberately to guide the eye. The mood is confident, modern, and disciplined, evoking clarity, order, and forward momentum.

**[Video Prompt:](https://www.tiktok.com/@davelumai/video/7587232726223310110)**
Animate the geometric forms so they slide, rotate, and lock into place with crisp, mechanical motion. Rectangles glide horizontally while circles pulse subtly, and diagonal lines sweep across the frame like precision tools aligning a structure. Use smooth transitions, rhythmic timing, and gentle camera pans to emphasize balance and movement. The animation should feel purposeful and kinetic, with a clean, modern flow that keeps the viewer engaged from start to finish.

**Songs to pair with the video:**
- Bad Kingdom – Moderat
- Neon Pattern Drum – Jon Hopkins
