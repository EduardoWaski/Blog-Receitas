"use strict"

const other_user_comment = [...document.querySelectorAll(".other_user_comment")]


other_user_comment.map((element) => {
    element.disabled = true
})
