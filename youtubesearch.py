import pafy as pf
import urllib.request as reqq
import urllib.parse as par
import re
search_str = par.urlencode({"search_query" : input()})
html_content= reqq.urlopen("https://www.youtube.com/results?"+search_str)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
download_url="http://www.youtube.com/watch?v=" + search_results[0]
video=pf.new(download_url)
print(video.title)
if(input("Are you sure you want to download? Type yes")=="yes"):
    best=video.getbest()
    filename = best.download(quiet=False,filepath="C:/Users/nilav/Documents/"+video.title[0:5]+"." + best.extension)

else:
    exit()
