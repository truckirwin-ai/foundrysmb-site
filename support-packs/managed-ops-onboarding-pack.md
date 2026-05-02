# Managed Ops Onboarding Pack

Use this after a sprint or install proves that a workflow deserves recurring support.

## Purpose

Managed AI Ops exists to keep workflows alive after launch.

The monthly work is not "support tickets." It is operating-system maintenance:

- prompt and SOP improvements
- context vault updates
- workflow QA
- measurement
- adoption support
- next-workflow backlog
- executive reporting

The monthly retainer should be sold only when there is a workflow worth maintaining. If the workflow does not run often, affect business value, or require recurring context/SOP/prompt improvement, do not force it into managed ops.

## Managed ops fit test

| Question | Good sign | Bad sign |
| --- | --- | --- |
| Does the workflow run weekly? | Repeated operating need | One-off project |
| Is there measurable value? | Time, speed, quality, revenue, owner load | "AI usage" only |
| Does context change? | New customers, jobs, reports, policies, examples | Static content |
| Is adoption still fragile? | Team needs support | Nobody will use it |
| Is there expansion potential? | Adjacent workflows visible | No next workflow |
| Is the client engaged? | Owner/reviewer attends cadence | No owner |

If four or more answers are good, managed ops is worth proposing.

## Onboarding checklist

Before monthly support starts, confirm:

- [ ] Installed workflow has a named owner.
- [ ] Current SOP exists.
- [ ] Prompt chain or automation path is documented.
- [ ] Source context is saved.
- [ ] Review gate is defined.
- [ ] Usage metric is defined.
- [ ] Business value metric is defined.
- [ ] Monthly cadence is scheduled.
- [ ] Backlog is started.
- [ ] Escalation path is clear.

## Client intake

```text
Client:
Primary owner:
Backup owner:
Workflow supported:
Current tools:
Current SOP location:
Context vault location:
Review cadence:
Monthly business goal:
Known risks:
Approval boundaries:
Communication channel:
Meeting cadence:
```

## Operating agreement

Before the first month starts, document:

- workflow covered
- monthly outcomes expected
- response expectations
- meeting cadence
- what Foundry owns
- what the client owns
- what requires client approval
- where context is stored
- where changes are logged
- what metrics will be reported
- what counts as out of scope

## RACI model

| Work | Foundry | Client owner | Client operator |
| --- | --- | --- | --- |
| Update prompt/SOP | Responsible | Approves | Uses |
| Add source context | Supports | Accountable | Provides |
| Review customer-facing output | No | Accountable | Responsible |
| Track usage | Responsible | Reviews | Provides inputs |
| Decide next workflow | Recommends | Accountable | Advises |
| Handle exceptions | Supports | Accountable | Escalates |
| Approve automation changes | Recommends | Accountable | Tests |

## Monthly operating cadence

Week 1:

- review usage
- inspect failures
- update prompts/SOPs
- confirm priorities

Week 2:

- improve one workflow step
- add examples to vault
- test revised output

Week 3:

- build or refine one backlog item
- train/retrain operator
- document adoption issues

Week 4:

- report results
- update ROI notes
- decide next month's focus
- identify install/expansion opportunities

## First 30 days

Week 0 setup:

- confirm scope and operating agreement
- collect current SOP, prompts, context, examples, and metrics
- define review gate
- set meeting calendar
- create backlog

Week 1 stabilize:

- inspect current use
- find failures and adoption friction
- patch prompt/SOP gaps
- confirm metric baseline

Week 2 improve:

- improve one high-friction step
- add 3-5 approved examples
- test revised output against real cases
- document changes

Week 3 adoption:

- train the operator
- observe one real use
- collect objections and workarounds
- update handoff notes

Week 4 prove:

- produce first monthly report
- compare baseline to current
- recommend next month focus
- identify expansion opportunity or stop condition

## Monthly report template

```text
# Managed Ops Monthly Report

Client:
Month:
Workflow:

## What ran

## What improved

## Issues found

## Context added

## Prompt/SOP changes

## Metrics

| Metric | Baseline | Current | Notes |
| --- | --- | --- | --- |

## Business impact

## Next month focus

## Decisions needed
```

## Workflow change log

```text
Date:
Workflow:
Change type: prompt / SOP / context / review / automation / metric
Reason for change:
Source evidence:
Before:
After:
Risk:
Reviewer:
Result:
Next watch item:
```

## Adoption interview

Ask the operator monthly:

- When did you use the workflow?
- Where did it help?
- Where did it slow you down?
- What output did you distrust?
- What did you still do manually?
- What context was missing?
- What would make this easier next week?
- Would you keep using it if nobody reminded you?

Ask the owner monthly:

- Did this reduce your direct involvement?
- Did quality improve?
- Did response speed improve?
- Did anything create risk?
- What would make this worth renewing?
- What workflow now looks like the next bottleneck?

## Backlog scoring

Score each improvement from 1 to 5.

| Dimension | Question |
| --- | --- |
| Value | Will this save time, improve quality, speed revenue, or reduce owner load? |
| Frequency | Does this happen often enough to matter? |
| Ease | Can we improve it without major systems work? |
| Risk | Can it be reviewed safely? |
| Adoption | Will the team actually use it? |

Work on high-value, high-frequency, low-drag improvements first.

## Backlog categories

- Prompt improvement
- SOP improvement
- Context vault cleanup
- Approved examples
- Review gate tightening
- User adoption/training
- Reporting/measurement
- Tool integration
- Adjacent workflow
- Expansion opportunity

## Expansion paths

| Signal | Possible expansion |
| --- | --- |
| Workflow is used weekly and saves owner time | Managed ops renewal |
| Same context could support another workflow | Second install |
| Team needs more standardization | SOP/context vault engagement |
| Reports are now easier but data intake is messy | Intake automation |
| Lead follow-up improved but quoting is slow | Bid/proposal workflow |
| Client asks for dashboard/reporting | Measurement/reporting add-on |

## Renewal proof

Every month should show at least one of:

- fewer owner hours
- faster response time
- more consistent follow-up
- better report quality
- cleaner SOPs
- improved team adoption
- reduced rework
- clearer next workflow backlog

If none of those are happening, the managed engagement needs to change or end.

## Stop conditions

End or redesign managed ops if:

- the workflow is not being used
- no owner attends review cadence
- there is no measurable business value
- Foundry is being asked to replace human judgment
- context cannot be maintained
- the client wants unlimited support outside the workflow
- the monthly report cannot name what improved

The discipline matters. Managed ops should feel like operating leverage, not an open-ended support bucket.
