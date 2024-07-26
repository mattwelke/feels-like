import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def find_main_forecast_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find('div', id='main-forecast-content')

def extract_forecast_data(main_forecast_content):
    forecast_data = []
    current_day = ""

    for element in main_forecast_content.descendants:
        if element.name == 'div' and element.get('data-testid') == 'period-section-heading':
            day_div = element.find('div', class_='sc-eDPEul cHVRQd')
            if day_div:
                current_day = day_div.get_text(strip=True)

        if element.name == 'div' and element.get('data-testid') == 'forecast-module-row':
            time_div = element.find('div', {'data-testid': 'row-date-or-time'})
            feels_like_div = element.find('div', {'data-testid': 'row-feels-like'})

            if time_div and feels_like_div:
                time = time_div.get_text(strip=True)
                feels_like = feels_like_div.get_text(strip=True)

                # Parse the temperature from the feels_like string and add degrees Celsius.
                # Example: "Feels26" -> "26 °C".
                feels_like = feels_like.replace('Feels', '') + ' °C'

                if time in ['7pm', '8pm', '9pm']:
                    forecast_data.append((current_day, time, feels_like))

    return forecast_data

def main():
    url = 'https://www.theweathernetwork.com/en/city/ca/ontario/toronto/hourly'  # Replace with your URL
    html = fetch_html(url)
    main_forecast_content = find_main_forecast_content(html)

    if not main_forecast_content:
        print("main-forecast-content div not found")
        return

    forecast_data = extract_forecast_data(main_forecast_content)
    
    for day, time, feels_like in forecast_data:
        print(f'Day: {day}, Time: {time}, Feels Like: {feels_like}')

if __name__ == '__main__':
    main()
