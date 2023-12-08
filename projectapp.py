# from flask import Flask, render_template, request
# from webscraping import parse_html, download_page
# from sendingemail import sending_email
# import traceback

# app = Flask(__name__)


# @app.route("/", methods=["GET", "POST"])
# def index():
#     return render_template("index.html")


# @app.route("/info", methods=["GET", "POST"])
# def info():
#     if request.method == "GET":
#         return render_template("form.html")
#     elif request.method == "POST":
#         try:
#             product_url = request.form.get("product_url")
#             userinput_email = request.form.get("userinput_email")

#             product_html = download_page(product_url)
#             original_price, discounted_price, percent_off = parse_html(product_html)

#             if original_price > discounted_price:
#                 sending_email(
#                     userinput_email, percent_off, original_price, discounted_price
#                 )
#             return render_template(
#                 "result.html",
#                 original_price=original_price,
#                 discounted_price=discounted_price,
#                 percent_off=percent_off,
#             )

#         except Exception as e:
#             print(f"Error: {e}")
#             traceback.print_exc()  # Print the full traceback for debugging
#             return render_template("error.html")


# @app.route("/about", methods=["GET", "POST"])
# def about():
#     return render_template("about.html")


# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask, render_template, request
from webscraping import parse_html, download_page
from sendingemail import sending_email
import traceback
import schedule
import time

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
            return render_template("result.html", product_url=product_url)

        except Exception as e:
            print(f"Error: {e}")
            traceback.print_exc()  # Print the full traceback for debugging
            return render_template("error.html")


@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html")


monitored_products = {}


def monitor_prices():
    for product_url, user_email in monitored_products.items():
        try:
            product_html = download_page(product_url)
            original_price, discounted_price, percent_off = parse_html(product_html)

            if original_price > discounted_price:
                sending_email(user_email, percent_off)
        except Exception as e:
            print(f"Error monitoring {product_url}: {e}")
            traceback.print_exc()


if __name__ == "__main__":
    # Schedule the monitor_prices function to run every hour
    schedule.every().hour.do(monitor_prices)

    # Start the Flask app
    app.run(debug=True)

    while True:
        schedule.run_pending()
        time.sleep(1)

