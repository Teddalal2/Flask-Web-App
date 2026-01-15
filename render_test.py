from website import create_app
import traceback

app = create_app()

with app.test_request_context("/"):
    try:
        from flask import render_template

        print(render_template("home.html"))
    except Exception as e:
        traceback.print_exc()
