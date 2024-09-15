"use strict"


// VARIÁVEIS
const add_recipe_btn = document.querySelector(".add_ingredient_btn")
const ingredients_container = document.querySelector(".ingredients_container")
const img_input = document.querySelector(".img_input")
const img_container = document.querySelector(".img_container")

let ingredients_counter = 1

// LISTENERS
add_recipe_btn.addEventListener("click", add_ingredient_input)
img_input.addEventListener("change", show_preview_img)

// FUNÇÕES
function add_ingredient_input(event) {

    ingredients_counter += 1

    // Criando o novo input
    let new_input = document.createElement("div")
    new_input.classList.add("input_container")

    new_input.innerHTML = `<input type="text" name="recipe_ingredient${ingredients_counter}">`

    ingredients_container.insertBefore(new_input, add_recipe_btn)
}

function show_preview_img (event) {
    
    // Removendo imagem colocada anteriormente
    remove_previous_img()

    // Recuperando a nova imagem inputada
    let inputed_img = event.target.files[0]

    if (inputed_img) {

        // Objeto que fará a leitura da imagem
        const reader = new FileReader();

        reader.onload = (event) => {

            let img_element = document.createElement("img")
            img_element.src = event.target.result
            img_container.append(img_element)
        }

        // Lendo a imagem
        reader.readAsDataURL(inputed_img)

    }

}

function remove_previous_img(event) {
    
    let previous_img = img_container.firstChild

    console.log("aqui")
    console.log(previous_img)

    if (previous_img) {
        img_container.removeChild(previous_img)
    }
}