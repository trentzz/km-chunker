from pathlib import Path
from kmtools.utils import Utils


class Plot:
    def __init__(self, file, output_dir=".", charts="all", verbose=False):
        self.file = Path(file)
        self.output_dir = Path(output_dir)
        self.charts = charts.split(",") if charts != "all" else ["vaf", "patient", "sample", "overall"]
        self.verbose = verbose

    def run(self):
        Utils.log(f"Generating plots from {self.file} -> {self.output_dir}", self.verbose)
        for chart in self.charts:
            print(f"Generating {chart} chart...")
        print("Plotting complete.")
