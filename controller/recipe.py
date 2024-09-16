from flask import Blueprint, render_template, request, send_file, flash, session, redirect, url_for
from models.db_config import *
from models.models import *
from controller.auxiliar import *
from io import BytesIO
from bson import ObjectId

recipe = Blueprint('recipe', __name__)


# ---------------------------- ROTA DA RECEITA --------------------------------------------
@recipe.route('/receita/', defaults={'recipe_id': None})  # Define o valor padrão para 'id_receita'
@recipe.route("/receita/<recipe_id>", methods = ["GET"])
def recipe_get(recipe_id):

    # Verificando se há algum usuário logado
    if not "username" in session:
        return redirect(url_for("auth.login_signup"))
    
    # Caso não tenha sido informado um id da receita, o sistema pegará a receita anterior
    if not recipe_id:
        recipe = recipes_collection.find_one({"_id": ObjectId(session["current_recipe_id"])})
        return render_template("recipe.html", recipe=recipe)
    
    # Caso o id exista, vamos atualizá-lo na session
    session["current_recipe_id"] = recipe_id
    recipe = recipes_collection.find_one({"_id": ObjectId(session["current_recipe_id"])})
    
    return render_template("recipe.html", recipe=recipe)


@recipe.route("/receita", methods = ["POST"])
def recipe_post():

    # Verificando se há algum usuário logado
    if not "username" in session:
        return redirect(url_for("auth.login_signup"))
    
    # Recuperando o formulário e seus valores
    form = request.form.to_dict()
    user_comment = form.get("user_comment")
    view_recipe_id = form.get("view_recipe_btn")
    delete_recipe_id = form.get("delete_recipe_btn")

    # Se o usuário apertou o botão de visualizar a receita
    if view_recipe_id:
        return redirect(url_for("recipe.recipe_get", recipe_id=view_recipe_id))
    
    # Se o usuário clicou no botão de deletar a receita
    if delete_recipe_id:
        
        # Antes de deletar as receitas, temos que recuperar os comentários associados a ela para deletá-los também
        comments_list = recipes_collection.find_one({"_id": ObjectId(delete_recipe_id)}, {"comments": 1, "_id": 0})['comments']
        comments_ids = []

        # Recuperando apenas os IDs dos comentários
        for comment_dict in comments_list:
            comments_ids.append(comment_dict["_id"])
        
        # Deletando os comentários do banco de dados
        for id in comments_ids:
            comments_collection.delete_one({"_id": id})

        # Por fim, deletando a receita
        recipes_collection.delete_one({"_id": ObjectId(delete_recipe_id)})

        return redirect(url_for("profile.profile_page_get"))
    
    if user_comment:
        user_comment = user_comment.strip()

        logged_user = users_collection.find_one({"username": session['username']})

        # Adicionando o comentário na base de dados
        comment = Comment(logged_user["_id"],session["current_recipe_id"], user_comment).__dict__
        comments_collection.insert_one(comment)
        
        # Retirando as informações desnecessárias para adicionar na receita
        comment.pop("recipe_id", "Não encontrado")
        comment['username'] = logged_user['username']

        recipes_collection.update_one(
        {"_id": ObjectId(session["current_recipe_id"])},
        {"$push": {"comments": comment}}
        )

        # Recarregando a página
        return redirect(url_for("recipe.recipe_get"))

# ---------------------------- ROTA DAS RECEITAS --------------------------------------------

@recipe.route("/receitas", methods = ["POST"])
def recipes_post():

    # Verificando se há algum usuário logado
    if not "username" in session:
        return redirect(url_for("auth.login_signup"))

    chosen_category = request.form.get("category").lower()
    category_recipes = list(recipes_collection.find({"category": chosen_category}))
    return render_template("recipes.html", category_recipes = category_recipes) # A PRIMEIRA VAR É COMO VAI SER CHAMADA NO HTML E A SEGUNDA É A VARIAVEL DA ROTA

# ---------------------------- ROTAS PARA CRIAR RECEITAS -----------------------------------------------------------------------

@recipe.route("/receitas/criar_receitas", methods=["GET"])
def add_recipes_get():

    # Verificando se há algum usuário logado
    if not "username" in session:
        return redirect(url_for("auth.login_signup"))

    session.pop('_flashes', None)
    return render_template("add_recipe.html")



@recipe.route("/receitas/criar_receitas", methods=["POST"])
def add_recipes_post():

    # Verificando se há algum usuário logado
    if not "username" in session:
        return redirect(url_for("auth.login_signup"))

    form = request.form.to_dict()

    if any_empty_value(form, False):
        return render_template("add_recipe.html", empty_value=True)

    # Recuperando os dados do formulário
    inputed_name = form.get("name")
    inputed_preparation = form.get("preparation")
    inputed_category = form.get("category").lower()

    # Salvando a imagem no gridfs e recuperando seu id
    inputed_img = request.files['img'].read()
    image_id = fs.put(inputed_img)

    ingredients_list = []
    user = users_collection.find_one({"username": session["username"]})

    # Colocando os ingrendientes em uma lista própria
    for key in form.keys():
        if "recipe_ingredient" in key:
            ingredients_list.append(form[key])

    # Criando e armazenando a receita
    new_recipe = Recipe(user['_id'], image_id, inputed_name, inputed_preparation, ingredients_list, inputed_category)
    added_recipe = recipes_collection.insert_one(new_recipe.__dict__)
    users_collection.update_one({"username": user["username"]}, {"$push": {"my_recipes" : added_recipe.inserted_id}})

    flash(f'Receita "{inputed_name}" criada com sucesso!')
    return render_template("add_recipe.html")

# -------------------------------------------- ROTA PARA RETORNAR A IMAGEM DAS RECEITAS NO <img> ---------------------------------------------

@recipe.route("/get_image/<file_id>")
def get_image(file_id):

    # Verificando se há algum usuário logado
    if not "username" in session:
        return redirect(url_for("auth.login_signup"))

    my_img = fs.get(ObjectId(file_id))
    stream = BytesIO(my_img.read())

    return send_file(stream, mimetype="image/png")