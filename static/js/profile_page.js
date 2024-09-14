"use strict"

const navs = document.querySelectorAll(".nav h2")
const nav_forms = document.querySelectorAll(".nav_content > form")
const inputs = [...document.querySelectorAll(".input_container input")]
const buttons = [...document.querySelectorAll("button:not(.header_btn")]
const password_inputs = [...document.querySelectorAll("input[name=password]")]
const auth_msgs = [...document.querySelectorAll(".no_display")]

navs.forEach((nav, index) => {
    nav.addEventListener("click", () => {

        // Deselecionando todas as opções
        nav_forms.forEach((content) => {
            content.classList.remove("active")
        })  

        // Deselecionando todos os conteúdos
        navs.forEach((nav) => {
            nav.classList.remove("active")
        })

        // Limpando todos os inputs
        inputs.map((element) => {
            element.value = ""
        })

        // Selecionando a opção e o conteúdo escolhido
        navs[index].classList.add("active")
        nav_forms[index].classList.add("active")

    })
})

buttons.map((btn) => {
    btn.addEventListener("click", (event) => {

        // Previne o comportamento "submit" do botão
        event.preventDefault()

        // Procurando o campo em que o usuário colocou a senha
        let inputed_password = ""

        password_inputs.map((input) => {
            let input_value = input.value.toString().trim()
            if (input_value.length > 0) {
                inputed_password = input_value
            }
        })

        // Elaborando a entrada do fetch
        let entry = {
            "inputed_new_username": document.querySelector("input[name=new_username]").value,
            "inputed_new_password": document.querySelector("input[name=new_password]").value,
            "inputed_password": inputed_password,
            "pressed_btn": event.target.value
        }

        // Comunicando com o servidor através de uma requisição assíncrona
        fetch(window.location.href, {
            method: "POST",
            body: JSON.stringify(entry),
            headers: {"content-type": "application/json"}
        })

        .then((response) => {
            return response.json()
        })

        .then((converted_response) => {
            
            let status = converted_response["status"]

            switch (status) {
                case "invalid_password":
                    auth_msgs.map((msg) => {
                        msg.classList.remove("no_display")
                        msg.classList.remove("valid_msg")
                        msg.classList.add("invalid_msg")
                        msg.innerHTML = "Nova senha inválida!"
                    })
                    break;

                case "invalid_username":
                    auth_msgs.map((msg) => {
                        msg.classList.remove("no_display")
                        msg.classList.remove("valid_msg")
                        msg.classList.add("invalid_msg")
                        msg.innerHTML = "Usuário inválido!"
                    })
                    break;

                case "incorrect_password":
                    auth_msgs.map((msg) => {
                        msg.classList.remove("no_display")
                        msg.classList.remove("valid_msg")
                        msg.classList.add("invalid_msg")
                        msg.innerHTML = "Senha incorreta!"
                    })
                    break;
            
                case "credentials_changed":
                    auth_msgs.map((msg) => {
                        msg.classList.remove("no_display")
                        msg.classList.remove("invalid_msg")
                        msg.classList.add("valid_msg")
                        msg.innerHTML = "Credenciais alteradas com sucesso!"
                    })
                    break;
            }
        })
    })
})