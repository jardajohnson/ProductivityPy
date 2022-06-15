from app import app
from app.controllers import users, notes
from app.models import quote


if __name__ == "__main__":

    app.run(debug=True)
