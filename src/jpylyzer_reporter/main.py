import os
import argparse
from jpylyzer_reporter.reporter import JpylyzerReporter


###
# Main #
###
if __name__ == '__main__':
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser(
        description="Reports status of Jpylyzer to database (csv for now)")
    ap.add_argument('-c', '--csv_file',
                    required=True,
                    help='Location of existing or to-be-create output CSV file')
    ap.add_argument('-x', '--is_output', action="store_true",
                    required=False,
                    help='Indicates that input is XML output of Jpylyzer')
    ap.add_argument('input_file',
                    help='Input file. Either JP2 or Jpylyzer XML output')
    args = vars(ap.parse_args())

    is_output = args['is_output']
    input_file = args['input_file']
    csv_file = args['csv_file']

    reporter = JpylyzerReporter(csv_file)
    reporter.run(input_file, is_output)
