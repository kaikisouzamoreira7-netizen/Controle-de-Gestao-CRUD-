import sqlite3
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

NOME_BANCO = "banco.db"


def conectar_banco():
    conexao = sqlite3.connect(NOME_BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_banco():
    conexao = conectar_banco()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            setor TEXT NOT NULL,
            cargo TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    try:
        dados = request.get_json()

        nome = dados.get("nome", "").strip()
        setor = dados.get("setor", "").strip()
        cargo = dados.get("cargo", "").strip()
        email = dados.get("email", "").strip()

        if not nome or not setor or not cargo or not email:
            return jsonify({
                "mensagem": "Preencha todos os campos."
            }), 400

        conexao = conectar_banco()

        conexao.execute("""
            INSERT INTO registros (nome, setor, cargo, email)
            VALUES (?, ?, ?, ?)
        """, (nome, setor, cargo, email))

        conexao.commit()
        conexao.close()

        return jsonify({
            "mensagem": "Registro cadastrado com sucesso!"
        })

    except Exception as erro:
        print("Erro ao cadastrar:", erro)

        return jsonify({
            "mensagem": "Erro ao cadastrar o registro."
        }), 500


@app.route("/registros", methods=["GET"])
def listar_registros():
    try:
        conexao = conectar_banco()

        registros = conexao.execute("""
            SELECT id, nome, setor, cargo, email
            FROM registros
            ORDER BY id DESC
        """).fetchall()

        conexao.close()

        return jsonify([
            dict(registro)
            for registro in registros
        ])

    except Exception as erro:
        print("Erro ao listar:", erro)

        return jsonify({
            "mensagem": "Erro ao carregar os registros."
        }), 500


@app.route("/editar/<int:id>", methods=["PUT"])
def editar_registro(id):
    try:
        dados = request.get_json()

        nome = dados.get("nome", "").strip()
        setor = dados.get("setor", "").strip()
        cargo = dados.get("cargo", "").strip()
        email = dados.get("email", "").strip()

        if not nome or not setor or not cargo or not email:
            return jsonify({
                "mensagem": "Preencha todos os campos."
            }), 400

        conexao = conectar_banco()

        registro = conexao.execute("""
            SELECT id
            FROM registros
            WHERE id = ?
        """, (id,)).fetchone()

        if registro is None:
            conexao.close()

            return jsonify({
                "mensagem": "Registro não encontrado."
            }), 404

        conexao.execute("""
            UPDATE registros
            SET nome = ?,
                setor = ?,
                cargo = ?,
                email = ?
            WHERE id = ?
        """, (nome, setor, cargo, email, id))

        conexao.commit()
        conexao.close()

        return jsonify({
            "mensagem": "Registro atualizado com sucesso!"
        })

    except Exception as erro:
        print("Erro ao editar:", erro)

        return jsonify({
            "mensagem": "Erro ao atualizar o registro."
        }), 500


@app.route("/excluir/<int:id>", methods=["DELETE"])
def excluir_registro(id):
    try:
        conexao = conectar_banco()

        registro = conexao.execute("""
            SELECT id
            FROM registros
            WHERE id = ?
        """, (id,)).fetchone()

        if registro is None:
            conexao.close()

            return jsonify({
                "mensagem": "Registro não encontrado."
            }), 404

        conexao.execute("""
            DELETE FROM registros
            WHERE id = ?
        """, (id,))

        conexao.commit()
        conexao.close()

        return jsonify({
            "mensagem": "Registro excluído com sucesso!"
        })

    except Exception as erro:
        print("Erro ao excluir:", erro)

        return jsonify({
            "mensagem": "Erro ao excluir o registro."
        }), 500


if __name__ == "__main__":
    criar_banco()

    app.run(debug=True)