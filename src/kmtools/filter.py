from kmtools.utils import Utils


class Filter:
    def __init__(self, reference, km_output, output, verbose=False):
        self.reference = reference
        self.km_output = km_output
        self.output = output
        self.verbose = verbose

    def run(self):
        Utils.log(f"Filtering {self.km_output} using reference {self.reference}", self.verbose)
        # TODO: implement filtering logic
        print(f"Filtered results written to {self.output}")
