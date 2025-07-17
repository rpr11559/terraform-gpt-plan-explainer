import os
from unittest.mock import patch
from src.explain import explain_plan


@patch("src.explain.explain_with_gpt", return_value="Mocked LLM Response")
def test_explain_plan(mock_llm, tmp_path):
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
    output_file = tmp_path / "summary.md"

    # Write the plan data to input file
    with open(input_file, "w") as f:
        import json
        json.dump(plan_data, f)

    # Run the explain_plan function
    explain_plan(input_file, output_file)

    # Read the output and assert expected content
    with open(output_file, "r") as f:
        content = f.read()

    assert "| Action  | Resource Type | Resource Name |" in content
    assert "| Add | aws_instance | web_server |" in content
    assert "| Modify | aws_s3_bucket | logs_bucket |" in content
    assert "| Destroy | aws_ebs_volume | unused_volume |" in content
    assert "Mocked LLM Response" in content