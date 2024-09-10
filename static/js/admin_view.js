"use strict"

const edit_radio_buttons = [...document.querySelectorAll(".edit_radios_container input")]
const is_admin_radio_buttons = [...document.querySelectorAll("input[name=is_admin_radio]")]
const text_inputs = [...document.querySelectorAll("input[type=text]")]
const ok_btn = document.querySelector(".ok_btn")

// Desabilitando todos os inputs e o botão de submit
text_inputs.map(input => input.disabled = true)
is_admin_radio_buttons.map(btn => btn.disabled = true)
ok_btn.disabled = true

// Adicionando um listener
edit_radio_buttons.map((btn) => {
    btn.addEventListener("click", validate_radio_value)
})


// FUNÇÕES

function validate_radio_value (event) {

    let pressed_radio = event.target
    let option = pressed_radio.value == 'true' ? true : false

    if (option) {
        text_inputs.map(input => input.disabled = false)
        is_admin_radio_buttons.map(btn => btn.disabled = false)
        ok_btn.disabled = false
    } else {
        text_inputs.map(input => input.disabled = true)
        is_admin_radio_buttons.map(btn => btn.disabled = true)
        ok_btn.disabled = true
    }
}