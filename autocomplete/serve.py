from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
# on créé l'application Flask en utilisant le nom du fichier.
# cela permet de faire les commandes :
# export FLASK_APP=serve.py
# python3 -m flask run


@app.route("/", methods=['GET'])
def index():
    """Renvoie la page HTML associée à la racine du site.
    
    Cela est plus utile pour des pages dynamique dont le contenu va dépendre
    d'objets python, mais on peut très bien afficher une page toute simple comme
    on le fait ici. Pour une page comme index.html, on peut se contenter de
    double-cliquer dessus.
    """
    return render_template("index.html")

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    """Renvoie les candidats pour l'autocomplétion.
    
    Cette fonction doit rester la plus simple possible. Le gros du code doit
    être écrit dans un module à part.
    """
    response = ""
    term = request.args.get('term')
    if term:
        items = [ "c++", "java", "php", "python", "javascript", "asp", "ruby", "perl", "ocaml", "haskell", "rust", "go" ]
        candidates = [item for item in items if item.startswith(term)]
        response = jsonify(candidates)
        response.headers.add('Access-Control-Allow-Origin', '*') # Pour éviter les erreurs de type CORS en dév local
    return response
