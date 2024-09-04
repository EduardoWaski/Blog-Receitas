
const navs = document.querySelectorAll(".nav h2")
const nav_forms = document.querySelectorAll(".nav_content > form")
const inputs = [...document.querySelectorAll(".input_container input")]

console.log(nav_forms)

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
