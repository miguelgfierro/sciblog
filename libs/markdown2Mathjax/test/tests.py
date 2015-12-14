#Some simple test strings.
test='This is a test string with \\$ some escaped $2+3$ and some non-escaped $\\$$ characters.  I hope we can find a pattern to work on this \\$$\\$ ugly$ bitch.  We had better include some $$ double $ like this $$ as well just in case.'
dtest="""This one will start off with some dobule $$ 2+4$ = 3$$, just to make shit diffiult."""
ptest = """ Let's put a few instances of the $0$ placeholder in $23+2$ just to see $0$ if it $$ $0$ $ $$ gets picked up.  Oh and don't forget a few which are escaped \\$0$ $23$"""

import libs.markdown2Mathjax.lib.markdown2Mathjax as m
tmp=m.sanitizeInput(test)
tmpd=m.sanitizeInput(dtest)
tmpp=m.sanitizeInput(ptest)

if m.reconstructMath(tmp[0],tmp[1])==test:
    print "PASS"
if m.reconstructMath(tmpd[0],tmpd[1])==dtest:
    print "PASS"
if m.reconstructMath(tmpp[0],tmpp[1])==ptest:
    print "PASS"
