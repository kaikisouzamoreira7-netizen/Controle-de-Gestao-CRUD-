const formCadastro = document.getElementById("formCadastro");
const listaRegistros = document.getElementById("listaRegistros");
const botaoCadastro = formCadastro.querySelector("button");

let registroEditando = null;


formCadastro.addEventListener("submit", async function (event) {
    event.preventDefault();

    const nome = document.getElementById("nome").value.trim();
    const setor = document.getElementById("setor").value.trim();
    const cargo = document.getElementById("cargo").value.trim();
    const email = document.getElementById("email").value.trim();

    if (nome === "" || setor === "" || cargo === "" || email === "") {
        alert("Preencha todos os campos.");
        return;
    }

    const dados = {
        nome: nome,
        setor: setor,
        cargo: cargo,
        email: email
    };

    try {
        let resposta;

        if (registroEditando !== null) {
            resposta = await fetch(`/editar/${registroEditando}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(dados)
            });
        } else {
            resposta = await fetch("/cadastrar", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(dados)
            });
        }

        const resultado = await resposta.json();

        if (!resposta.ok) {
            throw new Error(
                resultado.mensagem || "Erro na operação."
            );
        }

        alert(resultado.mensagem);

        formCadastro.reset();
        registroEditando = null;
        botaoCadastro.textContent = "Cadastrar";

        carregarRegistros();

    } catch (erro) {
        console.error(erro);
        alert("Erro ao salvar o registro.");
    }
});


async function carregarRegistros() {
    try {
        const resposta = await fetch("/registros");

        if (!resposta.ok) {
            throw new Error("Erro ao buscar registros.");
        }

        const registros = await resposta.json();

        listaRegistros.innerHTML = "";

        if (registros.length === 0) {
            listaRegistros.innerHTML = "<p>Nenhum registro cadastrado.</p>";
            return;
        }

        registros.forEach(function (registro) {
            const elemento = document.createElement("div");

            elemento.innerHTML = `
                <p><strong>Nome:</strong> ${registro.nome}</p>
                <p><strong>Setor:</strong> ${registro.setor}</p>
                <p><strong>Cargo:</strong> ${registro.cargo}</p>
                <p><strong>E-mail:</strong> ${registro.email}</p>

                <button class="btnEditar">Editar</button>
                <button class="btnExcluir">Excluir</button>

                <hr>
            `;

            const botaoEditar = elemento.querySelector(".btnEditar");
            const botaoExcluir = elemento.querySelector(".btnExcluir");


            botaoEditar.addEventListener("click", function () {
                document.getElementById("nome").value = registro.nome;
                document.getElementById("setor").value = registro.setor;
                document.getElementById("cargo").value = registro.cargo;
                document.getElementById("email").value = registro.email;

                registroEditando = registro.id;

                botaoCadastro.textContent = "Salvar alteração";

                window.scrollTo({
                    top: 0,
                    behavior: "smooth"
                });
            });


            botaoExcluir.addEventListener("click", async function () {
                const confirmar = confirm(
                    `Deseja excluir o registro de ${registro.nome}?`
                );

                if (!confirmar) {
                    return;
                }

                try {
                    const resposta = await fetch(
                        `/excluir/${registro.id}`,
                        {
                            method: "DELETE"
                        }
                    );

                    const resultado = await resposta.json();

                    if (!resposta.ok) {
                        throw new Error(
                            resultado.mensagem || "Erro ao excluir."
                        );
                    }

                    alert(resultado.mensagem);

                    carregarRegistros();

                } catch (erro) {
                    console.error(erro);
                    alert("Erro ao excluir o registro.");
                }
            });


            listaRegistros.appendChild(elemento);
        });

    } catch (erro) {
        console.error(erro);
        listaRegistros.innerHTML =
            "<p>Erro ao carregar os registros.</p>";
    }
}


carregarRegistros();