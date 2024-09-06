"use strict"

const navs = document.querySelectorAll(".nav h2")
const nav_forms = document.querySelectorAll(".nav_content > form")
const inputs = [...document.querySelectorAll(".input_container input")]
const buttons = [...document.querySelectorAll("button")]
const password_inputs = [...document.querySelectorAll("input[name=password]")]

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
        fetch(window.location, {
            method: "POST",
            cache: 'no-cache',
            credentials: "omit",
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
                    alert("Senha inválida")
                    break;
            
                case "user_deleted":
                    alert("Usuário deletado")
                    break;
            
                case "username_changed":
                    alert("Usuário mudou")
                    break;
            
                case "invalid_password":
                    alert("Senha mudou")
                    break

                default:
                    alert("Status default")
            }
        })
    })
})