use warehouse COMPUTE_WH;
use database COVID19INDIA;
use schema PUBLIC;

create or replace table staging
(
    RAW_DATA VARIANT
);

PUT file:///home/soumya/Documents/covid19india/raw_data_integration.json  @%staging;

LIST @%staging;

copy into staging
   from @%staging
   file_format = (type = 'json' STRIP_OUTER_ARRAY = TRUE)
   on_error = 'skip_file';