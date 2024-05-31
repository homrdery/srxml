#!/usr/bin/python

import sys


class Logger:
    def __init__(self, verbose, output=sys.stderr):
        self.verbose = verbose
        self.output = output

    def msg(self, msg):
        print(msg, file=self.output)

    def msg_info(self, msg):
        if self.verbose > 0:
            self.msg(f"Info: {msg}")

    def msg_debug(self, msg):
        if self.verbose > 1:
            self.msg(f"Debug: {msg}")

    def msg_error(self, msg, do_exit=True):
        self.msg(f"Error: {msg}")
        if do_exit:
            sys.exit(5)

if __name__ == '__main__':
    logger=Logger(verbose=1)
    logger.msg_info(msg="test")