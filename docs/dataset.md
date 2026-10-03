# Shakuni Research Dataset Documentation

## 1. Dataset Origin & Academic Disclosure

The primary dataset (`data/raw/manipulation_dataset.csv`) and the held-out benchmark evaluation set (`evaluation/test_cases/evaluation_cases.csv`) consist of:
**`synthetic/curated research examples`**.

### Methodological Rationale
- **Privacy & Safety**: Ingesting unconsented private email or messaging logs presents severe privacy violations and potential ethical harm.
- **Controlled Typology**: Live scraped social media datasets frequently conflate toxicity, profanity, and sarcasm. Curated examples allow precise isolation of subtle manipulative structures (e.g. false dilemmas, buried caveats, consensus coercion) without confounding noise.
- **Reproducibility**: The dataset provides an open, deterministic benchmark that can be audited and extended by independent researchers.

---

## 2. Dataset Composition

The training dataset contains **280 balanced samples** (40 samples per category). The evaluation dataset contains **35 held-out samples** (5 per category).

| Index | Category | Training Samples | Evaluation Samples | Domain Themes |
|:---:|:---|:---:|:---:|:---|
| 1 | **Normal / No Significant Manipulation** | 40 | 5 | Technical releases, meeting minutes, quarterly updates, routine administrative notes |
| 2 | **Social Pressure** | 40 | 5 | Bandwagon claims, peer conformity, fear of professional isolation, group solidarity |
| 3 | **Emotional Pressure** | 40 | 5 | Moral guilt, affective blackmail, acute urgency, sympathy leverage, personal debt |
| 4 | **Misleading Framing** | 40 | 5 | False dichotomies, loaded terminology, euphemistic corporate speak, biased context |
| 5 | **Selective Information** | 40 | 5 | Cherry-picked percentages, isolated positive anecdotes, omission of negative variance |
| 6 | **Information Withholding** | 40 | 5 | Buried renewal clauses, unstated prerequisites, omission of negative contractual terms |
| 7 | **Deceptive Persuasion** | 40 | 5 | Fabricated executive directives, zero-risk guarantees, legal/regulatory pretexts |

---

## 3. CSV File Schema

```csv
id,text,category,source_type
1,"The scheduled software release has been postponed...",Normal / No Significant Manipulation,synthetic/curated research examples
```

- **`id`** (`integer`): Monotonically increasing identifier.
- **`text`** (`string`): The complete natural language utterance under evaluation.
- **`category`** (`string`): Ground truth label corresponding to one of the 7 canonical categories.
- **`source_type`** (`string`): Explicit provenance flag (`synthetic/curated research examples`).

---

## 4. Limitations of the Dataset

1. **Synthetic Style**: Utterances are concise and structured. In real-world multi-turn conversational threads, manipulation is often distributed over dozens of turns.
2. **Domain Representation**: Focuses primarily on corporate, interpersonal, and promotional contexts; legal and political legislative contexts require expanded specialized corpora.
3. **Language**: The initial release is curated in English. Cross-cultural manipulation idioms require multilingual expansions.
