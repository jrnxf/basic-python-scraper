import sys
import requests
import json

def main():
    username = ''
    while username == '':
        username = input("Username to search?\n")

    try:
        url = (f'https://api.github.com/users/{username}')
        response = requests.get(url).content
        data = json.loads(response)
        name = data['name']
        company = data['company']
        location = data['location']
        blog = data['blog']
        html_url = data['html_url']

        print(f'{name} lives in {location} and works for {company}. You can visit their website at {blog} and their github profile at {html_url}.')
    except:
        print('An error occured. Let\'s try that again!\n')
        main()

main()