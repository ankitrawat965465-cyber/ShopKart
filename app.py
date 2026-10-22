from flask import Flask, render_template, abort, request, jsonify
from datetime import datetime
import uuid
import requests
import os

app = Flask(__name__)

OLLAMA_HOST = os.getenv(
    "OLLAMA_HOST",
    "http://127.0.0.1:11434"
).rstrip("/")

# ShopKart product catalogue
products = [
    {
        "id": 1,
        "name": "Wireless Headphones",
        "price": 1499,
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=500&q=80"
    },
    {
        "id": 2,
        "name": "Smart Watch",
        "price": 2499,
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=500&q=80"
    },
    {
        "id": 3,
        "name": "Running Shoes",
        "price": 1999,
        "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=500&q=80"
    },
    {
        "id": 4,
        "name": "Laptop Backpack",
        "price": 999,
        "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&w=500&q=80"
    },
]

# Orders are currently stored in memory
orders = []


@app.route("/")
def home():
    return render_template("index.html", products=products)


@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = next(
        (p for p in products if p["id"] == product_id),
        None
    )

    if product is None:
        abort(404)

    return render_template("product.html", product=product)


@app.route("/order/<int:product_id>", methods=["GET", "POST"])
def place_order(product_id):
    product = next(
        (p for p in products if p["id"] == product_id),
        None
    )

    if product is None:
        abort(404)

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        address = request.form.get("address", "").strip()
        phone = request.form.get("phone", "").strip()

        if not name or not address or not phone:
            return render_template(
                "order.html",
                product=product,
                error="Please fill in all fields."
            ), 400

        order = {
            "order_id": str(uuid.uuid4())[:8].upper(),
            "name": name,
            "address": address,
            "phone": phone,
            "product": product,
            "date": datetime.now().strftime("%d-%m-%Y %H:%M")
        }

        orders.append(order)

        return render_template(
            "confirmation.html",
            order=order
        )

    return render_template(
        "order.html",
        product=product,
        error=None
    )


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "").strip()

    if not message:
        return jsonify({
            "reply": "Please type a message."
        }), 400

    # Send ShopKart catalogue details to the AI assistant
    product_info = "\n".join(
        f'{p["name"]}: Rs. {p["price"]}'
        for p in products
    )

    try:
        response = requests.post(
            f"{OLLAMA_HOST}/api/chat",
            json={
                "model": "llama3.2:1b",
                "stream": False,
                "keep_alive": "10m",
                "options": {"num_predict": 80, "num_ctx": 2048},
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "You are ShopKart's shopping assistant. "
                            "Help customers choose products. "
                            "Use this product catalogue:\n"
                            + product_info
                            + "\nRecommend only listed products. "
                            "Reply in simple language. "
                            "Do not claim that an order or payment "
                            "has been completed."
                        )
                    },
                    {
                        "role": "user",
                        "content": message
                    }
                ]
            },
            timeout=300
        )

        response.raise_for_status()
        answer = response.json()["message"]["content"]

        return jsonify({
            "reply": answer
        })

    except requests.RequestException:
        app.logger.exception("Ollama request failed")

        return jsonify({
            "reply": (
                "ShopKart AI abhi available nahi hai. "
                "Please check that Ollama is running and "
                "the llama3.2:1b model is installed."
            )
        }), 503


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )