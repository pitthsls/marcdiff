**marcdiff** generates an HTML diff of files containing MARC21 records.

Currently, the files must use field 001 as a consistent record ID between
the files, and all records in the second file must be present in the first 
file.

Records present in the first file and not the second file will not be displayed
unless the --include_missing option is specified.

Missing records only have their record ID (field 001) displayed, and
diffs only show 5 lines before and after a change unless --no-brief is 
specified.

    Usage: marcdiff [OPTIONS] FILE1 FILE2 [OUTFILE]
    
      Compare 2 files of MARC records. file2 must be a subset of the records in
      file1, with existing records in the same order in both files. If OUTFILE
      is not given, output will be written to 'marcdiff_output.html' in the
      working directory.
    
    Options:
      --include_missing     include records missing from file2 in output
      --brief / --no-brief  only show changed and nearby lines, not entire records
                            (default)
      --help                Show this message and exit.



