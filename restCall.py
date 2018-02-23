


import urllib2


i_ticker = "C_USA_CHN"
i_field = "EXPORT"
i_source = "USDA"
i_key = "ENTER_KEY"

link = 'http://localhost:5000/data?ticker=' + i_ticker
link = link + '&field=' + i_field + '&source=' + i_source
link = link + '&key=' + i_key


print urllib2.urlopen(link).read()

