# 05 Agent Thesis Context Pack

## One-line thesis positioning
This project studies an execution harness for high-risk service agents in local-service fulfillment exception scenarios, with clarification-first control, process-aware evaluation, and experience-driven continual improvement.

## What this repository is trying to prove
1. A service agent should be evaluated by policy adherence and process quality, not only final response quality.
2. Clarification before action is a core capability in high-risk service workflows.
3. The main system asset is the execution harness, not a giant prompt.
4. Continual improvement should first happen through memory, strategy updates, and evaluation feedback, not frequent base-model retraining.

## Primary scenario
Fulfillment exception handling:
- urge arrival
- delay
- reschedule
- no-show

## Primary research object
Execution Harness:
- policy graph
- clarification router
- action gating
- process trace
- replayable runtime
- experience writeback

## Secondary research object
Continual Improvement Layer:
- strategy memory
- clarification preference updates
- recovery preference updates
- offline optimizer driven by execution feedback

## Primary baselines
- rule baseline
- static prompt baseline
- harness only

## Enhanced variants
- harness + process eval feedback
- harness + experience loop

## What stronger models should continue writing
### A. PolicyGraph branch
Need to implement:
- real node schema
- transition guards
- node-level risk policy
- scenario-specific graphs

### B. Clarification branch
Need to implement:
- ambiguity scoring
- clarification templates
- multi-turn missing-slot handling
- cost-aware clarification policy

### C. Eval branch
Need to implement:
- trace schema
- weighted compliance scoring
- judge interface
- replay runner

### D. Evolution branch
Need to implement:
- experience extraction
- strategy memory update
- clarification policy update
- recovery pattern mining

### E. Simulator branch
Need to implement:
- user simulator
- fault injector
- variant generator
- regression case pack

## Writing constraints for all future contributors
- Keep the thesis question narrow.
- Avoid turning this repo into a generic customer-service framework.
- Keep execution harness as the center of gravity.
- Continual improvement is an enhancement axis, not a replacement for the main problem.
