from copy import deepcopy
import glob
import sys

from search import *
from solitaire import *


f = glob.glob("IA201819-Solitaire-Tests/*")

for link in f:
    if ('.' in link):
        f.remove(link)

EXEC_RETURN=''
#overwrites the print function
def print(arg):
    global EXEC_RETURN
    EXEC_RETURN= arg



for link in f:

    with open(link+"/input", 'r') as content_file:
        content = content_file.read()

    with open(link + "/output", 'r') as content_file:
        output = content_file.read()

    sys.stdout.write("INPUT\n")
    sys.stdout.write(content+"\n")
    sys.stdout.write("REAL\n")
    sys.stdout.write(output+"\n")
    try:
        exec(content)

        sys.stdout.write("OUT\n")
        sys.stdout.write(str(EXEC_RETURN))
        sys.stdout.write("\n\n")

        user_out=str(EXEC_RETURN)
        result1 = ''
        result2 = ''

        # handle the case where one string is longer than the other
        maxlen = len(output) if len(user_out) < len(output) else len(user_out)

        # loop through the characters
        for i in range(maxlen):
            # use a slice rather than index in case one string longer than other
            letter1 = user_out[i:i + 1]
            letter2 = output[i:i + 1]
            # create string with differences
            if letter1 != letter2:
                result1 += letter1
                result2 += letter2

        # print out result
        if(result1):
            sys.stdout.write("Letters different in input:"+ result1)
        # sys.stdout.write("Letters different in output:"+ result2)

    except Exception as e:
        sys.stdout.write("ERROR\n")
        sys.stdout.write(str(e))
        sys.stdout.write("\n\n")
