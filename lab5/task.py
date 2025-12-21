import requests
from bs4 import BeautifulSoup
import csv
import time
import sys
import os
import argparse
import re
from urllib.parse import quote

def setup_cache_directory():
    cache_path = 'wiki_cache'
    if not os.path.exists(cache_path):
        os.makedirs(cache_path)
    return cache_path

def retrieve_page(country_name):
    normalized_name = country_name.replace(' ', '_').replace('/', '_')
    cache_file_path = f"wiki_cache/{normalized_name}.html"
    
    if os.path.isfile(cache_file_path):
        with open(cache_file_path, 'r', encoding='utf-8') as file:
            return file.read()
    
    safe_name = quote(country_name.replace(' ', '_'))
    target_url = f"https://en.wikipedia.org/wiki/{safe_name}"
    
    request_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        page_response = requests.get(target_url, headers=request_headers)
        page_response.raise_for_status()
        
        page_content = page_response.text
        
        with open(cache_file_path, 'w', encoding='utf-8') as file:
            file.write(page_content)
        
        time.sleep(1.5)
        return page_content
        
    except Exception as error:
        print(f"Failed to retrieve page for {country_name}: {error}")
        return None

def sanitize_numeric_value(input_string):
    if not input_string:
        return ""
    digits_only = re.sub(r'[^\d]', '', str(input_string))
    return digits_only if digits_only else ""

def locate_demographic_info(info_table):
    for table_row in info_table.find_all('tr'):
        header_cell = table_row.find('th')
        if header_cell:
            header_content = header_cell.get_text().strip().lower()
            if 'population' in header_content:
                data_cell = table_row.find('td')
                if data_cell:
                    cell_text = data_cell.get_text()
                    numeric_patterns = re.findall(r'\d{1,3}(?:,\d{3})*', cell_text)
                    if numeric_patterns:
                        largest_value = max(numeric_patterns, key=lambda val: len(val.replace(',', '')))
                        clean_value = sanitize_numeric_value(largest_value)
                        return clean_value

    for table_row in info_table.find_all('tr'):
        header_cell = table_row.find('th')
        data_cell = table_row.find('td')
        if header_cell and data_cell:
            header_text = header_cell.get_text().strip().lower()
            cell_text = data_cell.get_text()
            if any(term in header_text for term in ['estimate', 'census']):
                if any(str(year) in cell_text for year in range(2020, 2025)):
                    numeric_patterns = re.findall(r'\d{1,3}(?:,\d{3})*', cell_text)
                    if numeric_patterns:
                        largest_value = max(numeric_patterns, key=lambda val: len(val.replace(',', '')))
                        clean_value = sanitize_numeric_value(largest_value)
                        return clean_value

    demographics_section = info_table.find('th', string=re.compile('.*Demographics.*', re.IGNORECASE))
    if demographics_section:
        following_rows = demographics_section.find_parent('tr').find_next_siblings('tr')
        for row in following_rows[:6]:
            data_cell = row.find('td')
            if data_cell:
                cell_text = data_cell.get_text()
                numeric_patterns = re.findall(r'\d{1,3}(?:,\d{3})*', cell_text)
                if numeric_patterns:
                    largest_value = max(numeric_patterns, key=lambda val: len(val.replace(',', '')))
                    clean_value = sanitize_numeric_value(largest_value)
                    return clean_value

    candidate_numbers = []
    for data_cell in info_table.find_all('td'):
        cell_text = data_cell.get_text()
        numeric_patterns = re.findall(r'\d{1,3}(?:,\d{3})*', cell_text)
        for pattern in numeric_patterns:
            cleaned_pattern = sanitize_numeric_value(pattern)
            if cleaned_pattern:
                candidate_numbers.append(cleaned_pattern)
    
    if candidate_numbers:
        return max(candidate_numbers, key=len)

    return ""

def extract_country_details(page_html, country_name):
    if not page_html:
        return None
    
    document_tree = BeautifulSoup(page_html, 'html.parser')
    info_panel = document_tree.find('table', {'class': re.compile('infobox.*')})
    
    if not info_panel:
        return {'country': country_name, 'capital': '', 'area': '', 'population': ''}
    
    result = {'country': country_name, 'capital': '', 'area': '', 'population': ''}
    
    try:
        for row in info_panel.find_all('tr'):
            header_element = row.find('th')
            if header_element:
                header_text = header_element.get_text().strip().lower()
                if 'capital' in header_text:
                    data_element = row.find('td')
                    if data_element:
                        capital_element = data_element.find('a')
                        if capital_element:
                            result['capital'] = capital_element.get_text().strip()
                            break

        for row in info_panel.find_all('tr'):
            header_element = row.find('th')
            if header_element:
                header_text = header_element.get_text().strip().lower()
                if 'area' in header_text or 'total' in header_text:
                    data_element = row.find('td')
                    if data_element:
                        area_text_content = data_element.get_text()
                        area_match_result = re.search(r'(\d[\d,.]*)\s*(?:km|sq)', area_text_content)
                        if area_match_result:
                            result['area'] = sanitize_numeric_value(area_match_result.group(1))
                            break

        result['population'] = locate_demographic_info(info_panel)

    except Exception as error_message:
        print(f"Error parsing details for '{country_name}': {error_message}")
        return None

    return result

def read_country_list(filename):
    possible_encodings = ['utf-8-sig', 'utf-8', 'latin-1', 'cp1252']
    
    for encoding_type in possible_encodings:
        try:
            with open(filename, 'r', encoding=encoding_type) as file:
                countries = [line.strip() for line in file if line.strip()]
            if countries:
                return countries
        except UnicodeDecodeError:
            continue
    
    print(f"Unable to read {filename} with supported encodings")
    return []

def process_country_data(input_filename, output_filename):
    setup_cache_directory()
    
    country_list = read_country_list(input_filename)
    if not country_list:
        return
    
    collected_results = []
    
    for index, country in enumerate(country_list, 1):
        print(f"Processing {index}/{len(country_list)}: {country}")
        
        page_content = retrieve_page(country)
        country_data = extract_country_details(page_content, country)
        
        if country_data:
            collected_results.append(country_data)
    
    with open(output_filename, 'w', newline='', encoding='utf-8') as file:
        field_names = ['country', 'capital', 'area', 'population']
        csv_writer = csv.DictWriter(file, fieldnames=field_names)
        csv_writer.writeheader()
        csv_writer.writerows(collected_results)
    
    print(f"Results saved to {output_filename}")

def main():
    argument_parser = argparse.ArgumentParser(description='Extract country information from Wikipedia')
    argument_parser.add_argument('-i', '--input', default='countries.txt', help='Input text file with country names')
    argument_parser.add_argument('-o', '--output', default='countries_data.csv', help='Output CSV file for results')
    
    parsed_args = argument_parser.parse_args()
    
    process_country_data(parsed_args.input, parsed_args.output)

if __name__ == "__main__":
    main()