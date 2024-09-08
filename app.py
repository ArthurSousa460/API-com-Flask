from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from database.clientes import clientes
import os


basedir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(basedir, 'database', 'dataBase.sqlite3')


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{database_path}"

db = SQLAlchemy()
db.init_app(app)


class Client(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)


with app.app_context():
    db.create_all()


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