from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

SERVICES = [
    {
        "id": "initial-assessment",
        "title": "Initial Assessment",
        "description": (
            "A 60-minute one-on-one session to evaluate your dog's behavior, "
            "history, and your goals. Includes a written summary and starter plan."
        ),
        "price": "$75",
    },
    {
        "id": "behavior-modification",
        "title": "Behavior Modification Program",
        "description": (
            "Six structured sessions addressing reactivity, anxiety, aggression, "
            "or other complex behaviors. Weekly check-ins included."
        ),
        "price": "$450",
    },
    {
        "id": "group-classes",
        "title": "Group Classes",
        "description": (
            "Small-group obedience and socialization classes (max 6 dogs). "
            "Great for puppies and dogs who need confidence building."
        ),
        "price": "$30 / class",
    },
]

SERVICE_NAMES = [s["title"] for s in SERVICES]


@app.route("/")
def home():
    return render_template("index.html", active="home")


@app.route("/services")
def services():
    return render_template("services.html", active="services", services=SERVICES)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return redirect(url_for("success"))
    return render_template("contact.html", active="contact", service_names=SERVICE_NAMES)


@app.route("/contact/success")
def success():
    return render_template("success.html", active="contact")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
