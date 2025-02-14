from __future__ import annotations

import argparse
import pandas
import os

from greycat import GreyCatServer, std


class ServerNamespace(argparse.Namespace):
    def __init__(self):
        self.greycat_abi_path: str

    @staticmethod
    def parse_args() -> ServerNamespace:
        args_parser: argparse.ArgumentParser = argparse.ArgumentParser()
        args_parser.add_argument(
            "--greycat_abi_path",
            type=str,
            default="."
        )
        return args_parser.parse_args()


args: ServerNamespace = ServerNamespace.parse_args()
app: GreyCatServer = GreyCatServer(
    __name__,
    args.greycat_abi_path,
    static_url_path="",
    static_folder=os.path.join(os.getcwd(), "demo", "js", "webroot")
)


@app.expose()
def get_csv(csv_path: str):
    print(csv_path)
    df: pandas.DataFrame = pandas.read_csv(csv_path)
    table: std.core.Table = std.core.Table.from_pandas(app.gc, df)
    return table


app.run()
