# Jpylyzer Reporter

This tool is designed to store the results of Jpylyzer in a "database".
The use case is for downstream tools to be able to query the "database" to:
- know if an image has been reported as valid or invalid
- know the error details in the case that the image is invalid
- know the OCFL content path location of the file
- know if this file has been previously remediated

The fields of the "database" are:
- `File ID`
- `Filepath`
- `Error Type`
- `Error Value`
- `Repeat Offender`
- `Resolution`

The initial implementation of the "database" is a CSV file. 
This implementation can be replaced by another database in the future (e.g. Mongo, PostgreSQL).

## Development

The following steps are for development, not production deployment.
These steps also assume you are in the project directory (i.e. `cd jpylyzer_reporter`)

The general idea is that the developer is working inside of the local Docker container.
That means:
- The local clone of the code is mounted into a Docker container
- The developer has a terminal inside the container where the unit tests are being run
- The developer has an IDE or text editor outside of the Docker container, making changes to:
   - functional code
   - testing code

In the spirit of Test Driven Development, there should be back and forth between:
- unit tests be incrementally written, and 
- implementation of the functional code that then make updates to the tests pass


### Start service in Docker

1. Build the image
   ```
   docker build -t jpy-reporter .
   ```
1. Run the image
   Note, this assumes your are in the 
   ```
   docker run --rm -d -t --name jpy --mount type=bind,src="$(pwd)",target=/home/appuser jpy-reporter
   ```
1. Exec into the container
   ```
   docker exec -it jpy /bin/bash
   ```
1. Run unit tests
   ```
   pytest
   ```

# Usage

The tool can either take as input a JP2 file or the output of Jpylyzer.
In the case of a JP2 as input, the tool will run Jpylyzer over the image and record the details of the Jpylyzer output in the "database".
In the case of the output of Jpylyzer as input, the tool will record the details of the Jpylyzer output in the "database".

```
$ python src/jpylyzer_reporter/main.py -h

usage: main.py [-h] -c CSV_FILE [-x] input_file

Reports status of Jpylyzer to database (csv for now)

positional arguments:
  input_file            Input file. Either JP2 or Jpylyzer XML output

options:
  -h, --help            show this help message and exit
  -c CSV_FILE, --csv_file CSV_FILE
                        Location of existing or to-be-create output CSV file
  -x, --is_output       Indicates that input is XML output of Jpylyzer
```

## Examples

*Note: The following examples have not yet been implemented* 

Run tool against a JP2 file
```
$ docker run --mount type=bind,src="$(pwd)",target=/home/appuser jpy-reporter relative-path/to/example.jp2
```

Run tool against the XML output of Jpylyzer
```
$ docker run --mount type=bind,src="$(pwd)",target=/home/appuser jpy-reporter -x relative-path/to/jpylyzer-output.xml
```



