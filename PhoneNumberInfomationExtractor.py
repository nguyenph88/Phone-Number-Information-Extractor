# PhoneNumberInformationExtractor.py
# ------------
# Licensing Information:  You are free to use or extend this class/project/file
# for personal or educational purposes provided that:
# 1. You do not re-distribute under other names.
# 2. You retain this notice and include a link to its original source.
# 3. You notice me if you want go use it for any other purposes.
# 
# Last modified: April 06, 2014 
#
# 		Author: Peter Nguyen  - nguyenph88@gmail.com
# 		nguyenphuoc.net | github.com/nguyenph88 | linkedin.com/in/nguyenphuoc
#
# PhoneNumberInformationExtractor.py : Get Carrier Name, City, State etc ... based on
#     the given phone number.
#
# Requirement:
#  - Beautiful Soup 4 <http://www.crummy.com/software/BeautifulSoup/>
#  - agent.py <https://github.com/nguyenph88/User-Agent-Generator>
#------------------------------------------------------------------------------------

import os
import urllib2, re
import agent
from bs4 import BeautifulSoup

class PhoneNumberInformationExtractor:
	def __init__(self, phone_number = None):
		if (phone_number is None):
			self.phone = ''
		else:
			self.phone = phone_number
				
	def setPhoneNumber(self, pn):
		self.phone = pn

	def getPhoneNumber(self):
		return self.phone

	'''
	Every request will be handled and sent from here 
	Reason I seperate it because I will implement sock/proxy connection later
	'''
	def getWebResponse(self,url):
		request = urllib2.Request(url)
		request.add_header('User-Agent', agent.genUserAgent())
		response = urllib2.urlopen(request)
		#return str(self.response.read()) --> cast it to string if don't use Beautiful Soup
		return response.read()       # Otherwise keep the html object for Beautiful Soup

	'''
	Get Phone Carrier based on the phone number
	'''
	def getCarrier(self):
		url = 'http://www.fonefinder.net/findome.php?npa=' + self.phone[0:3] + '&nxx=' + \
				self.phone[3:6] + '&thoublock=' + self.phone[6:]
		html = self.getWebResponse(url)
		soup = BeautifulSoup(html)
		# invalid phone number or no record found
		if 'no records found' in html:
			return 'failed'
		# valid cases
		else:
			tables = soup.findAll('table')           # We just need the 2nd tables from the list
			for row in tables[1].findAll('tr'):
				for data in row.findAll('td'):
					# Condition, change for each Get
					if 'fonefinder' in str(data) and not 'graphic' in str(data):
						result = str(data.findAll(text=True))
		# Should concat the result as it will have special chars there
		return result[3:len(result)-2]


	'''
	Get City based on the given phone number
	'''
	def getCity(self):
		url = 'http://www.fonefinder.net/findome.php?npa=' + self.phone[0:3] + '&nxx=' + \
				self.phone[3:6] + '&thoublock=' + self.phone[6:]
		html = self.getWebResponse(url)
		soup = BeautifulSoup(html)
		# invalid phone number or no record found
		if 'no records found' in html:
			return 'failed'
		# valid cases
		else:
			tables = soup.findAll('table')           # We just need the 2nd tables from the list
			for row in tables[1].findAll('tr'):
				for data in row.findAll('td'):
					# Condition, change for each Get
					if 'findcity' in str(data) and not 'State info' in str(data):
						result = str(data.findAll(text=True))
		# Should concat the result as it will have special chars there
		return result[3:len(result)-2]

	'''
	Get State based on given phone number
	'''
	def getState(self):
		url = 'http://www.fonefinder.net/findome.php?npa=' + self.phone[0:3] + '&nxx=' + \
				self.phone[3:6] + '&thoublock=' + self.phone[6:]
		html = self.getWebResponse(url)
		soup = BeautifulSoup(html)
		# invalid phone number or no record found
		if 'no records found' in html:
			return 'failed'
		# valid cases
		else:
			tables = soup.findAll('table')           # We just need the 2nd tables from the list
			for row in tables[1].findAll('tr'):
				for data in row.findAll('td'):
					# Condition, change for each Get
					if 'graphic' in str(data):
						result = str(data.findAll(text=True))
		# Should concat the result as it will have special chars there
		return result[3:len(result)-2]
if __name__ == '__main__':
	test = PhoneNumberInformationExtractor('5104693890')
	print test.getCarrier()
	print test.getCity()
	print test.getState()
