"strict"

const recipe_boxes = [...document.querySelectorAll(".recipe_box")]


// Função para redirecionar o usuário para a página da receita clicada
recipe_boxes.map((element) => {
    element.addEventListener("click", (event) => {

        // Recuperando o article que o usuário clicou

        let pressed_recipe_box = ''
        if (event.target.parentNode.classList.contains('recipe_box')) {
            pressed_recipe_box = event.target.parentNode
        } else {
            pressed_recipe_box = event.target
        }

        // Recuperando o id da receita
        let recipe_id = pressed_recipe_box.id

        // Fazendo o redirecionamento para a página da receita
        window.location.assign(`${window.location.href}receita/${recipe_id}`)
    })
})