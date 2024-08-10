from flask import Flask, request, jsonify, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


def scrape_properties(url, max_budget, min_size=None, max_size=None):
  headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
  }
  response = requests.get(url, headers=headers)
  
  if response.status_code != 200:
      app.logger.error(f"Failed to fetch data from {url}, status code: {response.status_code}")
      return []

  soup = BeautifulSoup(response.content, "html.parser")
  property_elements = soup.find_all("div", class_="cardv2--landscape__content__body")
  
  if not property_elements:
      app.logger.warning(f"No property elements found for URL: {url}")
      return []

  properties = []

  for element in property_elements:
      try:
          name_element = element.find("div", class_="cardv2--landscape__content__body__details_address_left_add")
          price_element = element.find("div", class_="cardv2--landscape__content__body__details_price")
          image_element = element.find("a", class_="photolink")
          url_element = element.find("a")
          
          # Finding size
          size = None
          feature_elements = element.find_all("div", class_="cardv2--landscape__content__body__details_features_item")
          for feature in feature_elements:
              if "Sqft." in feature.text:
                  size_element = feature.find("span")
                  if size_element:
                      size = int(size_element.text.strip().replace(",", ""))
                      break

          if not (name_element and price_element and image_element and url_element):
              app.logger.warning(f"Missing one or more required elements for property: {element}")
              continue

          name = name_element.text.strip()
          price_text = price_element.text.strip()
          price = int(price_text.replace("$", "").replace(",", ""))
          image = "https://har.com" + image_element["href"]
          property_url = "https://www.har.com" + url_element["href"]

          properties.append({
              "name": name,
              "price": price,
              "size": size,
              "image": image,
              "url": property_url
          })
      except Exception as e:
          app.logger.error(f"Error parsing property element: {e}")

  
  app.logger.info(f"Filtering properties with min_size: {min_size} and max_size: {max_size}")

  # Filtering properties by max budget by user
  properties = [prop for prop in properties if prop['price'] <= max_budget]

  # Finally, Filtering properties by size
  if min_size is not None or max_size is not None:
      properties = [prop for prop in properties if (min_size is None or (prop['size'] is not None and prop['size'] >= min_size)) and (max_size is None or (prop['size'] is not None and prop['size'] <= max_size))]

  # Sorting properties by price
  properties.sort(key=lambda x: x["price"])

  return properties[:5]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
  try:
      data = request.json
      zipcode = data.get('zipcode')
      max_budget = int(data.get('max_budget')) 

      min_size = data.get('min_size')
      max_size = data.get('max_size')
    
      
      min_size = int(min_size) if min_size and min_size != '' else None
      max_size = int(max_size) if max_size and max_size != '' else None

      url = f"https://www.har.com/zipcode_{zipcode}/realestate/for_sale"
      
      top_properties = scrape_properties(url, max_budget, min_size, max_size)
      return jsonify(top_properties)
  except Exception as e:
      app.logger.error(f"Error occurred: {e}")
      return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)