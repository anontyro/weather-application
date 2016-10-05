import requests
import bs4

def main():
    print_the_header()

    code = input('What Zipcode do you want to weather for? ')
    
    html = get_html_from_web(code)

    report = get_weather_from_html(html)

    print('The current temparature in {} is {}{},\n the current weather condition is {}'.format(
        report[3],
        report[1],
        report[2],
        report[0]
        ))

def print_the_header():
    print('--------------------------------------------------------')
    print('                    Weather App             ')
    print('--------------------------------------------------------')

def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    
    return response.text

def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')

    loc = soup.find(id='location').find('h1').get_text()
    loc = find_city_and_state_from_location(loc)
    condition = soup.find(id = 'curCond').find(class_='wx-value').get_text()
    temp = soup.find(id = 'curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id = 'curTemp').find(class_='wx-unit').get_text()

    loc = cleanup_text(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    return (condition, temp, scale, loc)

def find_city_and_state_from_location(loc):
    parts = loc.split('\n')
    return parts[1].strip()

def cleanup_text(text):
    if not text:
        return text
    
    text = text.strip()
    return text

if (__name__ == '__main__'):
    main()