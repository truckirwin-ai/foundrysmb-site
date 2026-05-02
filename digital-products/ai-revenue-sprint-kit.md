# AI Revenue Sprint Kit

Free operating guide for choosing the first workflow that can make AI pay.

## Who this is for

Use this if you run an owner-led business and feel pressure from manual work, missed follow-up, inconsistent admin, slow proposals, scattered company knowledge, or reporting that depends on one person's memory.

This is not for learning every AI tool. It is for deciding where AI belongs in the business.

## The promise

In 90 minutes, you should be able to:

- name three candidate workflows
- score them against cost, repetition, data, risk, and authority
- pick the one most likely to pay
- define the first usable AI-assisted version
- decide whether to self-install, book a sprint, or leave it alone

## Core principle

Do not start with a tool.

Start with a workflow where better speed, accuracy, consistency, or follow-up would create measurable business value.

Beginner mistake:

> "How can we use ChatGPT?"

Operator question:

> "Which workflow is costing money because the team cannot move, decide, write, retrieve, or follow up consistently?"

## The Foundry workflow screen

Score each candidate workflow from 1 to 5.

| Dimension | 1 point | 3 points | 5 points |
| --- | --- | --- | --- |
| Business cost | Annoying but cheap | Costs several hours/week | Delays revenue, cash, delivery, or owner time |
| Repetition | Rare | Monthly or ad hoc | Weekly/daily with similar structure |
| Inputs exist | Mostly in someone's head | Some examples exist | Emails, docs, spreadsheets, notes, examples exist |
| Review is possible | Hard to judge output | Owner can review quality | Clear pass/fail criteria exists |
| Workflow owner | Nobody owns it | Shared responsibility | One person can approve changes |
| Risk level | Customer/legal/financial risk high | Moderate risk with review | Safe if reviewed before use |
| Implementation drag | Requires major software change | Requires light tool setup | Can start with docs, prompts, spreadsheet, or SOP |
| Follow-on value | One-time cleanup | Useful if maintained | Can become install/managed ops/recurring asset |

Interpretation:

- 32-40: strong sprint candidate
- 24-31: possible, but narrow scope first
- 16-23: toolkit/self-audit candidate
- under 16: do not automate yet

## The six workflow types that usually pay first

### 1. Proposal and bid assembly

Symptoms:

- estimates take too long
- scope questions are inconsistent
- follow-up happens late
- old examples are hard to find
- owner has to rewrite everything

AI role:

- extract project details
- identify missing scope questions
- draft proposal structure
- compare against past projects
- draft follow-up
- produce internal bid-prep checklist

Human review:

- pricing
- exclusions
- scope
- legal/commercial language
- customer promises

### 2. Lead triage and follow-up

Symptoms:

- inbound leads sit too long
- good opportunities are not researched
- team does not know which leads matter
- follow-up is inconsistent

AI role:

- summarize lead
- classify fit
- draft reply
- create call prep notes
- identify missing data
- create CRM next step

Human review:

- fit score
- message tone
- qualification judgment
- priority

### 3. Reporting and client updates

Symptoms:

- weekly reports are rebuilt manually
- updates are late
- owner has to interpret raw notes
- clients ask for status repeatedly

AI role:

- convert raw updates into report draft
- identify blockers
- summarize decisions
- draft client-facing status
- create internal action list

Human review:

- accuracy
- commitments
- tone
- sensitive information

### 4. SOP and onboarding capture

Symptoms:

- "ask Sarah" is the operating system
- onboarding takes too long
- quality depends on who is working
- edge cases live in memory

AI role:

- turn expert walkthroughs into SOPs
- extract decision rules
- create checklists
- create training outline
- capture examples and exceptions

Human review:

- missing steps
- real-world exceptions
- compliance/safety issues

### 5. Inbox and admin triage

Symptoms:

- owner lives in email
- requests arrive without structure
- small tasks interrupt deep work
- no one knows what needs action

AI role:

- categorize messages
- draft replies
- identify deadlines
- extract tasks
- prepare decision queue

Human review:

- authority to respond
- customer sensitivity
- money/legal commitments

### 6. Knowledge retrieval and context vaults

Symptoms:

- company facts are scattered
- people cannot find past examples
- AI outputs are generic
- same questions get answered repeatedly

AI role:

- search and summarize source documents
- retrieve relevant examples
- answer from approved context
- identify missing documentation

Human review:

- source quality
- outdated facts
- confidential data

## The 90-minute workflow audit

### Minutes 0-10: Choose three candidates

Write down three workflows that are painful enough to discuss in a meeting.

Use this structure:

```text
Workflow:
Who owns it:
How often it happens:
What triggers it:
What output is expected:
What goes wrong:
What it costs:
```

### Minutes 10-30: Map the current workflow

For each workflow, map:

```text
Trigger:
Inputs:
Tools:
People involved:
Steps:
Decision points:
Review points:
Output:
Where work stalls:
Where errors happen:
Where money is delayed or lost:
```

### Minutes 30-50: Score the workflow

Use the Foundry workflow screen above. Be strict. A high score means the workflow is business-relevant and narrow enough to improve.

### Minutes 50-70: Define the first assisted version

Do not design the perfect system. Define the smallest version that changes the work.

Choose one:

- AI intake assistant
- prompt chain
- spreadsheet plus prompts
- report template
- proposal draft system
- SOP generator
- CRM follow-up assistant
- context vault
- client-update packet

Define:

```text
First version:
User:
Inputs:
AI output:
Human review:
Final output:
Pass/fail test:
```

### Minutes 70-90: Decide the path

Use this decision model:

| Condition | Decision |
| --- | --- |
| High cost, repeated weekly, examples exist, owner can approve | Book a Revenue Sprint |
| Useful but low urgency | Use the toolkit and self-install |
| Needs company knowledge first | Build Context Vault |
| High customer/legal/financial risk | Create SOP and review gates before AI |
| No clear owner or pass test | Do not automate yet |

## Prompt pack

Use these prompts with real but sanitized examples. Do not paste confidential customer, employee, medical, legal, financial, or regulated data into public AI tools.

### Workflow diagnosis prompt

```text
You are an operations analyst helping an owner-led business evaluate one workflow for AI assistance.

Workflow:
[describe workflow]

Current steps:
[list steps]

Inputs:
[list documents, notes, emails, spreadsheets, systems]

Problems:
[list delays, errors, rework, missed follow-up, owner bottlenecks]

Business impact:
[hours, missed revenue, slow cash, customer experience, quality risk]

Analyze:
1. What is the actual business problem?
2. Which parts are judgment, which parts are formatting, retrieval, summarization, drafting, or routing?
3. Where could AI help without removing human review?
4. What data/examples are required?
5. What are the main risks?
6. What is the smallest useful first version?
7. What should the human review before anything is sent to a customer?
8. What would be a good pass/fail test?

Return the answer as:
- Workflow diagnosis
- AI-fit opportunities
- Required inputs
- Human review gates
- First-version recommendation
- Risks
- Pass/fail test
```

### Workflow scoring prompt

```text
Score this workflow from 1 to 5 on each dimension:
- business cost
- repetition
- available inputs
- reviewability
- workflow ownership
- risk level
- implementation drag
- follow-on value

Explain each score in plain business language.

Then recommend one of:
- do not automate
- self-install with toolkit
- build context vault first
- book AI Revenue Sprint
- move directly to system install

Workflow details:
[paste details]
```

### First-version design prompt

```text
Design the smallest useful AI-assisted version of this workflow.

Constraints:
- No customer-facing output without human review.
- Prefer simple tools first: docs, spreadsheets, prompts, forms, email drafts, SOPs.
- Do not recommend complex software unless the workflow cannot work without it.
- The owner must be able to test this with one real example in under 30 minutes.

Return:
1. First-version name
2. User
3. Required inputs
4. AI steps
5. Human review steps
6. Final output
7. SOP draft
8. Pass/fail test
9. What to measure
10. What would justify a paid install
```

## Sprint readiness checklist

You are ready for a sprint when you have:

- one workflow, not a department
- one owner who can approve changes
- at least three real examples
- current tools listed
- a rough value estimate
- clear review authority
- a pass/fail test
- time to review the prototype during the sprint

You are not ready when:

- the goal is "use AI"
- the workflow has no owner
- no examples exist
- nobody can review quality
- the team wants a platform before a process
- success is not measurable

## What to bring into a Foundry sprint

- three real examples
- screenshots of current tools
- current templates
- recent email chains
- spreadsheets or reports
- current SOPs, even bad ones
- notes from the person who does the work
- estimate of hours lost or revenue delayed

## The operator mindset

AI is not the operating system. The business is the operating system.

AI becomes useful when it is placed inside:

- clear inputs
- narrow workflow
- source context
- review gates
- documented procedure
- measurable output

That is what this kit is built to find.
