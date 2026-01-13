import os
import sys

# Ensure the project root (parent of this folder) is on sys.path so
# `from website import create_app` works when running this file directly.
parent_dir = os.path.dirname(os.path.dirname(__file__))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

import importlib.util  # noqa: E402

# Load the app factory directly from website/__init__.py to avoid
# package import issues when the script is executed directly.
website_init = os.path.join(os.path.dirname(__file__), "website", "__init__.py")
spec = importlib.util.spec_from_file_location("website", website_init)
website_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(website_mod)

create_app = getattr(website_mod, "create_app")

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
