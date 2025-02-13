from __future__ import annotations

import argparse
import pandas
import time

from greycat import GreyCatServer, std


class ServerNamespace(argparse.Namespace):
    def __init__(self):
        self.greycat_abi_path: str

    @staticmethod
    def parse_args() -> ServerNamespace:
        args_parser: argparse.ArgumentParser = argparse.ArgumentParser()
        args_parser.add_argument("--greycat_abi_path",
                                 type=str, default=".")
        return args_parser.parse_args()


args: ServerNamespace = ServerNamespace.parse_args()
headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "*",
}
app: GreyCatServer = GreyCatServer(
    __name__, args.greycat_abi_path, headers=headers)


@app.route("/project::get_csv")
def get_csv():
    csv_path: str
    csv_path, = GreyCatServer.request().gcargs

    print(f"Pandas read_csv(\"{csv_path}\")…")
    start = time.time()
    df = pandas.read_csv(csv_path)
    end = time.time()
    print("\t%.6fs" % (end - start))

    print(f"GC Table from_pandas…")
    start = time.time()
    table = std.core.Table.from_pandas(app.gc, df)
    end = time.time()
    print("\t%.6fs" % (end - start))

    return table


app.run()
