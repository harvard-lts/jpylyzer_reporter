from jpylyzer_reporter.reporter import JpylyzerReporter
from project_paths import paths
import pytest
import os
import shutil

"""
Author: awoods
Since: 5/28/23
"""

@pytest.fixture(scope='class', autouse=True)
def setup_teardown():
  global out_dir
  out_dir = os.path.join(paths.dir_unit_out, "reporter")
  os.makedirs(out_dir, exist_ok=True)

  # Run tests
  yield

  # Teardown
  shutil.rmtree(out_dir)


@pytest.mark.usefixtures("setup_teardown")
class TestWorkerClass():


    def test_constructor_bad_input_none(self):
        with pytest.raises(Exception):
            reporter = JpylyzerReporter(None)


    def test_bad_input_none(self):
        reporter = JpylyzerReporter(os.path.join(out_dir, "test.csv"))
        with pytest.raises(Exception):
            report.run(None)


    def test_bad_input_not(self):
        reporter = JpylyzerReporter(os.path.join(out_dir, "test.csv"))
        with pytest.raises(Exception):
            reporter.run("/not/a/file")


    def test_reporter_xml(self):
        test_resources_dir = paths.dir_unit_resources
        test_file = "46818915-valid.xml"

        reporter = JpylyzerReporter(os.path.join(out_dir, test_file + ".csv"))
        reporter.run(os.path.join(test_resources_dir, test_file), is_output=True)
