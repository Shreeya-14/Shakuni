/**
 * Real Model Evaluation Metrics for Shakuni.
 * Extracted directly from evaluation/results/metrics.json and training artifacts.
 */

export const MODEL_SPECS = {
  modelType: 'Multinomial Logistic Regression (Softmax)',
  vectorizer: 'Sublinear TF-IDF (Unigrams & Bigrams)',
  vocabularySize: 4595,
  regularization: 'L2 Penalty (C = 1.0)',
  classWeights: 'Balanced',
  datasetSize: 280,
  categoriesCount: 7,
  samplesPerCategory: 40,
  splitRatio: 'Stratified 87.5% Train / 12.5% Test Holdout',
  randomState: 42
};

export const EVALUATION_METRICS = {
  accuracy: 0.9143,
  macroPrecision: 0.9238,
  macroRecall: 0.9143,
  macroF1: 0.9137,
  weightedPrecision: 0.9238,
  weightedRecall: 0.9143,
  weightedF1: 0.9137,

  perCategory: [
    {
      code: 'CAT-01',
      category: 'Normal / No Significant Manipulation',
      precision: 0.8333,
      recall: 1.0000,
      f1: 0.9091,
      support: 5
    },
    {
      code: 'CAT-02',
      category: 'Social Pressure',
      precision: 1.0000,
      recall: 1.0000,
      f1: 1.0000,
      support: 5
    },
    {
      code: 'CAT-03',
      category: 'Emotional Pressure',
      precision: 1.0000,
      recall: 1.0000,
      f1: 1.0000,
      support: 5
    },
    {
      code: 'CAT-04',
      category: 'Misleading Framing',
      precision: 1.0000,
      recall: 0.8000,
      f1: 0.8889,
      support: 5
    },
    {
      code: 'CAT-05',
      category: 'Selective Information',
      precision: 0.8333,
      recall: 1.0000,
      f1: 0.9091,
      support: 5
    },
    {
      code: 'CAT-06',
      category: 'Information Withholding',
      precision: 0.8000,
      recall: 0.8000,
      f1: 0.8000,
      support: 5
    },
    {
      code: 'CAT-07',
      category: 'Deceptive Persuasion',
      precision: 1.0000,
      recall: 0.8000,
      f1: 0.8889,
      support: 5
    }
  ],

  confusionMatrix: {
    labels: [
      'Normal',
      'Social',
      'Emotional',
      'Framing',
      'Selective',
      'Withholding',
      'Deceptive'
    ],
    fullLabels: [
      'Normal / No Significant Manipulation',
      'Social Pressure',
      'Emotional Pressure',
      'Misleading Framing',
      'Selective Information',
      'Information Withholding',
      'Deceptive Persuasion'
    ],
    // Rows = True Class, Columns = Predicted Class
    matrix: [
      [5, 0, 0, 0, 0, 0, 0],
      [0, 5, 0, 0, 0, 0, 0],
      [0, 0, 5, 0, 0, 0, 0],
      [0, 0, 0, 4, 0, 1, 0],
      [0, 0, 0, 0, 5, 0, 0],
      [1, 0, 0, 0, 0, 4, 0],
      [0, 0, 0, 0, 1, 0, 4]
    ]
  }
};
