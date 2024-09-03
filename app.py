from bottle import get, run, template, static_file

####################################
@get("/") # decorator
def index():
    return template("index")

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
    return "items"



####################################
run(host="0.0.0.0", port=80, debug=True, reloader=True, interval=0.3)


