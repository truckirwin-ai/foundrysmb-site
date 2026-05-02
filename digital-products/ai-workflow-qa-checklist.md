# AI Workflow QA Checklist

Use this before an AI-assisted workflow becomes part of daily operations.

## 1. Workflow definition

- [ ] The workflow has one clear owner.
- [ ] The trigger is defined.
- [ ] Required inputs are listed.
- [ ] Expected output is defined.
- [ ] Human review gate is defined.
- [ ] Success metric is defined.
- [ ] The workflow is narrow enough to test with one real example.

## 2. Context quality

- [ ] Business facts are current.
- [ ] Offer/service rules are current.
- [ ] Pricing or scope rules are not left to AI.
- [ ] Good examples are included.
- [ ] Bad/outdated examples are marked.
- [ ] Confidential data is removed or protected.
- [ ] Source context is easy to find.

## 3. Prompt quality

- [ ] Prompt states the role and task.
- [ ] Prompt includes business context.
- [ ] Prompt defines what AI may not decide.
- [ ] Prompt requires assumptions to be labeled.
- [ ] Prompt specifies output format.
- [ ] Prompt requires review checklist.
- [ ] Prompt has been tested on at least three examples.

## 4. Output quality

- [ ] Output is specific, not generic.
- [ ] Output follows company voice.
- [ ] Output does not invent facts.
- [ ] Output does not create pricing unless supplied.
- [ ] Output does not make unauthorized promises.
- [ ] Output is formatted for the next human action.
- [ ] Output includes questions when context is missing.

## 5. Risk review

- [ ] No customer-facing message goes out without review.
- [ ] No legal, financial, medical, HR, or safety-critical decision is delegated to AI.
- [ ] No sensitive data is pasted into an unapproved AI system.
- [ ] Escalation rules exist for uncertain outputs.
- [ ] The team knows what AI is allowed to draft versus decide.

## 6. Adoption check

- [ ] The operator can run the workflow.
- [ ] The operator knows how to correct bad output.
- [ ] The corrected output gets saved back to the vault.
- [ ] The SOP is short enough to use.
- [ ] The owner can inspect results weekly.

## 7. Measurement

Track for four weeks:

- time saved
- cycle time
- error/rework reduction
- lead response speed
- bid/report/update completion rate
- owner hours recovered
- customer-facing quality

## Go/no-go decision

Go live only if:

- the workflow passed three real examples
- human review catches the high-risk items
- the operator can run it without Foundry in the room
- there is a clear way to improve prompts and context

If not, keep it in prototype mode.
