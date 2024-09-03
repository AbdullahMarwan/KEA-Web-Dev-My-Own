from bottle import get, run, post, put, delete, template, static_file, response
import json

####################################
@get("/") # decorator
def index():
    return template("index")

####################################
@get("/about-us")
def _():
    return template("about_us")

####################################
@get("/app.css")
def _():
    return static_file("app.css", ".")

####################################
@get("/app.js")
def _():
    return static_file("app.js", ".")

# API
####################################
"""
CREATE READ UPDATE DELETE (Known as CRUD)

HTTP METHOD GET (To read data)
/items

HTTP METHOD POST (To create data)
/items

HTTP METHOD PUT (To update data)
/items/<id>

HTTP METHOD DELETE (To delete data)
/items/<id>

"""

####################################
@get("/items")
def _():
    # List is an array
    item = {"id" : 1, "name" : "a"}

    # Convert list to string
    # Type casting or cast
    # dumps stands for dump string
    response.content_type = "application/json"
    return json.dumps([item])

####################################
@get("/items/<id>")
def _(id):
    # Dictionary
    item = {
        "id" : 1,
        "name" : "a"
    }
    return item

####################################
@post("/items")
def _():
    return "item created"

####################################
# f string
@put("/items/<id>")
def _(id):
    return f"item {id} updated"

####################################
@delete("/items/<id>")
def _(id):
    return f"item {id} deleted"


####################################
run(host="0.0.0.0", port=80, debug=True, reloader=True, interval=0.3)


