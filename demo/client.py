from __future__ import annotations

import argparse
import time

from greycat import GreyCat, std


class ClientNamespace(argparse.Namespace):
    def __init__(self):
        self.url: str

    @staticmethod
    def parse_args() -> ClientNamespace:
        args_parser: argparse.ArgumentParser = argparse.ArgumentParser(
            add_help=False)
        args_parser.add_argument(
            "-u", "--url", type=str, default="http://localhost:8080")
        return args_parser.parse_args()


def main():
    args: ClientNamespace = ClientNamespace.parse_args()
    gc: GreyCat = GreyCat(args.url)

    csv_path = "data/huge.csv"

    print(f"gc.project::get_csv(\"{csv_path}\")…")
    start = time.time()
    csv: std.core.Table = gc.call("project::get_csv", [csv_path])
    end = time.time()
    print("\t%.6fs" % (end - start))

    print(f"table to pandas")
    start = time.time()
    df = csv.to_pandas()
    end = time.time()
    print("\t%.6fs" % (end - start))

    print(csv.shape)
    print(df.head())


if "__main__" == __name__:
    main()
