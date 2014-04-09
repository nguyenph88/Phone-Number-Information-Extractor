Phone-Carrier-Finder
====================

Given a phone number, the code returns the Carrier Name, City, State that the phone number is registered to. I made this small app in order to learn 'Beautiful Soup 4' which is a really powerful and useful tool for HTML markup. I play a lot with data analysis and extracting data from website so this BS4 is really helpful for me.

Usage:
```
test = PhoneNumberInformationExtractor('xxxxxxxxxx')
print 'Carrier:', test.getCarrier()
print 'City:', test.getCity()
print 'State', test.getState()

Carrier: SPRINT SPECTRUM L.P.
City: OKLD MN-PD
State: California
```

Requirement:
```
- Beautiful Soup 4 <http://www.crummy.com/software/BeautifulSoup/>
- agent.py <https://github.com/nguyenph88/User-Agent-Generator>
```