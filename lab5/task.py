import requests
from bs4 import BeautifulSoup
import csv
import argparse
import time
import os
import re

class CountryDataScraper:
    def init(self, cache_dir='cache'):
        self.cache_dir = cache_dir
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
    
    def get_cache_filename(self, country):
        safe_name = re.sub(r'[^\w\s-]', '', country).strip().lower()
        safe_name = re.sub(r'[-\s]+', '_', safe_name)
        return os.path.join(self.cache_dir, f"{safe_name}.html")
    
    def fetch_page(self, country):
        cache_file = self.get_cache_filename(country)
        
        if os.path.exists(cache_file):
            print(f"using cache for {country}")
            with open(cache_file, 'r', encoding='utf-8') as f:
                return f.read()
        
        url = f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"
        headers = {
            'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        try:
            print(f"downloading page for {country}")
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            with open(cache_file, 'w', encoding='utf-8') as f:
                f.write(response.text)
            
            return response.text
            
        except requests.RequestException as e:
            print(f"error downloading page for {country}: {e}")
            return None
    
    def parse_number(self, text):
        if not text:
            return None
        cleaned = re.sub(r'[^\d]', '', text)
        try:
            return int(cleaned) if cleaned else None
        except ValueError:
            return None
    
    def extract_data(self, html, country):
        if not html:
            return {'country': country, 'capital': None, 'area': None, 'population': None}
        
        soup = BeautifulSoup(html, 'html.parser')
        data = {'country': country, 'capital': None, 'area': None, 'population': None}
        
        try:
            capital_th = soup.find('th', string=re.compile('capital', re.I))
            if capital_th:
                capital_td = capital_th.find_next('td')
                if capital_td:
                    capital_link = capital_td.find('a')
                    data['capital'] = capital_link.get_text(strip=True) if capital_link else capital_td.get_text(strip=True)
            
            area_th = soup.find('th', string=re.compile(r'Area\s*•\s*Total', re.I))
            if not area_th:
                area_th = soup.find('th', string=re.compile('total area', re.I))
            if not area_th:
                area_th = soup.find('th', string=re.compile('area', re.I))
            
            if area_th:
                area_td = area_th.find_next('td')
                if area_td:
                    area_text = area_td.get_text(strip=True)
                    km_match = re.search(r'(\d[\d,]*)\s*km²', area_text)
                    if km_match:
                        data['area'] = self.parse_number(km_match.group(1))
            
            population_th = soup.find('th', string=re.compile('population', re.I))
            if population_th:
                population_td = population_th.find_next('td')
                if population_td:
                    population_text = population_td.get_text(strip=True)
                    numbers = re.findall(r'\d[\d,]*', population_text)
                    if numbers:
                        data['population'] = self.parse_number(numbers[-1])
                        
        except Exception as e:
            print(f"error parsing data for {country}: {e}")
        
        return data
    
    def process_countries(self, input_file, output_file):
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                countries = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"input file {input_file} not found")
            return
        except Exception as e:
            print(f"error reading file {input_file}: {e}")
            return
        
        if not countries:
            print("country list file is empty")
            return
        
        results = []
        for i, country in enumerate(countries, 1):
            print(f"processing {country} ({i}/{len(countries)})...")
            
            html = self.fetch_page(country)
            data = self.extract_data(html, country)
            results.append(data)
            
            time.sleep(1)
        
        try:
            with open(output_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=['country', 'capital', 'area', 'population'])
                writer.writeheader()
                writer.writerows(results)
            
            print(f"data saved to {output_file}")
            print(f"processed countries: {len(results)} out of {len(countries)}")
            
            success_count = sum(1 for r in results if r['capital'] or r['area'] or r['population'])
            print(f"successfully retrieved data for {success_count} countries")
            
        except Exception as e:
            print(f"error saving to CSV: {e}")

def main():
    parser = argparse.ArgumentParser(description='collect country data from Wikipedia')
    parser.add_argument('-i', '--input', default='countries.txt', 
                       help='input file with country list (default: countries.txt)')
    parser.add_argument('-o', '--output', default='countries_data.csv',
                       help='output CSV file (default: countries_data.csv)')
    
    args = parser.parse_args()
    
    scraper = CountryDataScraper()
    scraper.process_countries(args.input, args.output)