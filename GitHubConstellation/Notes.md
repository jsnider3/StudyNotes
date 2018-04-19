# Notes

GitHub Constellation is an event that GitHub hosts that moves around.
It was in DC on 2018/4/19 and I attended it there.

The event has a website at https://githubconstellation.com/.

GitHub universe is the big event (Oct 16 - 17, 2018), that spawned this series.

## Part 1: At Work

This was the day event starting at 8:30 AM. A half-dozen speakers were lined
up for the event.

### Schedule
9:00 Welcome
9:15 Code.gov
9:45 US Small Business Administration
10:15 GitHub in 2018
11:00 Break
11:15 US Digital Service
11:45 Northrop Grumman
12:15 Lunch
1:00 AWS Public Sector
1:30 Booz Allen Hamilton
2:00 Networking

### Sponsors
waffle.io - Project overviews.
cloudbees - Jenkins but for the enterprise.
circleci - Continuous integration service.
amazon web services
Modus Create - Mobile-web development group / consultancy.

### Code.gov
Presentation by Joseph Castle, GSA.
github.com/jcastle
joseph.castle@gsa.gov

#### History of open source in the fed.
* In the 1940s, Grace Hopper was an Admiral that did computers.
	Most computers back then were doing anti-aircraft stuff.
	She got input from academics to build a compiler(?) in the 50s.
* Obama required 20% of custom-code to be open-source.

#### Five Propositions of Org Barriers to Open-Source.
This is actually part of his PhD thesis.

As of April 2016, 600 govt orgs were on GitHub with 9k+ repos.
There's a lot of intrinsic motivation for individuals to contribute to open
source, but there's still a shortage of open-source work by government. This
has to be an organizational issue then. 

P1: Organizations that use high technology as core technology to produce
	outputs are more likely to publish OSS.
	
P2: Orgs that use new development technology with source code creation and
	publication are more likely to publish OSS.
	
P3: OSS publication occurs in decentralized orgs with a bottom-up approach by
	individuals that perceive value of publishing code for organizational	
	and computing field benefit.
	
P4: New and existing organizations that develop source code or have high
	technology skills to understand code are more likely to publish OSS.

P5: Organizations with culture exhibiting traits of the Hacker's Ethos are
	more likely to publish OSS.

Not sharing code means people have to pay for things multiple times.

code.gov was founded in August 2016. It was started to help implement
the Federal Source Code policy. Also, we want to update acquisition language
to encourage people to open-source things.

Then he proposed a study to look at analytics.usa.gov, compare it across
city equivalents and see what's popular. Philadelphia parking tickets, and
Sacramento WiFi.

### US Small Business Administration
Digital Transformation 7 Ingredients for Change by Ryan Hillard

ryan.hillard@sba.gov

A while ago they wanted to reimagine SBA.gov.

#### Ingredient 1: Executive Sponsorship

Large organizations are the Death Star, they're complex have gravity and inertia.
Require a fast, powerful ship to navigate them.

Two people is best, they had the CIO and Chief Digital Officer. Now they have
the CIO and Officer for Communications.

#### Ingredient 2: Common Language
What is user-centered design? What is agile software development? What does
DevOps really mean?

Also, WHY?

#### Ingredient 3: Versatile Team
Design (Research, UX, UI)
Product (High-level view, Intentional, Delivery)
Technology (Digital, Call bull, Call yahtzee)

But, HOW?

#### Ingredient 4: Modern Procurement
He recommends Firm Fixed Price per ITERATION.
Product Owner, Development Team, Iterations

#### Ingredient 5: Agile Methods
Kanban for content. Scrum for iterations.

Focus on Value Delivered

#### Ingredient 6: Right technology
Prototype, modern, productive.

Do the MATH.

#### Ingredient 7: Change Management
Everyone knows this is important.

Governance, hidden costs.

### GitHub in 2018
By Jamie Jones
NO PROMISES!

Periodic Table of DevOps Tools

#### Integration Improvements
Plans:
VSTS(Microsoft CI)
Slack V1
Multiple organization management
StatusCheck API
Slack V2
GVFS
Jira
Unified Search

Top-level primitive - Manage multiple orgs with a single account, easier license
agreement.

StatusCheck API - Better status messages, better data from tools, GitHub as
	message bus between dev tools.

Unified search / Unified contribution graph - Combine Enterprise and public.

GitHub has 500 TB worth of code, 100 million pull requests.
85% of pull requests are private.

#### Secure Coding Improvements
AI-powered vulnerability detection.

Token scanning (Beta) - Reduce risk of credential leaks

GitHub-native security scanner (Alpha)

#### Productivity Improvements
Issue templates
Developer dashboard
Developer profile
Pull Request enhancements (Require multiple reviewers)
GitHub Learning Lab (12:30 Eastern time today!)

### US Digital Service
Login.gov Data Engineering and Analytics by Jordan Bramble

What is USDS?

What is Login.gov? Attempt to create single account across government,
	to save money, to update experiences, and to do it without failing.
	This is using a new, better team. Using a tour-of-duty model.

How we handle data at scale? They currently have 4 million users.
	They use AWS Lambda to avoid provisioning servers.
	
How to get involved? Go to usds.gov/join

### Northrop Grumman
Guidance on GitHub by Rickey Zachary

Status Quo is not where we need to be. GitHub is something we can
use to switch tribal knowledge to systemic knowledge. His use of it
seems like using GitHub as a competitor for OneNote, but I think his
idea is to have examples of things like Maven and Jenkins with guidance.

This guidance and examples lets people start faster.

### AWS Public Sector

### Booz Allen Hamilton

## Part 2: Explore

This part of the event started at 6:00 PM.