# Enterprise DevOps
by Bill Ott, Haluk Saker, Jimmy Pham
Publisher: O'Reilly Media, Inc.
Release Date: December 2016
ISBN: 9781492030065

This can be found at https://www.oreilly.com/library/view/enterprise-devops-playbook/9781492030065/

## Intro

Book claims hat DevOps wouldn't exist without Agile, but I disagree. I remember the way
test engineers and support staff at TCS and that seemed reasonably DevOps-y to me even
though the project wasn't very agile.

The corollary however that better DevOps has made Agile viable is something I do agree with.
Without DevOps, Agile has massive pains getting software to customers.

To excel at DevOps, enterprises need to transform their cultures, build and design software
in a modular way, automate legacy processes, and design contracts to enable integration of
operations and development.

## 5 Plays
Book mentions five plays for becoming more agile, but they're more like a
sequence of steps than an actual playbook.

## Play 1: Develop the Team
The first step is to see what roles they already have, overlay that with the DevOps model,
and then see what steps are needed to develop the team.

### Agile Principles

Organizations can fail to adopt DevOps due to cultural issues. Adopting these principles
can help.

1) Treat operations as first class citizens: Operational needs raised by the team during
  production need to be treated as priorities.
2) Develops act as first responders with the production system: The person who
  developed the code should be one of the first responders. Instead of on a separate team.
3) Shorten the time between identification of a production issue and its repair: Make
  production support proactive by making developers part of the operations support team.
4) Shorten the time between code commit and code deploy: Most of the steps in deployment
  can be automated, but you also need to make the system better at deploying discrete changes
  instead of the entire application.
5) Minimize coordination to deploy releases.
6) Stop and fix potential defects identified by continuous flow and monitoring:
  Monitor systems so that you can catch issues before they grow big enough to inconvenience
  users.
7) Enforce standardized processes to ensure predictable outcomes: You can't automate things
  unless they are. Exceptions lead to instability.
8) Become a learning organization through continual feedback and action: Create a corporate
  culture that rewards constant improvement.
  
### DevOps Roles
The authors DO NOT believe in stand alone DevOps teams.

DevOps Architect - Uses automation to create efficient effective processes and standards to
  continuously improve quality and estimation. Oversees tool analysis and selection.
DevOps Engineer - Hybrid role mixing development and operations. Implement architect's plans.
Test Automation Engineer - Builds test code. Does it in anyway that others can contribute to.
Site Reliability Engineer - Monitors applications in post-deployment. Collects metrics and
  hooks them up to tests.
Software Engineer - Like traditional, but they embrace the principles and have a whole team
  mindset.
  
## Play 2: Study the DevOps Practices

DevOps becoming a buzzword has made it vague, but it does have core practices.

### Practice 1: Configuration Management

Essentially code management

Good = Centralized workflow: Everyone checks in and out of "master" branch
Better = Feature workflow: People make feature branches and then check them into "master".
Best Gitflow workflow: Feature, but uses master for public releases and does dev workflow
                       in a separate dev branch. By Vincent Driessen.

### Practice 2: Continuous Integration

Constantly check in code to minimize integrations efforts and to make other practices
easier.

### Practice 3: Automated testing

Integrate with CI and CD throughout the process.

### Practice 4: Infrastructure as code

Automatically setup machine environments in reproducable ways. Uses things like
Docker, Kubernetes, Chef etc.

### Practice 5: Continuous Delivery

People are constantly checking in. The previous practices prevent this from being a disaster.
Master is not necessarily sent into prod automatically.

### Practice 6: Continuous Integration

The opposite of "Master is not necessarily sent into prod automatically."

### Practice 7: Continuous Monitoring

Should be built into the code as it's written. Part of a system with three steps.
1) Monitor values 2) Create alerts 3) Take action.

## Play 3: Assess Your DevOps Maturity Level and Define a Roadmap

This section is a questionnaire basically where you answer questions and that determines
the DevOps maturity of your company culture. It serves as a decent summary of Play 2.

## Play 4: Create a DevOps Pipeline

Once you have a roadmap, the first step is to build a DevOps pipeline. These tools will provide
workflow automation for every step to take code to production.

This pipeline needs:
* Automated building, testing, and deploying
* Automated infrastructure
* Repeatable results with immutable infrastructure
* Visibility

Basic pipeline should let you:
* Check out code
* Change code and integrate it into repo
* Run validation and predeployment tests
* Deploy your builds
* Move the build dev -> testing -> QA -> prod

## Play 5: Improve through Metrics and Visibility

Metrics serve five critical purposes
* Detect failure
* Diagnose perf. problems
* Plan capacity
* Obtain insights about user interaction
* Identify intrusions

You also want to track these four DevOps facets:
* Deployment frequency
* Change lead testing - How long to get committed code into prod
* Change failure rate
* Mean-time-to-recovery

Other benchmarks
* Delivery frequency
* Change volume (size of code changes)
* Customer tickets (e.g. per week)
* Change in user volume
* Availability
* Response time

Cultural metrics
* Cross-skilling
* Focus
* Multidisciplinary teams
* Project-based teams
* Business demand
* Extra lines of code
* Attitude
* Number of metrics
* Technological experimentation
* Team autonomy
* Rewards

Many of these are hard to measure.

The authors believe that the strength of a DevOps culture can be
measured through the maturity of the component processes of the DevOps
toolchain.

## Recommendations

For metrics tools, the authors recommend Nagios, Sense, Icinga, Ganglia, Graylog2, Logstash,
and Splunk.

If you want to read some more, the authors recommend:
* The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology
  Organizations
* Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation
* Building - DevOps Culture
* The DevOps 2.0 Toolkit: Automating the Continuous Deployment Pipeline with
  Containerized Microservices
* Building Microservices












