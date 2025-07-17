import argparse
from explain import explain_plan
from diagram import generate_diagram


def main():
    parser = argparse.ArgumentParser(
        description="Terraform GPT Plan Explainer: Convert Terraform JSON plans into human-readable summaries."
    )
    parser.add_argument(
        "--input", "-i",
        required=True,
        help="Path to Terraform JSON plan (output of `terraform show -json`)"
    )
    parser.add_argument(
        "--output", "-o",
        required=True,
        help="Path to output markdown summary file"
    )
    parser.add_argument(
        "--diagram", "-d",
        help="Optional: Path to output infrastructure diagram image"
    )
    args = parser.parse_args()

    explain_plan(input_file=args.input, output_file=args.output)

    if args.diagram:
        generate_diagram(input_file=args.input, output_file=args.diagram)


if __name__ == "__main__":
    main()
