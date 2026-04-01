# 50 Reproduction and Experiment Plan

## Experiment order
1. Rule baseline
2. Static prompt baseline
3. Harness only
4. Harness plus process-feedback loop
5. Harness plus experience loop

## Offline case types
- normal path
- missing order id
- missing service time
- tool failure
- user changes request
- high emotion
- unreachable worker

## Ablations
- without policy graph
- without clarification
- without action gating
- without trace-based scoring
- without experience updates

## Desired outputs
- trace report
- compliance score
- error clusters
- recovery analysis
