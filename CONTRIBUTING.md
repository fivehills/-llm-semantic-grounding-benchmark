# Contributing to LLM Semantic Grounding Benchmark

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Ways to Contribute

### 1. Add New Model Evaluations

We welcome evaluations of new LLM models!

**Requirements**:
- Use the same cue words from `data/human_norms/wax_human_labelled.csv`
- Follow the prompting templates in `data/metadata/prompts.json`
- Generate 3 associations per cue
- Include model-generated explanations
- Use deterministic decoding (temperature=0) when possible

**Submission Process**:
1. Fork the repository
2. Add your model outputs to `data/llm_outputs/{condition}/`
3. Follow the naming convention: `{model-name}_{condition}.csv`
4. Update `README.md` with model details
5. Submit a pull request

### 2. Extend to Other Languages

We encourage multilingual extensions!

**Guidelines**:
- Create a new directory: `data/{language_code}/`
- Include human reference norms for that language
- Document language-specific relation types
- Provide translation mappings to English taxonomy

### 3. Improve Analysis Tools

Contributions to analysis scripts are welcome:

**Areas for improvement**:
- Additional network metrics
- Visualization tools
- Statistical analysis methods
- Performance optimization

### 4. Add Validation Benchmarks

Help us validate semantic networks with more behavioral tasks:

**Potential benchmarks**:
- Category fluency tasks
- Similarity ratings
- Feature verification
- Analogy completion

### 5. Report Issues

Found a bug or have a question?

- Check existing issues first
- Use issue templates when available
- Provide reproducible examples
- Include system information

## Code Style Guidelines

### Python

Follow PEP 8 style guide:

```python
# Good
def calculate_kl_divergence(p_dist, q_dist, epsilon=1e-10):
    """
    Calculate KL divergence between two distributions

    Args:
        p_dist: Reference distribution
        q_dist: Model distribution
        epsilon: Smoothing constant

    Returns:
        KL divergence value
    """
    # Implementation
    pass

# Use type hints when helpful
from typing import Dict, List
def process_associations(data: pd.DataFrame) -> Dict[str, float]:
    pass
```

### Documentation

- Add docstrings to all functions
- Include usage examples in README files
- Comment complex logic
- Keep comments up-to-date

### Data Files

- CSV files: UTF-8 encoding, comma-separated
- Column names: lowercase with underscores
- Missing values: empty string or "nan"
- File names: lowercase with hyphens

## Pull Request Process

1. **Fork** the repository
2. **Create a branch**: `git checkout -b feature/your-feature-name`
3. **Make changes** with clear, atomic commits
4. **Test** your changes locally
5. **Update documentation** as needed
6. **Submit PR** with description of changes

### PR Checklist

- [ ] Code follows style guidelines
- [ ] Tests pass (if applicable)
- [ ] Documentation updated
- [ ] CHANGELOG.md updated (for significant changes)
- [ ] No merge conflicts

## Model Addition Checklist

When adding a new model:

- [ ] Baseline condition data (required)
- [ ] Perceptual condition data (recommended)
- [ ] Functional condition data (recommended)
- [ ] Multimodal condition data (if applicable)
- [ ] Model metadata (size, architecture, training data)
- [ ] Generation timestamp
- [ ] Prompt templates used
- [ ] Update model table in README.md
- [ ] Verify data format matches schema

## Data Quality Standards

All contributed data must meet these criteria:

### Completeness
- All cue words from reference set
- 3 associations per cue (or document exceptions)
- No missing relation labels

### Format Consistency
- Match column schema exactly
- Use standardized relation type names
- Include required metadata fields

### Annotation Quality
- Relation types verified (manual or validated automatic)
- Explanations present and coherent
- No duplicates within same cue

## Testing

Run validation scripts before submitting:

```bash
# Validate data format
python scripts/validate_data.py data/llm_outputs/baseline/new-model.csv

# Check for missing cues
python scripts/check_completeness.py data/llm_outputs/baseline/new-model.csv

# Verify relation types
python scripts/verify_relations.py data/llm_outputs/baseline/new-model.csv
```

## Communication

- **GitHub Issues**: Bug reports, feature requests
- **Pull Requests**: Code contributions
- **Discussions**: Questions, ideas, showcase
- **Email**: Sensitive or private matters

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Acknowledged in paper (if significant contribution)
- Tagged in release notes (for version contributions)

## Questions?

Feel free to:
- Open an issue with the `question` label
- Start a discussion in GitHub Discussions
- Contact the maintainers directly

Thank you for contributing to advancing LLM evaluation!
