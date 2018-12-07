"""Module for creating app"""
from app import create_app

app = create_app()
@app.errorhandler(404)
def page_not_found(e):
    """error handler default method for error 404"""

    return make_response(
        jsonify(
            {"message": "Oops! not found, check if you have "
            "right url or correct input type", "status": 404}
            ), 404
        )

if __name__ == "__main__":
    app.run(debug=True)

