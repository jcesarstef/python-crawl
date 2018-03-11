# python-crawl
Personal library to extract internal links from domain

# Usage

### Basics

```
python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from crawler import crawl

>>> out = crawl('http://www.inseguro.com.br')
Total URL's: 60

>>> for url in out:
...     print(url)
... 
http://www.inseguro.com.br
http://www.inseguro.com.br/2017/10/bwapp-1-xss-reflected-overview.html
http://www.inseguro.com.br/2017/10/bwapp-1-xss-reflected-overview.html#more
http://www.inseguro.com.br/2017/10/bwapp-1-xss-reflected-overview.html#comment-form
http://www.inseguro.com.br/2017/10/bwapp-1-xss-reflected-overview.html#links
http://www.inseguro.com.br/search/label/bWAPP
http://www.inseguro.com.br/search/label/Code%20Review
http://www.inseguro.com.br/search/label/hacking
http://www.inseguro.com.br/search/label/penetration%20testing
http://www.inseguro.com.br/search/label/xss
http://www.inseguro.com.br/2017/10/bwapp-buggy-web-application-ambiente.html
http://www.inseguro.com.br/2017/10/bwapp-buggy-web-application-ambiente.html#more
http://www.inseguro.com.br/2017/10/bwapp-buggy-web-application-ambiente.html#comment-form
http://www.inseguro.com.br/2017/10/bwapp-buggy-web-application-ambiente.html#links
http://www.inseguro.com.br/2017/09/paralelos-descubra-como-pirataria-e-o.html
http://www.inseguro.com.br/2017/09/paralelos-descubra-como-pirataria-e-o.html#more
http://www.inseguro.com.br/2017/09/paralelos-descubra-como-pirataria-e-o.html#comment-form
http://www.inseguro.com.br/2017/09/paralelos-descubra-como-pirataria-e-o.html#links
http://www.inseguro.com.br/search/label/cultura
http://www.inseguro.com.br/2017/08/seo-e-suas-armadilhas-de-seguranca.html
http://www.inseguro.com.br/2017/08/seo-e-suas-armadilhas-de-seguranca.html#more
http://www.inseguro.com.br/2017/08/seo-e-suas-armadilhas-de-seguranca.html#comment-form
http://www.inseguro.com.br/search/label/Google%20Dork
http://www.inseguro.com.br/search/label/OSINT
[...]

```
### Export to txt
```
>>> crawl('http://www.inseguro.com.br', output="www.inseguro.com.br.txt")
```
