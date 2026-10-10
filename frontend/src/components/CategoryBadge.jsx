import React from 'react';
import { 
  ShieldCheck, 
  Users, 
  HeartHandshake, 
  Split, 
  BarChart2, 
  EyeOff, 
  AlertTriangle 
} from 'lucide-react';

const CATEGORY_MAP = {
  'Normal / No Significant Manipulation': {
    code: 'CAT-01',
    className: 'normal',
    icon: ShieldCheck,
    label: 'Normal / Neutral'
  },
  'No significant manipulation detected': {
    code: 'CAT-00',
    className: 'normal',
    icon: ShieldCheck,
    label: 'No Significant Manipulation'
  },
  'Insufficient evidence to classify': {
    code: 'CAT-UNC',
    className: 'normal',
    icon: ShieldCheck,
    label: 'Insufficient Evidence'
  },
  'Social Pressure': {
    code: 'CAT-02',
    className: 'social',
    icon: Users,
    label: 'Social Pressure'
  },
  'Emotional Pressure': {
    code: 'CAT-03',
    className: 'emotional',
    icon: HeartHandshake,
    label: 'Emotional Pressure'
  },
  'Misleading Framing': {
    code: 'CAT-04',
    className: 'framing',
    icon: Split,
    label: 'Misleading Framing'
  },
  'Selective Information': {
    code: 'CAT-05',
    className: 'selective',
    icon: BarChart2,
    label: 'Selective Information'
  },
  'Information Withholding': {
    code: 'CAT-06',
    className: 'withholding',
    icon: EyeOff,
    label: 'Information Withholding'
  },
  'Deceptive Persuasion': {
    code: 'CAT-07',
    className: 'persuasion',
    icon: AlertTriangle,
    label: 'Deceptive Persuasion'
  }
};

export default function CategoryBadge({ category }) {
  const meta = CATEGORY_MAP[category] || {
    code: 'CAT-??',
    className: 'framing',
    icon: AlertTriangle,
    label: category
  };

  const Icon = meta.icon;

  return (
    <span className={`category-badge-chip ${meta.className}`}>
      <span style={{ opacity: 0.85, letterSpacing: '0.06em' }}>{meta.code}</span>
      <Icon size={13} style={{ display: 'inline', verticalAlign: 'middle', flexShrink: 0 }} />
      <span>{category}</span>
    </span>
  );
}
