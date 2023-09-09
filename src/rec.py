import argparse
import queue
import sys

import sounddevice as sd
import numpy as np

class Rec():

    global q

    def int_or_str(text):
        """Helper function for argument parsing."""
        try:
            return int(text)
        except ValueError:
            return text

    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(add_help=False)
        self.parser.add_argument('-l', '--list-devices', action='store_true',
                            help='show list of audio devices and exit')
        self.args, self.remaining = self.parser.parse_known_args()

        if self.args.list_devices:
            print(sd.query_devices())
            self.parser.exit(0)

        self.parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            parents=[self.parser])
        self.parser.add_argument(
            'filename', nargs='?', metavar='FILENAME',
            help='audio file to store recording to')
        self.parser.add_argument(
            '-d', '--device', type=self.int_or_str,
            help='input device (numeric ID or substring)')
        self.parser.add_argument(
            '-r', '--samplerate', type=int, help='sampling rate')
        self.parser.add_argument(
            '-c', '--channels', type=int, default=1, help='number of input channels')
        self.parser.add_argument(
            '-t', '--subtype', type=str, help='sound file subtype (e.g. "PCM_24")')
        self.args = self.parser.parse_args(self.remaining)

        self.q = queue.Queue()

    def callback(self,indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        self.q.put(indata.copy())
