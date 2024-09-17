"use strict"

const recipes = [...document.querySelectorAll(".recipe")]

recipes.map((element) => {
    element.addEventListener("click", (event) => {

        let recipe_container = ''
        if (event.target.classList.contains("recipe")) {
            recipe_container = event.target
        } else {
            recipe_container = event.target.closest(".recipe")
        }

        let recipe_id = recipe_container.id

        window.location.assign(`${window.location.origin}/receita/${recipe_id}`)

    })
})