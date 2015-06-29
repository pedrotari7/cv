import urllib
import re

url = "http://trakt.tv/calendar/my-shows"
request = urllib.urlopen(url).read()
test= re.findall("^http://trakt.tv/show/", request)[0]