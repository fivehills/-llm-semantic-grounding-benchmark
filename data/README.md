# Data Directory

This directory contains all datasets for the LLM Semantic Grounding Benchmark.

## Directory Structure

```
data/
├── human_norms/              # Human word association reference data
├── llm_outputs/              # LLM-generated associations
│   ├── baseline/             # Neutral prompting condition
│   ├── perceptual/           # Perceptual cuing condition
│   ├── functional/           # Functional cuing condition
│   └── multimodal/           # Image + text condition
├── benchmarks/               # External validation datasets
│   ├── semantic_priming/     # RT data for priming effects
│   ├── lexical_decision/     # Lexical decision times
│   └── piqa/                 # Physical reasoning benchmark
└── metadata/                 # Model configurations and prompts
```

## Data Files

### Human Reference Norms

**File**: `human_norms/wax_human_labelled.csv`

Contains human word association norms with semantic relation labels.

**Columns**:
- `cue` (str): The prompt word
- `association` (str): The associated response word
- `relation` (str): Semantic relation type (16 categories)
- `frequency` (int): Response frequency from human participants

**Size**: 580 cue-associate pairs

**Source**: Combination of:
- WAX Dataset (Word Association eXplanations)
- SWOW (Small World of Words) norms
- Manual relation type annotation

### LLM Output Files

**Location**: `llm_outputs/{condition}/`

Each model has one CSV file per condition with format: `{model_name}_{condition}.csv`

**Columns**:
- `cue` (str): The prompt word
- `association` (str): Generated association (top-3 per cue)
- `relation` (str): Classified relation type
- `explanation` (str): Model-generated explanation for the association
- `model` (str): Model identifier (e.g., "gpt-4o", "claude-sonnet-4")
- `condition` (str): Experimental condition
- `temperature` (float): Generation temperature (typically 0)
- `timestamp` (str): Generation timestamp

### Naming Conventions

**Model Names**:
- Use lowercase with hyphens: `gpt-4o`, `claude-sonnet-4`, `gemini-2.5-flash`
- Consistent with official model identifiers

**Condition Names**:
- `baseline`: Neutral prompt ("What word comes to mind?")
- `perceptual`: Perceptual cuing ("Think about how this looks/sounds/feels")
- `functional`: Functional cuing ("Think about what you do with this")
- `multimodal`: Image + text prompt

### File Sizes

Approximate file sizes:
- Human norms: ~50 KB
- LLM baseline (per model): ~200-300 KB
- LLM perceptual/functional (per model): ~150-200 KB
- LLM multimodal (per model): ~80-100 KB

Total dataset size: ~20-30 MB (uncompressed)

## Downloading the Data

### Option 1: Clone with Git LFS

If using Git Large File Storage:

```bash
git lfs install
git clone https://github.com/fivehills/llm-semantic-grounding-benchmark.git
cd llm-semantic-grounding-benchmark
git lfs pull
```

### Option 2: Direct Download

Download the complete dataset from:
- [Zenodo DOI: TBD]
- [Hugging Face Datasets: TBD]

Extract to the `data/` directory.

### Option 3: Generate Your Own

Run LLM evaluation using the prompts in `metadata/prompts.json`:

```bash
python scripts/collect_associations.py --model gpt-4o --condition baseline
```

## Data Quality

All data files have been:
- ✅ Validated for completeness (no missing cues)
- ✅ Checked for format consistency
- ✅ Relation types verified against taxonomy
- ✅ Deduplicated (no repeated associations per cue)

### Known Issues

- Some models (smaller-scale) show higher rates of generic responses
- Multimodal condition limited to 53 cues with clear visual concepts
- Some relation types have low frequency (<5%) in certain models

## Relation Type Taxonomy

The 16 relation types are grouped into 4 categories:

**Perceptual** (4 types):
- `HasProperty`: sensory attributes (color, texture, sound)
- `MaterialMadeOf`: material composition
- `Location`: spatial location or origin
- `PartOf`: physical part-whole relations

**Functional** (3 types):
- `Function`: purpose or use
- `Action`: associated actions
- `HasPrerequisite`: required conditions

**Structural** (2 types):
- `CategoryExemplar`: category-instance relations
- `SameCategory`: co-hyponyms (same category members)

**Abstract** (7 types):
- `Synonym`: same meaning
- `Antonym`: opposite meaning
- `Thematic`: thematic/script-based associations
- `EmotionEvaluation`: emotional valence
- `Result-In`: causal outcome
- `CommonPhrase`: idiomatic collocations
- `Time`: temporal associations

## Citation

When using this data, please cite:

```bibtex
@inproceedings{yourname2026grounding,
  title={Semantic Grounding in Large Language Models: A Multi-Condition Benchmark},
  author={Your Name and Collaborators},
  booktitle={NeurIPS},
  year={2026}
}
```

And the original data sources:
- WAX: Liu et al. (2022)
- SWOW: De Deyne et al. (2019)

## License

- Human reference data: Original sources retain their respective licenses
- LLM outputs: MIT License
- Aggregate benchmark: MIT License

See main `LICENSE` file for details.
