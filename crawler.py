#!/usr/bin/python3
import requests
import re
from bs4 import BeautifulSoup


#
def normalize(proburl, domain, path):
	if not re.match("^http:|^https:|^//|^javascript:", proburl):
		if not re.match("^/", proburl):
			proburl = "/" + proburl
		if re.match(domain, proburl):
			if proburl not in path:
				return proburl

		else:
			proburl = domain + proburl
			if proburl not in path:
				return proburl

	elif re.match(domain, proburl):
		if proburl not in path:
			return proburl
	#print("proburl: " + proburl)

class Crawl(object):
	def crawl(self, url, output=None, limitreqs=20, verbose=False):
		domain = re.findall("http[s]?://[a-z0-9.][a-z0-9-.]{0,61}[a-z0-9.]*", url)[0]
		path = []
		self.url = []
		self.status_code = []
		self.text = []
		done = []
		totalreqs = 0
		if url not in path:
			path.append(url)
		# TODO
		# notprocessfiles = (".jpg", ".gif", ".jpeg", ".ico", ".tiff", ".png", ".bmp")
		extract = {
			"a": "href",
			"img": "src",
			"form": "action",
			"script": "src",
			"iframe": "src",
			"div": "src",
			"frame": "src",
			"embed": "src",
			"link": "href",
		}
		for urlvalue in path:
			if urlvalue not in done and totalreqs != limitreqs:
				httpreq = requests.get(urlvalue)
				totalreqs += 1
				if verbose:
					print("[" + str(totalreqs) + "]" + "[" + str(len(path)) + "] " + urlvalue)
				soup = BeautifulSoup(str(httpreq.text), "lxml")
				for tag in extract:
					# print(tag + " => " + extract[tag])
					for htmltag in soup.find_all(tag):
						try:
							link = htmltag[extract[tag]]
							#print("LINK: " + link)
							internallink = normalize(link, domain, path)

							if internallink is not None:
								path.append(internallink)
								self.url.append(link)
								self.status_code.append(httpreq.status_code)
								self.text.append(httpreq.text)


						# print("Total URL's: "+ str(len(path)))
						except KeyError:
							pass
				done.append(urlvalue)
		print("Total URL's found: " + str(len(path)))

		if output is not None:
			f = open(output, 'w')
			for reg in done:
				print(reg)
				f.write(reg)
			f.close()
