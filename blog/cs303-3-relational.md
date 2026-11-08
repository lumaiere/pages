# CS303 Episode 2: Relational Thinking, or How to Organize Your Data Before It Organizes Your Suffering

There comes a moment in every programmer's life when a perfectly innocent-looking spreadsheet starts behaving like a small, poorly governed nation.

At first, everything is fine.

You have customers. Products. Orders. Maybe a few events. You put everything into one enormous table because it seems convenient.

Then someone changes their email address.

You update it in one place.

Unfortunately, their email address appears in seventeen other places.

Now your database contains eighteen versions of the truth, three of which are misspelled, two of which belong to someone else, and one of which is apparently a phone number.

Congratulations.

You have discovered why relational database design exists.

Welcome to **CS303 Episode 2: Relational Thinking**, where we learn that organizing information is not merely about making tables look tidy.

It is about making information trustworthy, understandable, and remarkably resistant to the creative destruction of future programmers.

Including ourselves.

Especially ourselves.

---

## Where We Left Off: From Remembering Things to Understanding Them

In [CS303 Episode 1: Why Databases Exist](https://medium.com/@DaveLumAI/cs303-episode-1-why-databases-exist-or-because-text-files-eventually-become-a-cry-for-help-8fa9d958625b?sharedUserId=DaveLumAI), we explored why applications need persistent storage.

Programs have temporary memory. Files can preserve information. Databases provide mechanisms for managing information reliably across applications, users, and time.

But persistence alone is not enough.

A database can preserve terrible information perfectly.

It can reliably remember that a customer's address is wrong, that an order belongs to a nonexistent customer, or that someone bought 300 tickets to an event with twelve seats.

The database may be functioning beautifully.

Your business, somewhat less so.

Relational thinking addresses a different question:

**How should we represent information so that its structure reflects the actual relationships and rules of the world?**

This connects directly to earlier material.

In **CS101**, [Episode 5: Data Structures](https://medium.com/@DaveLumAI/episode-5-data-structures-putting-things-somewhere-so-you-can-find-them-again-51483812ac35) introduced the importance of organizing information in useful ways.

In **CS102**, [Episode 10: Files, Input, and Output](https://medium.com/@DaveLumAI/episode-10-files-input-and-output-or-how-programs-stop-living-entirely-inside-their-own-heads-941dc13d407d) showed how programs interact with information beyond their own execution.

And in **CS102**, [Episode 12: Testing and Reliability](https://medium.com/@DaveLumAI/episode-12-testing-and-reliability-or-why-it-worked-once-is-not-a-career-strategy-a50f80c8d6dc) reminded us that correct behavior must be demonstrated rather than assumed.

Now we combine those ideas.

We want information that persists, has meaningful structure, and follows rules the system can enforce.

That brings us to one of the most influential ideas in computer science.

The relational model.

## A Brief History: When Edgar Codd Decided Databases Needed Mathematics

Before relational databases became popular, many database systems used hierarchical or network-based structures.

Data could be connected through predefined paths and pointers.

These systems were useful, but accessing information frequently required knowing how it was physically or logically arranged.

Imagine asking a librarian for every book borrowed by customers living in Florida.

Instead of answering, the librarian hands you a floor plan, a flashlight, and instructions for navigating the basement.

That was roughly the kind of complexity early database programmers could face.

In 1970, IBM researcher **Edgar F. Codd** published a groundbreaking paper titled *A Relational Model of Data for Large Shared Data Banks*.

Codd proposed a mathematical approach to representing information using relations.

A relation is a set of tuples defined over attributes.

Yes, that sentence sounds like mathematics has just entered the room wearing a tie.

Let us translate.

- **Relation:** Conceptually, a table.
- **Tuple:** A row in that table.
- **Attribute:** A named property, represented by a column.
- **Domain:** The set of permitted values for an attribute.

The important idea was not simply that databases could display tables.

It was that information could be represented and manipulated through a logical mathematical model without requiring applications to know exactly where or how the database stored it.

That separation between logical meaning and physical storage became enormously important.

The original work eventually influenced IBM's System R project, SQL, and the relational databases that power much of today's software.

You can explore [Codd's contribution to database history at IBM](https://www.ibm.com/history/edgar-codd).

His legacy is extraordinary.

He helped turn database management from a collection of implementation-specific techniques into something grounded in mathematical principles.

Which is impressive considering most of us still struggle to agree on how to name a variable.

## The Basic Ingredients: Rows, Columns, and Tables

Let us start with a tiny fictional university.

We have students.

| student_id | full_name | email |
|---|---|---|
| 101 | Alice Chen | alice@example.com |
| 102 | Bob Rivera | bob@example.com |
| 103 | Carol Singh | carol@example.com |

This is a table called `Students`.

Each row represents one student.

Each column describes one property of a student.

Simple.

Now suppose we have courses.

| course_id | course_name | credits |
|---|---|---|
| 201 | Databases | 3 |
| 202 | Algorithms | 4 |
| 203 | Computer Architecture | 3 |

That is our `Courses` table.

Already we have made an important modeling decision.

Students and courses are different kinds of things.

A student exists independently of any particular course.

A course exists independently of any particular student.

This distinction is the beginning of relational thinking.

**Instead of putting every fact into one enormous record, we identify the different things our system needs to represent.**

Database designers usually call these things *entities*.

An entity might be a student, customer, product, event, invoice, employee, or shipment.

An entity is not necessarily a physical object.

An appointment is an entity.

A subscription is an entity.

A financial transaction is an entity.

Even a relationship can become an entity when it has information of its own.

We will see why shortly.

### The important difference between a table and a spreadsheet

A spreadsheet is often organized visually.

People depend on row positions, column positions, formatting, and sometimes cells colored bright yellow for reasons nobody remembers.

A relational table has different expectations.

The information is described by its attributes and values.

In the underlying relational model:

- Rows are not inherently ordered.
- Columns have names and defined domains.
- Duplicate tuples are not part of a mathematical relation.
- Relationships are based on values rather than the visual position of cells.

Real SQL databases add some practical complications.

SQL tables can contain duplicate rows unless suitable constraints prevent them, and SQL supports `NULL`, which does not behave like an ordinary value in classical relational theory.

Also, a SQL query without an explicit `ORDER BY` does not guarantee any particular row order.

The fact that your database returned Alice before Bob yesterday does not mean it has signed a legally binding commitment to keep doing so.

**A relational database is about the meaning and organization of information, not where records happen to appear on the screen.**

## Keys: Giving Every Row a Reliable Identity

Our students have names.

Why not use the student's name to identify them?

Because somewhere in the world there are two people named John Smith.

Possibly several thousand.

And they are not required to coordinate their university enrollment schedules.

A database needs reliable ways to distinguish records.

Enter the key.

### Primary keys

A **primary key** is a column, or combination of columns, chosen to uniquely identify each row in a table.

In our `Students` table:

`student_id`

is the primary key.

Two students cannot have the same primary key value.

A primary key also cannot be `NULL`.

That means the database can distinguish Alice from every other student regardless of whether her name, email address, or hairstyle changes.

A primary key establishes identity.

It does not necessarily describe the person.

### Natural keys versus surrogate keys

A **natural key** uses information that already has business meaning.

For example, a course code such as `CS303` might identify a course within a particular university.

A **surrogate key** is an identifier created primarily for the database.

For example:

`student_id = 101`

Neither approach is universally superior.

Natural keys can express meaningful business rules and sometimes eliminate unnecessary identifiers.

But real-world identifiers can change, become reused, contain errors, or turn out not to be as unique as everyone confidently promised.

Surrogate keys give the database a stable internal identifier.

However, they do not automatically enforce business uniqueness.

Suppose two customer records have different numerical IDs but the same external customer number.

The surrogate primary key allows both records.

If the external customer number must be unique, the database still needs a separate uniqueness constraint.

**A technical identifier is not a replacement for understanding the business rules.**

### Candidate keys and composite keys

A **candidate key** is a minimal set of attributes capable of uniquely identifying a row.

One candidate key is selected as the primary key.

Others may be enforced through uniqueness constraints.

A **composite key** uses more than one column.

For example:

`(student_id, course_id)`

could identify a student's enrollment in a course, assuming the system allows only one enrollment per student per course.

Neither column is unique by itself.

Together, they are.

Composite keys are particularly useful when the identity of a record naturally depends on a combination of things.

And that leads to relationships.

## Relationships: Because Nothing Exists in Complete Isolation

Students take courses.

Customers place orders.

Employees belong to departments.

Products appear on invoices.

Events take place at venues.

These are not just collections of unrelated facts.

They describe how entities interact.

Relational database design usually distinguishes three important relationship patterns.

### One-to-one relationships

One record is associated with at most one record on the other side.

For example, a university might store optional confidential student profile information separately from its general student records.

Each student can have at most one confidential profile.

Each profile belongs to exactly one student.

A database can enforce this by using `student_id` as both the primary key and a foreign key in the profile table.

Why separate the information?

Perhaps it has different access controls, retention requirements, or operational responsibilities.

Not every one-to-one relationship deserves a separate table.

Splitting tables merely because you enjoy having more tables is not database architecture.

It is interior decorating.

### One-to-many relationships

One record can relate to several records in another table.

Imagine departments and employees.

One department may have many employees.

Each employee belongs to one department under our simplified business rule.

The employee record can contain a `department_id` identifying its department.

This is one-to-many.

It is among the most common patterns in relational databases.

### Many-to-many relationships

Now things become interesting.

One student can take many courses.

One course can contain many students.

That is many-to-many.

We cannot correctly represent this simply by putting one `course_id` into each student record.

Alice could then enroll in only one course.

Which would make getting a degree unusually convenient, but rather academically disappointing.

We also should not create columns like:

`course_1`, `course_2`, `course_3`, `course_4`

What happens when someone takes a fifth course?

Do we add another column?

Do we tell them education has reached its structural limit?

No.

We create a relationship table.

## The Junction Table: Small Idea, Enormous Payoff

Our new table is called `Enrollments`.

| student_id | course_id | enrolled_at | grade |
|---|---|---|---|
| 101 | 201 | 2026-08-20 | A |
| 101 | 202 | 2026-08-20 | B |
| 102 | 201 | 2026-08-21 | A |
| 103 | 203 | 2026-08-22 | B |

Notice something important.

The enrollment is not merely a pointer between a student and a course.

It is a meaningful record in its own right.

It has an enrollment date.

It may have a grade.

It could eventually have a status, academic term, completion date, or withdrawal reason.

The relationship itself carries information.

That is why junction tables are so useful.

They turn a many-to-many relationship into two one-to-many relationships.

Conceptually:

**Students → Enrollments ← Courses**

Each enrollment belongs to one student.

Each enrollment belongs to one course.

But each student can have many enrollments, and each course can have many enrollments.

This is a simple example of a **relational schema**, the blueprint describing tables, their attributes, and the constraints connecting them.

### What if students repeat a course?

Excellent question.

Our composite key `(student_id, course_id)` assumes that Alice cannot enroll in the same course twice.

But universities routinely allow students to repeat courses.

Now our original rule is too restrictive.

We might introduce a `course_offering_id` representing one specific course offering during a particular term.

Then an enrollment connects a student to that offering.

Or we might introduce a dedicated `enrollment_id` and enforce appropriate uniqueness rules separately.

The point is not that one key design always wins.

The point is that **the key must reflect what the business considers a distinct record**.

Database design is full of seemingly tiny decisions that eventually decide whether your software behaves like a disciplined system or an elaborate practical joke.

## Foreign Keys: Enforcing the Relationships

A primary key identifies a record.

A **foreign key** connects records while enforcing a relationship.

In `Enrollments`, the `student_id` column references `Students.student_id`.

Similarly, `course_id` references `Courses.course_id`.

If someone tries to enroll student 999, but student 999 does not exist, the database can reject the operation.

That is **referential integrity**.

It prevents references to records that do not exist.

Foreign keys make it much harder to create orphaned records.

Consider the difference.

Without a foreign key, the application might accidentally create an enrollment for a student who was never entered into the system.

With a properly enforced foreign key, the database can detect the violation regardless of which application, script, API, or distracted administrator attempts the operation.

This matters because applications are not the only things that modify databases.

Imports happen.

Administrative scripts happen.

Background jobs happen.

Emergency fixes happen.

AI-generated code happens.

And occasionally somebody with production access decides that Friday afternoon is an excellent time to improvise.

A database constraint provides protection at a level shared by all those operations.

You can explore how these mechanisms work in the [PostgreSQL documentation on constraints](https://www.postgresql.org/docs/current/ddl-constraints.html).

### A small SQL example

We will explore SQL properly in Episode 3, but a little preview helps show how relational thinking becomes executable structure.

Here is our university model expressed using SQL:

~~~sql
CREATE TABLE Students (
    student_id BIGINT PRIMARY KEY,
    full_name VARCHAR(150) NOT NULL,
    email VARCHAR(320) NOT NULL UNIQUE
);

CREATE TABLE Courses (
    course_id BIGINT PRIMARY KEY,
    course_name VARCHAR(150) NOT NULL,
    credits INTEGER NOT NULL
        CHECK (credits > 0)
);

CREATE TABLE Enrollments (
    student_id BIGINT NOT NULL,
    course_id BIGINT NOT NULL,
    enrolled_at DATE NOT NULL,
    grade VARCHAR(2),

    PRIMARY KEY (student_id, course_id),

    FOREIGN KEY (student_id)
        REFERENCES Students(student_id),

    FOREIGN KEY (course_id)
        REFERENCES Courses(course_id)
);
~~~

Look at what this design establishes.

- Every student has a unique identity.
- Every course has a unique identity.
- Student email addresses must be present and unique under the database's configured comparison rules.
- A course must have a positive credit value.
- Every enrollment references an existing student and course.
- The same student-course combination cannot appear twice.

We have encoded important assumptions about the university directly into the database.

That is much stronger than placing a comment in application code saying:

"Please do not create invalid enrollments."

A comment expresses hope.

A constraint enforces a rule.

There is another subtle lesson here.

A foreign key can be optional if its column permits `NULL`. In this example, we explicitly require non-null references because an enrollment without a student or course would make little sense.

And `NULL` is not the same thing as zero, an empty string, or a missing record.

Our nullable `grade` might mean the grade has not been assigned yet.

Those distinctions matter when designing systems that must represent incomplete information.

## Entity-Relationship Modeling: Drawing the System Before Building It

Before writing SQL, database designers often create an **Entity-Relationship Diagram**, or ERD.

An ERD identifies the entities in a system and the relationships between them.

Think of it as planning the building before hiring a construction crew.

Except the building has foreign keys, and the construction crew sometimes deploys on Friday.

In an ERD, we might represent:

- `Student` as an entity.
- `Course` as an entity.
- `Enrollment` as the association between them.
- The attributes belonging to each entity.
- The cardinality and optionality of each relationship.

**Cardinality** describes how many records may participate in a relationship.

**Optionality** describes whether participation is required.

For example:

A course may have zero or many enrollments.

Every enrollment must reference exactly one course.

A student may have zero or many enrollments.

Every enrollment must reference exactly one student.

Those are different rules.

And the difference matters.

If we incorrectly require every course to have enrolled students, we might prevent the university from creating courses before registration opens.

The database would be technically consistent with its constraints.

It would also be operationally ridiculous.

That is why database modeling requires conversations with people who understand the actual business.

A beautifully drawn ERD based on incorrect assumptions is still incorrect.

It just looks more professional during meetings.

## Normalization: Teaching Data to Stop Repeating Itself

Now we arrive at the part of database design that sounds intimidating but solves a very familiar problem.

**Normalization** is the process of organizing relations to reduce problematic redundancy and avoid certain kinds of data anomalies.

In plain English:

Stop storing the same independent fact in seventeen places when you can store it once and refer to it.

Consider this table:

| order_id | customer_name | customer_email | product_name | quantity |
|---|---|---|---|---|
| 5001 | Alice Chen | alice@example.com | Laptop | 1 |
| 5002 | Alice Chen | alice@example.com | Mouse | 2 |
| 5003 | Alice Chen | alice@example.com | Monitor | 1 |

Notice Alice's name and email repeated in every order.

What happens when she changes her email address?

We have to update multiple records.

If we miss one, our data becomes inconsistent.

This is called an **update anomaly**.

There are two other classic problems.

### Insertion anomalies

Suppose our database stores customer details only inside order records.

How do we add a customer who has not placed an order yet?

We might have to create a fake order just to preserve the customer information.

That is an insertion anomaly.

The structure prevents us from representing a legitimate fact independently.

### Deletion anomalies

Suppose Alice's only order is deleted.

If her customer information exists nowhere else, deleting that order also destroys her customer details.

We intended to delete an order.

Instead, we accidentally deleted a customer.

This is a deletion anomaly.

Not exactly the kind of bonus feature anyone requested.

### The normalized alternative

Separate customers from orders.

**Customers**

| customer_id | name | email |
|---|---|---|
| 101 | Alice Chen | alice@example.com |

**Orders**

| order_id | customer_id | order_date |
|---|---|---|
| 5001 | 101 | 2026-10-01 |
| 5002 | 101 | 2026-10-03 |
| 5003 | 101 | 2026-10-04 |

Now Alice's current email address is maintained in one customer record.

Orders reference her customer identity.

Changing her email no longer requires updating every historical order.

And deleting an order does not automatically delete the customer.

That is the central benefit of normalization.

**Each fact should be represented in the place where it logically belongs.**

Of course, the business may legitimately need to preserve the email address used for an individual transaction.

In that case, a historical snapshot belongs in the appropriate transaction record.

That is not accidental redundancy.

That is a deliberate business requirement.

The distinction is crucial.

## The Normal Forms: First, Second, and Third

Database normalization has several formal levels called **normal forms**.

They come from the mathematical study of relations and functional dependencies.

A functional dependency describes a relationship such as:

`student_id → full_name`

Meaning that, within our intended data model, a particular student ID determines one student name at a given point in time.

Understanding dependencies helps us recognize when a table combines facts that belong to different entities.

For an introductory database course, three normal forms deserve special attention.

### First Normal Form: One Value Per Attribute

**First Normal Form (1NF)** requires a relational representation with atomic attribute values appropriate to their domains, rather than repeating groups or collections of independent values stuffed into one attribute.

Imagine this:

| student_id | name | courses |
|---|---|---|
| 101 | Alice | CS101, CS102, CS303 |

The `courses` column contains several course identifiers packed into one field.

That makes relationships harder to query and enforce.

What if Alice drops CS102?

What if we need every student enrolled in CS303?

What if we need to ensure all listed courses actually exist?

We have turned one attribute into a miniature undocumented data format.

A better relational representation uses our separate `Enrollments` table.

Notice that *atomic* does not mean every value must be physically indivisible.

A date can be stored as one date value.

An address may sometimes be represented as one value, or divided into street, city, region, and postal code if the system needs those components separately.

Atomicity depends on the domain and what the application needs to treat as an individual value.

1NF is not a command to dismantle every string into individual characters.

Please do not create seventeen tables to represent someone's first name.

### Second Normal Form: Depend on the Whole Key

**Second Normal Form (2NF)** builds on 1NF and addresses partial dependencies on candidate keys.

This becomes particularly visible with composite keys.

Imagine an enrollment table:

| student_id | course_id | student_name | course_name | grade |
|---|---|---|---|---|
| 101 | 201 | Alice | Databases | A |
| 101 | 202 | Alice | Algorithms | B |

Suppose `(student_id, course_id)` identifies each enrollment.

The `grade` depends on the entire combination.

It belongs to the student's enrollment in that specific course.

But `student_name` depends only on `student_id`.

And `course_name` depends only on `course_id`.

Those facts belong in their respective entity tables.

2NF helps us separate them.

The formal rule concerns non-prime attributes depending on proper subsets of candidate keys.

A practical way to remember it is:

**If a fact describes only part of a composite identity, it probably belongs somewhere else.**

For tables whose candidate keys are all single attributes, partial-key dependencies are not an issue.

### Third Normal Form: Avoid the Dependency Chain

**Third Normal Form (3NF)** addresses additional dependencies that can create redundancy.

Suppose we store:

| employee_id | employee_name | department_id | department_name |
|---|---|---|---|
| 501 | Alice | 10 | Engineering |
| 502 | Bob | 10 | Engineering |
| 503 | Carol | 20 | Finance |

Here:

`employee_id → department_id`

And:

`department_id → department_name`

The department name depends on the department identifier, not directly on the employee's identity as a separate business fact.

If Engineering becomes Product Engineering, we must update multiple employee records.

Instead, create:

**Employees**

`employee_id, employee_name, department_id`

**Departments**

`department_id, department_name`

Now the department name is maintained in one appropriate place.

The formal definition of 3NF uses functional dependencies and candidate keys, with special treatment for prime attributes. The simple dependency-chain example captures the most common practical problem without pretending that the full mathematics is quite that short.

A useful beginner's memory aid is:

- **1NF:** Represent attributes cleanly without repeating groups.
- **2NF:** Eliminate inappropriate dependencies on part of a candidate key.
- **3NF:** Eliminate inappropriate dependencies between non-key facts.

These are teaching shortcuts, not complete mathematical definitions.

But they are excellent starting points.

And no, there are not just three normal forms.

There are stronger forms, including Boyce-Codd Normal Form, Fourth Normal Form, and Fifth Normal Form.

Their purpose is to address increasingly subtle dependency problems.

For now, we have enough normalization to prevent a respectable amount of suffering.

## A Real-World Example: Building an Event Ticketing System

Let us move beyond university exercises.

Imagine building a ticketing platform.

Users browse concerts, choose tickets, make purchases, and receive confirmation.

Your first design might use one table called `Everything`.

It contains:

- customer name
- customer email
- event name
- event date
- venue name
- venue address
- ticket type
- ticket price
- order number
- quantity
- payment status

This looks convenient until the system grows.

A single venue hosts fifty events.

A single customer places twenty orders.

A single order contains several ticket types.

Prices change.

Events are rescheduled.

Customers change email addresses.

And occasionally somebody decides to rename the venue after everyone has already bought tickets.

Suddenly our convenient table is a magnificent source of contradictory information.

A better starting design might include the following entities.

### Customers

Stores customer identity and current profile information.

**Primary key:** `customer_id`

### Venues

Stores the venue's identity, name, address, capacity, and other venue-specific information.

**Primary key:** `venue_id`

### Events

Stores each event's identity, name, start time, and venue reference.

**Primary key:** `event_id`

**Foreign key:** `venue_id`

One venue may host many events.

### TicketTypes

Describes ticket offerings for an event, such as General Admission, VIP, or Reserved Seating.

**Primary key:** `ticket_type_id`

**Foreign key:** `event_id`

Each ticket type belongs to a particular event.

### Orders

Stores purchases and their status.

**Primary key:** `order_id`

**Foreign key:** `customer_id`

One customer may place many orders.

### OrderItems

Stores the individual ticket types and quantities purchased in an order.

**Primary key:** `order_item_id`

**Foreign keys:** `order_id`, `ticket_type_id`

An order can contain multiple line items.

This design separates concepts that have different identities and different lifetimes.

A customer's current email address is not the same kind of fact as the ticket price paid three months ago.

A venue's current name is not necessarily the name printed on a historical ticket.

An event's scheduled date is not necessarily the same thing as its original scheduled date.

Those distinctions become critical when systems must preserve historical truth.

### The historical pricing trap

Suppose a VIP ticket currently costs $150.

Alice purchases one for $120 during an early promotion.

A month later, the current ticket price increases to $180.

What price should Alice's order show?

$120.

Always $120, unless a legitimate adjustment or refund changes the transaction history.

If the order displays the current ticket price, it rewrites history.

That is not a pricing system.

That is a financial gaslighting machine.

The solution is to store the actual purchase price in `OrderItems`, perhaps as `unit_price_paid`.

This is deliberate duplication of a value with a different meaning.

`TicketTypes.current_price` describes today's offering.

`OrderItems.unit_price_paid` describes the historical transaction.

They are not interchangeable facts.

**Good normalization is not about eliminating every repeated-looking value. It is about correctly representing what each value means.**

### The inventory trap

Now suppose only ten VIP tickets remain.

Two customers attempt to purchase all ten at the same time.

Does our beautifully normalized database prevent overselling?

Not by itself.

We have modeled the entities.

We have not yet fully solved concurrency.

The system still needs an appropriate transactional strategy to make inventory changes safely under simultaneous demand.

That brings us to **Episode 4: Transactions and Consistency**.

Relational structure establishes important rules.

Transactions protect operations that must succeed or fail together.

Both are necessary.

One without the other is like building a bank vault with excellent shelves and no door.

## What About Joins?

Once we separate data into related tables, how do we put useful information back together?

With queries that combine related records.

In SQL, a **JOIN** is one of the primary mechanisms.

Suppose we want the students enrolled in Databases.

Our information is distributed across:

`Students`

`Enrollments`

`Courses`

The relationship keys tell us how to connect them.

Here is a preview:

~~~sql
SELECT
    s.full_name,
    c.course_name
FROM Students AS s
JOIN Enrollments AS e
    ON s.student_id = e.student_id
JOIN Courses AS c
    ON e.course_id = c.course_id
WHERE c.course_name = 'Databases';
~~~

The query asks the database to combine matching records and return the requested attributes.

We do not need to store an enormous permanent table containing every possible student-course combination.

Instead, the database constructs the relevant result.

This connects to the relational algebra underlying database theory.

Three foundational operations are:

- **Selection:** Choose rows satisfying a condition.
- **Projection:** Choose particular attributes.
- **Join:** Combine related data using a matching condition.

SQL uses its own syntax and has more features than basic relational algebra, but the conceptual relationship is important.

A well-designed database can represent information in separate logical components while still answering questions involving several of those components.

That is where relational thinking becomes powerful.

And we will give SQL the attention it deserves in Episode 3.

Possibly with fewer table aliases that look like someone fell asleep on the keyboard.

## The Big Misconceptions About Relational Design

Several misunderstandings appear so frequently that they deserve their own small intervention.

### Misconception: Every table needs an automatically generated integer ID

Not necessarily.

A composite primary key can be perfectly appropriate.

Some business identifiers are stable and meaningful.

The right choice depends on the entity, its identity rules, and how the rest of the system uses it.

### Misconception: Every relationship should be a foreign key in both directions

Usually not.

If an employee contains a `department_id`, the department does not also need a column containing a comma-separated list of employee IDs.

The relationship can be traversed in either direction by querying the tables.

Storing both directions as independent lists invites disagreement.

### Misconception: Foreign keys automatically make queries fast

Foreign keys primarily enforce relationships.

They do not universally guarantee that every referencing column has an automatically created index.

Indexing behavior varies by database system and constraint type.

Indexes can dramatically improve performance, but they are a separate design consideration.

We will cover that in **Episode 5: Indexes and Performance**.

### Misconception: Normalization means more tables are always better

Absolutely not.

A normalized schema should accurately represent dependencies and reduce undesirable redundancy.

Creating unnecessary tables adds complexity.

It introduces more relationships to maintain, more joins to consider, and sometimes more opportunities to misunderstand the model.

Normalization is a tool for correctness and maintainability, not a contest to see who can produce the most rectangles in an ERD.

### Misconception: Once the schema is correct, the data must be correct

No.

A database can enforce declared constraints.

It cannot automatically understand every business rule you forgot to tell it.

A `NOT NULL` constraint cannot determine whether an email address belongs to the right person.

A foreign key cannot automatically determine whether a customer is authorized to make a particular purchase.

A positive quantity constraint cannot necessarily determine whether a purchase is fraudulent.

Good schemas help.

Validation, authorization, transaction handling, testing, and business logic still matter.

The database is powerful.

It is not psychic.

## Normalization Versus Performance: When Duplication Is Actually Useful

Now for an important tradeoff.

Normalized databases often make updates safer and the meaning of facts clearer.

But highly normalized structures can require multiple joins to answer certain questions.

Sometimes those joins become expensive at scale.

Consider a reporting dashboard that constantly calculates sales by region, product, and month.

The underlying normalized tables might be excellent for handling individual purchases.

But repeatedly calculating complex aggregates over millions of transactions could be unnecessarily expensive.

One solution is **denormalization**.

Denormalization deliberately stores some redundant or precomputed information to improve specific access patterns.

Examples include:

- maintaining summary tables
- creating materialized views
- caching frequently requested results
- storing computed aggregates
- building dedicated analytical models

These approaches can improve read performance.

But they introduce responsibilities.

If a total is stored in multiple places, how do we keep those values synchronized?

What happens when a transaction is reversed?

What happens when a background aggregation job fails?

A normalized design reduces some consistency problems.

Denormalization may bring some of them back intentionally.

The important difference is that we now understand the tradeoff.

**Normalize for a sound logical model. Denormalize when measured requirements justify it, with a plan for keeping derived data correct.**

That is a much healthier strategy than discovering that your database contains five competing revenue totals and choosing whichever one makes the quarterly presentation look nicest.

## What Does Relational Thinking Look Like in Modern Software?

The relational model is not an antique curiosity.

It remains central to modern application development.

Relational database systems such as PostgreSQL, MySQL, MariaDB, Microsoft SQL Server, SQLite, and Oracle Database implement relational concepts through SQL-based systems.

They appear in web applications, financial services, enterprise systems, mobile apps, cloud platforms, and internal business software.

A modern application might use:

- PostgreSQL for application records and transactional data.
- Redis for caching or specialized access patterns.
- Object storage for large files.
- A search engine for full-text retrieval.
- An analytical warehouse for reporting.
- A vector index for similarity search in an AI application.

These technologies serve different purposes.

Their existence does not make relational databases obsolete.

It simply means today's systems often use several data models together.

And that creates a new architectural challenge.

Which system owns the authoritative information?

If a product's price exists in the relational database, a search index, a cache, and an AI-generated summary, where does a price change originate?

Which copies are derived?

How do they get refreshed?

What happens when they disagree?

Those are relational-thinking questions even when some of the systems involved are not relational databases.

### What about AI-generated applications?

AI tools can generate database schemas impressively quickly.

They can suggest tables, relationships, migrations, and SQL queries.

That can be useful.

But generating a schema is not the same as understanding a business.

An AI system might decide that each customer has one address.

That seems reasonable.

Until you discover that the application supports billing addresses, shipping addresses, historical delivery addresses, and corporate accounts with multiple authorized contacts.

Now your one-address design has turned into a costly migration.

AI can assist with modeling.

It cannot replace clear requirements and careful scrutiny.

And AI applications themselves need thoughtful data models.

Consider a system storing uploaded documents and AI-generated embeddings.

You might need to distinguish:

- source documents
- document versions
- extracted text
- processing jobs
- generated chunks
- embeddings
- model versions
- access permissions

Why?

Because the same document may be reprocessed with a newer extraction tool or embedding model.

If you do not preserve which output came from which source version and processing run, debugging becomes an archaeological expedition.

Relational thinking helps establish identity, lineage, and ownership even when the application also uses a vector database.

The technology changes.

The need to understand what information means does not.

## Schema Changes: Because Requirements Have a Sense of Humor

One final practical reality deserves attention.

Database schemas evolve.

A university initially allows one instructor per course.

Later it introduces team teaching.

An event platform initially supports one venue per event.

Later it supports multi-location festivals.

An online store initially supports one shipping address per order.

Later it supports split shipments.

The original schema may have been entirely reasonable.

Then the business changed.

Changing a database schema is called a **schema migration**.

A migration might add tables, change columns, introduce new relationships, or modify constraints.

But schema migrations are not just structural changes.

Existing data must remain meaningful.

Old application versions may still be running.

Reports may depend on previous structures.

APIs may expose fields that no longer fit the new design.

That is why mature systems treat database changes as part of software engineering, not merely as a few SQL commands somebody found in a chat window.

Good migrations are planned, tested, monitored, and designed with compatibility in mind.

Sometimes they require backfilling data or temporarily supporting both old and new representations.

Relational thinking makes these changes easier because the original structure expresses what the information means.

A schema is not permanent.

But a good schema gives future changes somewhere sensible to begin.

## A Practical Exercise: Design a Small Library

Before we wrap up, here is a challenge.

Imagine a library system.

It needs to manage books, authors, physical copies, members, and loans.

Consider these questions.

**First:** Can one book have several authors?

Yes.

That suggests a many-to-many relationship between books and authors.

**Second:** Can the library own several physical copies of the same book?

Yes.

A book title and a physical copy are not the same entity.

**Third:** Can one member borrow several books?

Yes.

**Fourth:** Can the same physical copy be borrowed by different members at different times?

Also yes.

That suggests loans should be represented as records with their own identity and timing.

Now try to identify the entities.

One reasonable model might include:

- `Books`
- `Authors`
- `BookAuthors`
- `BookCopies`
- `Members`
- `Loans`

Then identify the keys and relationships.

A loan might contain:

`loan_id, copy_id, member_id, borrowed_at, due_at, returned_at`

The record represents a particular borrowing event.

Not the permanent ownership of a book.

And not the current state of a member.

That distinction allows the library to preserve borrowing history.

It also introduces an interesting rule.

A physical copy should not have two overlapping active loans.

A simple foreign key will not enforce that requirement by itself.

How would you handle it?

That is exactly the kind of question database designers should ask before writing the first production table.

Because the hardest database problems are often not about syntax.

They are about identifying the rules that must always remain true.

## What Should You Remember?

Relational thinking begins with a surprisingly simple question.

**What are the actual things my application needs to remember, and how are they related?**

From there, the pieces begin to fit together.

Entities represent meaningful things.

Attributes describe their properties.

Keys identify records.

Foreign keys establish enforceable references.

Junction tables represent many-to-many relationships.

Constraints protect important assumptions.

Normalization reduces problematic redundancy and helps prevent insertion, update, and deletion anomalies.

And good modeling distinguishes current facts, historical facts, and derived information.

There is mathematics beneath all of this.

There is engineering beneath the mathematics.

And beneath the engineering is a very practical desire to avoid spending Sunday afternoon explaining why an invoice suddenly belongs to a customer named NULL.

Relational database design is not simply a technique for storing data.

It is a method for describing reality in a form that software can understand, enforce, and manipulate.

That idea has shaped information systems for more than half a century.

And it remains essential.

## What's Coming Next?

In **CS303 Episode 3: Querying with SQL**, we will take the structures we have designed and learn how to ask them questions.

We will explore `SELECT`, `WHERE`, `JOIN`, `GROUP BY`, aggregation, and the practical art of retrieving exactly the information we need.

Because now that our data has a sensible home, we would like to find things inside it without conducting a full-scale search-and-rescue operation.

Then we will move into transactions, consistency, indexing, performance, and eventually the broader world of NoSQL systems.

For now, remember one lesson:

**A good database doesn't merely store information. It preserves the relationships and rules that give information meaning.**

And that is the quiet power of structure.

---

## Join the Conversation

Have you ever inherited a database schema that looked as though it had been designed during a power outage?

Have you had to clean up duplicate customer records, mysterious foreign keys, or a table with 247 columns and a name like `FinalData_NEW_v3`?

I'd love to hear about it.

**Leave a comment** with your most memorable database design triumph or disaster.

And **follow for more episodes** of our computer science journey as we continue moving from programming fundamentals into the deeper machinery of software engineering.

We are only two episodes into CS303.

The data is already developing opinions.

---

## [Art Prompt (Ashcan School):](https://lumaiere.com/?gallery=ashcan)

Create an extraordinary, dramatically atmospheric early twentieth-century American Ashcan School oil painting depicting the dazzling interior of a crowded Edwardian theater during a spectacular ballet performance. View the scene from an intimate, slightly elevated position behind a small group of elegantly dressed spectators seated in a darkened theater box, their shoulders, fashionable hats, and expressive silhouettes forming an irregular shadowy foreground. Beyond them, an expansive stage glows with mysterious pale golden illumination, revealing a graceful line of ballerinas dressed in luminous ivory and pearl-white tutus, their arms raised in expressive synchronized gestures and their delicate figures emerging from a smoky green-gray theatrical atmosphere. Capture the tension between the hushed darkness of the audience and the exhilarating movement of the performers. Employ vigorous, spontaneous yet disciplined oil brushwork, softly dissolved contours, broken color, painterly surface textures, and the observational immediacy of an artist fascinated by urban entertainment and human spectacle. Use a sophisticated palette of smoky olive, charcoal black, tarnished gold, muted ivory, dusty rose, deep umber, desaturated jade, and subtle hints of wine-red velvet. Let the bright skirts dissolve into expressive strokes of cream and pale silver, while the spectators retain nearly silhouetted forms accented by delicate reflected light. Emphasize cropped theatrical perspectives, dramatic chiaroscuro, lively gestural movement, atmospheric depth, and an intimate sense of being present at an extraordinary performance. The composition should feel spontaneous yet carefully balanced, both socially observant and richly theatrical, celebrating the restless energy, elegance, and visual poetry of metropolitan life. Museum-quality oil painting, authentic period atmosphere, tactile impasto details, exquisite cinematic lighting, richly expressive human figures, and a compelling sense of movement. No text, logos, modern objects, or photorealistic rendering.

## [Video Prompt:](https://www.tiktok.com/@davelumai/video/7704885739074358558)

Create a breathtaking, energetic 9:16 animated cinematic sequence based on the atmospheric Ashcan School theater painting. Begin immediately with a brilliant burst of warm stage light as an entire line of ivory-clad ballerinas leaps into synchronized movement, their flowing skirts unfurling in dramatic circles of luminous cream and silver against the smoky olive-green background. The camera rushes dynamically forward between shadowed spectators toward the glowing stage, then sweeps sideways across the dancers as their arms rise, ribbons flutter, and delicate costumes spin with rhythmic precision. Glowing particles of theatrical dust swirl through intersecting amber spotlights, while audience silhouettes lean forward and burst into animated applause. Preserve the expressive, visible oil-brush texture throughout every movement, allowing the choreography to feel as though the original painting has suddenly awakened. Introduce exciting rhythmic cuts between delicate ballet footwork, dramatically swirling skirts, expressive faces, theatrical curtains, and the glittering full ensemble. Use smooth, elegant motion combined with energetic visual transitions, rich historical atmosphere, painterly light, and irresistible musical synchronization. Build toward a spectacular final coordinated spin in which the dancers' white costumes form a dazzling circular flourish, then return naturally to the opening formation for a seamless loop. The overall result should feel joyful, sophisticated, immersive, magical, and immediately captivating for short-form video platforms, without modern objects, text, logos, or photorealistic effects.

## Music to Accompany the Video

**Inspector Norse – Todd Terje**

A gloriously playful electronic groove that transforms a graceful Edwardian ballet into something unexpectedly modern, exuberant, and impossible to ignore.

**Russian Dance (Trepak) – Pyotr Ilyich Tchaikovsky**

Explosive orchestral energy, dramatic rhythmic accents, and dazzling movement that give the animated ballet an irresistibly theatrical momentum.