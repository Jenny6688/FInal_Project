from flask import Flask, render_template, request
from webscraping import parse_html, download_page
from sendingemail import sending_email
import traceback
import schedule
import time
import threading



app = Flask(__name__)

# Store product URLs and associated email addresses


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/info", methods=["GET", "POST"])
def info():
    if request.method == "GET":
        return render_template("form.html")
    elif request.method == "POST":
        try:
            product_url = request.form.get("product_url")
            user_input_email = request.form.get("user_input_email")

            monitored_products[product_url] = user_input_email
            print(monitored_products)

            page = download_page(product_url)
            original_price, discounted_price, percent_off = parse_html(page)
            # print(original_price, discounted_price, percent_off)


            return render_template("result.html", original_price=original_price, discounted_price=discounted_price)

        except Exception as e:
            print(f"Error: {e}")
            traceback.print_exc()  # Print the full traceback for debugging
            return render_template("error.html")


@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html")


monitored_products = {}


def monitor_prices():
    """
    Check price for all the products in monitored_products
    to get pricing info, including (original_price, discounted_price, percent_off)

    Send email if original_price > discounted_price

    """
    print('Starting scheduled task ...')
    print(monitored_products)
    for product_url, user_email in monitored_products.items():
        try:
            product_html = download_page(product_url)
            original_price, discounted_price, percent_off = parse_html(product_html)

            if original_price > discounted_price:
                print(f'Sending email to {user_email}...')
                sending_email(user_email, percent_off, discounted_price, original_price)
        except Exception as e:
            print(f"Error monitoring {product_url}: {e}")
            traceback.print_exc()

def schedule_task():
    '''
    Schedule the monitor_prices function to run every 30 seconds.
    '''
    schedule.every(30).seconds.do(monitor_prices)
    
    while True:
        # print('Running schedule')
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    """
    Utilize thread to enable the flask app and the schedule task run at the same time.
    """
    thread = threading.Thread(target=schedule_task)  
    thread.start()

    # Start the Flask app
    app.run(debug=True, threaded=True)
  

    
