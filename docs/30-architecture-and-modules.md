# 30 Architecture and Modules

## System center of gravity
The center is the execution harness, not a giant prompt.

## Modules
### Policy Graph
Defines nodes, guards, transitions, and escalation points.

### Clarification Router
Decides whether more information is needed before action.

### Action Gating
Controls risky actions with explicit allow or deny logic.

### Harness Runtime
Runs the loop: state -> clarify or act -> trace.

### Process Trace
Stores every step for replay and scoring.

### Experience Loop
Turns outcomes and evaluation signals into reusable updates.

### Simulator
Builds synthetic and perturbed cases for offline testing.
