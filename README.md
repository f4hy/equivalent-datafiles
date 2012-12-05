equivalent-datafiles
====================

Compare two ascii data files and check if they are the same within
tolerance.

```usage: equivalent.py [-h] [-v] [-q] [-a ATOL] [-r RTOL] [-d DELIMITER]
                     file1 file2

Check if two data files are equivalent. Returns 0 if matched and 1 if not

positional arguments:
  file1                 first data file to compare
  file2                 second data file to compare

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         increase output verbosity
  -q, --quiet           run quietly, report only errors, twice report nothing
                        just return value
  -a ATOL, --atol ATOL  set the aboslute tolerance
  -r RTOL, --rtol RTOL  set the relative tolerance
  -d DELIMITER, --delimiter DELIMITER
                        delimiter of the data file
```
