from jpylyzer import jpylyzer
from jpylyzer_reporter.database_csv import DatabaseCSV
import os
import logging
import csv


class JpylyzerReporter():


    def __init__(self, csv_file):
      self.database = DatabaseCSV(csv_file)


    def run(self, input_file, is_output=False):
      """
      Either process the XML output of a Jpylyzer run, or validate an image
      """

      # Ensure input_file existss
      if not os.path.isfile(input_file):
        raise Exception("Input must be a file: {}".format(input_file))

      if is_output:
        self._process_output(input_file)
      else:
        output_xml = self._run_jpylyzer(input_file)
        self._process_output(output_xml)


    def _run_jpylyzer(self, image_file):
        """
        Execute Jpylyzer on provided image file
        """
        result = jpylyzer.checkOneFile(image_file)
        logging.info(result)




    def _process_output(self, output_xml):
        """
        Store results in output_xml into "database"
        """
        pass
        
