**marcdiff** generates an HTML diff of files containing MARC21 records.

Currently, the files must use field 001 as a consistent record ID between
the files, and all records in the second file must be present in the first 
file.

Records present in the first file and not the second file will not be displayed.

    Usage: marcdiff [OPTIONS] FILE1 FILE2 [OUTFILE]

    Options:
      --help  Show this message and exit.
