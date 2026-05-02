# Contractor Bid Automation Starter Pack

Free operating guide for turning scattered lead notes into a cleaner bid-prep workflow.

## Who this is for

This pack is for contractors, remodelers, specialty trades, local service companies, and owner-led firms that quote custom work.

It is especially useful when:

- the owner or estimator is the bottleneck
- leads arrive through email, phone, website forms, texts, referrals, and photos
- bids are delayed because scope is unclear
- follow-up is inconsistent
- old jobs are hard to reuse as examples
- the team loses margin through missed exclusions, assumptions, or scope gaps

This does not replace estimator judgment. It helps create a better bid-prep packet so the estimator can work faster and with fewer misses.

## The promise

After using this pack, you should have:

- a standard bid intake structure
- a missing-scope question generator
- a project fit and priority score
- a bid-prep checklist
- a clarification email draft
- a follow-up sequence
- a basic SOP for saving bid context

## The bid desk workflow

The goal is not "automated estimating." That is dangerous for many businesses.

The first useful AI workflow is usually:

```text
Lead notes in
-> clean project summary
-> missing scope questions
-> risk and assumption flags
-> bid-prep checklist
-> client clarification email
-> follow-up sequence
-> saved project context
```

The human still owns:

- pricing
- feasibility
- exclusions
- site conditions
- schedule
- customer promises
- legal/commercial language

## Bid intake worksheet

Use this for every bid candidate.

```text
Lead source:
Date received:
Customer name:
Customer contact:
Project location:
Project type:
Requested timeline:
Budget mentioned:
Decision deadline:
Photos/files received:
Site visit required:

Customer goal:

Known scope:

Unknown scope:

Constraints:

Potential risks:

Similar past jobs:

Next action:
```

## Fit and priority score

Score from 1 to 5.

| Dimension | What to look for |
| --- | --- |
| Scope clarity | Do we understand what is being requested? |
| Customer fit | Is this the kind of customer/job we want? |
| Margin potential | Could this be profitable? |
| Timeline fit | Can we deliver when needed? |
| Strategic fit | Does this lead to more good work? |
| Information completeness | Do we have enough to estimate? |
| Competition intensity | Are we one of many low-bid vendors? |
| Follow-up value | Is this worth a structured pursuit? |

Interpretation:

- 32-40: prioritize bid-prep
- 24-31: clarify before bidding
- 16-23: proceed only if strategically useful
- under 16: politely decline or ask qualifying questions first

## Prompt pack

### Lead notes to bid summary

```text
You are helping a contractor prepare a bid intake packet.

Do not price the job. Do not invent facts. Do not make promises.

Lead notes:
[paste sanitized notes, email, call transcript, form response, photo descriptions]

Create:
1. Project summary
2. Known scope
3. Unknown scope
4. Customer constraints
5. Timeline concerns
6. Missing information
7. Risk flags
8. Suggested next action

Use plain language. Mark assumptions clearly.
```

### Missing-scope question generator

```text
Based on this project summary, create the questions we need answered before producing a responsible estimate.

Group the questions by:
- site conditions
- measurements/dimensions
- materials
- access/logistics
- schedule
- customer preferences
- exclusions and assumptions
- permits/HOA/inspection issues
- photos/files needed

Return no more than 15 questions.
Make them customer-friendly.

Project summary:
[paste summary]
```

### Bid-prep checklist

```text
Turn this project into an internal bid-prep checklist.

Include:
- documents/photos needed
- measurements needed
- site visit requirements
- pricing inputs
- subcontractor/vendor checks
- scope exclusions to consider
- schedule constraints
- risks to review with owner/estimator
- follow-up deadline

Project:
[paste project summary and scope questions]
```

### Clarification email draft

```text
Draft a concise email to the customer asking for missing information before we prepare the estimate.

Tone:
- professional
- clear
- not robotic
- helpful
- no pricing commitments

Include:
- thanks for reaching out
- short summary of our understanding
- grouped questions
- request for photos/files if needed
- next step after they reply

Project summary:
[paste summary]

Missing questions:
[paste questions]
```

### Follow-up sequence for open bids

```text
Create a follow-up sequence for this open bid.

Rules:
- Do not sound desperate.
- Do not discount.
- Add value or reduce friction in each message.
- Include day 2, day 7, day 14, and final close-the-loop message.

Project summary:
[paste summary]

Customer priorities:
[paste if known]

Bid status:
[sent / awaiting clarification / waiting after site visit]
```

### Past-job reuse prompt

```text
Compare this new project to the past job examples below.

Do not assume the jobs are identical.
Find useful similarities and differences.

New project:
[paste summary]

Past jobs:
[paste sanitized summaries]

Return:
1. Similar scope elements
2. Differences that may affect cost or schedule
3. Risks from past jobs to remember
4. Useful language or exclusions to reuse
5. Questions to ask before pricing
```

## Bid desk SOP

### Trigger

A new bid opportunity arrives through email, website form, phone call, referral, text, or field note.

### Owner

Estimator, owner, project manager, or assigned bid coordinator.

### Steps

1. Save the raw lead notes in the bid intake folder or CRM.
2. Fill out the bid intake worksheet.
3. Run the lead notes through the bid summary prompt.
4. Run the missing-scope question prompt.
5. Score the opportunity.
6. Decide:
   - decline
   - clarify
   - schedule site visit
   - prepare estimate
7. Draft the customer clarification email.
8. Estimator reviews and edits.
9. Send customer message or schedule next action.
10. Save final summary, questions, and decision in the project record.

### Review gates

Human review is required before:

- any customer-facing email is sent
- any price is shared
- any deadline is promised
- any scope is confirmed
- any exclusion is removed

## Bid context folder structure

```text
Bid Desk/
  00-Intake/
  01-Active Opportunities/
    Customer_Project_Date/
      raw-notes.md
      intake-worksheet.md
      ai-summary.md
      missing-questions.md
      photos/
      estimate-inputs/
      follow-up-log.md
  02-Sent Bids/
  03-Won Jobs/
  04-Lost Jobs/
  05-Past Examples/
  06-Templates/
```

## Follow-up log template

```text
Customer:
Project:
Bid sent:
Follow-up owner:

Day 2:
Message:
Response:
Next action:

Day 7:
Message:
Response:
Next action:

Day 14:
Message:
Response:
Next action:

Close-the-loop:
Outcome:
Reason won/lost:
Lessons:
Reusable context:
```

## Quality checklist

Before sending any bid-related message, confirm:

- customer name is correct
- project location is correct
- scope summary is accurate
- assumptions are labeled
- no invented facts appear
- no price is created by AI
- no timeline is promised without review
- exclusions are not softened by AI
- tone sounds like the company
- next action is clear

## What to measure

Track these for four weeks:

- time from lead received to first response
- time from lead received to bid-ready packet
- number of missing-scope items caught before estimating
- number of follow-ups sent on time
- open bid close rate
- lost bids due to slow response
- owner/estimator hours spent on prep

## When to turn this into a sprint

Book a sprint when:

- bids are a real revenue bottleneck
- at least five recent examples exist
- the same questions and errors repeat
- follow-up discipline matters
- estimator time is expensive
- there is one person who can approve the workflow

The sprint target should not be "automate estimating."

The better target is:

> Build a bid-prep operating system that turns messy lead notes into a reviewed estimate packet and follow-up path.
