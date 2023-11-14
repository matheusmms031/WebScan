import requests



def robotsscan(url,header):
    
    response = requests.get(f"https://{url}/robots.txt",headers=header)
    if response.status_code == 200:
        elements = []
        directories = []
        for c in response.text.replace('\r', '').split("\n"):
            elements.append(c.split(':'))
        for element in elements:
            if len(element) == 2:
                directories.append(element[1])
        return [True, directories]
    else:
        return False