import os
import urllib2
import time

def webUpdate(url):
    cLocation = __file__
    tFile = open("temp.py", "wb")
    try:
        http = urllib2.urlopen(url)
    except Exception as e:
        if os.path.exists('update.log'):
            logErr = open('update.log', 'ab')
            logErr.write('/n')
            logErr.write(url)
            logErr.write('/n')
            logErr.write(datetime.datetime.now)
            logErr.write(e)
            logErr.write('/n')
            logErr.close()
        else:
            logErr = open('update.log', 'wb')
            logErr.write('/n')
            logErr.write(url)
            logErr.write('/n')
            logErr.write(datetime.datetime.now)
            logErr.write(e)
            logErr.write('/n')
            logErr.close()
        return    
    #uCode = http.read()
    aPos = "'''"
    tempCode = """import os
import time
import datetime
import urllib2
http = urllib2.urlopen('%s')
html = http.read()
try:
    time.sleep(10)
    fileLoc = '%s'
    mFile = open(fileLoc, "wb")
    mFile.write(html)
    mFile.close()
    os.startfile(fileLoc)
except Exception as e:
    print e
    if os.path.exists('update.log'):
        logErr = open('update.log', 'ab')
        logErr.write('/n')
        logErr.write(datetime.datetime.now)
        logErr.write(e)
        logErr.write('/n')
        logErr.close()
    else:
        logErr = open('update.log', 'wb')
        logErr.write('/n')
        logErr.write(datetime.datetime.now)
        logErr.write(e)
        logErr.write('/n')
        logErr.close()
    time.sleep(20)"""
    updateFile = tempCode % (url, cLocation)
    tFile.write(updateFile)
    os.startfile(os.getcwd() + '\\temp.py')
    quit()
