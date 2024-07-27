# import requests
# from bs4 import BeautifulSoup

# # URL of the website to scrape
# url = "https://www.har.com/zipcode_77030/realestate/for_sale"

# # Add headers to the request
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
# }
# # Send a GET request to the website with headers
# response = requests.get(url, headers=headers)


# # Create a BeautifulSoup object to parse the HTML content
# soup = BeautifulSoup(response.content, "html.parser")


# # Find the elements containing the names, prices, and images
# property_elements = soup.find_all(
#     "div", class_="cardv2--landscape__content__body"
# )

# # print("Property ELements", property_elements)
# print(f"Number of property elements found: {len(property_elements)}")


# # Extract the names, prices, and images from the elements
# for element in property_elements:
#     name = element.find("div", class_="cardv2--landscape__content__body__details_address_left_add").text.strip()
#     price = element.find("div", class_="cardv2--landscape__content__body__details_price").text.strip()
#     image = "https://har.com" + element.find("a", class_="photolink")["href"]
#     property_url = "https://www.har.com" + element.find("a")["href"]
#     print("Name:", name)
#     print("Price:", price)
#     print("Property URL:", property_url)
#     print("Image:", image)
    

#     # Send a GET request to the property URL
#     property_response = requests.get(property_url, headers=headers)
#     property_soup = BeautifulSoup(property_response.content, "html.parser")

#     table_wrapper = property_soup.find("div", class_="table_wrapper")
#     table = table_wrapper.find("table", class_="table--medium")

#     # Find all rows in the table body
#     rows = table.find("tbody").find_all("tr")
#     market_value_2023 = None
#     # for row in rows:
#     #     print(row)



# import requests
# from bs4 import BeautifulSoup

# def scrape_properties(url, max_budget):
#     # Add headers to the request
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
#     }
    
#     # Send a GET request to the website with headers
#     response = requests.get(url, headers=headers)

#     # Create a BeautifulSoup object to parse the HTML content
#     soup = BeautifulSoup(response.content, "html.parser")

#     # Find the elements containing the names, prices, and images
#     property_elements = soup.find_all("div", class_="cardv2--landscape__content__body")

#     properties = []

#     # Extract the names, prices, and images from the elements
#     for element in property_elements:
#         name = element.find("div", class_="cardv2--landscape__content__body__details_address_left_add").text.strip()
#         price_text = element.find("div", class_="cardv2--landscape__content__body__details_price").text.strip()
#         price = int(price_text.replace("$", "").replace(",", ""))
#         image = "https://har.com" + element.find("a", class_="photolink")["href"]
#         property_url = "https://www.har.com" + element.find("a")["href"]

#         if price <= max_budget:
#             properties.append({
#                 "name": name,
#                 "price": price,
#                 "image": image,
#                 "url": property_url
#             })

#     # Sort properties by price (ascending order)
#     properties.sort(key=lambda x: x["price"])

#     # Return top 5 properties
#     return properties[:5]

# def main():
#     zipcode = input("Enter the ZIP code: ")
#     max_budget = int(input("Enter your maximum budget: $"))
#     url = f"https://www.har.com/zipcode_{zipcode}/realestate/for_sale"
    
   

#     top_properties = scrape_properties(url, max_budget)

#     print(f"\nTop 5 properties within your budget of ${max_budget}:")
#     for i, prop in enumerate(top_properties, 1):
#         print(f"\n{i}. {prop['name']}")
#         print(f"   Price: ${prop['price']:,}")
#         print(f"   URL: {prop['url']}")
#         print(f"   Image: {prop['image']}")

# if __name__ == "__main__":
#     main()



from flask import Flask, request, jsonify, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_properties(url, max_budget):
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
            name = element.find("div", class_="cardv2--landscape__content__body__details_address_left_add").text.strip()
            price_text = element.find("div", class_="cardv2--landscape__content__body__details_price").text.strip()
            price = int(price_text.replace("$", "").replace(",", ""))
            image = "https://har.com" + element.find("a", class_="photolink")["href"]
            property_url = "https://www.har.com" + element.find("a")["href"]

            if price <= max_budget:
                properties.append({
                    "name": name,
                    "price": price,
                    "image": image,
                    "url": property_url
                })
        except Exception as e:
            app.logger.error(f"Error parsing property element: {e}")

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
        url = f"https://www.har.com/zipcode_{zipcode}/realestate/for_sale"
        top_properties = scrape_properties(url, max_budget)
        return jsonify(top_properties)
    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)