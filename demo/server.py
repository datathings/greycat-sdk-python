from __future__ import annotations

import argparse
import flask
import pandas
import os
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
app: GreyCatServer = GreyCatServer(__name__, args.greycat_abi_path, static_url_path="",
                                   static_folder=os.path.join(os.getcwd(), "demo", "js", "webroot"))


@app.expose("/project::get_csv")
def get_csv(csv_path: str):
    df = pandas.read_csv(csv_path)
    table = std.core.Table.from_pandas(app.gc, df)
    return table


app.run()
