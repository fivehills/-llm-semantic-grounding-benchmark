#!/usr/bin/env python3
"""
Example script: Load and explore the LLM semantic grounding benchmark data
"""

import pandas as pd
from pathlib import Path

# Set base path
BASE_PATH = Path(__file__).parent.parent

def load_human_norms():
    """Load human word association norms"""
    filepath = BASE_PATH / 'data' / 'human_norms' / 'wax_human_labelled.csv'

    if not filepath.exists():
        print(f"File not found: {filepath}")
        print("Please ensure the data files are downloaded and placed in the correct directory.")
        return None

    df = pd.read_csv(filepath)
    print(f"\n{'='*60}")
    print("HUMAN REFERENCE DATA")
    print(f"{'='*60}")
    print(f"Total associations: {len(df)}")
    print(f"Unique cues: {df['cue'].nunique()}")
    print(f"Unique relations: {df['relation'].nunique()}")
    print(f"\nRelation type distribution:")
    print(df['relation'].value_counts().head(10))

    return df

def load_llm_baseline(model_name='gpt-4o'):
    """Load LLM baseline outputs"""
    filepath = BASE_PATH / 'data' / 'llm_outputs' / 'baseline' / f'{model_name}_baseline.csv'

    if not filepath.exists():
        print(f"\nFile not found: {filepath}")
        print(f"Available models: Check data/llm_outputs/baseline/ directory")
        return None

    df = pd.read_csv(filepath)
    print(f"\n{'='*60}")
    print(f"LLM OUTPUT: {model_name.upper()}")
    print(f"{'='*60}")
    print(f"Total associations: {len(df)}")
    print(f"Unique cues: {df['cue'].nunique()}")
    print(f"\nRelation type distribution:")
    print(df['relation'].value_counts().head(10))

    return df

def compare_distributions(human_df, llm_df):
    """Compare relation type distributions"""
    if human_df is None or llm_df is None:
        return

    print(f"\n{'='*60}")
    print("DISTRIBUTION COMPARISON")
    print(f"{'='*60}")

    # Calculate percentages
    human_counts = human_df['relation'].value_counts(normalize=True) * 100
    llm_counts = llm_df['relation'].value_counts(normalize=True) * 100

    # Combine for comparison
    comparison = pd.DataFrame({
        'Human (%)': human_counts,
        'LLM (%)': llm_counts,
        'Difference': llm_counts - human_counts
    }).fillna(0).round(2)

    print("\nTop 10 relation types:")
    print(comparison.head(10))

    # Calculate perceptual vs functional vs thematic
    perceptual_types = ['HasProperty', 'MaterialMadeOf', 'Location', 'PartOf']
    functional_types = ['Function', 'Action', 'HasPrerequisite']

    human_perceptual = human_df[human_df['relation'].isin(perceptual_types)].shape[0] / len(human_df) * 100
    llm_perceptual = llm_df[llm_df['relation'].isin(perceptual_types)].shape[0] / len(llm_df) * 100

    human_functional = human_df[human_df['relation'].isin(functional_types)].shape[0] / len(human_df) * 100
    llm_functional = llm_df[llm_df['relation'].isin(functional_types)].shape[0] / len(llm_df) * 100

    print(f"\n{'Category':<20s} {'Human':>10s} {'LLM':>10s} {'Diff':>10s}")
    print("-" * 60)
    print(f"{'Perceptual':<20s} {human_perceptual:>9.1f}% {llm_perceptual:>9.1f}% {llm_perceptual-human_perceptual:>+9.1f}pp")
    print(f"{'Functional':<20s} {human_functional:>9.1f}% {llm_functional:>9.1f}% {llm_functional-human_functional:>+9.1f}pp")

def main():
    """Main execution"""
    print("\n" + "="*60)
    print("LLM SEMANTIC GROUNDING BENCHMARK - DATA EXPLORER")
    print("="*60)

    # Load human reference
    human_df = load_human_norms()

    # Load LLM baseline
    llm_df = load_llm_baseline('gpt-4o')

    # Compare distributions
    compare_distributions(human_df, llm_df)

    print("\n" + "="*60)
    print("Explore other models by changing the model_name parameter")
    print("Available models: See data/llm_outputs/baseline/ directory")
    print("="*60 + "\n")

if __name__ == '__main__':
    main()
