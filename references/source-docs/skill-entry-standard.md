# Skill Entry Standard Summary

Source: `/Users/zhuruoyan1/Downloads/录入Skill标准.pdf`

## Key Principle

The skill structure separates four concerns:

- `README.md`: human-facing explanation.
- `SKILL.md`: agent-facing execution contract.
- `references/`: reusable knowledge basis such as rules, workflow, background, and source documents.
- `examples/`: verifiable input/output examples for review, testing, teaching, and regression checks.

## Formal Skill Directory

Formal skills should use:

```text
.agents/skills/<skill-slug>/
├── README.md
├── SKILL.md
├── references/
│   ├── overview.md
│   ├── rules.md
│   ├── workflow.md
│   └── source-docs/
├── examples/
│   ├── input-01.md
│   └── output-01.md
├── assets/
├── scripts/
└── agents/
    └── openai.yaml
```

## Minimum Submission Standard

At minimum, a formal skill should include:

- `README.md`
- `SKILL.md`
- `references/rules.md`
- `examples/input-01.md`
- `examples/output-01.md`

## Maturity Levels

- **L0 minimum runnable**: `README.md`, `SKILL.md`.
- **L1 recommended**: `README.md`, `SKILL.md`, `references/`, `examples/`.
- **L2 complete**: `README.md`, `SKILL.md`, `references/`, `examples/`, `assets/`, `scripts/`, `agents/`.

## Naming Rule

The agent runtime entry file must remain named `SKILL.md`. Do not rename it to `<skill-name>.md`.
