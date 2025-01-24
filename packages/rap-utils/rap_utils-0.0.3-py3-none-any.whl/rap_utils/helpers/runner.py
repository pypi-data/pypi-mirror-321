"""Logging Runner

Usage:

runner.py <COMMAND TO EXECUTE>

This script runs the command specified, logging the return code, start time and
execution time.

By default the output is written to a file called `runner.log` in the current working
directory. This can be overriden by setting the RUNNER_LOGFILE environment variable
which must include the filename.

The first field of the log will contain either the command executed or an identifier
string, which can be provided using the `-i` or `--id` flags. If running in DVC, the
current stage name is printed out instead of the command executed.
"""

import os
import subprocess
import sys
from datetime import datetime
from getopt import getopt
from pathlib import Path

LOGFILE = Path(os.environ.get('RUNNER_LOGFILE')
               or Path(os.getcwd()).parent / 'runner.log')


def write_log(*fields):
    with open(LOGFILE, 'a', encoding='utf-8') as log:
        log.write(','.join((str(f) for f in fields)) + '\n')


def run(cmd, id=None):
    start_time = datetime.now()
    process = subprocess.run(cmd)
    run_time = datetime.now() - start_time
    write_log(
        id or " ".join(cmd),
        process.returncode,
        start_time,
        run_time,
    )


if __name__ == '__main__':
    optlist, args = getopt(sys.argv[1:], "i:", ["id="])

    # NB requires DVC > 3.49.0 for DVC_STAGE to be set
    id = os.environ.get('DVC_STAGE')
    for o, a in optlist:
        if o in ('-i', '--id'):
            id = a
        else:
            assert False, "unhandled option"

    LOGFILE.parent.mkdir(exist_ok=True, parents=True)
    if not LOGFILE.exists():
        write_log(
            'id',
            'status',
            'start_time',
            'run_time'
        )
    run(args, id=id)
