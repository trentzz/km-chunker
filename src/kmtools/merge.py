from pathlib import Path
from kmtools.utils import Utils


class Merge:
    def __init__(self, inputs, output, verbose=False):
        self.inputs = [Path(p) for p in inputs]
        self.output = Path(output)
        self.verbose = verbose

    def run(self):
        Utils.log(f"Merging {len(self.inputs)} input files into {self.output}", self.verbose)
        # TODO: implement JSON/CSV merging logic
        print(f"Merged results saved to {self.output}")
