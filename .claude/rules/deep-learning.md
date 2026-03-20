---
description: Rules for deep learning experiment code
globs:
  - "**/*.py"
  - "**/train*"
  - "**/experiment*"
---

# Deep Learning Experiment Rules

- Always set random seed (--seed 42) for reproducibility
- Check GPU availability before launching training
- Log all hyperparameters to experiment directory
- Save checkpoints periodically
- Use type hints on all Python functions
- Training scripts must support --dry-run flag
- Never hardcode absolute paths — use relative or environment variables
