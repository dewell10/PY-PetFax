from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello, this is PetFax"
# register pet blueprint 
    # configurations 

    # this imports our pet.py file as a blueprint for that route
    from . import pet 
    app.register_blueprint(pet.bp)
    
    from . import fact
    app.register_blueprint(fact.bp)

    return app