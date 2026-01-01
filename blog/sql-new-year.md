# Episode 8: SQL, the Language Your Data Already Trusts (Plus a Happy 2026)

If you have ever yelled, “WHERE DID THAT NUMBER COME FROM?” at a spreadsheet, a dashboard, or a coworker, congratulations: you are emotionally ready for SQL.

SQL is the reason your bank balance loads, your online cart remembers your impulse purchases, and your streaming service somehow knows you are about to rewatch the same comfort show for the fifth time.

Also yes, it is Episode 8 in this top-languages tour, which means we have officially arrived at the part of the series where the real world shows up wearing a sensible blazer and holding a clipboard.

And since we are also rolling into 2026: Happy New Year. May your queries be fast, your joins be correct, and your production database never meet your “just testing something real quick” energy.

## What is it?

SQL (Structured Query Language) is a language for talking to relational databases.

Not “talking” like a heartfelt conversation.

More like: “I have questions. You have rows. Answer me.”

You use SQL to:

* pull data out (SELECT)
* put data in (INSERT)
* change it (UPDATE)
* remove it (DELETE)
* and occasionally stare into the void with a 7-table JOIN and wonder what led you here

## Is it still relevant?

SQL is still relevant in the same way gravity is still relevant.

You can ignore it, but you will do so briefly and with consequences.

Even if your company swears it is “all NoSQL now,” there is usually a SQL-shaped machine behind the curtain doing the actual work. Or at least storing the boring, important parts: payments, users, orders, and the list of everyone who should not have admin access but definitely does.

## Pros and cons (strengths, weaknesses, and mild emotional damage)

**Pros**

* It is a universal skill. SQL transfers across databases and industries.
* It scales from “show me yesterday’s sales” to “power the analytics stack for a small nation.”
* It is declarative: you say what you want, not how to do it. The database figures out the plan.
* It plays beautifully with reporting, BI tools, ETL pipelines, and modern data platforms.

**Cons**

* Small mistakes can have big consequences. One missing WHERE clause and your week gets spicy.
* Performance tuning is its own hobby. Indexes exist because reality is cruel.
* Dialects differ. SQL is a “language family,” and some cousins are… opinionated.
* Debugging complex queries can feel like untangling holiday lights with oven mitts.

## What is it used for?

SQL shows up everywhere:

* backend apps that store user data
* analytics and dashboards
* data warehouses and lakehouses
* migrations and schema management
* ad tech, fintech, ecommerce, healthcare, logistics, gaming, and basically anything that has “data” and “problems”

## Who invented it? What is its history?

SQL began at IBM in the 1970s, originally influenced by the relational model work of Edgar F. Codd. The early language was called SEQUEL (because tech loves a cute acronym) and evolved into what became SQL.

Then it spread everywhere because it solved a real problem: “How do we ask sensible questions of a giant pile of structured data without writing custom code for every question?”

## How popular is it? Is it going up or down?

SQL’s popularity is weird because it is both:

1. extremely popular, and
2. often used by people who do not brag about it

It is not the loudest language in the room, but it is usually the one paying the rent.

If you want a quick snapshot of how widely it is used by working developers, the Stack Overflow survey is a solid thermometer: **[Stack Overflow Top languages](https://survey.stackoverflow.co/2025/technology?utm_source=substack&utm_medium=email#1-programming-scripting-and-markup-languages)**.

Trend-wise: SQL fluctuates on indexes depending on what they count and how they count it, but the real story stays the same. As long as businesses store structured data (spoiler: forever), SQL remains employed.

## What companies use it the most?

The short answer: all of them.

The slightly longer answer: any company with users, money, inventory, events, logs, analytics, or a CEO who likes dashboards.

So yes: Big Tech, banks, retailers, hospitals, airlines, and that startup whose entire business model is “a form that writes to a database.”

## Is it similar to anything else? What are the alternatives?

SQL is the main language for relational databases, but alternatives pop up depending on the job:

* **NoSQL query languages** for document stores (more “JSON-shaped” thinking)
* **Graph queries** for relationships and networks (think nodes and edges)
* **Search queries** for full-text search engines
* **Dataframe-style APIs** for analysis (great, until you need to operationalize it)

None of these replace SQL everywhere. They mostly replace it in specific niches, while SQL stays in the foundation like the concrete you forget exists until it cracks.

## Does it work well with AI?

Yes, and the combo is getting better.

AI is great at turning human intent into a first draft of a query (“Show me churn by cohort over the last 90 days”), and SQL is great at making that intent real.

The practical reality: you still want guardrails. AI can generate SQL confidently while being completely wrong, which is honestly very on-brand for all of us in week one of January.

But for analytics helpers, internal tools, and “translate questions into queries” workflows, SQL is one of the best places to apply AI because the output is testable. Either the query runs and the results make sense… or it does not, and you fix it.

## What tech stack does it work with?

SQL plays well with basically every modern stack:

* backend frameworks (APIs)
* ORMs (when you want nicer ergonomics)
* analytics platforms
* batch jobs and schedulers
* notebooks
* streaming pipelines that eventually land in tables anyway

## What tools work best with it?

* A good database client (for exploring and sanity-checking)
* Schema migration tools (so changes are tracked and repeatable)
* Observability and query monitoring (so slow queries do not quietly ruin your life)
* An editor that does SQL formatting and linting (because readable SQL is a love language)

## How much is it going to cost me?

SQL itself costs you nothing except time and the occasional dramatic sigh.

The cost comes from the database you choose:

* many options are free to start
* hosted solutions charge for compute, storage, and bandwidth
* enterprise vendors charge for everything, including your optimism

The good news: for most personal projects and early products, you can run SQL-backed databases cheaply and scale later.

## Can you give me an example?

Here is the kind of SQL that actually gets used in the wild: clear, practical, and slightly judgmental about missing data.

```sql
-- Create a table
CREATE TABLE orders (
  id            INTEGER PRIMARY KEY,
  customer_id   INTEGER NOT NULL,
  total_usd     DECIMAL(10, 2) NOT NULL,
  created_at    TIMESTAMP NOT NULL
);

-- Ask a real business question:
-- "What are total sales by day for the last 7 days?"
SELECT
  DATE(created_at) AS day,
  SUM(total_usd)   AS total_sales
FROM orders
WHERE created_at >= NOW() - INTERVAL '7 days'
GROUP BY DATE(created_at)
ORDER BY day;
```

That is SQL at its best: direct, readable, and immediately useful.

## Is SQL the subject of any famous art?

Not in the “museum has a velvet rope around it” sense.

But conceptually? SQL is pure composition: structure, balance, repetition, relationships, and contrast. It is the art of asking the right question and not lying to yourself about the answer.

Also, there is an entire genre of modern art called “dashboard screenshots,” and SQL is the paint under that paint.

## Any other interesting tidbits?

* SQL is one of the fastest “career ROI” skills you can pick up. You start useful, quickly.
* The best SQL writers think like editors: name things clearly, format consistently, and avoid cleverness unless it pays rent.
* Most SQL bugs are not “syntax” bugs. They are “logic” bugs. Your query ran. It just told you a beautiful lie.

## 2026 wishes (the fun part)

Here is to 2026: the year you ship more, panic less, and finally stop treating your production database like a public sandbox.

May your year be filled with:

* calm focus
* bold creativity
* gentle ambition
* and the rare, sacred joy of a query that runs on the first try

If you want to see what I am building and make the algorithm do a little happy dance, check out **[LumAIere.com](https://lumaiere.com/)** and grab something you like from the shop at **[Redbubble](https://www.redbubble.com/people/DaveLumAI/explore?page=1&sortOrder=recent)**.

And hey: follow along and drop a comment with your most ridiculous SQL moment. Bonus points if it involves a missing comma, a mysterious NULL, or a JOIN that turned your dataset into a small galaxy.

**[Art Prompt (Minimalism):](https://lumaiere.com/?gallery=minimalism)**
A serene minimalist composition on a tall canvas, built from an almost-white field with whisper-thin horizontal pencil lines forming a delicate grid that feels hand-drawn and human. Subtle bands of pale gray and faint icy-blue wash drift across the surface like quiet weather, barely there yet unmistakably present. The texture suggests layered gesso and soft paper grain, with tiny imperfections that make the geometry feel alive rather than mechanical. The mood is contemplative and hushed, like standing in a silent room where the light changes so slowly you only notice it after you blink.

**[Video Prompt:](https://www.tiktok.com/@davelumai/video/7589844676102950174)**
Create a crisp, hypnotic short sequence based on an ultra-minimal grid painting on a tall canvas. Start with a quick, clean reveal: the near-white surface snaps into focus as hairline horizontal lines shimmer into visibility. Animate the grid subtly as if the paper is breathing: micro-waves pass through the pencil lines, soft bands of pale gray and icy-blue drift diagonally like slow-moving weather, and the surface texture catches light in tiny sparkles of grain. Use rhythmic, snappy cuts between close-ups of line intersections, soft gradient swells, and wide shots where the entire canvas seems to pulse with calm energy. Add a gentle parallax effect that makes the grid feel deep and tactile, with occasional flicker-like glints as if the graphite is catching a studio lamp. Keep it mesmerizing, clean, and loopable, with motion that feels precise but soothing.

**Song Recommendations:**

* “Aruarian Dance” – Nujabes
* “Rose Rouge” – St Germain
