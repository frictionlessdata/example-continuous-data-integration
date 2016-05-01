from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import json
from goodtables import pipeline as _pipeline
from goodtables import processors

import datapackage

# TODO: consistent API for dp validate
# errors = dp.validate()
# if errors: ...

dp = datapackage.DataPackage('./datapackage.json')

def check_datapackage_json():
    try:
        dp.validate()
    except datapackage.exceptions.ValidationError as e:
        # Handle the ValidationError
        pass

def check_json_schema():
    pass

def check_structure():
    report_limit = 1000
    row_limit = 100000
    data_format = 'csv'
    processor = processors.StructureProcessor(format=data_format, fail_fast=False,
        row_limit=row_limit,
        report_limit=report_limit)

    data = dp.metadata['resources'][0]['path']

    valid, report, data = processor.run(data)

    valid_msg = 'Well done! The data is valid :)\n'.upper()
    invalid_msg = 'Oops.The data is invalid :(\n'.upper()

    print(valid_msg)

def check_data_schema():
    processor = processors.SchemaProcessor(schema=schema, format=format,
        fail_fast=fail_fast,
        row_limit=row_limit,
        report_limit=report_limit)
    valid, report, data = processor.run(data)

def run():
    # check_datapackage_json()
    check_structure()


if __name__ == '__main__':
    run()

