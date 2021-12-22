import requests
from bs4 import BeautifulSoup
# 2. Create a User Agent (Optional)
headers = {"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 ("
                         "KHTML, like Gecko) Version/4.0 Safari/534.30"}
# 3. Send get() Request and fetch the webpage contents
response = requests.get("https://shubhamsayon.github.io/python/demo_html.html", headers=headers)
webpage = response.content
# 4. Check Status Code (Optional)
# print(response.status_code)
# 5. Create a Beautiful Soup Object
soup = BeautifulSoup(webpage, "html.parser")
# 6. Implement the Logic.
for tr in soup.find_all('tr'):
    topic = "TOPIC: "
    url = "URL: "
    values = [data for data in tr.find_all('td')]
    for value in values:
        print(topic, value.text)
        topic = url
    print()