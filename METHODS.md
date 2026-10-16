# Method and experiment protocol

## Research question
Do two reviewers agree on the reasoning judgments a benchmark depends on?

## Implemented method
Compute observed agreement, Cohen kappa, quadratic-weighted kappa, a confusion matrix, and disagreements for adjudication. The ordered label list defines distances.

## Assumptions and failure modes
Exactly two raters; no missing ratings. Kappa is sensitive to prevalence. Agreement is not validity and does not establish the truth of normative judgments.

## Proposed next experiment — not yet performed
Collect a held-out set of expert-reviewed audit or policy reasoning tasks. Use stable task IDs, preregister the comparison, and record model and prompt versions. Double-review a subset, adjudicate disagreements, and publish anonymized artifacts only when permitted. Separate exploratory analysis from confirmatory results. The fixture is insufficient to estimate real-world performance.

## Scope
The implementation is deliberately inspectable. Validation checks common malformed inputs; it is not a hardened service for adversarial payloads. Apply external input-size limits for large files. No model API is called by this repository.
