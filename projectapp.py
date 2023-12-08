from flask import Flask, render_template, request
from webscraping import parse_html, download_page
from sendingemail import sending_email
import traceback

app = Flask(__name__)

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
            userinput_email = request.form.get("userinput_email")

            product_html = download_page(product_url)
            original_price, discounted_price, percent_off = parse_html(product_html)

            if original_price > discounted_price:
                sending_email(userinput_email, percent_off)
            return render_template("result.html", original_price=original_price, discounted_price=discounted_price, percent_off=percent_off)
        
        except Exception as e:
            print(f"Error: {e}")
            traceback.print_exc()  # Print the full traceback for debugging
            return render_template("error.html")
        
@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html") 

if __name__ == "__main__":
    app.run(debug=True)