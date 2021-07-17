from bs4 import BeautifulSoup
import requests
import json

class Webscrap:
    def __init__(self):
        self.dict = {"Key": "value"}
        self.dict2 = {"key": "value"}
        self.dict3 = {"key": "value"}
        self.dict4 = {"key": "value"}
        self.dict5 = {"key": "value"}
        self.url = "https://reach24.net/public_events/UnVSBUINPi1N75dp3cHxIA=="
        self.outer_key = []
        self.outer_key2 = []
        self.outer_key_lis = [self.dict2, self.dict3, self.dict4, self.dict5]
        self.i = 0



    def making_request(self):
        return requests.get(self.url).text

    def scraping_data(self, source_code):
        soup = BeautifulSoup(source_code, "html.parser")
        return soup.find("div", class_="tab-pane fade active in"), soup.find("div", class_="col-md-12 show_service_line_items")

    def data_preprosessing(self, html_code):
        data1, data2 = self.scraping_data(html_code)
        for i in range(len(data1.find_all("legend", class_="scheduler-border"))):
            self.outer_key.append(data1.find_all("legend", class_="scheduler-border")[i].text.replace("\n", ""))

        for i in range(len(data2.find_all("span", class_="mts pull-left"))):
            self.outer_key2.append(data2.find_all("span", class_="mts pull-left")[i].text)


        for i in data1.find_all(class_="flexi-div"):
            self.dict2[i.find_all(class_="info-label")[0].text.replace("\n", "").replace(":", "")] = i.find_all(class_="info-value")[0].text.replace("\n", "")
            self.i = self.i + 1
            if self.i == 12:
                break
        self.dict2.pop("key")
        for i in data1.find_all(class_="flexi-div")[self.i:]:
            self.dict3[i.find_all(class_="info-label")[0].text.replace("\n", "").replace(":", "")] = i.find_all(class_="info-value")[0].text.replace("\n", "")
            self.i = self.i + 1
            if self.i == 14:
                break
        self.dict3.pop("key")
        for i in data1.find_all(class_="flexi-div")[self.i:]:
            self.dict4[i.find_all(class_="info-label")[0].text.replace("\n", "").replace(":", "")] = i.find_all(class_="info-value")[0].text.replace("\n", "")
            self.i = self.i + 1
            if self.i == 24:
                break
        self.dict4.pop("key")
        for i in data1.find_all(class_="flexi-div")[self.i:]:
            self.dict5[i.find_all(class_="info-label")[0].text.replace("\n", "").replace(":", "")] = i.find_all(class_="info-value")[0].text.replace("\n", "")
            self.i = self.i + 1
            if self.i == 26:
                break
        self.dict5.pop("key")


        for i in range(len(self.outer_key)):
            self.dict[self.outer_key[i]] = self.outer_key_lis[i]
        self.dict.pop("Key")


        json_object = json.dumps(self.dict, indent=4)
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)



obj = Webscrap()
code = obj.making_request()
obj.data_preprosessing(code)










