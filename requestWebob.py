from webob import Request
requests=[]
wikipedia = Request.blank("wikipedia.org")
wikipedia.host = 'wikipedia.org'
wikipedia.environ["SERVER_NAME"] = 'wikipedia.org'
wikipedia.accept = "text/html"
wikipedia.user_agent = "User-Agent: Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9b5) Gecko/2008050509 Firefox/3.0b5"
requests.append(wikipedia)

httpbin1 = Request.blank("")
httpbin1.host = 'httpbin.org'
httpbin1.environ["SERVER_NAME"] = 'httpbin.org'
httpbin1.accept = '*/*'
requests.append(httpbin1)

httpbin2 = Request.blank("get?foo=bar&1=2&2/0&error=True")
httpbin2.host = 'httpbin.org'
httpbin2.environ["SERVER_NAME"] = 'httpbin.org'
httpbin2.accept = '*/*'
requests.append(httpbin2)

httpbin3 = Request.blank("post")
httpbin3.host = 'httpbin.org'
httpbin3.environ["SERVER_NAME"] = 'httpbin.org'
httpbin3.method = 'POST'
content = "foo=bar&1=2&2%2F0=&error=True".encode('ascii')
httpbin3.content_type = "application/x-www-form-urlencoded"
httpbin3.body = content
httpbin3.content_length = len(content)
httpbin3.headers['Connection'] = 'close'
requests.append(httpbin3)

httpbin4 = Request.blank('cookies/set?country=Ru')
httpbin4.host = 'httpbin.org'
httpbin4.environ["SERVER_NAME"] = 'httpbin.org'
httpbin4.accept = '*/*'
httpbin4.headers['Connection'] = 'close'
requests.append(httpbin4)

httpbin5 = Request.blank("cookies")
httpbin5.host = 'httpbin.org'
httpbin5.environ["SERVER_NAME"] = 'httpbin.org'
httpbin5.accept = '*/*'
httpbin5.headers['Connection'] = 'close'
requests.append(httpbin5)

httpbin6 = Request.blank('redirect/4')
httpbin6.host = 'httpbin.org'
httpbin6.environ["SERVER_NAME"] = 'httpbin.org'
httpbin6.accept = '*/*'
httpbin6.headers['Connection'] = 'close'
requests.append(httpbin6)

httpbin7 = Request.blank("post")
httpbin7.host = 'httpbin.org'
httpbin7.environ["SERVER_NAME"] = 'httpbin.org'
httpbin7.method = 'POST'
content = "firstname=Nikita&lastname=Ragozin&group=fo340001&message=empty_message".encode('ascii')
httpbin7.content_length = len(content)
httpbin7.content_type = "application/x-www-form-urlencoded"
httpbin7.body = content
httpbin7.headers['Connection'] = 'close'
requests.append(httpbin7)

for request in requests:
	responce = request.get_response()
	responce.content_type = 'text/plain'
	responce.charset = 'utf-8'
	print(responce)
	print("\n\n------------\n\n")

