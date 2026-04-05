---
tags: [linux, linux/commands]
title: tar and gzip
date created: Sunday, December 21st 2025, 4:21:55 pm
date modified: Sunday, April 5th 2026, 10:19:04 pm
parent: Linux
grand_parent: Misc
nav_order: 6
---
# tar and gzip
Compress: (with `gzip`)

```
$ tar czf NAME.tar.gz COMPRESS_PATH
```

Decompress: (with `gzip`)

```
$ tar xzf COMPRESSED_FILE OUTPUT_DIR
```

Add the `v` option to see what it's doing (can be slower as there's an extra step to output to `stdout`)

But a tar is just a archiver, it puts all of the files into one `.tar` archive. And on the web, browsers and HTTP servers are more friendly to just `.gz` which you do with:

```
$ gzip -k FILE
```

`-k` preserves the original file

#linux #linux/commands