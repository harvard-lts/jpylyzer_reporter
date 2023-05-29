from jpylyzer_reporter.database import Database
import csv
import os


"""
Author: awoods
Since: 5/28/23
"""
class DatabaseCSV(Database):

    csv_fieldnames = ['File ID',
                      'Filepath',
                      'Error Type',
                      'Error Value',
                      'Repeat Offender',
                      'Resolution'
                     ]


    def __init__(self, csv_file):
        if not csv_file:
            raise Exception("Input must have a value!")

        self._validate_or_create(csv_file)
        self.csv_file = csv_file


    def _validate_or_create(self, csv_file):
        """
        - if csv exists, verify its columns
        - else, create empty csv with expected columns
        """
        
        if os.path.isfile(csv_file):
            # Verify existing csv
            with open(csv_file, mode='r') as c:
                csv_reader = csv.DictReader(c)
                line_count = 0

                # Loop through csv_fieldnames, verifying that they match what \
                #   is in the file
                raise Exception("start here!!!")
                for row in csv_reader:
                    if line_count == 0:
                        print(f'Column names are {", ".join(row)}')
                        line_count += 1
                    line_count += 1
                print(f'Processed {line_count} lines.')
        else:
            # Create new csv at csv_file location
            with open(csv_file, mode='w') as c:
                fieldnames = ['emp_name', 'dept', 'birth_month']
                writer = csv.DictWriter(c, fieldnames=self.csv_fieldnames)
                writer.writeheader()
