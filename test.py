import re
samplestr = "aerbaer regae4tnb4a3t34na34an a4 00100,000.0 btcaw4nta4ta 4w"
print("sample test string to search: ", samplestr)
found = (
    re.findall(" [0-9]*[1-9] btc", samplestr)
    + re.findall(" [0-9]*[1-9]+0+ btc", samplestr)
    + re.findall(" \.[0-9]+ btc", samplestr)
    + re.findall(" [0-9]+\.[0-9]+ btc", samplestr)
    + re.findall("[0-9]{1,3}(?:,[0-9]{3})+ btc", samplestr)
    + re.findall("[0-9]{1,3}(?:,[0-9]{3})+\. btc", samplestr)
    + re.findall("[0-9]{1,3}(?:,[0-9]{3})+\.[0-9]+ btc", samplestr)
)
print("found= ", found)
'''
NO commas
' [0-9]+'
' [.][0-9]+'
'[0-9]+[.] '
'[0-9]+[.][0-9]+'

with commas

'[0-9]{1,3}(?:,[0-9]{3})


'[0-9]{1,3}[[,][0-9]{3}]+\. '
'[0-9]{1,3}[[,][0-9]{3}]+\.[0-9]+'
'''
