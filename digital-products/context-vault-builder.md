# Context Vault Builder for Small Business

Free operating guide for building the source-of-truth layer that makes AI useful inside a real business.

## Why this matters

Most AI output is generic because the assistant does not know the business.

It does not know:

- what you sell
- who you sell to
- how you price
- what you never promise
- what good work looks like
- how your team talks to customers
- what mistakes have happened before
- what edge cases matter
- where the rules live

The Context Vault fixes that.

It is not a document dump. It is a curated operating memory for AI-assisted work.

## Who this is for

Use this if your business depends on knowledge trapped in:

- owner memory
- old proposals
- emails
- spreadsheets
- Slack/Teams
- SOPs nobody trusts
- training docs
- project folders
- customer notes
- pricing rules
- expert judgment

## The promise

After using this guide, you should have:

- a clean folder structure
- a business facts file
- offer and service rules
- customer/project memory templates
- SOP capture workflow
- examples library
- AI usage rules
- review checklist
- maintenance cadence

## The Context Vault model

The vault has seven layers.

```text
01 Business Facts
02 Offers and Services
03 Customers and Markets
04 Work Examples
05 SOPs and Decision Rules
06 Voice and Communication
07 AI Usage and Review Rules
```

Each layer answers a different question:

| Layer | Question it answers |
| --- | --- |
| Business Facts | What is true about the business? |
| Offers and Services | What do we sell, include, exclude, and promise? |
| Customers and Markets | Who do we serve and what do they care about? |
| Work Examples | What does good work look like? |
| SOPs and Decision Rules | How do we do the work and make decisions? |
| Voice and Communication | How should we sound? |
| AI Usage and Review Rules | What can AI draft, and what must humans approve? |

## Folder structure

```text
Context Vault/
  00-Index.md
  01-Business-Facts/
    business-facts.md
    company-glossary.md
    tool-inventory.md
  02-Offers-and-Services/
    offer-catalog.md
    pricing-rules.md
    exclusions-and-boundaries.md
    guarantees-and-promises.md
  03-Customers-and-Markets/
    ideal-customers.md
    customer-objections.md
    industry-notes.md
    common-use-cases.md
  04-Work-Examples/
    good-proposals/
    good-emails/
    good-reports/
    good-projects/
    bad-examples-and-lessons/
  05-SOPs-and-Decision-Rules/
    workflow-sops/
    decision-rules/
    escalation-rules.md
    quality-standards.md
  06-Voice-and-Communication/
    brand-voice.md
    email-tone.md
    phrases-to-use.md
    phrases-to-avoid.md
  07-AI-Usage-and-Review/
    ai-usage-policy.md
    review-checklist.md
    approved-prompts/
    risk-register.md
```

## 00-Index.md template

```text
# Context Vault Index

Business:
Vault owner:
Last updated:
Review cadence:

## Most important files

- Business facts:
- Offer catalog:
- Pricing rules:
- Exclusions:
- Good examples:
- SOPs:
- AI review checklist:

## Current AI workflows

| Workflow | Owner | Source files | Review gate | Status |
| --- | --- | --- | --- | --- |

## Open gaps

| Missing context | Impact | Owner | Due date |
| --- | --- | --- | --- |
```

## Business facts template

```text
# Business Facts

Company name:
Location:
Service area:
Primary customers:
Secondary customers:
Core offers:
Notable differentiators:
Years in business:
Team size:
Operating model:
Primary tools:
Primary constraints:

## What we do

[Plain-English description]

## What we do not do

[Boundaries]

## What customers hire us for

[Buying triggers]

## What customers usually misunderstand

[Common confusion]

## Non-negotiables

[Quality, safety, legal, margin, schedule, brand, customer commitments]
```

## Offer catalog template

```text
# Offer Catalog

Offer name:
Buyer:
Problem solved:
Included:
Not included:
Typical timeline:
Typical price/range:
Required customer inputs:
Delivery process:
Common add-ons:
Common exclusions:
Risks:
Approval needed before promise:

## Good-fit customers

## Bad-fit customers

## Common objections

## Proof/examples
```

## Work example template

```text
# Work Example

Example name:
Date:
Customer type:
Workflow:
Why this is a good example:

## Input

[What came in]

## Process

[What we did]

## Output

[What went out]

## Quality notes

[Why it was good]

## Reusable language/rules

[What AI can learn from this]

## Do not copy

[Anything specific, private, outdated, or risky]
```

## SOP capture prompt

Use this after interviewing the person who knows the workflow.

```text
You are converting an expert walkthrough into a usable SOP.

Rules:
- Do not invent missing steps.
- Mark unknowns as questions.
- Separate judgment from routine tasks.
- Include review gates.
- Include tools, inputs, outputs, and exceptions.

Expert walkthrough:
[paste notes/transcript]

Create:
1. SOP title
2. Purpose
3. Trigger
4. Owner
5. Inputs required
6. Tools used
7. Step-by-step procedure
8. Decision points
9. Review gates
10. Common exceptions
11. Quality checklist
12. Questions for the expert
```

## Context extraction prompt

Use this to convert old documents into vault-ready context.

```text
Analyze this business document and extract reusable context.

Document:
[paste or summarize content]

Return:
- Business facts
- Offer/service rules
- Customer facts
- Pricing or scope rules
- Voice/tone examples
- Decision rules
- Good reusable language
- Risky or outdated language
- Questions to verify

Do not treat the document as current truth unless it is marked current.
```

## AI answer prompt using the vault

```text
Use only the context below unless you clearly mark an assumption.

Task:
[what you want]

Relevant vault context:
[paste selected context]

Required output:
[proposal/email/SOP/report/checklist/etc.]

Rules:
- Do not invent facts.
- If context is missing, ask questions.
- Mark assumptions.
- Preserve company voice.
- Follow exclusions and review rules.
- Create a human-review checklist at the end.
```

## AI usage policy template

```text
# AI Usage Policy

AI may draft:
- internal summaries
- checklists
- first-draft emails
- SOP drafts
- report drafts
- meeting notes
- project summaries
- research briefs

AI may not approve:
- pricing
- legal commitments
- customer promises
- medical, legal, financial, or regulated advice
- hiring/firing decisions
- safety-critical instructions
- final customer-facing outputs without review

Required review:
- accuracy
- source context
- tone
- confidential information
- commitments
- exclusions
- assumptions
```

## Vault quality checklist

Before using the vault for a workflow, confirm:

- files are current enough for the task
- outdated examples are marked
- private data is removed or protected
- offer rules are explicit
- exclusions are explicit
- good examples are labeled
- bad examples include lessons
- AI review rules are clear
- a human owns the workflow

## Maintenance cadence

Weekly:

- add new good examples
- add lost-job or error lessons
- update open questions

Monthly:

- review pricing/offer rules
- archive outdated docs
- update SOPs
- test one AI workflow against the vault

Quarterly:

- review AI usage policy
- remove stale context
- promote best examples
- update customer objections
- revise decision rules

## The vault maturity ladder

| Level | Description | What to do next |
| --- | --- | --- |
| 0 | Knowledge is scattered | Create folder structure |
| 1 | Basic facts exist | Add offer rules and examples |
| 2 | SOPs and examples exist | Add AI review policy |
| 3 | AI can draft from approved context | Add QA and measurement |
| 4 | Workflows run from vault context | Move to sprint/install |
| 5 | Vault is maintained monthly | Consider managed ops |

## The real lesson

AI does not need more enthusiasm. It needs context, constraints, examples, and review.

The Context Vault is the business memory layer that makes that possible.
