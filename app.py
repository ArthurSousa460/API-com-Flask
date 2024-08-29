from flask import Flask, render_template, request
from database.clientes import clientes



app = Flask(__name__)


def get_id():
    id = 1
    id += 1
    return id


@app.get("/clients")
def hello_world():
    return render_template("index.html", CLIENTES=clientes)


@app.post("/clients")
def create_client():
    newClient = {
        "id": get_id(),
        "name": request.json["name"],
        "email": request.json["email"]

    }
    clientes.append(newClient)

    return newClient

@app.delete("/clients/<int:id>")
def delete_client(id):
    for i in range(len(clientes)):
        if int(clientes[i]["id"]) == int(id):
            clientes.pop(i)
    return {"message": "deletado com sucesso!"}




if __name__ =="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)