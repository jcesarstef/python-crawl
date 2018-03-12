#!/usr/bin/python3
import requests
import re
from bs4 import BeautifulSoup


class Crawl(object):
	def __init__(self, url, output=None, limitreqs=20, verbose=False):
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
							# print(link)
							if not re.match("^http:|^https:|^//|^javascript:", link):
								# print(link)
								if not re.match("^/", link):
									link = "/" + link
								if re.match(domain, link):
									if link not in path:
										path.append(link)
										self.url.append(link)
										self.status_code.append(httpreq.status_code)
										self.text.append(httpreq.text)
								else:
									link = domain + link
									if link not in path:
										path.append(link)
										self.url.append(link)
										self.status_code.append(httpreq.status_code)
										self.text.append(httpreq.text)
							elif re.match(domain, link):
								if link not in path:
									path.append(link)
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
