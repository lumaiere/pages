# CS302 Episode 2: Parsing and Structure, or How Your Compiler Turns a Wall of Text Into Something It Can Reason About

Your compiler does not read code the way you do.

You glance at this:

    total = price + tax * 2

...and immediately see a variable named `total`, an assignment, some arithmetic, and the possibility that somebody is about to discover shipping costs.

The computer sees characters.

`t`

`o`

`t`

`a`

`l`

space

`=`

space

`p`

...

That is not yet a program.

It is text.

Before a compiler, interpreter, code editor, formatter, linter, or static analyzer can do much of anything useful with that text, somebody has to answer a surprisingly important question:

**What structure does this pile of characters represent?**

That job begins with **lexing** and **parsing**.

And once you understand those two ideas, a remarkable amount of programming-language machinery stops looking mysterious.

## Picking Up Where CS302 Episode 1 Left Off

In [CS302 Episode 1: What a Programming Language Is](https://medium.com/@DaveLumAI/cs302-episode-1-what-a-programming-language-is-or-more-than-syntax-less-than-religion-though-2be89ef1beb0), we separated **syntax** from **semantics**.

Syntax asks:

**Is this arranged according to the language's rules?**

Semantics asks:

**What does this arrangement mean?**

Episode 2 lives mostly on the syntax side.

Before a language implementation can decide what your program means, it first has to determine what your program **is**.

That distinction sounds philosophical until your compiler points at line 47 and says:

    SyntaxError: unexpected token

Then philosophy has entered the workplace.

## Continuity: You Have Already Been Using Grammar

You encountered programming-language grammar long before anyone called it grammar.

**From CS101:** [Episode 2: Variables and Conditionals](https://medium.com/@DaveLumAI/programming-fundamentals-part-1-variables-and-conditionals-aka-teaching-a-computer-to-stop-2d94ab24b91a) introduced things like assignments and `if` statements. [Episode 3: Loops and Functions](https://medium.com/@DaveLumAI/episode-3-loops-and-functions-or-how-to-stop-copy-pasting-yourself-into-madness-fac07f2d1bc4) added loops, function definitions, parameters, and calls.

Every one of those constructs has a grammatical structure.

**From CS102:** [Episode 11: Modular Design and Abstraction](https://medium.com/@DaveLumAI/episode-11-modular-design-and-abstraction-or-how-to-make-your-code-less-like-a-junk-drawer-9b6273bc3721) showed how programs become organized collections of meaningful pieces. [Episode 12: Testing and Reliability](https://medium.com/@DaveLumAI/episode-12-testing-and-reliability-or-why-it-worked-once-is-not-a-career-strategy-a50f80c8d6dc) pushed correctness further.

Parsing sits underneath both ideas.

A parser identifies the structure that later tools inspect, transform, test, compile, format, and complain about professionally.

## Step One: Characters Become Tokens

Suppose we start with:

    total = price + tax * 2

A **lexer**, also called a **scanner** or **tokenizer**, walks through those characters and groups them into meaningful units.

Conceptually, it might produce something like:

    IDENTIFIER("total")
    EQUALS("=")
    IDENTIFIER("price")
    PLUS("+")
    IDENTIFIER("tax")
    STAR("*")
    NUMBER("2")

Those units are called **tokens**.

A token usually has at least a **type** and the piece of source text that produced it.

The actual source text is often called a **lexeme**.

So in:

    customer_count

the lexeme is:

    customer_count

while its token category might simply be:

    IDENTIFIER

Likewise:

    42

might become:

    NUMBER

and:

    while

might become:

    WHILE

The lexer has converted raw characters into vocabulary the parser understands.

That is a big promotion for a semicolon.

## Keywords and Identifiers Are Awkward Neighbors

Consider these:

    if
    gift

The first contains the letters `i` and `f`.

The second also contains the letters `i` and `f`.

But `if` may be a reserved keyword while `gift` is just an identifier.

A lexer cannot simply shout "IF!" every time those two letters appear together.

It must recognize the entire lexeme and classify it according to the language's lexical rules.

This is why tokenization is more than splitting text on spaces.

This would be a spectacularly bad lexer:

    source.split(" ")

Programming languages contain operators, punctuation, strings, comments, numbers, escape sequences, keywords, identifiers, and situations where spaces are optional.

For example:

    x>=10

probably needs to become:

    IDENTIFIER("x")
    GREATER_EQUAL(">=")
    NUMBER("10")

not:

    IDENTIFIER("x")
    GREATER(">")
    EQUALS("=")
    NUMBER("10")

Lexers commonly use a principle sometimes called **maximal munch**: when multiple tokens could begin at the current position, prefer the longest valid token.

Because apparently even punctuation needs conflict-resolution procedures.

## What Happens to Whitespace?

That depends on the language.

In many languages:

    x = 10

and:

    x=10

produce essentially the same meaningful tokens.

Spaces mainly keep humans from developing headaches.

But whitespace is not universally irrelevant.

Python famously uses indentation to describe block structure:

    if temperature < 32:
        print("Cold")

The indentation is part of the language.

A Python tokenizer can effectively represent changes in indentation with tokens such as:

    INDENT
    DEDENT

That means "whitespace does not matter" is not a programming-language rule.

It is a language-design choice.

Comments are similar. The lexer often recognizes them so they do not confuse parsing, although tools may preserve them because formatters, documentation systems, IDEs, and source-to-source transformations still care about where they were.

## Tokens Still Are Not a Program

After lexing, we have a flat stream:

    IDENTIFIER
    EQUALS
    IDENTIFIER
    PLUS
    IDENTIFIER
    STAR
    NUMBER

Better than individual characters.

Still not enough.

Why?

Because structure matters.

Consider:

    price + tax * 2

Humans familiar with arithmetic interpret that as:

    price + (tax * 2)

not:

    (price + tax) * 2

The token stream alone does not visibly contain that hierarchy.

The parser has to construct it.

## Enter the Grammar

A programming-language **grammar** describes which arrangements of tokens are legal and how those arrangements are structured.

A tiny expression grammar might look something like this:

    expression → term (("+" | "-") term)*
    term       → factor (("*" | "/") factor)*
    factor     → NUMBER
               | IDENTIFIER
               | "(" expression ")"

Do not let the arrows make this look more ceremonial than it is.

Read the first rule as:

An `expression` consists of a `term`, possibly followed by additional `+` or `-` operations and more terms.

Then:

A `term` consists of a `factor`, possibly followed by `*` or `/` operations and more factors.

Finally:

A `factor` can be a number, an identifier, or another expression wrapped in parentheses.

That hierarchy gives multiplication tighter binding than addition.

So:

    price + tax * 2

naturally becomes:

    price + (tax * 2)

The precedence did not appear because the compiler remembered elementary-school arithmetic.

**The grammar encoded it.**

## Terminals, Nonterminals, and Productions

Formal grammars introduce a little vocabulary.

A **terminal** is something that ultimately appears in the token stream.

Examples:

    NUMBER
    IDENTIFIER
    "+"
    "*"
    "("
    ")"

A **nonterminal** is a grammatical category composed from other rules.

Examples:

    expression
    term
    factor

And a rule such as:

    factor → NUMBER

is called a **production**.

The left side says what kind of structure we are defining.

The right side says what may produce it.

Grammars become powerful because productions can refer to other productions, including recursively.

That is how a language can describe arbitrarily nested structures such as:

    calculate((a + b) * (c - d))

You do not need a grammar rule for nesting depth 1, another for depth 2, another for depth 3, and another for the programmer who has apparently declared war on readability.

Recursion handles the general case.

## A Brief Historical Detour That Actually Matters

During the 1950s, formal-language theory was developing mathematical ways to describe valid sequences and structures.

Noam Chomsky's work on formal grammars became highly influential in computer science, particularly the idea of **context-free grammars**.

Around the same era, John Backus and Peter Naur helped establish a notation for describing programming-language syntax that became known as **Backus-Naur Form**, or BNF, through the ALGOL work.

This mattered enormously.

Instead of defining a programming language with paragraphs like:

"Well, generally you can put an expression here, except sometimes when you cannot, and Gerald from the compiler team knows the details..."

language designers could describe syntax systematically.

Modern grammar notation has evolved in many directions, but the basic idea remains everywhere:

**Describe legal structures using formal rules.**

Your parser then tries to determine whether the token stream fits those rules.

## From Grammar to Parse Tree

Take:

    price + tax * 2

Using our little grammar, a parser could construct a tree resembling:

    expression
    ├── term
    │   └── factor
    │       └── IDENTIFIER: price
    ├── +
    └── term
        ├── factor
        │   └── IDENTIFIER: tax
        ├── *
        └── factor
            └── NUMBER: 2

This is a **parse tree**.

Notice what happened.

The original program was a line.

The resulting representation is hierarchical.

The multiplication is nested inside the second term.

The parser has recovered structure that was implicit in the text.

That structure is where things start getting interesting.

## Why Trees Show Up Everywhere

Programs naturally contain things inside other things.

A function contains statements.

An `if` statement contains a condition and branches.

A call contains arguments.

An arithmetic expression contains operands.

A class contains members.

A loop contains a body.

An array literal contains elements.

Nested structure practically begs to be represented as a tree.

Trees give compiler stages a way to reason about relationships rather than character positions.

Instead of asking:

"Is there a `*` somewhere around character 28?"

the compiler can ask:

"What are the left and right operands of this multiplication expression?"

That is an enormous improvement.

## Parse Tree Versus Abstract Syntax Tree

You will often hear another term:

**Abstract Syntax Tree**, or **AST**.

A parse tree tends to preserve much of the grammar's concrete structure.

An AST usually throws away details that later stages do not need.

For:

    price + tax * 2

a simplified AST might look like:

    Add
    ├── Name("price")
    └── Multiply
        ├── Name("tax")
        └── Number(2)

That is cleaner.

We no longer care that the grammar used categories called `expression`, `term`, and `factor`.

We care about what the source structurally represents:

Add this value to the result of multiplying those two values.

Parentheses may disappear from an AST once they have done their job of determining structure.

Commas may disappear.

Some punctuation disappears.

Certain keywords become node types.

The source code has begun turning into an internal model.

## Concrete Syntax Trees Still Have a Job

Do not conclude that "AST good, concrete syntax tree useless."

Different tools need different amounts of source detail.

A compiler may prefer a compact AST.

A formatter may care deeply about comments and punctuation.

An IDE may need precise source ranges.

A refactoring tool may need to preserve details that executable code generation does not care about.

Modern editor-oriented parsers can build concrete syntax trees and update them incrementally while you type.

That last part is especially important because source code inside an editor spends a surprising amount of time being invalid.

You type:

    calculate(

and for one brief moment the closing parenthesis does not exist.

Your editor cannot collapse in despair every time that happens.

It needs to keep useful structure even while the program is temporarily incomplete.

## How Does a Parser Actually Parse?

There is no single parsing algorithm ruling them all.

Several major families exist.

**Recursive-descent parsers** are written as functions that correspond closely to grammar rules. They are approachable, flexible, and popular in hand-written parsers.

**Pratt parsers** and **precedence-climbing techniques** are particularly elegant for expressions with many precedence levels.

**LL parsers** work from the top of the grammar downward while examining upcoming input.

**LR-family parsers** build structure from the input upward and can handle a broad class of grammars efficiently.

Parser generators can take a grammar description and generate much of the parsing machinery automatically.

Each approach involves tradeoffs.

Hand-written parsers can provide excellent control over diagnostics and language quirks.

Generated parsers can make the grammar itself a powerful source of truth.

Some parsing methods are easier to understand.

Others accept more complicated grammars.

Language implementation, like the language itself, is a pile of design choices pretending to be inevitable.

## A Tiny Recursive-Descent Parser

Our earlier grammar said:

    expression → term (("+" | "-") term)*

A hand-written parser for that rule might conceptually do this:

    parse_expression():
        left = parse_term()

        while next_token is "+" or "-":
            operator = consume_token()
            right = parse_term()
            left = BinaryExpression(operator, left, right)

        return left

Notice how directly the parser mirrors the grammar.

Then `parse_term()` handles multiplication and division.

`parse_factor()` handles numbers, identifiers, and parenthesized expressions.

Parsing is not magic.

It is disciplined pattern recognition over a token stream.

Once you see that, building a small parser becomes much less intimidating.

It is still very capable of ruining an afternoon, obviously. We are doing computer science, not aromatherapy.

## Ambiguity: When a Grammar Cannot Make Up Its Mind

Suppose we wrote this sloppy rule:

    expression → expression "+" expression
               | expression "*" expression
               | NUMBER

Now parse:

    2 + 3 * 4

There are at least two plausible structures:

    (2 + 3) * 4

and:

    2 + (3 * 4)

Different trees.

Different answers.

Same tokens.

That grammar is **ambiguous**.

Real language grammars need rules for precedence, associativity, or some other mechanism that resolves these choices.

Associativity answers another structural question.

For subtraction:

    10 - 5 - 2

we generally want:

    (10 - 5) - 2

because subtraction is normally left-associative.

Assignment in many languages behaves differently:

    a = b = 10

may be structured as:

    a = (b = 10)

That is right-associative.

Once again, these are not mysterious properties floating around operators.

They are language rules encoded into syntax and parsing behavior.

## Syntax Errors Are Parser Failures With Better Public Relations

Consider Python:

    if temperature < 32
        print("Cold")

Something is missing after the condition.

The parser reaches a point where the available tokens do not fit the grammatical structure it expects.

That is the essence of a syntax error.

A useful parser does more than announce:

    nope

It tracks source locations and expectations so it can say something closer to:

    expected ":" after condition

Good diagnostics are a genuine language-design feature.

Two parsers may reject the same malformed program while giving wildly different experiences to the programmer.

One tells you what happened.

The other gives you a message that sounds like an ancient curse discovered beneath `/usr/local/bin`.

## Error Recovery Is Harder Than Detecting the Error

Finding an error is one problem.

Continuing after it is another.

Suppose a parser sees one missing `)` near the top of a file.

If it simply loses track of structure, it may report 38 additional errors afterward.

Only the first one is real.

The rest are collateral damage.

Parsers therefore use **error recovery** strategies.

One common idea is synchronization: after detecting an error, skip ahead until reaching a token that looks like a reasonable boundary, such as the beginning of another statement or a closing delimiter.

Editor parsers may create explicit **error nodes** in the syntax tree so the rest of the file remains structurally useful.

This matters enormously in IDEs.

You want syntax highlighting, navigation, completion, and refactoring to keep functioning while you are halfway through typing something.

The parser needs to tolerate your code before your code is finished tolerating itself.

## A Real-World Example: Renaming a Function

Suppose a project contains:

    calculate_total(order)

You want an IDE to rename that function to:

    compute_total(order)

The dangerous approach is text replacement.

Search for:

    calculate_total

and replace every occurrence.

That might also change:

    "calculate_total"

inside a string.

Or:

    # calculate_total is retained for compatibility

inside a comment.

Or another identifier that merely contains the same characters.

A syntax-aware tool can operate on parsed structure.

It can identify nodes representing actual function declarations and references.

That is why parsing sits underneath sophisticated refactoring tools.

They are not merely searching text.

They are reasoning about structure.

## Formatters Also Need Structure

Consider:

    result=a+b*c

A formatter can space this nicely:

    result = a + b * c

But formatting gets far more complicated once expressions nest, function calls span lines, comments intervene, blocks appear, and language-specific conventions enter the picture.

A formatter benefits enormously from knowing:

"This is a binary expression."

"This is a function call."

"This is an argument list."

"This is a block."

Once code becomes structured data, tools can make decisions using syntax instead of guessing from punctuation.

## Why Regular Expressions Are Not Your Universal Parser

Regular expressions are excellent tools.

Lexers often rely on ideas closely related to regular languages.

Identifiers are easy to recognize with patterns.

Numbers can often be recognized with patterns.

Whitespace can be recognized with patterns.

But programming-language syntax contains recursive nesting:

    function_call(
        another_call(
            something_else()
        )
    )

That recursive structure is where full grammatical parsing becomes important.

Trying to parse an entire general-purpose programming language using a growing pile of regular expressions is one of those projects that begins with confidence and eventually produces a repository nobody is willing to delete.

Use the right abstraction.

Characters and token patterns are one problem.

Nested grammatical structure is another.

## Parsing Does Not Tell You Whether the Program Makes Sense

This program can be syntactically perfect:

    total = "banana" - customer

The parser may happily build a tree.

Whether subtracting `customer` from `"banana"` is legal is somebody else's problem.

That brings us toward **semantic analysis** and **type systems**, which are coming next in CS302.

Parsing answers:

**Does this have valid structure?**

Later stages ask questions such as:

**Does this identifier exist?**

**Can these types be combined?**

**Does this function receive the right number of arguments?**

**Is this operation legal here?**

And later still:

**What executable behavior should this structure produce?**

This separation between stages is one of the most important ideas in compiler design.

## Interpreted Languages Parse Too

Another common misconception is that parsing belongs only to compiled languages.

Nope.

Python source must be parsed.

JavaScript source must be parsed.

Ruby source must be parsed.

An interpreter still needs structured code before it can evaluate that code.

The eventual execution strategy may differ dramatically, but the language implementation still has to make sense of the program's syntax.

"Compiled" and "interpreted" do not mean "parsed" and "not parsed."

We will tackle that distinction directly later in this course.

## Parsing in Modern Editors

Parsing is no longer something that happens only after you press Build.

Modern development tools may parse continuously.

Every keystroke can trigger updates to a syntax tree.

That enables:

- syntax highlighting
- code folding
- navigation
- structural search
- symbol indexes
- automatic formatting
- linting
- refactoring
- autocomplete
- language-server features
- code analysis

Incremental parsing techniques avoid rebuilding everything from scratch when you change one character.

If line 8 changes, a good tool would prefer not to reconsider 70,000 unrelated lines merely because you added a comma.

That would be technically possible, but so is walking from Florida to California.

We generally try to improve on that.

## Parsing and AI-Generated Code

AI makes parsing more relevant, not less.

A language model generates **text**.

The programming environment needs **valid structure**.

If an AI assistant proposes a patch, one of the cheapest useful checks is:

**Does it parse?**

If not, there is little reason to begin deeper semantic analysis or run the full test suite.

Parsing can therefore become an early gate in an AI coding workflow:

    generated text
        ↓
    tokenize
        ↓
    parse
        ↓
    type-check or analyze
        ↓
    test
        ↓
    review
        ↓
    deploy

AI tools can also operate directly on syntax trees.

Instead of asking an agent to replace some text that vaguely resembles a function, tooling can identify a specific function declaration, inspect its body, insert a node, transform the tree, and regenerate valid source.

That is a much stronger foundation for automated code modification than glorified search-and-replace.

The AI may be probabilistic.

The grammar does not need to be.

## Failure Modes Worth Remembering

A few parsing mistakes show up repeatedly.

**Mistaking tokens for structure**

A token stream tells you what pieces exist, not necessarily how they relate.

**Using an ambiguous grammar**

If the same token sequence produces multiple valid structures, something must disambiguate it.

**Ignoring precedence and associativity**

Arithmetic and logical expressions can acquire completely different meanings.

**Stopping after the first malformed character**

Useful developer tooling needs good error recovery, not merely error detection.

**Assuming every valid parse is a valid program**

Parsing checks syntax. It does not prove sensible types, correct behavior, security, or good judgment.

**Treating syntax as decoration**

Syntax determines structure, and structure controls what later compiler stages receive.

A brace is small.

Its employment responsibilities are enormous.

## The Bigger Compiler Picture

We can now start seeing the larger pipeline:

    Source characters
        ↓
    Tokens
        ↓
    Parsed structure
        ↓
    Semantic analysis
        ↓
    Intermediate representations
        ↓
    Optimization
        ↓
    Code generation or execution

Real implementations vary.

Some stages overlap.

Some produce multiple intermediate forms.

Some interpreters walk syntax trees directly.

Some compilers lower code through several representations before reaching machine instructions.

But the conceptual progression matters.

Each stage turns the program into a representation better suited to the next question.

The parser's contribution is fundamental:

**It turns linear text into structured syntax.**

## The Mental Model to Keep

When you see:

    if score >= 90:
        print("A")

you see an `if` statement immediately.

A language implementation has to earn that understanding.

First, characters become tokens.

Then tokens are matched against grammar.

Then hierarchical structure is constructed.

Only after that can later stages start asking deeper questions about names, types, values, control flow, optimization, or execution.

That is parsing.

Not merely checking punctuation.

Not merely finding syntax errors.

It is the transformation that turns source code from text into something software can reason about.

And once your code has become a tree, an enormous amount of compiler technology suddenly has somewhere to stand.

Next up in CS302 is **Type Systems and Meaning**, where we finally get to ask a parser-approved program the uncomfortable follow-up question:

"Fine. You are grammatically legal. But do you make any sense?"

Follow along for the next episode, and drop a comment with the strangest syntax error you have ever received. Bonus points if the error was technically correct and still made you question every decision that led you to programming.

## For the Visuals

**[Art Prompt (Dadaism):](https://lumaiere.com/?gallery=dadaism)**

A bold painted-wood relief composed of overlapping biomorphic forms floating against an immaculate pale background, with irregular rounded silhouettes layered at different depths like strange botanical organisms discovered in an impossible garden. Use vivid vermilion red, hot pink, mustard yellow, leaf green, matte black, and small flashes of crisp white, keeping each color in a flat, sharply bounded plane with visible physical thickness at the edges. Arrange the forms asymmetrically so that one large uneven oval anchors the composition while smaller branching, seed-like, and almost figure-like shapes overlap it without becoming literal objects. Preserve the playful irrationality and organic abstraction of early Dada, balancing chance-like placement with surprisingly elegant visual rhythm. Use subtle shadows cast by the raised wooden layers to emphasize depth, but keep the surface handcrafted, direct, cheerful, mysterious, and slightly absurd. No scraps of paper, readable text, logos, recognizable people, or modern objects.

## Bring It to Life

**[Video Prompt:](https://www.tiktok.com/@davelumai/video/7676068050952768798)**

Open instantly with the brightly colored biomorphic wooden forms snapping outward from the center in rapid rhythmic layers, each red, pink, yellow, green, black, and white shape rotating a few degrees and locking into place with satisfying physical momentum. Let raised pieces briefly detach from the background, cast crisp moving shadows, slide past one another, bounce gently at their limits, and reorganize into a series of playful abstract configurations before returning toward the original composition. Add quick pulses of scale, sudden synchronized pivots, and one dramatic moment where the entire layered relief seems to inhale outward and contract again. Keep the pale background fixed and clean while the colorful forms supply all the motion. Preserve the handcrafted painted-wood texture and early Dada sense of playful irrationality. End with the shapes snapping precisely back into the opening arrangement so the video loops seamlessly for short-form platforms. No readable text, logos, recognizable people, or modern objects.

## Soundtrack

**Song recommendations:**

Get Innocuous! - LCD Soundsystem  
Inspector Norse - Todd Terje