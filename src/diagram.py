import json


def generate_diagram(input_file, output_file):
    with open(input_file, 'r') as f:
        plan_data = json.load(f)

    resource_changes = plan_data.get("resource_changes", [])

    nodes = {}
    for change in resource_changes:
        actions = change.get("change", {}).get("actions", [])
        resource_type = change.get("type")
        resource_name = change.get("name")
        node = f"{resource_type}_{resource_name}"

        if "create" in actions:
            label = f"🆕 {resource_name}"
        elif "update" in actions:
            label = f"🔄 {resource_name}"
        elif "delete" in actions:
            label = f"🔥 {resource_name}"
        else:
            label = resource_name

        nodes[node] = label

    with open(output_file, 'w') as f:
        f.write("```mermaid\n")
        f.write("graph TD\n")
        for node, label in nodes.items():
            f.write(f'    {node}["{label}"]\n')
        f.write("```\n")
