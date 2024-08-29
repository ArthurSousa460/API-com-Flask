from flask import Flask, render_template, request
from database.clientes import clientes



app = Flask(__name__)



@app.get("/clients")
def hello_world():
    return render_template("index.html", CLIENTES=clientes)


@app.post("/clients")
def create_client():
    newClient = {
        "id": len(clientes) + 1,
        "name": request.json["name"],
        "email": request.json["email"]

    }
    clientes.append(newClient)

    return newClient

@app.delete("/clients/<int:id>")
def delete_client(id):
    clientes.pop(id - 1)
    return "ok"




if __name__ =="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)