import urllib.request, re
req = urllib.request.Request('https://arstechnica.com/gadgets/2025/08/github-will-be-folded-into-microsoft-proper-as-ceo-steps-down/', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
match = re.search(r'property="og:image"\s+content="([^"]+)"', html)
if match:
    print(match.group(1))
else:
    print("Not found")
