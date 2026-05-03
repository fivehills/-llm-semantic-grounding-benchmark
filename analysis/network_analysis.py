#!/usr/bin/env python3
"""
Semantic network analysis tools
"""

import pandas as pd
import networkx as nx
import numpy as np

def build_semantic_network(df_or_path):
    """
    Build directed graph from word associations

    Args:
        df_or_path: DataFrame or path to CSV file with associations

    Returns:
        NetworkX DiGraph
    """
    if isinstance(df_or_path, str):
        df = pd.read_csv(df_or_path)
    else:
        df = df_or_path

    G = nx.DiGraph()

    for _, row in df.iterrows():
        cue = str(row['cue']).lower().strip()
        assoc = str(row['association']).lower().strip()

        if cue and assoc and cue != 'nan' and assoc != 'nan':
            G.add_edge(cue, assoc)

    return G

def calculate_network_metrics(G):
    """
    Calculate comprehensive network metrics

    Args:
        G: NetworkX graph

    Returns:
        Dictionary of network metrics
    """
    G_undirected = G.to_undirected()

    metrics = {
        'num_nodes': G.number_of_nodes(),
        'num_edges': G.number_of_edges(),
        'density': nx.density(G),
    }

    # Clustering coefficient
    try:
        metrics['avg_clustering'] = nx.average_clustering(G_undirected)
    except:
        metrics['avg_clustering'] = 0

    # Average degree
    degrees = [d for n, d in G.degree()]
    metrics['avg_degree'] = np.mean(degrees) if degrees else 0
    metrics['max_degree'] = np.max(degrees) if degrees else 0

    # Connectivity
    if nx.is_weakly_connected(G):
        metrics['weakly_connected'] = True
        metrics['diameter'] = nx.diameter(G.to_undirected())
    else:
        metrics['weakly_connected'] = False
        metrics['diameter'] = None

    # Number of connected components
    metrics['num_components'] = nx.number_weakly_connected_components(G)

    return metrics

def calculate_centrality_metrics(G, top_k=10):
    """
    Calculate various centrality measures

    Args:
        G: NetworkX graph
        top_k: Number of top nodes to return

    Returns:
        Dictionary of centrality measures
    """
    # Degree centrality
    degree_cent = nx.degree_centrality(G)

    # Betweenness centrality (sample for large graphs)
    if len(G.nodes()) > 500:
        betweenness_cent = nx.betweenness_centrality(G, k=min(100, len(G.nodes())))
    else:
        betweenness_cent = nx.betweenness_centrality(G)

    # Sort and get top-k
    top_degree = sorted(degree_cent.items(), key=lambda x: x[1], reverse=True)[:top_k]
    top_betweenness = sorted(betweenness_cent.items(), key=lambda x: x[1], reverse=True)[:top_k]

    return {
        'degree_centrality': dict(top_degree),
        'betweenness_centrality': dict(top_betweenness),
        'avg_degree_centrality': np.mean(list(degree_cent.values())),
        'avg_betweenness_centrality': np.mean(list(betweenness_cent.values()))
    }

def compare_network_topology(G1, G2):
    """
    Compare topological properties of two networks

    Args:
        G1, G2: NetworkX graphs

    Returns:
        Dictionary of comparative metrics
    """
    metrics1 = calculate_network_metrics(G1)
    metrics2 = calculate_network_metrics(G2)

    comparison = {
        'density_diff': abs(metrics1['density'] - metrics2['density']),
        'clustering_diff': abs(metrics1['avg_clustering'] - metrics2['avg_clustering']),
        'size_ratio': metrics1['num_nodes'] / max(metrics2['num_nodes'], 1)
    }

    return comparison

if __name__ == '__main__':
    print("Semantic Network Analysis Module")
    print("Import this module to use build_semantic_network() and related functions")
