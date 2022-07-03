from flask import Flask
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    # database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Tfoyiitp9*@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    from . import models
    models.db.init_app(app) 
    migrate = Migrate(app, models.db)


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