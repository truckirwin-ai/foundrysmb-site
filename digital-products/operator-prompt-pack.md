# Operator Prompt Pack

Reusable prompt systems for business operators. These are not clever one-off prompts. They are working prompts for diagnosing workflows, capturing operating knowledge, creating reviewable outputs, and deciding where AI should change the way the business runs.

Use them in order. The early prompts create clarity. The middle prompts create usable operating assets. The advanced prompts help an owner redesign roles, decisions, data, and recurring value.

## Operating rules

1. Start with a real workflow, not a tool idea.
2. Use sanitized examples. Remove confidential data, private customer details, and credentials.
3. Tell the model what it may draft, summarize, classify, or recommend.
4. Tell the model what it may not decide.
5. Require assumptions, gaps, and risks to be labeled.
6. Require a human review gate for anything customer-facing, financial, legal, hiring-related, safety-related, or operationally risky.
7. Save good outputs, examples, definitions, and corrections back into the Context Vault.
8. Treat every prompt as versioned operating infrastructure. If it improves the work, name it, store it, and test it again.

## Level 1: Workflow clarity

These prompts turn vague business pain into a specific workflow that can be improved.

### 1. Workflow finder

```text
Act as an operations consultant for an owner-led business.

Business:
[describe business, customers, team, services, current tools]

Symptoms:
[list recurring complaints, delays, errors, missed follow-ups, owner bottlenecks, customer issues, reporting pain, proposal drag, handoff problems]

Find the five workflows most likely to be wasting time or money.

For each workflow, return:
- workflow name
- trigger
- owner
- current output
- likely cost of failure
- evidence needed
- whether AI could help draft, retrieve, summarize, classify, route, or QA
- why this should or should not be the first workflow

Then recommend the best first workflow to inspect.
Do not recommend software yet.
```

### 2. One-workflow narrowing

```text
Help me narrow this broad problem into one sprintable workflow.

Broad problem:
[describe]

Current examples:
[paste 2-3 sanitized examples or notes]

Return:
1. The narrowest useful workflow definition
2. What starts the workflow
3. What ends the workflow
4. Who owns it
5. Required inputs
6. Required output
7. What currently breaks
8. What a first AI-assisted version could produce
9. What must remain human judgment
10. The pass/fail test for a five-day prototype
```

### 3. Pain-to-money translation

```text
Translate this workflow pain into business value.

Workflow:
[describe]

Pain:
[describe what goes wrong]

Volume:
[weekly or monthly frequency]

People involved:
[roles and rough hourly cost if known]

Revenue or cash impact:
[missed leads, slow bids, delayed invoices, churn risk, rework, customer dissatisfaction, owner time]

Return:
- direct time cost
- indirect owner-load cost
- customer experience cost
- revenue speed impact
- quality/rework impact
- conservative monthly value range
- what would need to be measured to prove value
- whether the workflow justifies a free toolkit, paid sprint, install, or managed ops
```

### 4. Current-state process map

```text
Map this workflow as it actually runs today.

Raw description:
[paste notes, transcript, or rough steps]

Create:
1. Trigger
2. Inputs
3. Current steps
4. Handoffs
5. Decisions
6. Waiting points
7. Tools used
8. Outputs
9. Rework loops
10. Failure points
11. Owner bottlenecks
12. Customer-visible pain

Then mark each step as:
- human judgment
- admin support
- retrieval/context lookup
- drafting/summarization
- routing/classification
- QA/review
- not worth automating
```

### 5. Root-cause teardown

```text
Teardown this workflow and find the real cause of the pain.

Workflow:
[describe]

Known failures:
[list]

Current tools:
[list]

Return:
- visible symptoms
- likely root causes
- missing context
- unclear ownership
- weak decision rules
- bad handoffs
- overreliance on owner memory
- tool/process mismatch
- what should change before AI is added
- where AI could make the problem worse
- where AI could safely create leverage
```

### 6. Workflow readiness score

```text
Score this workflow for AI-assisted improvement.

Workflow:
[describe]

Score 1-5 and explain:
- business value
- frequency
- input availability
- output reviewability
- risk level
- decision clarity
- owner availability
- adoption likelihood
- data/context quality
- implementation drag

Return:
- total score
- red flags
- missing prerequisites
- best first version
- recommended next step: ignore, self-install, sprint, install, or managed ops
```

### 7. First-version scope guard

```text
Prevent this project from getting too big.

Desired workflow improvement:
[describe]

Ideas already on the table:
[list features, tools, automations, integrations, dashboards, agents]

Define the smallest first version that creates real value.

Return:
- what is in scope
- what is explicitly out of scope
- first usable output
- required examples
- manual steps we should keep for now
- review gate
- success metric
- stop condition
- what can wait until install or managed ops
```

## Level 2: Build the operating asset

These prompts turn a chosen workflow into assets a team can actually use.

### 8. Context vault blueprint

```text
Design a Context Vault for this workflow.

Workflow:
[describe]

Outputs we need AI to help produce:
[list]

Existing materials:
[proposals, emails, SOPs, spreadsheets, policies, examples, reports, FAQs, pricing rules, customer notes]

Return a vault structure with:
- source folders
- approved examples
- definitions/glossary
- decision rules
- exclusions and boundaries
- tone/voice examples
- customer-specific facts
- project or job history
- review checklist
- stale-content review schedule

Then list the minimum context needed before the workflow can be tested.
```

### 9. SOP generator

```text
Turn this workflow into an SOP a trained teammate could follow.

Inputs:
[paste current notes]

SOP format:
1. Purpose
2. Trigger
3. Owner
4. Required inputs
5. Tools
6. Steps
7. Decision points
8. AI-assist points
9. Human review gates
10. Common exceptions
11. Quality checklist
12. Escalation rules
13. Metrics
14. Change log

Mark unclear items as questions.
Do not hide ambiguity.
```

### 10. Prompt chain designer

```text
Design a prompt chain for this workflow.

Workflow:
[describe]

Input examples:
[paste]

Desired final output:
[describe]

Return a chain with:
- Prompt 1: intake cleanup
- Prompt 2: context retrieval questions
- Prompt 3: first draft or analysis
- Prompt 4: quality review against rules
- Prompt 5: final human-review packet

For each prompt include:
- purpose
- required input
- exact prompt text
- expected output format
- human review question
- failure mode to watch
```

### 11. Customer-facing draft with guardrails

```text
Draft a customer-facing message.

Context:
[paste approved context]

Message purpose:
[state purpose]

Tone:
[direct/helpful/professional/etc.]

Rules:
- Do not make promises not present in context.
- Do not include pricing unless provided.
- Do not soften exclusions.
- Mark assumptions.
- End with a clear next action.

After the draft, include:
- facts to verify
- commitments made
- risks
- recommended human edits
- review checklist
```

### 12. Executive decision brief

```text
Create an executive decision brief for a busy owner.

Raw notes:
[paste notes]

Decision needed:
[state if known]

Return:
- situation
- decision needed
- options
- tradeoffs
- risks
- recommended path
- what happens if no decision is made
- next actions
- owner approval required

Keep it direct. No motivational language.
```

### 13. QA reviewer

```text
Review this AI-assisted workflow output before a human uses it.

Workflow purpose:
[describe]

Source context:
[paste or summarize]

AI output:
[paste]

Review against:
- factual accuracy
- source support
- missing assumptions
- unsupported promises
- tone
- completeness
- decision boundaries
- customer risk
- legal/financial/safety risk
- format usefulness

Return:
- pass/fail
- issues by severity
- corrected version if safe
- questions for human review
- what context should be added to prevent this next time
```

### 14. Exception handler

```text
Build an exception-handling guide for this workflow.

Workflow:
[describe]

Common weird cases:
[list or paste examples]

Return:
- normal path
- exception categories
- how to identify each exception
- who decides
- what AI may draft or summarize
- what AI must not decide
- escalation path
- customer communication template
- log fields for future improvement
```

### 15. Handoff packet builder

```text
Create a handoff packet for a teammate who must run this workflow.

Workflow:
[describe]

Current assets:
[SOP, prompt, examples, tools, context, known issues]

Return:
- workflow summary
- what good looks like
- required inputs
- step-by-step operating instructions
- AI-assist instructions
- quality checks
- examples of acceptable output
- examples of unacceptable output
- escalation rules
- first-week adoption checklist
```

## Level 3: Business transformation prompts

These prompts move beyond "use AI here" and ask how the business should operate differently.

### 16. Role redesign around AI leverage

```text
Analyze how this workflow changes team roles when AI is used responsibly.

Workflow:
[describe]

Team roles:
[list]

Current responsibilities:
[list]

AI-assisted first version:
[describe]

Return:
- work AI can support
- work humans should stop doing manually
- work humans should do more carefully
- new review responsibilities
- new context-maintenance responsibilities
- role changes by person/team
- training needed
- adoption risks
- management cadence needed
- what the owner must still own
```

### 17. Operating-model redesign

```text
Redesign this workflow as part of the company's operating model.

Business:
[describe]

Workflow:
[describe]

Current operating model:
[how work is assigned, tracked, reviewed, measured, and improved]

Return:
- new operating principle
- new workflow map
- new owner/reviewer roles
- context vault requirements
- prompt/SOP requirements
- measurement cadence
- management meeting rhythm
- recurring improvement loop
- what should become a company standard
- what should remain custom per client/job/project
```

### 18. Data and context maturity assessment

```text
Assess whether this business has the data/context maturity for AI workflows.

Business:
[describe]

Current assets:
[SOPs, CRM, project files, proposals, reports, templates, emails, spreadsheets, knowledge base]

Return a maturity score from 1-5 for:
- source availability
- source quality
- ownership
- freshness
- retrieval
- naming/structure
- examples
- decision rules
- review history
- privacy/security boundaries

Then return:
- biggest blockers
- fastest improvements
- minimum viable context vault
- 30-day context improvement plan
- workflows that should wait
```

### 19. AI risk boundary designer

```text
Define the risk boundaries for this AI-assisted workflow.

Workflow:
[describe]

Potential outputs:
[list]

Customer/business risk:
[describe]

Return:
- decisions AI may never make
- content AI may draft only with review
- information AI may summarize
- information AI must not access
- required disclaimers or internal warnings
- approval path
- audit log fields
- failure escalation
- kill switch condition
- safe test examples
```

### 20. Recurring-revenue expansion finder

```text
Look at this completed workflow improvement and identify recurring value.

Workflow improved:
[describe]

Sprint/install output:
[what was built]

Client usage:
[how often, who uses it, early results]

Remaining pain:
[list]

Return:
- monthly maintenance needs
- context updates needed
- measurement needs
- adoption support needed
- adjacent workflows
- backlog items
- managed ops scope
- renewal proof metrics
- expansion offer recommendation
- what to avoid selling too early
```

### 21. Transformation roadmap

```text
Create a 90-day AI operating roadmap for an owner-led business.

Business:
[describe]

Current workflows:
[list]

Constraints:
[budget, tools, staff, owner availability, data quality, risk]

Known opportunities:
[list]

Build a roadmap with:
- first workflow to improve
- why it comes first
- 5-day sprint outcome
- 30-day install/adoption plan
- 60-day second workflow or managed ops focus
- 90-day operating-system milestone
- required assets
- owner responsibilities
- team responsibilities
- metrics
- risks
- decisions not to make yet

The roadmap must prioritize cash, owner time, customer experience, and repeatable operating discipline.
```

## Prompt improvement loop

Use this after an AI output is wrong.

```text
The output below failed.

Original prompt:
[paste]

AI output:
[paste]

Why it failed:
[accuracy, tone, missing context, bad assumptions, wrong format, unsafe recommendation]

Relevant correct context:
[paste]

Improve the prompt so the next output is safer and more useful.

Return:
- revised prompt
- missing context to add to the vault
- review checklist item to prevent this failure
- test case to run before using this prompt again
```

## Good output standard

A useful AI output is:

- specific to the business
- traceable to source context
- reviewable by a human
- formatted for the next step
- explicit about assumptions
- clear about what it cannot decide
- easy to correct and reuse
- connected to a workflow metric
- stored back into the operating system when it works
