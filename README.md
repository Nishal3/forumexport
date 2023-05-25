# forumexport 

A simple database reader and transformer for `posts` and `comments` databases

# Usage

Fetch a database from the cloud:
``` bash
$ export DB_URL="postgresql://username:password@IP:PORT/reviews"
$ PYTHONPATH=. python
>>> from forumexport.config import Session
>>> db_session = Session()
>>> ...
```


Export data to CSV by using export_csv.py 

Here's what the CSV format looks like
``` CSV
id,body,author_name,created_on,comments,positive_comments,negative_comments
1,This is a great tool,Kevin Bacon,2019-07-04,10,8,2
```

