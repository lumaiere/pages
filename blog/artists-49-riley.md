# Episode 49: Bridget Riley, or How to Make Your Eyeballs Do Jumping Jacks

Bridget Riley is the rare artist who can make a flat, motionless surface feel like it just chugged an espresso and decided to jog directly across your retinas.

If you have ever stared at a painting and thought, “Is this moving… or did I forget to drink water today?”, congratulations: you have entered the wonderfully disorienting world of Op Art, and Riley is one of its most iconic masterminds.

## Who is this artist?

Bridget Riley (born April 24, 1931) is an English painter whose optical-pattern works became central to the Op Art movement of the 1960s. 

She studied at Goldsmiths College and later the Royal College of Art, which is basically the artistic equivalent of training at a dojo where the black belts critique your brushstrokes and your life choices. 

## What is she known for?

She is known for paintings built from repeated geometric forms that create intense illusions of vibration, movement, bulging space, and visual “events” that happen inside the act of looking. If the painting makes you feel like the floor is gently rolling, that’s not a bug. That’s the feature.

A landmark early piece is her square-based optical work from 1961, where simple alternating shapes become a full-blown perceptual roller coaster.

## What is her style?

Riley’s style is disciplined, geometric abstraction designed to activate perception. Early on, she leaned hard into high-contrast black-and-white patterns. Later, she expanded into color systems that still behave like they’re alive and slightly mischievous. 

This is art that doesn’t just sit there looking pretty. It *performs*—quietly, relentlessly, directly in your visual cortex.

## Who taught her?

You can trace her formation through formal training (Goldsmiths and the Royal College of Art), but one especially important influence was her mentor Maurice de Sausmarez, who pushed her to look closely and think seriously about the mechanics of seeing and modern painting. 

## Does she use any special technique?

Yes: she treats perception like a medium.

Riley’s process is intensely planned—studies, precise designs, tight control of edges and spacing—because tiny differences create totally different physical sensations in the viewer. In printmaking, she embraced screenprinting for its ability to produce sharp geometry and flat, even fields, and she used stencils to keep edges aggressive and clean.

Also: this is not “close your eyes and feel the muse” painting. This is “measure twice, make the viewer’s eyeballs pirouette, measure again” painting.

Here’s a tiny example of how “simple rules” can create wild optical energy (and how computers, like obedient little apprentices, will happily do the repetition for you):

```python
# A quick-and-dirty optical grid generator (concept demo)
# Tip: tweak frequency and phase to change the "wobble" feeling.

import math

width = 60
height = 20
freq = 0.35

for y in range(height):
    row = []
    for x in range(width):
        v = math.sin(x * freq + math.sin(y * 0.35))
        row.append("█" if v > 0 else " ")
    print("".join(row))
````

## Who has she worked with?

Riley’s work often involves collaboration in the practical, studio sense: assistants help translate carefully developed studies into finished works, following her decisions like musicians reading a score. 

In the print world, she worked with professional studios and publishers because precision matters here the way tuning matters to a piano: you don’t “kind of” tune it and hope Beethoven forgives you later. 

## Was she wealthy?

Not in the “born into golden paintbrushes” sense. Her early life included disruptions and practical work, and her rise was built through training, persistence, and eventually major institutional attention. She later earned major prizes and global recognition, and her work became highly collected—so yes, success arrived, but it didn’t show up on day one like a limo with a monocle. 

## When was she most popular?

Her breakout moment hit in the mid-1960s, when Op Art became a lightning rod for attention and debate, and her work appeared in the Museum of Modern Art’s famous exhibition *The Responsive Eye* (1965). 

Then something very predictable happened: the world tried to copy the look everywhere, and serious people briefly panicked about whether geometry was secretly taking over civilization. (It wasn’t. Mostly.)

Her influence and visibility continued well beyond the 1960s, with ongoing critical attention and decades of evolving work. 

## Tell me more, please

One of the best “aha” keys for Riley is this: she’s not trying to depict objects. She’s trying to create *experience*.

That experience lives in the viewer’s body: micro-movements of the eye, unstable edges, rhythms that feel like they’re humming. You don’t just look at a Riley—you *participate* in it, whether you meant to or not. 

## Anything else left to tell?

Yes: Riley proves something wonderfully annoying (in the best way): a limited vocabulary can produce endless expressive outcomes.

Squares, lines, curves, repeats, shifts—these are not “simple.” They’re the alphabet. And she writes whole novels with it.

## Any other interesting tidbits?

* A single repeated form can create very different sensations depending on spacing, scale, and edge clarity—her work is a masterclass in how small decisions become big effects. 
  
* Her prints are a huge part of how widely her work circulates; the medium fits her precision like it was made for it.

## Follow and comment

If you’ve ever had a painting mess with your depth perception (politely or otherwise), drop a comment with the moment you realized your eyes were doing extra work.

And if you want more art, more episodes, and more friendly chaos, follow me—because your feed deserves at least one thing that isn’t trying to sell you a miracle pan.

More long-form writing lives here: **[DaveLumAI on longer-form](https://medium.com/@DaveLumAI)**

---

**References:**

* **[Britannica biography](https://www.britannica.com/biography/Bridget-Riley)**
* **[MoMA: The Responsive Eye](https://www.moma.org/interactives/moma_through_time/1960/the-responsive-eye/)**
* **[Google Arts & Culture: 1961 square-based work overview](https://artsandculture.google.com/asset/movement-in-squares-bridget-riley/dwGpQ5o3Dc4FrQ)**
* **[Princeton Art Museum: screenprint note on stencils + optical effect](https://artmuseum.princeton.edu/art/collections/objects/80869)**
* **[Yale Center for British Art: printmaking + studies + assistants](https://britishart.yale.edu/printmaking-precision)**
* **[Paul Mellon Centre artist guide](https://www.paul-mellon-centre.ac.uk/archives-and-library/artist-subject-guides/bridget-riley)**

---

**[Art Prompt (Op Art):](https://lumaiere.com/?gallery=op-art)**
A large-scale abstract composition built from repeating geometric units that create a powerful illusion of depth and shifting motion, as if the surface is subtly bending inward. Use a stark, high-contrast palette dominated by matte black and warm off-white, with occasional soft gray transitions that feel like breathing space. The structure is crisp and architectural: a grid of evenly spaced forms that gradually compress and skew toward one side, producing a visual “pull” that feels both controlled and unsettling. Edges must be razor-clean, spacing mathematically consistent, and the overall rhythm hypnotic, like a silent machine humming. Lighting is flat and even to emphasize optical tension rather than texture, with the mood oscillating between calm precision and a faint sense of vertigo.

**[Video Prompt:](https://www.tiktok.com/@davelumai/video/7608034195901893918)**
Animate the abstract geometric grid so the repeated units subtly compress, expand, and skew in a smooth wave that travels across the frame, creating a hypnotic illusion of bending space. Add a gentle camera drift and slow zoom that amplifies the optical pull, with micro-vibrations in the transitions between black, off-white, and gray to enhance the sensation of motion. Keep edges razor-sharp and lighting perfectly even, but introduce rhythmic pulses where the grid “breathes” in time, like a visual metronome. Make the movement loop seamlessly, alternating between calm, controlled alignment and a momentary warped “snap” that feels satisfyingly strange without becoming chaotic.

**Song suggestions for the video:**

* Everything Connected – Jon Hopkins
* Breezeblocks – alt-J
