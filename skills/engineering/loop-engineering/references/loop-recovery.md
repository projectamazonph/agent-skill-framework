# Loop Recovery

## Failure Classification

| Failure | Signal | Next move |
| --- | --- | --- |
| Wrong hypothesis | Focused evidence cleanly disproves the expected cause | Record refutation; choose a new diagnostic loop |
| Invalid observation | Test or metric cannot distinguish causes | Add one narrower observation point |
| Oversized loop | Several behaviors or modules move together | Split by outcome, boundary, or caller |
| Broken baseline | Failure existed before the change | Isolate and report; repair only if in scope |
| Environment fault | Dependency, permission, service, or tool prevents evidence | Verify configuration; report material blocker |
| Architecture resistance | Small behavior needs broad mocking or edits | Return to SOLID change mapping |
| Hidden contract | Focused pass but broader regression fails | Capture the failing contract and add a regression loop |
| Flaky evidence | Result changes without relevant code change | Control time, state, concurrency, network, or randomness |

## Repetition Guard

After two materially similar failed loops:

1. Stop repeating the same class of change.
2. Compare the two hypotheses, actions, and outputs.
3. Identify the assumption shared by both attempts.
4. Add an observation that can falsify that assumption.
5. Reduce scope or return to architecture shaping.

Do not use arbitrary additional retries as evidence.

## Focused Pass, Broad Failure

1. Preserve the broad failure output.
2. Find the nearest boundary where expected and actual behavior diverge.
3. Add the smallest reproducing test at that boundary.
4. Classify whether the cause is a missing contract, shared state, side effect, compatibility issue, or environment difference.
5. Repair through a new atomic TDD loop.

## Flake Recovery

Control or observe:

- Clock and timezone
- Random seeds and generated IDs
- Parallel execution and race conditions
- Shared database or filesystem state
- Network availability and rate limits
- Test order and leaked globals

Quarantine only when repository policy permits and the task records ownership and remediation. Do not call a relevant flaky suite green.

## Safe Experiment Rollback

Remove only changes introduced by the failed experiment using a precise patch. Re-run the baseline evidence. Preserve unrelated user changes and successful earlier loops.
