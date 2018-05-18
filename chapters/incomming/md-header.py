#!/usr/bin/env python

import os
import re
from glob import glob

metahead = \
'''
|          | {head} |
| -------- | {dash} |
| title    | {title} |
| status   | {status} |
| section  | {section} |
| keywords | {keywords} |
'''

# adding table header
# changing section header lien from the underlying '----' to prefixing '##'
#
# for all *.md files in the current directory
mdfiles = glob("*.md")
findtitlept = re.compile("([^\n]+?)\n-+\n(.*)", re.M | re.I | re.S)
for amdfile in mdfiles:
    contentin = None
    with open(amdfile) as fin:
        contentin = fin.read()
    matchret = re.match(findtitlept, contentin)
    if matchret:
        title = matchret.group(1)
        content = matchret.group(2)
        nlen = len(title)
        status = 95
        sectitle = 'TBD'
        keywords = 'TBD'
        output = "## %s\n\n%s\n\n%s" % (title,
                                        metahead.format(head=' ' * nlen,
                                                        dash='-' * nlen,
                                                        title=('{0: <%s}' % nlen).format(title),
                                                        status=('{0: <%s}' % nlen).format(status),
                                                        section=('{0: <%s}' % nlen).format(sectitle),
                                                        keywords=('{0: <%s}' % nlen).format(keywords)
                                                        ),
                                        content)
        with open(amdfile, 'w') as fout:
            fout.write(output)

#
# adding url link after the header table
#
# as we have changed the section header style, we have to redo the matching again
mdfiles = glob("*.md")
tableheaderpt = re.compile("(.+?)\| keywords \|(.*?)\|\n(.*)", re.M|re.I|re.S)
for amdfile in mdfiles:
    print amdfile
    contentin = None
    with open(amdfile) as fin:
        contentin = fin.read()
    matchret = re.match(tableheaderpt, contentin)
    if matchret:
        beforeheader = matchret.group(1)
        headerkwds = matchret.group(2)
        content = matchret.group(3)
        link = "Link to source in github [:cloud:](https://github.com/cloudmesh/technologies/blob/master/chapters/incomming/%s)" % amdfile
        output = "%s| keywords |%s|\n\n%s\n%s" % (beforeheader,
                                                  headerkwds,
                                                  link,
                                                  content)
        print output

        with open(amdfile, 'w') as fout:
            fout.write(output)
