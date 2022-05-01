import codecs
import re
import sys
sys.stdin = codecs.getreader('latin-1')(sys.stdin.detach())
print(sum([len(re.sub('[^A-Za-z0-9 ]', '', line).split()) for line in sys.stdin]))