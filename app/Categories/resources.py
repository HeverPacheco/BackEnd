from flask.views import MethodView
from flask import Blueprint
from flask import request

Categories_blueprint = Blueprint("categories_blueprint", __name__, url_prefix='/api/')

#Lista De Categorias

class CategoriesList(MethodView):
    def get(self):
        return { "message": "Categories List"}

#Seleccion De Categorias

#class CategoriesSelectionList(MethodView):
    #def get(id):
        #category = next((c for c in categories if c["id"] == id), None)
        #if category:
            #return str(category)
        #else:
            #return ({"message": "Categoría no encontrada"}), 404
    
#Crear Categorias

#class CreateCategories(MethodView):
    #def post():
        #new_category = {
            #"id": request.form.get["id"],
            #"name": request.form.get["name"]
        #}
        #categories.append(new_category)
        #return "Categoría creada correctamente", 201
    
#URL's
    
#Categories_blueprint.add_url_rule(
    #'Categories',
    #view_func=CategoriesList.as_view("categories_list")
#)

#Categories_blueprint.add_url_rule(
    #'Categories',
    #view_func=CategoriesSelectionList.as_view("Categories")
#)

#Categories_blueprint.add_url_rule(
    #'Categories',
    #view_func=CreateCategories.as_view("Category_view")
#)