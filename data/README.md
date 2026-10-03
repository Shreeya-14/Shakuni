# Shakuni Research Dataset

## Dataset Description & Provenance

This directory contains the training and evaluation datasets for the **Shakuni** strategic deception and information manipulation pattern analysis framework.

### Important Ethical & Methodological Disclosure
All data rows in `data/raw/manipulation_dataset.csv` and `evaluation/test_cases/evaluation_cases.csv` are explicitly categorized as:
`synthetic/curated research examples`.

**No claims are made that these examples were collected from private user surveillance or unauthorized communications.** The examples were systematically crafted and curated by researchers to represent canonical linguistic expressions across seven manipulation categories for academic NLP research and benchmarking.

## Categories & Distribution

The primary dataset contains 280 balanced samples (40 samples per category):

| # | Category | Sample Count | Domain Focus |
|---|---|---|---|
| 1 | Normal / No Significant Manipulation | 40 | Routine corporate, technical, academic, and administrative updates |
| 2 | Social Pressure | 40 | Bandwagon appeals, consensus coercion, peer conformity, ostracization fear |
| 3 | Emotional Pressure | 40 | Guilt trips, emotional blackmail, panic-inducing urgency, sympathy leverage |
| 4 | Misleading Framing | 40 | False dilemmas, euphemistic corporate speak, loaded labels, biased context |
| 5 | Selective Information | 40 | Cherry-picked metrics, isolated testimonials, omission of adverse facts |
| 6 | Information Withholding | 40 | Buried caveats, hidden recurring fees, unstated contractual restrictions |
| 7 | Deceptive Persuasion | 40 | Fabricated executive authority, false guarantees, impersonation, pretexting |

## Data Schema

The CSV files use the following schema:
- `id` (int): Unique numeric sample identifier.
- `text` (string): The natural language utterance to be analyzed.
- `category` (string): The ground-truth manipulation pattern category.
- `source_type` (string): Documentation tag (`synthetic/curated research examples`).

## Preprocessing Pipeline

During training, text undergoes:
1. Normalization (lowercasing, unicode cleanup, whitespace compaction).
2. TF-IDF feature extraction with word n-grams (1, 2) and sublinear term frequency scaling.
3. Stratified splitting (80% train, 20% test) with a fixed random seed (`42`) for full reproducibility.
