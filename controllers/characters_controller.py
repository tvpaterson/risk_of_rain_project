from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.character import Character
import repositories.character_repository as character_repository

characters_blueprint = Blueprint("character", __name__)

# @characters_blueprint.route("/home")
# def home_page():
#     return render_template("index.html")
    
