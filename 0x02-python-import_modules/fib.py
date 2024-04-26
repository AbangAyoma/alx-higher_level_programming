import sys
from urllib.request import urlopen # module To access internet
import smtplib # module to send mails.
from datetime import date #module for date and time
import zlib # FOR COMPRESSION AND DECOMPRESSION
#import gzip 
# import bz2 
# import lzma
# import tarfile
# import zipfile

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
# This code makes the module to run as a script with command line
#arguments.

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
# this code will open the url and check fot the line 
#that start with datetime, removed the newline character and print the date
# and time
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()             # Convert bytes to a str
        if line.startswith('datetime'):
            print(line.rstrip()) 

server = smtplib.SMTP('localhost') #to access server, localhost
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org

Beware the Ides of March.
""")
server.quit()
# Note that this needs a mailserver running on localhost  

#TO FIND DATE
now = date.today()
now

now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
age.days

#FOR DATA COMPRESSION AND DECOMPRESSION
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s) #to compress s
len(t)
zlib.decompress(t) # to decompress
zlib.crc32(s)