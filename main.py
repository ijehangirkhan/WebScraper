import requests
import re

URL ='https://propakistani.pk/2021/04/05/official-lg-has-stopped-making-smartphones/'
page = requests.get(URL)


web_data = page.text
# text = re.findall(r'<(?:h1 class="entry-title".*|<div class="the-post-content">.*<p ).*>(.*?)</(?:h[1-6]|p)>', web_data)
# div_text = re.findall(r'<(?:div class="the-post-content")>(.*?)</(?:div)>', web_data)
# print(web_data)

# Some error
# (<div class="the-post-content">.*)*(.*</div>)
h_text = re.findall(r'<(?:h1 class="entry-title".*).*>(.*?)</(?:h[1-6])>', web_data)
print(h_text)

div_text = str(re.findall(r'<div class="the-post-content">((.|\n)*)<span class="tve-leads-two-step-trigger tl-2step-trigger-0">', web_data))
# div_text = re.findall(r'<div class="the-post-content">(.*)</div>', web_data)
# print(div_text)

p_text = re.findall(r'<p>([a-zA-Z].*?)</p>', div_text)
p_text = [w.replace('&#8217;', '\'') for w in p_text]
p_text = [w.replace('\\xa0<em>', ' ') for w in p_text]
p_text = [w.replace('\\xa0</em>', '') for w in p_text]
print(p_text)

# Header corrected
text = re.findall(r'<(?:h1 class="entry-title".*|p).*>(.*?)</(?:h[1-6]|p)>', web_data)

# heads = re.findall(r'<h1(.*?)>(.*?)</h1>', web_data)
# text = re.findall(r'<(?:h[1-6].*|p).*>(.*?)</(?:h[1-6]|p)>', web_data)
# print(text)
# p_text = re.findall(r'<p.*>(.*?)</p>', web_data)
# print(p_text)

file = open('data.txt', 'w')
for line in h_text:
    file.write(f"{line}\n")
for line in p_text:
    file.write(f"{line}\n")
file.close()
