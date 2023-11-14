import requests



def robotsscan(url,header):
    """
    The function `robotsscan` takes a URL and a header as input, sends a GET request to the URL's
    robots.txt file with the provided header, and returns a list of directories if the request is
    successful, or False otherwise.
    
    Args:
      url: The `url` parameter is the URL of the website you want to scan for the robots.txt file. It
    should be a string representing the domain name of the website (e.g., "example.com").
      header: The "header" parameter is a dictionary that contains the headers to be included in the
    HTTP request. Headers are used to provide additional information to the server, such as the user
    agent, content type, etc.
    
    Returns:
      a list. If the response status code is 200, it returns a list with the first element as True and
    the second element as a list of directories. If the response status code is not 200, it returns a
    list with the first element as False.
    """
    
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