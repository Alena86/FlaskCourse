from flask import Flask, render_template

app = Flask(__name__)

class GalileanMoons: 
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

@app.route("/")
def render_jinja_intro(): 
    return render_template(
        "jinja_intro.html",
        name = "Alena Volarevic", 
        template_name = "jinja2")

@app.route("/first")
def render_hello_world(): 
    return render_template("first_page.html")

@app.route("/second")
def render_hello_world_fancy(): 
    return render_template("second_page.html")

@app.route("/expressions")
def render_expression_intro(): 
    # Interpolation 
    color = "brown"
    animal_one = "dog"
    animal_two = "cat"

    # Addition and substraction
    orange_amount = 10
    apple_amount = 20
    donate_amount = 15

    # string concatenation
    first_name = "Captain"
    last_name = "Marvel"

    kwargs = {
        "color": color, 
        "animal_one": animal_one, 
        "animal_two": animal_two, 
        "orange_amount": orange_amount,
        "apple_amount": apple_amount,
        "donate_amount": donate_amount,
        "first_name": first_name,
        "last_name": last_name
    }

    return render_template("expressions.html", **kwargs)


@app.route("/data_structure")
def render_data_structure(): 
    movies = [
        "Titanic", 
        "Gone with the wind", 
        "Avatar"
    ]

    car = {
        "brand" : "Mazda", 
        "model": "CX-5", 
        "year": 2019
        }

    moons = GalileanMoons("Io", "Europa", "Ganymede", "Callisto")

    kwargs = {
        "movies": movies,
        "car": car, 
        "moon": moons
    }

    return render_template("data_structures.html", **kwargs)

@app.route("/conditional_basics")
def render_conditional_basics(): 
    company = "Apple"
    return render_template("conditionals_basics.html", company=company)

@app.route("/forLoop")
def render_loop(): 
    planets=[
        "Mercury",
        "Venus", 
        "Earth", 
        "Pluton",
        "Neptune",
        "Saturn", 
        "Jupiter",
        "Mars"
    ]

    return render_template("for_loop.html", planets = planets)


@app.route("/forLoop/conditionals")
def render_for_loop_conditional(): 
    user_os = {
        "Bob Smith" : "Windows", 
        "Anne Pun" : "MacOs", 
        "Adam Lee" : "Linux", 
        "Jose Salcatierra" : "Windows"
    }

    return render_template("loops_and_conditionals.html", user_os=user_os)