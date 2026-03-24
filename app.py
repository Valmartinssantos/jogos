from flask import Flask, jsonify, request, g
import sqlite3

DATABASE = "jogos.db"

app = Flask(__name__)


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def row_to_dict(row):
    return {
        "id": row["id"],
        "titulo": row["titulo"],
        "genero": row["genero"],
        "plataforma": row["plataforma"],
        "ano_lancamento": row["ano_lancamento"],
        "quantidade": row["quantidade"],
    }


@app.route("/")
def home():
    return jsonify({
        "mensagem": "API de inventário de jogos funcionando",
        "rotas": {
            "listar_todos": "GET /jogos",
            "buscar_por_id": "GET /jogos/<id>",
            "inserir": "POST /jogos",
            "atualizar": "PUT /jogos/<id>",
            "remover": "DELETE /jogos/<id>"
        }
    }), 200


@app.get("/jogos")
def listar_jogos():
    db = get_db()
    rows = db.execute("""
        SELECT id, titulo, genero, plataforma, ano_lancamento, quantidade
        FROM jogos
        ORDER BY id
    """).fetchall()

    return jsonify([row_to_dict(row) for row in rows]), 200


@app.get("/jogos/<int:jogo_id>")
def buscar_jogo(jogo_id):
    db = get_db()
    row = db.execute("""
        SELECT id, titulo, genero, plataforma, ano_lancamento, quantidade
        FROM jogos
        WHERE id = ?
    """, (jogo_id,)).fetchone()

    if row is None:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    return jsonify(row_to_dict(row)), 200


@app.post("/jogos")
def inserir_jogo():
    dados = request.get_json(silent=True)

    if not dados:
        return jsonify({"erro": "JSON inválido ou ausente"}), 400

    campos_obrigatorios = ["titulo", "genero", "plataforma", "ano_lancamento", "quantidade"]
    faltando = [campo for campo in campos_obrigatorios if campo not in dados]

    if faltando:
        return jsonify({
            "erro": f"Campos obrigatórios ausentes: {', '.join(faltando)}"
        }), 400

    db = get_db()
    cursor = db.execute("""
        INSERT INTO jogos (titulo, genero, plataforma, ano_lancamento, quantidade)
        VALUES (?, ?, ?, ?, ?)
    """, (
        dados["titulo"],
        dados["genero"],
        dados["plataforma"],
        dados["ano_lancamento"],
        dados["quantidade"]
    ))
    db.commit()

    novo_id = cursor.lastrowid
    row = db.execute("""
        SELECT id, titulo, genero, plataforma, ano_lancamento, quantidade
        FROM jogos
        WHERE id = ?
    """, (novo_id,)).fetchone()

    return jsonify(row_to_dict(row)), 201


@app.put("/jogos/<int:jogo_id>")
def atualizar_jogo(jogo_id):
    dados = request.get_json(silent=True)

    if not dados:
        return jsonify({"erro": "JSON inválido ou ausente"}), 400

    campos_obrigatorios = ["titulo", "genero", "plataforma", "ano_lancamento", "quantidade"]
    faltando = [campo for campo in campos_obrigatorios if campo not in dados]

    if faltando:
        return jsonify({
            "erro": f"Campos obrigatórios ausentes: {', '.join(faltando)}"
        }), 400

    db = get_db()
    existente = db.execute("SELECT id FROM jogos WHERE id = ?", (jogo_id,)).fetchone()

    if existente is None:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    db.execute("""
        UPDATE jogos
        SET titulo = ?, genero = ?, plataforma = ?, ano_lancamento = ?, quantidade = ?
        WHERE id = ?
    """, (
        dados["titulo"],
        dados["genero"],
        dados["plataforma"],
        dados["ano_lancamento"],
        dados["quantidade"],
        jogo_id
    ))
    db.commit()

    return "", 204


@app.delete("/jogos/<int:jogo_id>")
def remover_jogo(jogo_id):
    db = get_db()
    existente = db.execute("SELECT id FROM jogos WHERE id = ?", (jogo_id,)).fetchone()

    if existente is None:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    db.execute("DELETE FROM jogos WHERE id = ?", (jogo_id,))
    db.commit()

    return "", 204


if __name__ == "__main__":
    app.run(debug=True)