import argparse
from jyyslide_md.converter import converter


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", help="select a Markdown file to convert", type=str)
    parser.add_argument(
        "--watch",
        help="watch the file for changes, requires watchdog library",
        action=argparse.BooleanOptionalAction,
    )
    args = parser.parse_args()
    converter(args.filepath)

    if args.watch:
        print("watching file for changes")
        import livereload

        def generate_slides():
            converter(args.filepath)

        server = livereload.Server()
        server.watch(args.filepath, generate_slides)
        server.serve()


if __name__ == "__main__":
    main()
