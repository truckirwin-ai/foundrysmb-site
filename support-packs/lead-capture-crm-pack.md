# Lead Capture and CRM Pack

Use this pack to turn free Toolkit interest into qualified pipeline.

## Goal

Every form submission should answer:

- Who is this?
- What business are they in?
- What workflow hurts?
- Is there urgency?
- Is there budget?
- What should happen next?
- Where did the lead come from?

## Minimum form paths

| Intent | Form path | Required qualification |
| --- | --- | --- |
| Toolkit | `contact.html?interest=toolkit` | Name, email, company, workflow pain |
| Revenue Sprint | `contact.html?interest=revenue-sprint` | Full workflow, tools, urgency, $1,500 confirmation |
| System Install | `contact.html?interest=system-install` | Current workflow, existing prototype or sprint output, $5K-$15K confirmation |
| Managed Ops | `contact.html?interest=managed-ops` | Existing workflow, desired monthly support, paid engagement understanding |
| Coaching | `contact.html?interest=coaching-1on1` | Current asset/workflow to review |

## CRM stages

```text
New Toolkit Lead
Qualified Workflow Lead
Discovery Scheduled
Discovery Complete
Sprint Proposed
Sprint Won
Sprint Delivered
Install Proposed
Install Won
Managed Ops Proposed
Managed Ops Active
Nurture
Closed Lost
```

## Lead scoring

Score each inbound lead from 0 to 20.

| Dimension | 0 | 2 | 4 |
| --- | --- | --- | --- |
| Workflow specificity | vague | named pain | specific workflow with examples |
| Business impact | curiosity | time pain | revenue/cash/margin/owner-time impact |
| Urgency | none | this quarter | this week/month |
| Authority | unknown | influencer | owner/decision maker |
| Fit | outside ICP | adjacent | owner-led ops-heavy business |

Next step:

- 16-20: reply personally and offer call times
- 11-15: send worksheet and ask one clarifying question
- 6-10: nurture sequence
- 0-5: keep on list, no manual time

## Qualification matrix

Use this matrix to decide how much founder time a lead deserves.

| Signal | Strong fit | Weak fit | Follow-up question |
| --- | --- | --- | --- |
| Workflow | One named workflow with examples | "Need AI help" | "What is the one workflow you want fixed first?" |
| Pain | Tied to time, revenue, margin, customer response, or owner load | General curiosity | "What happens when this workflow fails?" |
| Data/context | Has examples, templates, tickets, proposals, reports, or SOPs | No source material | "Can you share one sanitized example?" |
| Buyer | Owner, GM, operator, department lead | Student, vendor, unclear role | "Who owns the workflow and budget?" |
| Urgency | Active issue this month | Someday exploration | "Why now?" |
| Budget | Understands sprint/install economics | Wants free consulting | "If we can scope this, are you prepared for a paid sprint?" |

## Routing rules

```text
IF interest = toolkit AND workflow is vague:
  Send Toolkit start email and ask for one workflow sentence.

IF interest = toolkit AND workflow is specific:
  Send Toolkit start email plus Workflow ROI Scorecard.
  Ask for one example.

IF interest = revenue-sprint AND score >= 16:
  Reply personally within 4 business hours.
  Offer 2-3 call times.

IF interest = revenue-sprint AND score 11-15:
  Ask one narrowing question before offering a call.

IF interest = system-install:
  Ask whether a workflow has already been mapped, prototyped, or tested.

IF interest = managed-ops:
  Ask what workflow is already live and what monthly improvement would justify support.

IF lead asks for "AI strategy" only:
  Reframe to one operational workflow before booking time.
```

## CRM fields

Create these fields even if the first CRM is a spreadsheet.

| Field | Type | Why it matters |
| --- | --- | --- |
| Lead source | text/dropdown | Shows what creates real pipeline |
| Form intent | dropdown | Separates toolkit, sprint, install, managed ops |
| Workflow pain | long text | Core sales context |
| Workflow category | dropdown | Bid, lead follow-up, reporting, SOP, support, finance, other |
| Urgency | dropdown | Drives response speed |
| Budget confirmation | checkbox | Filters free-only traffic |
| Fit score | number | Prioritizes founder time |
| Next action | text | Prevents dropped leads |
| Next action date | date | Enables follow-up discipline |
| Last touch | date | Keeps pipeline honest |
| Proposed offer | dropdown | Toolkit, sprint, install, managed ops |
| Loss reason | dropdown | Improves offer and targeting |

## Pipeline health targets

Early-stage weekly targets:

| Metric | Minimum | Good | Excellent |
| --- | --- | --- | --- |
| Toolkit requests | 5 | 15 | 30+ |
| Qualified workflow leads | 2 | 6 | 12+ |
| Discovery calls booked | 1 | 3 | 6+ |
| Sprint proposals | 1 | 2 | 4+ |
| Sprint wins | 0-1 | 1 | 2+ |
| Install/managed ops opportunities | 0 | 1 | 2+ |

If toolkit requests rise but qualified workflow leads do not, the lead magnet is attracting the wrong audience or the follow-up question is too soft.

If discovery calls happen but proposals do not, the form is under-qualifying or the call is failing to narrow scope.

## First response templates

### Toolkit lead

```text
Subject: Your Foundry Toolkit next step

Thanks for requesting the Toolkit.

Start with the Workflow ROI Scorecard and pick one workflow that costs time, margin, or follow-up discipline.

If you want, reply with the workflow in one sentence:
"We lose time/money when ____ because ____."

I will tell you whether it looks like a self-install, sprint candidate, or not worth touching yet.

Truck
```

### Strong toolkit lead

```text
Subject: This is a useful workflow to inspect

Thanks for sending the workflow.

This is specific enough to evaluate:
[workflow summary]

Start with two things:
1. Fill out the Workflow ROI Scorecard.
2. Pull one sanitized example of the current input and current output.

The question is whether the workflow is:
- a self-install using the free toolkit
- a five-day Revenue Sprint
- too risky or unclear to touch yet

If you send the example, I will tell you which path I would take.

Truck
```

### Install-ready lead

```text
Subject: Sounds like this may be past the toolkit stage

If you already have examples, an owner, and a workflow people use every week, this may be an install conversation instead of a starter sprint.

Useful next step:
send the current workflow map, SOP, prompt, automation, or sample output.

I will look for:
- whether the output is reviewable
- whether the context is reliable
- whether adoption is already happening
- whether the business value is measurable

If those are present, we can discuss the $5K-$15K install path.

Truck
```

### Strong sprint lead

```text
Subject: This looks like a sprint candidate

I read your workflow notes. This looks specific enough to discuss.

The useful question is not "can AI help?" It is whether we can build a reviewed first version in five business days.

Send one real example if you can:
- email chain
- estimate/report
- spreadsheet
- SOP
- intake form
- before/after output

Then we can use the call to decide scope instead of talking in circles.

Truck
```

### Not ready yet

```text
Subject: Narrow this first

I would not sprint this yet.

The workflow is still too broad. Before spending money, narrow it to one trigger, one owner, one output, and one pass/fail test.

Use the AI Revenue Sprint Kit and send back:
- workflow trigger
- current inputs
- expected output
- what goes wrong
- what it costs

Then we can decide whether it is worth a paid sprint.

Truck
```

## Source tracking

Track:

- URL
- UTM source
- UTM campaign
- form intent
- first CTA clicked
- referring page
- date submitted
- follow-up owner
- next action

## Weekly review

Every Friday:

- count toolkit requests
- count qualified workflow leads
- count discovery calls booked
- count sprint proposals sent
- count sprint wins
- identify highest-converting content/source
- update the next week's outreach and content based on actual lead pain

## Lost-lead review

Every two weeks, inspect leads that did not convert.

| Pattern | Likely fix |
| --- | --- |
| Too many vague toolkit leads | Make the page ask for a named workflow before download |
| Many calls, few proposals | Add budget/urgency confirmation earlier |
| Proposals stall | Proposal lacks ROI, scope boundary, or implementation next step |
| Leads want free consulting | Tighten first response and point to self-serve assets |
| Wrong industries | Adjust content examples and outbound targeting |
| No urgency | Add pain-specific CTAs around slow bids, lost leads, reporting drag, and owner bottlenecks |

## First 72-hour lead process

```text
Hour 0:
- form submitted
- confirmation page shows resources and asks for one workflow example

Hour 0-4:
- score lead
- send matching first response
- update CRM next action

Hour 24:
- if qualified and no reply, send one clarifying question

Hour 48:
- send relevant resource, example, or worksheet

Hour 72:
- if no engagement, move to nurture
- if engagement, book call or ask for example
```
