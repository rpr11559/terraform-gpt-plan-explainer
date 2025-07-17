# Terraform GPT Plan Explainer

![CI](https://github.com/rpr11559/terraform-gpt-plan-explainer/actions/workflows/ci.yml/badge.svg?event=push)

## 🚀 What is this?

**Terraform GPT Plan Explainer** is a CLI tool that takes Terraform plan outputs and turns them into human-readable summaries with clear explanations of infrastructure changes. It helps DevOps, SREs, and Cloud Engineers quickly understand what's changing, why, and how risky those changes are — without digging through JSON or raw `terraform plan` output.

## 🎯 Why does it exist?

Terraform's output is designed for machines, not humans. This tool uses LLMs (like GPT-4) to bridge that gap by providing:
- Human-friendly explanations of infra changes.
- Categorized summaries (Add, Modify, Destroy).
- Optional risk assessments and diagrams.

Great for onboarding, PR reviews, and reducing "terraform fear."

## 🛠 Installation

```bash
git clone https://github.com/rpr11559/terraform-gpt-plan-explainer.git
cd terraform-gpt-plan-explainer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 💡 Usage

First, generate a Terraform JSON plan:
```bash
terraform plan -out=plan.out
terraform show -json plan.out > plan.json
```

Then run the explainer:
```bash
python src/cli.py --input examples/example-plan.json --output examples/output-summary.md
```

Optional with diagram:
```bash
python src/cli.py --input examples/example-plan.json --output examples/output-summary.md --diagram examples/output-diagram.mmd
```

## 🔍 Example Output

See [`examples/`](examples/) for:
- `example-plan.json`: Sample input
- `output-summary.md`: Human-readable output
- `output-diagram.mmd`: Visual Mermaid diagram (optional)

## 📦 Project Structure

```
terraform-gpt-plan-explainer/
├── src/
│   ├── cli.py
│   ├── explain.py
│   ├── diagram.py
│   └── llm.py
├── examples/
├── tests/
└── README.md
```

## 🛤 Roadmap

- [x] v0.1 MVP CLI
- [x] Optional Mermaid diagram integration
- [x] GitHub Action integration
- [ ] Slack / GitHub Bot PR comment support

## 🤝 Contributing

PRs welcome! Please open issues for discussion.

## 📝 License
MIT License.