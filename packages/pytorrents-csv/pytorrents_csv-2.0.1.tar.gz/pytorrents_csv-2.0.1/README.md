# pytorrents-csv

a python client for https://torrents-csv.com/

Installation: `pip install pytorrents-csv`

Usage:

```
usage: pytorrents-csv [-h] -q QUERY [-n NUMBER] [-p PAGE]

a python cli client for torrents-csv

options:
  -h, --help            show this help message and exit
  -q QUERY, --query QUERY
                        Torrent names to search
  -n NUMBER, --number NUMBER
                        The number of results to return (default 10)
  -p PAGE, --page PAGE  Page number to return (default 1)
```

Example:

```
pytorrents-csv -q "the art of war epub" -n 1
```
```

-------------------------------------
Name: THE ART OF WAR - Sun Tzu (pdf, epub, mobi)
Size: 989.0 KB
Date Created: 2013-07-20 16:44:32
Seeders: 24
Infohash: 485df096772c4532da1e987dbd28481cb11a7eaa
-------------------------------------

Query: the art of war epub
Number of results: 1
Page: 1
```

---
### Disclaimer
I am not encouraging piracy and I am not responsible for any legal troubles you may get yourself in. Only download material that is public domain or that you are allowed to download. 

Not affiliated with torrents-csv.com
