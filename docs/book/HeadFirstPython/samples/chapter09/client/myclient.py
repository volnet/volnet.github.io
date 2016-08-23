import urllib.request  
import urllib.parse

class MyClient:
    def send_to_server(self, cgi_url, post_data = None):
        http_server = "http://localhost:8081"
        url = http_server + '/cgi-bin/' + cgi_url

        print(url)
        print(post_data)

        if post_data:
            resp = urllib.request.urlopen(url, urllib.parse.urlencode(post_data).encode('utf-8'))
        else:
            resp = urllib.request.urlopen(url)
        return (resp.read().decode("utf-8"))

