#!/usr/bin/env python3
"""
KL Divergence computation for relation type distributions
"""

import pandas as pd
import numpy as np
from scipy.stats import entropy

def calculate_relation_distribution(df, relation_col='relation'):
    """
    Calculate distribution of relation types

    Args:
        df: DataFrame with relation annotations
        relation_col: Column name containing relation types

    Returns:
        Dictionary mapping relation types to probabilities
    """
    total = len(df)
    relation_counts = df[relation_col].value_counts()

    # Convert to probabilities
    distribution = (relation_counts / total).to_dict()

    return distribution

def calculate_kl_divergence(human_df, model_df, epsilon=1e-10):
    """
    Calculate KL divergence D_KL(P_human || P_model)

    Args:
        human_df: DataFrame with human associations
        model_df: DataFrame with model associations
        epsilon: Small constant to avoid log(0)

    Returns:
        KL divergence value
    """
    # Get distributions
    human_dist = calculate_relation_distribution(human_df)
    model_dist = calculate_relation_distribution(model_df)

    # Ensure same categories
    all_relations = sorted(set(list(human_dist.keys()) + list(model_dist.keys())))

    # Convert to arrays
    p_array = np.array([human_dist.get(rel, 0) for rel in all_relations], dtype=float)
    q_array = np.array([model_dist.get(rel, 0) for rel in all_relations], dtype=float)

    # Normalize to probabilities
    p_array = p_array / (p_array.sum() + epsilon)
    q_array = q_array / (q_array.sum() + epsilon)

    # Add epsilon to avoid log(0)
    p_array = p_array + epsilon
    q_array = q_array + epsilon

    # Renormalize
    p_array = p_array / p_array.sum()
    q_array = q_array / q_array.sum()

    # Calculate KL divergence
    kl_div = entropy(p_array, q_array)

    return kl_div

def calculate_grounding_scores(df, human_baseline=None):
    """
    Calculate perceptual and functional grounding scores

    Args:
        df: DataFrame with associations
        human_baseline: Optional dict with human baseline percentages

    Returns:
        Dictionary with grounding metrics
    """
    perceptual_types = ['HasProperty', 'MaterialMadeOf', 'Location', 'PartOf']
    functional_types = ['Function', 'Action', 'HasPrerequisite']

    total = len(df)

    perceptual_count = df[df['relation'].isin(perceptual_types)].shape[0]
    functional_count = df[df['relation'].isin(functional_types)].shape[0]

    perceptual_pct = (perceptual_count / total) * 100
    functional_pct = (functional_count / total) * 100
    thematic_pct = 100 - perceptual_pct - functional_pct

    scores = {
        'perceptual': perceptual_pct,
        'functional': functional_pct,
        'thematic': thematic_pct
    }

    # Calculate deficits if human baseline provided
    if human_baseline:
        scores['perceptual_deficit'] = perceptual_pct - human_baseline.get('perceptual', 16.4)
        scores['functional_deficit'] = functional_pct - human_baseline.get('functional', 21.5)

    return scores

if __name__ == '__main__':
    print("KL Divergence Analysis Module")
    print("Import this module to use calculate_kl_divergence() and related functions")
