from crypt import methods
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.character import Character
import repositories.character_repository as character_repository

characters_blueprint = Blueprint("character", __name__)

@characters_blueprint.route("/characters")
def all_characters():
    characters = character_repository.select_all()
    return render_template("/characters/index.html", characters = characters)
    
@characters_blueprint.route("/characters/<id>", methods=["GET"])
def show_character(id):
    character = character_repository.select(id)
    return render_template("characters/show.html", character = character)

