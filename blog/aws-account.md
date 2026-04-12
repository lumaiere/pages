# Managing Multiple AWS Accounts Securely, or How to Stop Giving Everyone the Keys to the Entire Cloud Kingdom

At some point every growing AWS setup reaches the same charming little crossroads.

One path says, "Let us organize this properly."

The other path says, "Surely one giant account full of workloads, billing, experiments, permissions, logs, and twelve different kinds of regret will remain manageable forever."

That second path has a strong historical record of becoming a bonfire.

If you want the sane version, AWS has already done a lot of the hard thinking for you. The basic combination is **[AWS Organizations](https://aws.amazon.com/organizations/)** for account structure and central governance, plus **[AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/)** for workforce access across those accounts. In plain English, one gives you the house with rooms, and the other decides who gets a key, which room they can enter, and whether they are allowed to touch the expensive machinery once they get there.

So if you are imagining one management account for billing and control, plus three more accounts for actual work, yes, that is a very reasonable way to start.

## The four-account setup that makes sense without becoming a tiny bureaucracy

For a small but serious setup, I would structure the four accounts like this:

**1. Management account**
This is the organization owner account. Let it handle consolidated billing, organization-level control, and the absolute minimum number of terrifyingly powerful tasks. Do not treat it like a normal work account. Do not build random workloads in it. Do not let half the company wander through it like it is a food court.

**2. Shared services or identity admin account**
This is the smart place to put day-to-day administration that does not need to live in the management account. AWS explicitly supports delegated administration for IAM Identity Center, and that matters because fewer people touching the management account is generally how you keep your blood pressure civilized. The official guidance on **[delegated administration in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/delegated-admin.html)** is worth reading because it is basically AWS saying, "Please stop using the management account as your everyday office kitchen."

**3. Production account**
Real workloads. Real data. Real consequences. Very few humans should have broad access here, and even fewer should have admin-level power.

**4. Non-production account**
Development, testing, staging, experiments, and the occasional noble mistake made in the spirit of progress. This is where people should be allowed to learn, break things in contained ways, and discover that infrastructure is much more educational when it is not also customer-facing.

Could your three member accounts be Production, Staging, and Development instead? Absolutely. Could one of them be Security or Logging instead of Shared Services? Also yes. The main point is separation of duties. Billing and org control should not be living in the same everyday mess as your applications.

## How AWS wants you to administer users, and why it is honestly pretty sensible

AWS is very clear in the IAM Identity Center documentation that the recommended model for a multi-account setup is an **organization instance**, not an account instance. The quick overview in **[What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)** makes this pretty plain: organization instances are the recommended choice and the ones built for centrally managing access across multiple AWS accounts.

That matters because account instances are for narrower, more isolated scenarios. They are not the main event here. They are the side room with a folding chair.

For actual user administration, the best-practice shape looks like this:

Use IAM Identity Center as the central place to assign workforce access.

Keep the management account locked down to as few people as possible.

Use delegated administration from a member account so your identity admins are not constantly stomping around in the crown jewels.

Use dedicated permission sets for the management account instead of casually reusing the same powerful bundle everywhere.

And this is an especially important one: for the management account, AWS recommends assigning **users directly**, not groups. That sounds slightly annoying until you remember why. If you grant management-account access through a group, then whoever can change that group membership can quietly hand out management-account access like party favors. That is not a fun surprise. That is the kind of surprise that gets a post-incident meeting and a grimly worded slide deck.

AWS also recommends separating identity-center configuration duties from permission-set management. That is a polite way of saying the person who changes your identity source, SCIM settings, and session behavior does not necessarily need to be the same person who can spray powerful roles across every account in the organization.

Which, when you say it out loud, sounds less like bureaucracy and more like basic adult supervision.

## How the permissions should be set up

This is where people often make the cloud version of buying a house and then handing out one universal key because labeling things feels like work.

Do not do that.

Set up permission sets by job function and by environment.

A clean starting point might look like this:

**Management account permission sets**
Very small list. Very few people. Think billing admin, organization admin, maybe an audit or read-only role, and a carefully limited break-glass admin path.

**Production permission sets**
ReadOnly, Support, Operator, Deployer, maybe a ProductionAdmin if you absolutely must, and even then only for a small number of people.

**Non-production permission sets**
Broader access is more acceptable here, because this is where people build and test. Still, broad does not need to mean delirious.

**Shared services or identity admin permission sets**
Identity administration, logging access, maybe automation management, but still scoped to purpose.

The nice part is that IAM Identity Center permission sets can be assigned across multiple accounts, so you are not recreating the same idea eighteen different times with slightly different spelling.

Also, a useful little detail that deserves more attention than it usually gets: IAM Identity Center creates IAM roles in accounts when you assign permission sets. So if your environment gets large and very role-happy, keep an eye on IAM role quotas. Nobody enjoys learning about scale limits during an already irritating week.

## How people actually log in

In a good setup, your humans do not maintain a separate local IAM user in every AWS account like they are collecting cursed library cards.

They sign in once through the AWS access portal, choose the account they need, then choose the permission set they were assigned. From there they can open the console or use programmatic access for the CLI and SDKs.

That is one of the biggest quality-of-life upgrades in the whole design. Instead of remembering which account has which user and which password and which little ritual dance gets you into which environment, you centralize workforce access and let the portal do its job.

So the answer to "How do I log in to the various accounts?" is basically this:

You do not log in to each account as a separate identity.

You log in once, then select the account and role you are allowed to use.

Which is much cleaner and much less likely to produce the sentence, "I think I am accidentally in prod."

## What if you do not have an IdP

Then AWS gives you a perfectly workable starting point.

If you do not already have Okta, Google Workspace, Entra ID, or Active Directory handling workforce identity, IAM Identity Center can use its own built-in directory so you can create and manage users directly. The overview in **[this part of the IAM Identity Center user guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source.html)** is refreshingly straightforward about that.

That means "no IdP" is not a blocker. It just means AWS can be your starting identity store.

The main caution is this: choose thoughtfully at the beginning. Changing identity source later can be disruptive, and AWS is not being melodramatic about that. Identity changes in access systems have a way of becoming exciting in exactly the wrong direction.

## Can you use AWS for some users and Google Workspace for others

This is where the answer becomes annoyingly nuanced, because reality loves nuance precisely when everyone wants a yes or no.

If you mean, "Can one IAM Identity Center organization instance use its built-in directory for some users and Google Workspace as the identity source for other users?" then no, not in the clean central model. You get one identity source per organization. One. Singular. Not one and a half. Not one with a side quest.

If you want Google Workspace as the identity source, the official setup path is here in AWS's **[Google Workspace integration tutorial](https://docs.aws.amazon.com/singlesignon/latest/userguide/gs-gwp.html)**.

Now, there is a separate nuance. AWS does say you can continue using existing IAM-based federation workflows for some AWS account access scenarios while using IAM Identity Center for application access. So coexistence can happen in the broader universe. But if your goal is a tidy, centrally managed, multi-account workforce model, split-brain identity is generally not the way to achieve inner peace.

Pick one workforce identity source for the organization and be done with it.

Your future self would like a calmer Thursday.

## Other security considerations that deserve a suspiciously serious nod

A few other points are worth calling out.

Do not let the management account become an everyday playground. If somebody needs to administer IAM Identity Center day to day, delegated administration exists for a reason.

Use least privilege like you actually mean it, not like it is a decorative slogan you mounted in the hallway.

Create separate permission sets for different kinds of administrators. Identity admins, billing admins, platform admins, and workload operators do not all need the same giant sack of power.

Be careful with anything related to SCIM bearer tokens if you connect an external IdP. Those tokens are not magical. They are powerful. Treat them accordingly.

If you care about resilience, multi-Region IAM Identity Center is now much more interesting than it used to be. AWS has expanded that story, which is good news for anyone who enjoys not being emotionally dependent on a single Region for workforce access.

And perhaps the most underrated best practice of all: keep environments emotionally and technically separate. Production should not be one bad afternoon away from development habits.

## So what is the practical answer?

If you want a management account plus three others, here is the short version.

Create the organization.

Keep the management account for billing, organization governance, and only the most sensitive controls.

Use an organization instance of IAM Identity Center.

Choose one identity source early.

Delegate day-to-day IAM Identity Center administration to a member account.

Use permission sets by job function and environment.

Give management-account access directly to named users, not broad groups.

Have people sign in through the access portal instead of maintaining a junk drawer of account-local users.

And above all, design the structure so access is boring.

Because in cloud security, boring is beautiful.

If this saved you from one future permissions disaster, give me a follow, drop a comment, and tell me what your current AWS account layout looks like. I am always curious how close other people are to elegance, chaos, or that very special middle state where both are somehow happening at once.

**[Art Prompt (Neoclassicism):](https://lumaiere.com/?gallery=neoclassical)** A refined neoclassical interior bathed in clear morning light, centered on a poised woman in luminous ivory and muted saffron drapery standing beside two children near a polished marble pedestal. Surround the scene with fluted columns, pale stone steps, a distant blue-gray sky glimpsed through an open colonnade, and restrained accents of antique gold. Compose the figures with graceful stillness, idealized anatomy, crisp contours, and balanced geometry, letting soft coral, dusty rose, cool cream, and lapis hints animate the otherwise calm palette. The mood should feel noble, tender, disciplined, and quietly radiant, with satin-smooth surfaces, measured folds, and the polished serenity of virtue made visible.

**[Video Prompt:](https://www.tiktok.com/@davelumai/video/7627841700462955806)** Begin with a brisk reveal through sunlit columns into a poised neoclassical hall where a woman in ivory and muted saffron drapery turns gently toward two children at her side. Let gauzy fabric ripple, gold trim catch quick flashes of light, and dust motes shimmer in the bright air as the camera arcs in elegant semicircles around polished marble steps and a pale stone pedestal. Add subtle hand movement, a child shifting closer, a breeze stirring the distant blue-gray sky beyond the colonnade, and tiny gleams skating across carved surfaces. Keep the motion graceful, rhythmic, and immediately captivating, with balanced composition, crisp contours, and a noble atmosphere that feels serene, radiant, and alive.

A couple songs to go with it: *Emerald and Stone* by Brian Eno & Jon Hopkins and *New Grass* by Talk Talk.
