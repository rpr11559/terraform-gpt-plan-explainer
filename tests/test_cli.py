

import subprocess
import os


def test_cli(tmp_path):
    input_file = tmp_path / "plan.json"
    output_file = tmp_path / "summary.md"
    diagram_file = tmp_path / "diagram.mmd"

    # Sample plan JSON
    plan_data = {
        "resource_changes": [
            {
                "type": "aws_instance",
                "name": "web_server",
                "change": {"actions": ["create"]}
            },
            {
                "type": "aws_s3_bucket",
                "name": "logs_bucket",
                "change": {"actions": ["update"]}
            },
            {
                "type": "aws_ebs_volume",
                "name": "unused_volume",
                "change": {"actions": ["delete"]}
            }
        ]
    }

    with open(input_file, "w") as f:
        import json
        json.dump(plan_data, f)

    # Run the CLI as a subprocess
    subprocess.run(
        ["python", "src/cli.py", "--input", str(input_file), "--output", str(output_file), "--diagram", str(diagram_file)],
        check=True,
    )

    # Verify files were created and contain expected content
    assert output_file.exists()
    with open(output_file, "r") as f:
        content = f.read()
        assert "| Action  | Resource Type | Resource Name |" in content
        assert "Mocked LLM Response" in content or "LLM Explanation" in content  # Depending on test setup

    assert diagram_file.exists()
    with open(diagram_file, "r") as f:
        content = f.read()
        assert "```mermaid" in content
        assert "🆕 web_server" in content
        assert "🔄 logs_bucket" in content
        assert "🔥 unused_volume" in content