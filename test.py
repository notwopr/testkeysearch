import re
samplestr = "159.41 btc"
print("sample test string to search: ", samplestr)
found = re.findall('[1-9]+ btc', samplestr)
print("found= ", len(found))
