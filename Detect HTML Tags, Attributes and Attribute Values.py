from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for attr in attrs:
                print("-> " + str(attr[0]) + " > " +  str(attr[1]))
                

if __name__ == '__main__':
    html = ""
    for i in range(int(input())):
        html += input().rstrip()
        html += '\n'
    
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()