import requests
reading_web_status_list = []
with open("websites_to_check.txt", "r", encoding="UTF-8") as file:
    reading_web = file.readlines()
    print(reading_web)
    for i in reading_web:
        temp = i.strip()
        reading_web_status_list.append(temp.split(" "))
print(reading_web_status_list)
with open("filter_ok_websites.txt", "w", encoding="UTF-8") as fileappend:
    for i in reading_web_status_list:
        i = i[0]
        try:
            web = requests.get(i)
        except requests.exceptions.MissingSchema:
            print("To nie jest strona www:",i)

        web = str(web)
        if web == "<Response [200]>":
            fileappend.write(i)
            fileappend.write("\n")
        web = ""