# Shakuni Research Dataset: Curation & Provenance Report

**Total Samples:** 529  
**Train Samples (70%):** 370  
**Validation Samples (15%):** 79  
**Test Samples (15%):** 80  
**Random Seed:** 42  
**Source Provenance:** `synthetic/curated research examples`  

## 1. Class Distribution Across Splits

| Category | Total | Train | Validation | Test |
|:---|:---:|:---:|:---:|:---:|
| **Normal / No Significant Manipulation** | 109 | 76 | 16 | 17 |
| **Social Pressure** | 70 | 49 | 11 | 10 |
| **Emotional Pressure** | 70 | 49 | 11 | 10 |
| **Misleading Framing** | 70 | 49 | 10 | 11 |
| **Selective Information** | 70 | 49 | 10 | 11 |
| **Information Withholding** | 70 | 49 | 10 | 11 |
| **Deceptive Persuasion** | 70 | 49 | 11 | 10 |

## 2. Methodology & Linguistic Coverage

The dataset addresses previous lexical trapping and false positive triggers by expanding coverage of:
- **Everyday Neutral Announcements:** Routine meeting notices, deadlines, and schedule adjustments.
- **Ordinary Requests & Instructions:** Polite workplace questions, technical reviews, and coordination.
- **Subjective Emotions Without Coercion:** Stress, worry, and disappointment expressed without interpersonal manipulation.
- **Legitimate Persuasion:** Rational technical and economic arguments grounded in evidence.
- **Balanced Discussions:** Nuanced pros and cons analysis contrasting with false dichotomies.
- **Hard Negatives:** Benign sentences containing high-frequency words (`everyone`, `all`, `CEO`, `decision`, `urgent`).
- **Zero Data Leakage:** Preprocessing and vocabulary are strictly learned from the 70% training split only.
