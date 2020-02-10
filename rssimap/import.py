# encoding: utf-8
import opml

o = opml.parse("YOUR_FILE_HERE")
for f in o:
    if len(f) > 0:
        for f2 in f:
            print("'%s': '%s'," % (f2.title, f2.xmlUrl))
    else:
        print("'%s': '%s'," % (f.title, f.xmlUrl))
