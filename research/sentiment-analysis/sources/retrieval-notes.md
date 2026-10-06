# Retrieval and provenance

- Research/access date: **6 October 2026**, using the user's America/Toronto date.
- Scope: English text sentiment methods, financial sentiment, prompted LLM
  comparisons, efficiency, interpretability, calibration, and robustness.
  Multilingual/dialect papers were included where relevant to generalization.
- Discovery: foundational references, OpenAlex title-filtered searches for
  sentiment/LLM/financial/benchmark papers dated through 6 October 2026, and
  references in primary papers and their implementation repositories.
- Verification: original ACL Anthology pages, arXiv pages, the AAAI publisher
  page, official Notre Dame dictionary page, scikit-learn documentation,
  GitHub/Hugging Face project pages, and publisher-supplied Crossref metadata.
- Search results were used for discovery. Claims in the report use the primary
  source or official implementation rather than search-result snippets.
- This was a targeted review. It has no registered protocol, exhaustive database
  coverage, or systematic-review inclusion/exclusion counts.

## Review depth

The methods/results/limitations sections of full PDFs were inspected for
**R03, R12, R13, R24, R25, R26, R27, and R35**. The PDFs were downloaded into a
temporary research directory for text extraction; they are not redistributed
in this repository. Direct PDF links are included in the bibliography.

The extended review adds R38–R42. R40's full publisher HTML article
and result table were inspected; R41's official NIST section 3 and publication
page were inspected. R38, R39, and R42 were checked through primary
abstracts/metadata. R11's abstract was revisited to verify the contributed
distillation figures. R40 was published online on 2 July 2026, while its citation
metadata also lists a December 2026 issue date; both dates are distinguished in
the JSON record. It names an earlier 2025 conference version.

The earlier draft is preserved in
[the archive](../archive/README.md). It has numbered citations but no
reference list. New empirical additions were independently sourced rather than
assuming that those original numbers resolve to specific papers. Unidentified
study claims remain in the original contribution, with their status documented,
and were not adopted into the verified synthesis.

Other paper entries were reviewed through abstracts and bibliographic metadata.
R36 and R37 were checked through Crossref's publisher-supplied records, not
their full journal articles. Official code/model pages were inspected for
their purpose and artifact identity. No code from those repositories was run.

The JSON bibliography preserves URLs, author/title metadata, DOI where available,
review depth, and access status. It excludes copied full abstracts and page
contents. Some entries use a preprint publication date; this is distinguished
from conference/journal publication in the annotated reading notes. Live pages
can change after access. Repository commit snapshots provide a revision reference
without copying the repositories.

## Evidence boundaries

- Historical scores are explicitly attributed to the studied versions and tasks.
- 2025/2026 sources add contemporary evidence, but are not assumed to settle
  every deployment question. The evidence ledger identifies methodological
  concerns where observed.
- Hypothetical examples and cost calculations are labeled as such.
- No current provider price survey, latency measurements, trained baseline,
  API benchmark, or trading backtest was performed.
- Research summaries and recommendations are original synthesis. Numerical
  findings belong to the cited studies and were not reproduced locally.
