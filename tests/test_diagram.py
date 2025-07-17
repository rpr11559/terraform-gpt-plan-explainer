


import os
from src.diagram import generate_diagram


def test_generate_diagram(tmp_path):
    # Create a sample Terraform plan JSON
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

    input_file = tmp_path / "plan.json"
    output_file = tmp_path / "diagram.mmd"

    # Write the plan data to input file
    with open(input_file, "w") as f:
        import json
        json.dump(plan_data, f)

    # Run the generate_diagram function
    generate_diagram(input_file, output_file)

    # Read the output and assert expected content
    with open(output_file, "r") as f:
        content = f.read()

    assert "```mermaid" in content
    assert "🆕 web_server" in content
    assert "🔄 logs_bucket" in content
    assert "🔥 unused_volume" in content