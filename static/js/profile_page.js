
const navs = document.querySelectorAll(".nav h2")
const navsContent = document.querySelectorAll(".nav_content > div")
const inputs = [...document.querySelectorAll(".input_container input")]

navs.forEach((nav, index) => {
    nav.addEventListener("click", () => {

        // Deselecionando todas as opções
        navsContent.forEach((content) => {
            content.classList.remove("active")
        })  

        // Deselecionando todos os conteúdos
        navs.forEach((nav) => {
            nav.classList.remove("active")
        })

        inputs.map((element) => {
            element.value = ""
        })

        // Selecionando a opção e o conteúdo escolhido
        navs[index].classList.add("active")
        navsContent[index].classList.add("active")

    })
})
