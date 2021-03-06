''' Main application module '''

from app_package import create_app, db
from app_package.models import User, Post


app = create_app()

# This creates a shell context that adds the database instance and models 
# to the shell session ('flask shell' in cmd), useful for testing;
@app.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User, 'Post': Post}