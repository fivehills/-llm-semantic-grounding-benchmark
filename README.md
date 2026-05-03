# LLM Semantic Grounding Benchmark

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Dataset](https://img.shields.io/badge/Dataset-Available-blue.svg)]()
[![Paper](https://img.shields.io/badge/Paper-NeurIPS%202026-red.svg)]()

A comprehensive benchmark for evaluating semantic grounding in Large Language Models (LLMs) through word association tasks.

## Overview

This repository contains datasets and evaluation tools for assessing how well LLMs capture human-like semantic knowledge, particularly focusing on perceptual, functional, and thematic associations. The benchmark includes:

- **18 LLM models** tested across multiple conditions
- **4 experimental conditions**: Baseline, Perceptual cuing, Functional cuing, and Multimodal
- **16 semantic relation types** aligned with human annotation standards
- **Human reference data** from established word association norms

## Quick Start

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/llm-semantic-grounding-benchmark.git
cd llm-semantic-grounding-benchmark

# Install dependencies
pip install -r requirements.txt

# Load and explore the data
python examples/load_data.py
```

## Dataset Structure

```
llm-semantic-grounding-benchmark/
├── data/
│   ├── human_norms/              # Human word association baselines
│   │   └── wax_human_labelled.csv
│   ├── llm_outputs/              # LLM-generated associations
│   │   ├── baseline/             # Neutral prompting condition
│   │   ├── perceptual/           # Perceptual cuing condition
│   │   ├── functional/           # Functional cuing condition
│   │   └── multimodal/           # Image + text condition
│   ├── benchmarks/               # External validation datasets
│   │   ├── semantic_priming/
│   │   ├── lexical_decision/
│   │   └── piqa/
│   └── metadata/                 # Model information and configs
├── analysis/                     # Analysis scripts
│   ├── kl_divergence.py
│   ├── network_analysis.py
│   └── grounding_metrics.py
├── visualizations/               # Plotting scripts
├── examples/                     # Usage examples
└── docs/                         # Documentation

```

## Data Files

### Core Datasets

#### 1. Human Reference Data
- **File**: `data/human_norms/wax_human_labelled.csv`
- **Size**: 580 cue-associate pairs
- **Columns**: `cue`, `association`, `relation`, `frequency`
- **Source**: WAX dataset + SWOW norms

#### 2. LLM Outputs (Baseline Condition)
- **Directory**: `data/llm_outputs/baseline/`
- **Models**: 15 LLMs with complete baseline data
- **Format**: One CSV per model
- **Columns**: `cue`, `association`, `relation`, `explanation`, `model`

#### 3. LLM Outputs (Perceptual/Functional Conditions)
- **Directories**: `data/llm_outputs/perceptual/`, `data/llm_outputs/functional/`
- **Models**: 13-14 LLMs with cross-condition data
- **Purpose**: Test sensitivity to grounding cues

#### 4. LLM Outputs (Multimodal Condition)
- **Directory**: `data/llm_outputs/multimodal/`
- **Models**: 10 vision-capable models
- **Cues**: 53 cues with concept-consistent images
- **Total**: 1,590 associations (53 cues × 10 models × 3 associations)

### Model Coverage

| Model Class | Models | Baseline | Perceptual | Functional | Multimodal |
|-------------|--------|----------|------------|------------|------------|
| **Frontier** | Claude-Sonnet-4, DeepSeek-V3, Gemini-2.5-Flash, GPT-4.1, Grok-3-Beta | ✓ | ✓ | ✓ | ✓ |
| **Multimodal** | Claude-3.5-Sonnet, GPT-4o, Gemini-3-Flash, Grok-4.1-Fast | ✓ | ✓ | ✓ | ✓ |
| **Open Source** | Llama-3.1-8B, Llama-3.3-70B, Qwen-2.5-72B | ✓ | ✓ | ✓ | - |
| **Smaller Scale** | Claude-Haiku-4.5, Mistral-Large, Phi-4 | ✓ | ✓ | ✓ | - |

## Semantic Relation Taxonomy

The benchmark uses 16 semantic relation types:

### Perceptual Relations
- `HasProperty` (e.g., apple → red)
- `MaterialMadeOf` (e.g., window → glass)
- `Location` (e.g., beach → ocean)
- `PartOf` (e.g., wheel → car)

### Functional Relations
- `Function` (e.g., knife → cut)
- `Action` (e.g., ball → throw)
- `HasPrerequisite` (e.g., read → book)

### Structural Relations
- `CategoryExemplar` (e.g., fruit → apple)
- `SameCategory` (e.g., dog → cat)

### Abstract Relations
- `Synonym` (e.g., happy → joyful)
- `Antonym` (e.g., hot → cold)
- `Thematic` (e.g., king → crown)
- `EmotionEvaluation` (e.g., gift → happy)
- `Result-In` (e.g., study → knowledge)
- `CommonPhrase` (e.g., black → coffee)
- `Time` (e.g., morning → sunrise)

## Evaluation Metrics

The benchmark includes several evaluation dimensions:

### 1. Distribution Alignment
- **KL Divergence**: Measures distributional distance from human norms
- **Relation Type Coverage**: Percentage of each relation type
- **Grounding Deficit**: Underrepresentation of perceptual/functional relations

### 2. Network Topology
- **Degree Centrality**: Node importance in semantic network
- **Betweenness Centrality**: Bridge nodes in network paths
- **Procrustes Distance**: Structural alignment between networks
- **Clustering Coefficient**: Local connectivity patterns

### 3. Behavioral Validation
- **Semantic Priming Effects**: RT facilitation prediction
- **Lexical Decision Times**: Network accessibility correlations
- **Task Performance**: PIQA, MMLU, HumanEval correlations

## Usage Examples

### Example 1: Load and Compare Distributions

```python
import pandas as pd
from analysis.kl_divergence import calculate_kl_divergence

# Load human reference
human_df = pd.read_csv('data/human_norms/wax_human_labelled.csv')

# Load LLM output
llm_df = pd.read_csv('data/llm_outputs/baseline/gpt-4o_baseline.csv')

# Calculate KL divergence
kl_div = calculate_kl_divergence(human_df, llm_df)
print(f"KL Divergence: {kl_div:.4f}")
```

### Example 2: Analyze Grounding Patterns

```python
from analysis.grounding_metrics import compute_grounding_scores

# Compute grounding metrics across conditions
scores = compute_grounding_scores(
    model_name='gpt-4o',
    conditions=['baseline', 'perceptual', 'functional']
)

print(f"Baseline Perceptual: {scores['baseline']['perceptual']:.1f}%")
print(f"Cued Perceptual: {scores['perceptual']['perceptual']:.1f}%")
print(f"Overcorrection: {scores['overcorrection']:.1f} pp")
```

### Example 3: Build Semantic Network

```python
from analysis.network_analysis import build_semantic_network
import networkx as nx

# Build network from associations
G = build_semantic_network('data/llm_outputs/baseline/gpt-4o_baseline.csv')

# Compute network metrics
density = nx.density(G)
avg_clustering = nx.average_clustering(G.to_undirected())

print(f"Network Density: {density:.6f}")
print(f"Clustering Coefficient: {avg_clustering:.4f}")
```

## Key Findings

Our analysis reveals three levels of semantic grounding in LLMs:

1. **Preserved Network Topology**: LLMs maintain human-like graph structures (density, centrality, clustering) despite distributional shifts

2. **Systematic Content Deficits**: All models underrepresent perceptual relations (23-43% vs. 16% human baseline) and overrepresent functional relations

3. **Prompt-Sensitive Calibration**: Models show extreme overcorrection under perceptual cuing (77-84 pp gains), revealing calibration deficits rather than pure representational absence

## Citation

If you use this benchmark in your research, please cite:

```bibtex
@inproceedings{yourname2026grounding,
  title={Semantic Grounding in Large Language Models: A Multi-Condition Benchmark},
  author={Your Name and Collaborators},
  booktitle={Advances in Neural Information Processing Systems},
  year={2026}
}
```

## Data Format Specification

### CSV Column Definitions

**Human Norms (`wax_human_labelled.csv`)**:
- `cue` (str): The prompt word
- `association` (str): The associated response word
- `relation` (str): Semantic relation type (16 categories)
- `frequency` (int): Number of human participants giving this response

**LLM Outputs**:
- `cue` (str): The prompt word
- `association` (str): Generated association
- `relation` (str): Classified relation type
- `explanation` (str): Model-generated explanation
- `model` (str): Model identifier
- `condition` (str): Experimental condition (baseline/perceptual/functional/multimodal)
- `temperature` (float): Generation temperature (typically 0 for deterministic)

## Reproducibility

All experiments were conducted with:
- **Deterministic decoding**: `temperature = 0`
- **API access**: January-March 2026
- **Prompt templates**: Available in `data/metadata/prompts.json`
- **Relation annotation**: Via GPT-4.1-Turbo with validation

See `docs/REPRODUCTION.md` for detailed reproduction instructions.

## License

This dataset is released under the **MIT License**. See `LICENSE` for details.

The human reference data is derived from:
- WAX Dataset: [Liu et al., 2022](https://arxiv.org/abs/2205.01780)
- SWOW Norms: [De Deyne et al., 2019](https://doi.org/10.3758/s13428-018-1115-7)

Please cite the original sources when using the human baseline data.

## Contributing

We welcome contributions! Please see `CONTRIBUTING.md` for guidelines on:
- Adding new model evaluations
- Extending to other languages
- Improving analysis tools
- Reporting issues

## Contact

For questions or issues, please:
- Open an issue on GitHub
- Email: your.email@institution.edu

## Changelog

### Version 1.0.0 (2026-05)
- Initial release
- 18 models, 4 conditions
- Complete analysis pipeline
- Visualization tools

## Acknowledgments

This work builds on several excellent resources:
- WAX Dataset (Liu et al., 2022)
- Small World of Words (De Deyne et al., 2019)
- McRae Feature Norms (McRae et al., 2005)
- Semantic Priming Project (Hutchison et al., 2013)

---

**Note**: This is a living benchmark. We plan to add more models, conditions, and languages over time. Stay tuned for updates!
