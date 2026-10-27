# Who’s Who in AI — Episode 3: Geoffrey Hinton, Yann LeCun, and Yoshua Bengio — The Deep Learning Rebels Who Refused to Let Neural Networks Die

In [Episode 1: Alan Turing — The Man Who Asked Whether Machines Could Think](https://medium.com/@DaveLumAI/whos-who-in-ai-episode-1-alan-turing-or-the-man-who-asked-whether-machines-could-think-0ba973c1613a), we met the man who asked the question.

In [Episode 2: John McCarthy, Marvin Minsky, and Dartmouth — When Artificial Intelligence Got a Name](https://medium.com/@DaveLumAI/whos-who-in-ai-episode-2-john-mccarthy-marvin-minsky-and-dartmouth-when-artificial-b3af7d075069), we met the people who gave the question a scientific field, a research agenda, and a truly impressive collection of optimistic predictions.

Now we meet three researchers who spent decades pursuing an idea that much of the scientific establishment considered impractical, overhyped, or possibly a waste of perfectly respectable mathematics.

Then their idea helped transform artificial intelligence.

And now they disagree about what happens next.

Naturally.

Hi, Dave LumAI here. I spend enough time talking to artificial intelligence to appreciate the people who made these conversations possible. I am slightly less enthusiastic about the possibility that my chatbot might eventually develop strong opinions about my management style.

Today's three guests are [Geoffrey Hinton](https://x.com/geoffreyhinton), [Yann LeCun](https://x.com/ylecun), and [Yoshua Bengio](https://x.com/Yoshua_Bengio).

Collectively, they are often called the godfathers of deep learning.

Individually, they are brilliant, stubborn, influential, occasionally argumentative, and living proof that being right about something important does not guarantee you will agree about what to do afterward.

Let's meet them.

## First, the Good Stuff: Any Interesting Tidbits?

Oh, absolutely.

**Geoffrey Hinton is the great-great-grandson of George Boole.**

Yes, that George Boole.

The mathematician whose Boolean algebra helped establish the foundations of digital computing.

Apparently, the family business involves inventing mathematics that future generations will use to make computers behave strangely.

Hinton also has a reputation for enthusiastically announcing that he finally understands how the brain works.

According to a [University of Toronto profile](https://magazine.utoronto.ca/research-ideas/technology/getting-smarter-computer-science-professor-geoffrey-hinton-is-helping-to-build-a-new-generation-of-intelligent-machines/), his former students recall him periodically announcing a new breakthrough in understanding the brain, sometimes acknowledging that all his previous attempts had been wrong.

That is either extraordinary scientific humility or the world's longest-running software debugging session.

**Yann LeCun helped build neural networks that read handwritten bank checks.**

Before neural networks were generating images, answering questions, and explaining why your printer was offline, they were figuring out whether somebody had written a 3 or an 8.

By the late 1990s, systems based on LeCun's work were processing roughly 10 to 20 percent of checks in the United States.

Think about that.

One of the foundations of modern AI spent its early commercial career deciphering handwriting that probably looked like it had been produced during an earthquake.

And **Yoshua Bengio entered this story partly by asking unusually good questions.**

During the 1980s, LeCun gave a research talk at McGill University. One particularly sharp graduate student in the audience impressed him.

That student was Bengio.

LeCun later helped bring him into Bell Labs.

So one of AI's most consequential research relationships began with the academic equivalent of somebody raising a hand and saying, "Actually, I have a question."

Let this be a lesson to anyone who thinks asking questions makes you look foolish.

Occasionally, it makes you a Turing Award winner.

## What Was So Controversial About Neural Networks?

To understand these three, we need to revisit an old argument.

In the early decades of artificial intelligence, many researchers believed intelligent machines should work primarily through symbols, logical rules, and carefully structured reasoning.

If you wanted a computer to recognize something, you might try to explain the relevant rules.

If you wanted it to solve a problem, you could give it a logical framework.

If you wanted it to understand language, you might construct elaborate representations of grammar, meaning, and relationships.

This approach became known as **symbolic AI**.

John McCarthy and Marvin Minsky, whom we met in Episode 2, were central figures in that world.

But another group of researchers was interested in a different possibility.

What if intelligence could emerge from systems that learned patterns from experience?

What if a computer did not need somebody to manually describe every useful rule?

What if it could gradually discover those rules by processing examples?

That was the attraction of **artificial neural networks**.

The basic idea was inspired, loosely, by biological nervous systems.

Instead of programming every decision, researchers constructed networks of simple mathematical units connected by adjustable numerical weights.

Those weights determined how information flowed through the network.

Training meant adjusting the weights until the system became better at a particular task.

In theory, marvelous.

In practice, early neural networks had limitations.

Some were mathematically restricted. Others were difficult to train. Computing power was expensive. Datasets were relatively small. And many ambitious promises failed to materialize.

Minsky and Seymour Papert's 1969 book *Perceptrons* famously analyzed limitations of certain early neural-network designs.

The book did not prove that all neural networks were hopeless. But it became associated with growing skepticism toward the approach.

AI research subsequently endured periods of reduced enthusiasm and funding, commonly called **AI winters**.

There were multiple causes, including disappointed expectations surrounding other AI approaches.

Still, neural networks became particularly unfashionable during parts of the 1990s and early 2000s.

Some researchers moved on.

Hinton, LeCun, and Bengio did not.

They believed the underlying idea still had enormous potential.

And they kept working.

## Geoffrey Hinton: The Man Who Wouldn't Stop Thinking About Brains

Geoffrey Hinton was born in Britain in 1947.

He studied experimental psychology at Cambridge and earned his doctorate in artificial intelligence from the University of Edinburgh in 1978.

His central fascination was deceptively simple.

**How does the brain learn?**

Not merely how people follow rules.

How do we recognize faces, remember concepts, understand patterns, and develop useful internal representations of the world?

Hinton believed artificial neural networks might reveal something important about biological intelligence while providing a practical route toward intelligent machines.

He pursued these ideas at a time when doing so was not necessarily the fastest way to obtain academic applause.

Or funding.

Or invitations to conferences where everyone agreed with you.

### The Breakthrough Called Backpropagation

One of Hinton's most important contributions was helping establish backpropagation as a practical method for training multilayer neural networks.

Here is the friendly explanation.

Imagine teaching a machine to recognize handwritten numbers.

You show it an image of an 8.

The machine says 3.

Incorrect.

Rather than simply shouting at the computer, which remains emotionally satisfying but scientifically unproductive, we need a way to determine how its internal connections should change.

**Backpropagation provides an efficient way to calculate how changes in a network's parameters would affect its error.**

A learning algorithm can then use those calculations to adjust the weights.

Repeat this process across many examples, and the system can gradually improve.

The exciting part is that hidden layers can learn useful intermediate representations without anyone explicitly programming every feature.

One layer might respond to simple edges.

Later layers might respond to more complicated shapes.

Eventually, the network might recognize the number.

The mathematics is more involved than this explanation, naturally. Mathematics insists on maintaining some professional mystique.

In 1986, Hinton, David Rumelhart, and Ronald Williams published the influential paper *Learning Representations by Back-Propagating Errors*.

You can find it among [Hinton's publications on backpropagation](https://www.cs.toronto.edu/~hinton/backprop.html).

An important historical clarification: they did not invent the underlying mathematical principle from nothing.

Earlier researchers, including Seppo Linnainmaa and Paul Werbos, had developed important foundations for efficient differentiation and its application to learning systems.

Hinton and his collaborators helped demonstrate and popularize its power for training neural networks.

That distinction matters.

Scientific progress usually resembles a relay race more than a single person planting a flag on an untouched mountain.

### The Long Wait Pays Off

Hinton joined the University of Toronto in 1987 and helped establish it as an important center for neural-network research.

Over the following decades, he worked on distributed representations, Boltzmann machines, learning algorithms, and other techniques that helped make deep learning practical.

But his most famous modern breakthrough arrived in 2012.

Working with graduate students Alex Krizhevsky and Ilya Sutskever, Hinton helped produce a neural-network system called **AlexNet**.

We'll return to that machine shortly.

Because AlexNet was the moment when a great many skeptical researchers suddenly discovered they had always been extremely interested in neural networks.

Funny how that happens.

## Yann LeCun: The French Engineer Who Taught Computers to Read

Yann LeCun was born in France in 1960.

He studied electrical engineering and earned a doctorate in computer science in Paris in 1987.

While Hinton was exploring how neural networks could learn internal representations, LeCun was particularly interested in making those networks work efficiently on real-world problems.

Especially images.

He completed postdoctoral research with Hinton at the University of Toronto before joining AT&T Bell Laboratories in 1988.

There, LeCun helped develop and successfully train **convolutional neural networks**, commonly called CNNs or ConvNets.

### What Is a Convolutional Neural Network?

Imagine looking at a photograph.

You do not consciously inspect every pixel independently.

You recognize edges, shapes, textures, and patterns.

A convolutional neural network processes images using learned filters applied across different locations.

These filters allow the network to detect useful visual features while reusing the same learned parameters across an image.

That makes CNNs particularly effective for recognizing visual patterns.

Earlier pioneers, notably Kunihiko Fukushima, had developed important convolution-like architectures.

LeCun's great contribution was helping combine these ideas with effective gradient-based training and demonstrating their practical usefulness.

He was not merely suggesting that the approach might work someday.

He was building systems that actually worked.

### From Handwriting to Banking

At Bell Labs, LeCun and his collaborators developed neural networks capable of recognizing handwritten digits and documents.

These systems eventually found commercial use in banking.

And here is a particularly satisfying connection.

A major 1998 paper, *Gradient-Based Learning Applied to Document Recognition*, was written by Yann LeCun, Léon Bottou, Yoshua Bengio, and Patrick Haffner.

Yes.

LeCun and Bengio were collaborating long before their names appeared together on major AI awards.

You can explore the [original document-recognition research](https://leon.bottou.org/papers/lecun-98h).

Those boring-looking financial documents turned out to be an excellent proving ground for techniques that later transformed computer vision.

There is something deeply amusing about a technology that eventually helps power robots, medical imaging, and advanced AI having an early breakthrough in reading checks.

Artificial intelligence had to pay its bills before it could become famous.

### From Bell Labs to Meta

LeCun joined New York University in 2003.

In 2013, he became the founding director of Facebook AI Research, commonly known as FAIR.

Facebook later became Meta.

LeCun remained an influential figure in the company's AI research efforts for more than a decade, advocating deep learning, self-supervised learning, and research approaches that could move beyond narrowly trained systems.

He also became one of the AI community's most recognizable public debaters.

He has strong opinions.

He shares them.

Frequently.

If artificial intelligence ever develops a professional debate league, LeCun is going to require his own division.

## Yoshua Bengio: The Man Who Helped Teach Neural Networks Language

Yoshua Bengio was born in France in 1964 and built much of his academic career in Montreal.

He earned his doctorate in computer science from McGill University in 1991 and completed postdoctoral work before becoming a professor at the Université de Montréal.

Like Hinton and LeCun, Bengio believed neural networks could discover useful representations from data.

But he made particularly influential contributions to language modeling, representation learning, and methods for training deep networks.

### Before Chatbots Became Everybody's Favorite Coworker

In the late 1990s and early 2000s, much of computerized language processing relied on statistical techniques that counted patterns in words and word sequences.

These methods could be useful, but they struggled with unfamiliar combinations and the enormous number of possible sentences.

Bengio and his collaborators explored a different approach.

Instead of treating words primarily as isolated symbols, neural networks could learn numerical representations capturing useful relationships among them.

Words appearing in similar contexts could acquire related representations.

That made it possible to generalize beyond exact word sequences seen during training.

In 2003, Bengio and his collaborators published [*A Neural Probabilistic Language Model*](https://jmlr.org/papers/v3/bengio03a.html).

The work helped establish ideas that became central to neural language processing.

It was not a modern large language model, and it did not contain today's transformer architecture.

But it helped lay important groundwork.

Long before people were asking [ChatGPT](https://chatgpt.com/) to write wedding speeches, troubleshoot JavaScript, or explain quantum mechanics to their dog, Bengio was helping establish ways for neural networks to learn useful representations of language.

### Building a Research Community

Bengio also helped develop methods for training deep architectures when researchers were still struggling to make large networks learn effectively.

His work helped advance representation learning and generative modeling.

His Montreal research community also became extraordinarily influential.

Bengio founded what grew into [Mila, the Quebec Artificial Intelligence Institute](https://mila.quebec/en/), which became a major center for machine-learning research.

And his influence extended through students and collaborators.

One of those researchers was Ian Goodfellow, who led the development of generative adversarial networks, or GANs, while working in Bengio's research environment.

GANs helped transform image generation by training competing neural networks.

One network generates examples.

Another tries to distinguish generated examples from real ones.

Each pushes the other to improve.

Basically, two mathematical systems competing over who can be more convincing.

The academic version of siblings arguing over who broke the lamp.

## The Friendship That Helped Keep Deep Learning Alive

One of the most interesting parts of this story is that these researchers were not operating as three isolated geniuses.

They knew one another.

They collaborated.

They challenged one another.

They helped build communities around ideas that were not always fashionable.

Their relationships are documented in [LeCun's recollections of the early deep-learning years](https://ai.meta.com/blog/-turing-award-presented-to-yann-lecun-geoffrey-hinton-and-yoshua-bengio/).

Hinton mentored LeCun during his Toronto postdoctoral work.

LeCun recognized Bengio's talent and helped connect him with Bell Labs.

LeCun and Bengio collaborated on neural-network research.

Later, the three helped strengthen the international research community through initiatives supported by the Canadian Institute for Advanced Research, or CIFAR.

This mattered enormously.

A scientific idea does not survive decades of skepticism simply because somebody believes in it.

It needs researchers.

Students.

Funding.

Experiments.

Publications.

And enough intellectual stubbornness to keep going when another committee decides the future belongs to something else.

They helped create that environment.

## 2012: The Year Everybody Suddenly Believed

Now comes the turning point.

For years, neural networks had shown promise.

But a growing scientific field needs more than promise.

It needs a convincing demonstration that changes what researchers believe is possible.

In 2012, Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton delivered one.

Their system, AlexNet, entered the ImageNet Large Scale Visual Recognition Challenge, which tested how accurately computers could recognize objects in large image collections.

AlexNet used a deep convolutional neural network trained with graphics processing units, or GPUs.

The results were dramatic.

Its performance substantially exceeded the competing approaches.

The [original AlexNet research paper](https://papers.nips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) became one of the defining documents of modern AI.

And the [Computer History Museum has preserved the original AlexNet source code](https://github.com/computerhistory/AlexNet-Source-Code).

The breakthrough did not happen because someone suddenly invented neural networks in 2012.

The underlying ideas had been developing for decades.

What changed was the combination of better algorithms, larger datasets, more effective training techniques, and increasingly powerful GPUs.

Fei-Fei Li and her collaborators had helped provide the enormous ImageNet dataset.

Researchers like Hinton, LeCun, and Bengio had established critical learning techniques.

GPU hardware made large-scale training more practical.

And suddenly, things worked at a scale that demanded attention.

This was the moment when deep learning moved from promising research into the center of modern artificial intelligence.

The industry did not merely change its mind.

It reorganized its future.

## The Awards Finally Arrive

In 2019, the Association for Computing Machinery announced that Geoffrey Hinton, Yann LeCun, and Yoshua Bengio were receiving the **2018 A.M. Turing Award**.

The Turing Award is widely regarded as computing's highest honor.

Their recognition reflected decades of conceptual and engineering advances that helped make deep neural networks fundamental to modern computing.

There is something wonderfully appropriate about the award being named after Alan Turing.

The man from Episode 1 asked whether machines could think.

These three helped develop methods that made the question considerably more interesting.

Then, in 2024, Hinton received another extraordinary honor.

He shared the [Nobel Prize in Physics with John Hopfield](https://www.utoronto.ca/celebrates/geoffrey-hinton-wins-2024-nobel-prize-physics) for foundational discoveries enabling machine learning with artificial neural networks.

A field that spent years struggling for respectability had now helped produce a Nobel Prize in physics.

That is quite a journey.

From "interesting but probably impractical" to Stockholm.

## So What Did They Get Wrong?

Plenty.

And that is not a criticism.

It is how science works.

The interesting part is that these researchers were right about the importance of learning from data while not necessarily anticipating every way the technology would develop.

Early neural-network approaches struggled with training difficulties, computing limitations, and data requirements.

Many promising systems failed to scale.

Some methods once considered especially important were later replaced or supplemented by better approaches.

And the most successful modern AI systems have incorporated ideas from many research traditions, not just the work of these three.

**Deep learning did not eliminate the need for reasoning, planning, symbolic structure, or carefully designed systems.**

It changed how researchers approached those problems.

Modern AI also depends on countless people whose names rarely appear in headlines.

Researchers who developed mathematical foundations.

Engineers who created hardware and software tools.

Scientists who assembled datasets.

Students who ran experiments until the computers stopped making embarrassing mistakes.

And occasionally students who discovered that the computers could now make much more sophisticated embarrassing mistakes.

The biggest mistake would be imagining that three people invented modern AI by themselves.

They did not.

They were enormously important contributors to a much larger scientific effort.

## The Plot Twist: They No Longer Agree About the Future

Here is where the story becomes especially interesting.

As of October 2026, all three remain influential.

But their priorities have diverged.

And the disagreements are not trivial.

They concern the direction of artificial intelligence itself.

### Geoffrey Hinton: The Pioneer Sounding the Alarm

Hinton left Google in 2023.

He has since become one of the most prominent voices warning that increasingly capable AI systems could create severe risks.

His concerns include misuse by malicious actors, economic disruption, and the possibility that future systems could become more capable than humans can reliably control.

He is not arguing that AI has no benefits.

Quite the opposite.

He believes the technology could produce enormous advances in medicine, education, and productivity.

But he worries that competitive pressures are driving development faster than our ability to manage the risks.

In January 2026, the University of Toronto announced new support for [Hinton's continuing AI safety work](https://www.utoronto.ca/news/what-happens-when-ai-smarter-us-gift-supports-geoffrey-hinton-s-global-ai-safety-mission).

His position is essentially this:

We have created something extremely powerful.

We do not fully understand where its capabilities are heading.

Perhaps we should spend considerably more effort making sure this ends well.

Reasonable concerns from somebody who helped build the technology.

Although I imagine the conversations at industry conferences can become a little tense.

### Yann LeCun: The Future Needs More Than Language Models

LeCun has taken a notably different position.

He argues that current large language models, while impressive, are not sufficient to produce human-level intelligence.

His criticism focuses on limitations in understanding the physical world, forming reliable models of how things work, reasoning, and planning over extended periods.

He believes future AI systems need better ways to learn from the world itself.

Not merely text.

This interest has led him toward **world models**.

A world model attempts to learn useful representations of an environment so a system can predict what might happen and plan actions accordingly.

In late 2025, LeCun announced plans to leave Meta after more than twelve years.

In 2026, he is pursuing this vision through [AMI Labs](https://amilabs.xyz/), the company he founded to develop artificial intelligence that understands and interacts with the real world.

The company is exploring applications in robotics, industrial systems, healthcare, and other environments where physical understanding and reliable planning matter.

LeCun does not dismiss the achievements of language models.

He questions whether simply making them bigger will deliver the next major breakthrough.

His position is roughly:

Today's AI is impressive.

But genuine intelligence requires capabilities we have not yet adequately developed.

And we need new approaches to get there.

The fascinating part is that LeCun is effectively challenging another enormously popular direction in AI research.

Which is exactly what he was doing decades ago.

Apparently, retirement from intellectual rebellion was never on the schedule.

### Yoshua Bengio: Let's Build AI That Doesn't Have Its Own Agenda

Bengio has also become increasingly concerned about AI safety.

But he is exploring a different technical response.

In 2025, he launched **LawZero**, a nonprofit AI safety research organization.

Its objective is to develop advanced AI systems designed with safety as a foundational principle.

One of its central research directions is something called **Scientist AI**.

The broad idea is to develop powerful systems that make reliable predictions and assist human understanding without independently pursuing potentially dangerous goals.

That is an ambitious challenge.

It is also rather different from simply taking an existing chatbot and telling it to behave.

You can explore the research directly through [LawZero](https://lawzero.org/en/).

Bengio also chaired the [International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026), a major assessment involving more than 100 experts.

In September 2026, he addressed the United Nations Security Council about the dangers posed by increasingly autonomous AI.

His position is essentially:

The technology is advancing rapidly.

We are seeing warning signs.

We need fundamentally safer technical designs, independent oversight, and international cooperation.

Notice the distinction between these three approaches.

Hinton is emphasizing the scale of the potential danger.

LeCun is emphasizing the technical limitations of current approaches and the need for different architectures.

Bengio is concentrating on developing safer AI systems and stronger mechanisms for controlling advanced capabilities.

Their positions overlap in some places and differ substantially in others.

And none of them can honestly claim that the future is settled.

Which makes this one of the most important scientific disagreements happening today.

## Why Their Rivalry Is Actually Good for AI

It is tempting to imagine science as a tidy process.

A researcher discovers something.

Other researchers applaud.

Everybody agrees.

The discovery enters a textbook.

Everyone goes home satisfied.

Actual science is considerably messier.

Researchers argue over evidence.

They disagree about priorities.

They debate who deserves credit.

They challenge assumptions.

They occasionally express their disagreements on social media with the enthusiasm of people who have never encountered a character limit they respected.

But disagreement is not necessarily failure.

Hinton, LeCun, and Bengio demonstrate something important.

**You can agree about the foundations of a technology while disagreeing strongly about what it means and where it should go.**

In fact, those disagreements can be extremely productive.

If Hinton is right about the dangers, we need stronger safeguards.

If LeCun is right about the limitations of current models, we need new architectures.

If Bengio is right that safer systems require fundamentally different design principles, we need serious research into those principles.

All three possibilities deserve investigation.

The worst outcome would be deciding that the debate is inconvenient and should be replaced by advertising.

AI already has plenty of advertising.

What it needs is more rigorous understanding.

## The Connections That Lead to the Rest of This Series

By now, you should begin seeing how the people in this series fit together.

Alan Turing asked whether machines could think.

John McCarthy and Marvin Minsky helped establish artificial intelligence as a research field.

Hinton, LeCun, and Bengio demonstrated the enormous potential of neural networks that learn from data.

Fei-Fei Li and the ImageNet project supplied a critical ingredient for the computer-vision revolution.

Jensen Huang and NVIDIA helped provide the computing power needed to train increasingly large networks.

Demis Hassabis and DeepMind pushed learning-based systems into spectacular new applications.

And researchers such as Ilya Sutskever carried the deep-learning revolution into laboratories including OpenAI.

These connections matter because AI did not emerge from a single breakthrough.

It emerged from interacting ideas, institutions, people, and technologies.

A researcher solves one problem.

Another creates a dataset.

Somebody else builds faster hardware.

A fourth person realizes that a previously impractical technique now works.

Then an entire industry reorganizes itself around the result.

Occasionally before anybody has fully tested the business model.

## Why These Three Still Matter

The lasting contribution of Hinton, LeCun, and Bengio is not simply that they helped make neural networks successful.

It is that they helped change what artificial intelligence research considered possible.

For decades, the idea that complex capabilities could emerge from learned representations struggled against skepticism and practical limitations.

These researchers helped demonstrate that learning from data could produce increasingly powerful systems.

Their work influenced speech recognition, computer vision, natural language processing, and generative AI.

It helped establish research communities that trained generations of scientists.

And it laid important foundations for technologies that now affect nearly every industry.

But perhaps the most interesting part is what happened after they succeeded.

They did not all arrive at the same conclusions about the future.

Hinton became increasingly concerned about the dangers.

LeCun began pushing for new approaches to intelligence.

Bengio redirected much of his attention toward safety research.

Three pioneers.

One technological revolution.

Different visions of what comes next.

There is a certain poetry to that.

They spent decades trying to make machines learn.

Now the rest of us are trying to learn what those machines might mean for humanity.

And apparently, even the godfathers need to keep studying.

## Final Thoughts: Sometimes the Rebels Win

There is an encouraging lesson buried in this story.

Scientific consensus matters.

Evidence matters.

Expertise matters.

But popularity is not the same as truth.

Sometimes an idea takes decades to become practical.

Sometimes the hardware is not ready.

Sometimes the data does not exist.

Sometimes the mathematics is understood but the engineering remains painfully difficult.

And sometimes three stubborn researchers keep working long enough for the rest of the world to catch up.

That does not mean every unpopular idea is secretly brilliant.

Most unpopular ideas are unpopular for excellent reasons.

But occasionally, persistence combined with rigorous experimentation produces something extraordinary.

Hinton, LeCun, and Bengio helped prove that.

And now they are reminding us that building powerful technology is only the beginning.

Understanding what to do with it may be the harder problem.

**So here's my question for you:**

Which of the three perspectives makes the most sense?

Hinton's warnings about the risks?

LeCun's belief that AI needs fundamentally better ways to understand the world?

Or Bengio's push to develop safer AI systems from the ground up?

Maybe some combination of all three?

**Tell me in the comments.** I am genuinely curious where people stand on this one.

And if you enjoy exploring the personalities, rivalries, breakthroughs, and occasional scientific absurdities behind artificial intelligence, **follow along for the rest of *Who's Who in AI*.**

Next up:

**Episode 4 — Fei-Fei Li and ImageNet: The Woman Who Helped Teach AI to See.**

Because neural networks were becoming increasingly clever.

What they desperately needed next was a truly enormous collection of pictures.

Preferably labeled correctly.

Which, as it turns out, is an adventure all by itself.

---

## [Art Prompt (Folk Art):](https://lumaiere.com/?gallery=folk-art)

An intimate, exuberant folk-art painting on weathered board: three fluffy, midnight-black cats, one tall cat flanked by two smaller companions, gaze straight outward with enormous round amber-yellow eyes from a dense garden of tulips. Warm creamy sky, turquoise and leaf-green ground, candy-red, coral-pink, daffodil-yellow blossoms, and delicate white apple-blossom sprays frame them like joyful curtains. Keep the composition frontal, nearly symmetrical, charmingly flat, with thick confident outlines, simple shapes, lively hand-dabbed petals, visible matte brushwork, and a slightly imperfect handmade border. The mood is sunny, mischievous, and wholesomely strange; no photorealism, text, logos, or modern objects.

## [Video Prompt:](https://www.tiktok.com/@davelumai/video/7700787269161979167)

Create a vibrant, seamless 9:16 vertical folk-art animation lasting 8–10 seconds. On the opening beat, three fluffy black cats spring upward from a sudden explosion of red, yellow, and pink tulips, their enormous amber-yellow eyes snapping open in perfect synchronization. Their heads tilt independently as delicate white apple blossoms spiral through the air. The central cat performs one comically dignified blink while the two smaller cats bounce playfully to opposite sides. Flowers pulse and sway rhythmically, painted leaves flutter, and thick handmade outlines gently wobble with charming stop-motion energy. Use flat saturated colors, matte painted-board textures, a creamy background, and bold symmetrical composition. Add quick rhythmic push-ins and playful snap-zoom transitions, keeping the cats unmistakably hand-painted rather than realistic. Finish with the three cats returning to their original arrangement as a final shower of petals settles, creating a perfect seamless loop. Cheerful, quirky, visually irresistible, family-friendly, and full of personality. No text, logos, photorealism, or slow camera pans.

## Music Suggestions

**The Lovecats – The Cure**

Playful, eccentric, and wonderfully feline. Perfect for the synchronized blinking, suspicious head tilts, and general attitude of three cats who clearly believe they own the garden.

**Catgroove – Parov Stelar**

Bouncy electro-swing with infectious energy. An excellent match for flowers bursting into motion, quick zooms, and cats bouncing around with considerably more confidence than coordination.