# 30 Architecture and Modules

## System center
The center is the execution harness.

## Core modules
### Policy Graph
Defines nodes, transitions, required slots, allowed actions, and escalation conditions.

### Clarification Router
Checks whether enough information is available before action.

### Action Gating
Allows, denies, or escalates risky actions.

### Harness Runtime
Runs the loop from node selection to trace writing.

### Process Trace
Stores the whole execution path for replay and scoring.

### Eval Factory
Scores path quality, step coverage, and action order.

### Experience Loop
Turns outcomes into reusable improvements.

### Simulator
Creates normal and perturbed cases for offline testing.
