Continuous Data Integration!

[![Build Status](https://img.shields.io/travis/frictionlessdata/example-continuous-data-integration.svg?branch=master&label=datapackage%20validation)](https://travis-ci.org/frictionlessdata/example-continuous-data-integration)

It goes like this:

1. You have a data package - like the one here.
2. You install a small script for testing the data package - see `scripts/test_data.py`
3. Configure travis CI - see `.travis.yml`
4. Hey presto - your data will be checked on every commit or pull request


## Examples

Here's some example of actual builds:

* TODO

We also list the sample outputs below. You can configure error output to be in JSON
or CSV rather than TXT.

### Bad Structure

This "bad" CSV (won't get any dinner):

```
Date,Country,Number,
2015-01-01,3,20.3
2015-02-01,United States,23.5,,
2015-02,United States,x23.5,,,
,,
```

Results in:

```
+----------------+---------------+-------------+-------------------------------------------------------+
| result_name    | result_id     |   row_index | result_message                                        |
+================+===============+=============+=======================================================+
| Missing Header | structure_001 |           0 | Headers column is empty.                              |
+----------------+---------------+-------------+-------------------------------------------------------+
| Defective Row  | structure_003 |           0 | The row dimensions are incorrect compared to headers. |
+----------------+---------------+-------------+-------------------------------------------------------+
| Defective Row  | structure_003 |           1 | The row dimensions are incorrect compared to headers. |
+----------------+---------------+-------------+-------------------------------------------------------+
| Defective Row  | structure_003 |           2 | The row dimensions are incorrect compared to headers. |
+----------------+---------------+-------------+-------------------------------------------------------+
| Empty Row      | structure_005 |           3 | Row is empty.                                         |
+----------------+---------------+-------------+-------------------------------------------------------+
| Defective Row  | structure_003 |           3 | The row dimensions are incorrect compared to headers. |
+----------------+---------------+-------------+-------------------------------------------------------+
```

### Bad Schema

This "bad" CSV (must be punished):

```
Date,Country,Number
2015-01-01,3,20.3
2015-02-01,United States,23.5
2015-02,United States,x23.5
```

Results in:

```
+----------------+----------------+-------------+-------------------------------------------------------------+
| result_name    |   column_index |   row_index | result_message                                              |
+================+================+=============+=============================================================+
| Incorrect Type |              0 |           2 | The value "2015-02" in column "Date" is not a valid Date.   |
+----------------+----------------+-------------+-------------------------------------------------------------+
| Incorrect Type |              2 |           2 | The value "x23.5" in column "Number" is not a valid Number. |
+----------------+----------------+-------------+-------------------------------------------------------------+
```
