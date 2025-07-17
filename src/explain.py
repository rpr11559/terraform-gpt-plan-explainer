import json
from llm import explain_with_gpt


def explain_plan(input_file, output_file):
    with open(input_file, 'r') as f:
        plan_data = json.load(f)

    resource_changes = plan_data.get("resource_changes", [])

    table_rows = []

    for change in resource_changes:
        action = change.get("change", {}).get("actions", [])
        resource_type = change.get("type")
        resource_name = change.get("name")
        if "create" in action:
            table_rows.append(("Add", resource_type, resource_name))
        if "update" in action:
            table_rows.append(("Modify", resource_type, resource_name))
        if "delete" in action:
            table_rows.append(("Destroy", resource_type, resource_name))

    summary = "# Terraform Plan Summary\n\n"

    if table_rows:
        summary += "| Action  | Resource Type | Resource Name |\n"
        summary += "|---------|---------------|---------------|\n"
        for action, rtype, rname in table_rows:
            summary += f"| {action} | {rtype} | {rname} |\n"
        summary += "\n"
    else:
        summary += "No resource changes detected.\n"

    # Build LLM prompt
    prompt = (
        "Summarize these Terraform infrastructure changes for a human reader:\n\n"
        + summary
    )

    # Get GPT explanation
    llm_summary = explain_with_gpt(prompt)

    with open(output_file, 'w') as f:
        f.write("# Terraform Plan Summary\n\n")
        f.write(summary)
        f.write("\n")
        f.write("## LLM Explanation\n")
        f.write(llm_summary)
        f.write("\n")