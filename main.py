import argparse


def main():
    parser = argparse.ArgumentParser(description="A simple command-line program")
    parser.add_argument("name", help="Your name")
    parser.add_argument("--greet", "-g", action="store_true", help="Greet the user")

    args = parser.parse_args()

    if args.greet:
        print(f"Hello, {args.name}!")
    else:
        print(f"Your name is {args.name}")


if __name__ == "__main__":
    main()
