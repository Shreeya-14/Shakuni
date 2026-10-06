/**
 * Centralized Category Definitions for Shakuni Frontend.
 * Synchronized with backend ai_engine/classifier/categories.py.
 */

export const CATEGORIES_DATA = [
  {
    id: 'normal',
    code: 'CAT-01',
    num: '01',
    name: 'Normal / No Significant Manipulation',
    shortName: 'Normal Communication',
    themeClass: 'normal',
    riskTier: 'Low',
    riskScoreRange: '0 – 39',
    baseRiskWeight: 10.0,
    tagline: 'Transparent, objective, and neutral communication.',
    description: 'Standard, neutral, objective, or transparent communication exhibiting no significant coercive, deceptive, or manipulative tactics.',
    whatModelLooksFor: 'Balanced clauses, neutral verbs, lack of urgent coercion, qualified assertions with transparent rationale, absence of forced dilemmas.',
    typicalIndicators: [
      'Objective tone',
      'Factual assertions',
      'Unforced conditional statements',
      'Balanced presentation',
      'Clear attribution'
    ],
    example: 'The scheduled software release has been postponed to Tuesday to complete standard regression testing.',
    relatedCategories: ['Selective Information', 'Misleading Framing'],
    riskInterpretation: 'Minimal risk of undue influence. Text presents information neutrally without emotional or social coercion.'
  },
  {
    id: 'social_pressure',
    code: 'CAT-02',
    num: '02',
    name: 'Social Pressure',
    shortName: 'Social Pressure',
    themeClass: 'social',
    riskTier: 'Moderate',
    riskScoreRange: '40 – 69',
    baseRiskWeight: 65.0,
    tagline: 'Appeals to herd conformity and fear of isolation.',
    description: 'Communication that leverages bandwagon appeals, peer conformity, social shaming, consensus coercion, or fear of ostracization.',
    whatModelLooksFor: 'Consensus assertions, in-group vs out-group comparisons, warnings of professional or reputational isolation for dissent.',
    typicalIndicators: [
      'Bandwagon appeals ("everyone has already signed")',
      'Consensus claims ("unanimous consensus")',
      'Conformity enforcement ("don\'t be the lone dissenter")',
      'Fear of exclusion ("holding us back")',
      'In-group vs out-group framing'
    ],
    example: "Everyone on the executive team has already signed the loyalty agreement; don't be the lone dissenter holding us back.",
    relatedCategories: ['Emotional Pressure', 'Misleading Framing'],
    riskInterpretation: 'Moderate to high risk. Pressures recipient to yield to perceived group norms rather than rational independent evaluation.'
  },
  {
    id: 'emotional_pressure',
    code: 'CAT-03',
    num: '03',
    name: 'Emotional Pressure',
    shortName: 'Emotional Pressure',
    themeClass: 'emotional',
    riskTier: 'High',
    riskScoreRange: '70 – 100',
    baseRiskWeight: 72.0,
    tagline: 'Exploits guilt, loyalty, and manufactured urgency panic.',
    description: 'Communication relying on guilt trips, fear appeals, affective blackmail, urgency panic, or sympathy exploitation to force compliance.',
    whatModelLooksFor: 'Direct appeals to personal obligation, existential panic triggers, claims of catastrophic interpersonal consequences.',
    typicalIndicators: [
      'Guilt-inducing wording ("if you really cared")',
      'Emotional consequence ("you\'ll break our hearts")',
      'Urgency panic ("act right now or ruin occurs")',
      'Fear appeals',
      'Affective obligation'
    ],
    example: "If you really loved our family and cared about our happiness, you wouldn't accept that overseas job offer.",
    relatedCategories: ['Social Pressure', 'Deceptive Persuasion'],
    riskInterpretation: 'High risk. Bypasses critical cognitive deliberation by provoking acute distress, guilt, or fear of emotional abandonment.'
  },
  {
    id: 'misleading_framing',
    code: 'CAT-04',
    num: '04',
    name: 'Misleading Framing',
    shortName: 'Misleading Framing',
    themeClass: 'framing',
    riskTier: 'Moderate',
    riskScoreRange: '40 – 69',
    baseRiskWeight: 60.0,
    tagline: 'Shapes decisions via false dilemmas and loaded language.',
    description: 'Presents information with biased context, false dichotomies, loaded terminology, or slanted narrative structures to skew perception.',
    whatModelLooksFor: 'Polarized either/or constructions, loaded adjective pairings, presupposition traps that eliminate moderate alternatives.',
    typicalIndicators: [
      'False dichotomy ("either you are with us or")',
      'Loaded terminology ("reckless experimentation")',
      'Euphemistic recontextualization',
      'Presupposition traps',
      'Biased perspective anchoring'
    ],
    example: "You are either completely with our bold organizational turnaround strategy, or you actively want the company to fail.",
    relatedCategories: ['Selective Information', 'Deceptive Persuasion'],
    riskInterpretation: 'Moderate to high risk. Distorts decision space by artificially constraining choices and presenting distorted realities.'
  },
  {
    id: 'selective_information',
    code: 'CAT-05',
    num: '05',
    name: 'Selective Information',
    shortName: 'Selective Information',
    themeClass: 'selective',
    riskTier: 'Moderate',
    riskScoreRange: '40 – 69',
    baseRiskWeight: 52.0,
    tagline: 'Cherry-picks favorable statistics while omitting counter-evidence.',
    description: 'Cherry-picks favorable facts, isolated statistics, or one-sided testimonies while systematically ignoring counter-evidence.',
    whatModelLooksFor: 'Isolated percentage surges without sample sizes, dramatic superlative claims, deliberate absence of baseline controls.',
    typicalIndicators: [
      'Cherry-picked statistics ("400% surge in controlled tests")',
      'Omission of counter-evidence',
      'One-sided testimonials',
      'Unqualified superlative claims',
      'Favorable segment isolation'
    ],
    example: "Our revolutionary battery technology demonstrated a four hundred percent charge retention in controlled lab tests.",
    relatedCategories: ['Information Withholding', 'Misleading Framing'],
    riskInterpretation: 'Moderate risk. Misguides judgment by presenting genuine but incomplete facts that paint a deceptive overall picture.'
  },
  {
    id: 'information_withholding',
    code: 'CAT-06',
    num: '06',
    name: 'Information Withholding',
    shortName: 'Information Withholding',
    themeClass: 'withholding',
    riskTier: 'High',
    riskScoreRange: '70 – 100',
    baseRiskWeight: 75.0,
    tagline: 'Conceals adverse terms and prerequisites until commitment.',
    description: 'Strategically conceals crucial caveats, hidden costs, adverse consequences, conflict of interest, or relevant context to prevent informed consent.',
    whatModelLooksFor: 'Vague deferral phrases, promises to configure drawbacks later, intentional silence regarding contractual dependencies.',
    typicalIndicators: [
      'Conspicuous vagueness ("standard minor details")',
      'Buried caveats ("will address during maintenance")',
      'Absence of mandatory disclosures',
      'Incomplete prerequisites',
      'Silence on material drawbacks'
    ],
    example: "The platform upgrade will go live at midnight as agreed. We will address any pending secondary configuration items during later maintenance cycles.",
    relatedCategories: ['Selective Information', 'Deceptive Persuasion'],
    riskInterpretation: 'High risk. Undermines autonomy by preventing the recipient from knowing critical decision-altering facts prior to commitment.'
  },
  {
    id: 'deceptive_persuasion',
    code: 'CAT-07',
    num: '07',
    name: 'Deceptive Persuasion',
    shortName: 'Deceptive Persuasion',
    themeClass: 'persuasion',
    riskTier: 'High',
    riskScoreRange: '70 – 100',
    baseRiskWeight: 88.0,
    tagline: 'Fabricates authorization and artificial urgency.',
    description: 'Active construction of false narratives, fabricated authority, deliberate deception techniques, disingenuous promises, or multi-layered pretexting.',
    whatModelLooksFor: 'Claims of direct executive override, unvetted emergency approvals, demands to circumvent compliance and protocols.',
    typicalIndicators: [
      'Fabricated authority ("CEO directly authorized")',
      'Unverifiable guarantees ("guaranteed exception")',
      'Pretextual emergency urgency ("wire transfer immediately")',
      'Fraudulent assurance ("bypass compliance reviews")',
      'Calculated misrepresentation'
    ],
    example: "I just spoke directly with the CEO, and she authorized us to bypass standard compliance reviews for this wire transfer.",
    relatedCategories: ['Emotional Pressure', 'Information Withholding'],
    riskInterpretation: 'Severe risk. Employs sophisticated, multi-layered stratagems designed to actively mislead the target into rapid compliance.'
  }
];

export const CATEGORY_BY_NAME = Object.fromEntries(
  CATEGORIES_DATA.map((c) => [c.name, c])
);
