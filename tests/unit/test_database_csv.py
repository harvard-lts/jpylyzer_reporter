import pytest
import os
import shutil
from project_paths import paths
from jpylyzer_reporter.database_csv import DatabaseCSV


"""
Author: awoods
Since: 5/28/23
"""

@pytest.fixture(scope='class', autouse=True)
def setup_teardown():
  global out_dir, resources_dir
  out_dir = os.path.join(paths.dir_unit_out, "db_csv")
  resources_dir = paths.dir_unit_resources
  os.makedirs(out_dir, exist_ok=True)

  # Run tests
  yield

  # Teardown
  shutil.rmtree(out_dir)
        
       
 
@pytest.mark.usefixtures("setup_teardown")
class TestDatabaseCSV():


    def test_constructor_none(self):
        with pytest.raises(Exception):
            DatabaseCSV(None)


    def test_constructor_not_exist(self):
        csv_file = os.path.join(out_dir, "csv-not-exist.csv")
        assert not os.path.isfile(csv_file)

        # Create DB from non-existent file
        database = DatabaseCSV(csv_file)

        assert os.path.isfile(csv_file)


    def test_constructor_exist(self):
        test_filename = "test-db.csv"
        csv_file_orig = os.path.join(resources_dir, test_filename)
        csv_file = os.path.join(out_dir, test_filename)
        shutil.copyfile(csv_file_orig, csv_file)

        assert os.path.isfile(csv_file)

        # Open to existing DB
        database = DatabaseCSV(csv_file)

        assert os.path.isfile(csv_file)


