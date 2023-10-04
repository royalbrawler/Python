import argparse

parser = argparse.ArgumentParser(
    description="Provides a greeting"
)
parser.add_argument(
    "-n", "--name",
    metavar="name",
    required=True,
    # dest="name", # output reference (args.name)
    help="The name you want to greet",
)
args = parser.parse_args()

msg = f"Heyo {args.name}"
print(msg)
