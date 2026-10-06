# Constructed smoke fixtures

The CSVs contain 18 training examples and nine test examples authored for this
repository. Each split has equal support for negative, neutral, and positive.
Labels mean unfavorable evaluation, no expressed evaluation, and favorable
evaluation of the whole text. These are deliberately simple illustrations,
with overlapping vocabulary between distinct sentences. They are not sampled
from a published corpus or validated by independent annotators.

Use them to verify training, split checks, prediction, and artifact writing.
Their scores cannot establish research performance, domain transfer, or model
superiority. Do not tune prompts or models on them for a subsequent benchmark.

Required columns are `id,text,label`; optional `group_id` groups documents/events
that must stay in one split. The runner rejects duplicate IDs, duplicate text
after case/whitespace normalization, and cross-split ID/text/group overlap.
Near-duplicate detection and chronological splitting require dataset preparation
outside this runner.
