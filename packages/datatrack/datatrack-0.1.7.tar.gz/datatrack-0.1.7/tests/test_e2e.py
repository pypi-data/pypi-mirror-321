#!/usr/bin/env python

"""
Tests a basic ETL scenario

Usage:
  test_e2e.py [--project=PROJECT] [--name=NAME] --id=ARTIFACT_ID

Options:
  -p, --project=PROJECT     a name of the project [default: test]
  -n, --name=NAME           a name of the project [default: e2e]
      --id=ARTIFACT_ID      an input artifact
  -h, --help                display this help and exit
"""


import logging
import sys
import tempfile
from pathlib import Path
from docopt import docopt
from datatrack import Artifact, Experiment, Run


logging.basicConfig(
    stream=sys.stderr,
    level=logging.getLevelName(logging.INFO),
    format="%(asctime)s %(levelname)s %(name)s -- %(message)s",
)
logger = logging.getLogger(Path(__file__).name)


def process_data(path, dst):
    for f in Path(path).rglob("*"):
        outname = Path(dst) / f.relative_to(path)
        logger.info(f"Creating {outname}")
        if f.is_dir():
            outname.mkdir()
        else:
            with open(outname, "w") as out:
                print(f.stat().st_size, file=out)


if __name__ == "__main__":
    args = docopt(__doc__)
    with Experiment(args["--project"], args["--name"]).run() as run:
        run.create_parameter(args)
        with tempfile.TemporaryDirectory() as tmpdir:
            path = run.get_artifact(Artifact(args["--id"]))
            process_data(path, tmpdir)
            a = run.create_artifact(args["--name"], tmpdir)
            Run.current.create_parameter("test-str", "test-str")
            print(a)
