from flask import Flask, request
from lib2to3.refactor import RefactoringTool, get_fixers_from_package
import sys

app = Flask(__name__)


@app.route("/convert", methods=["POST"])
def convert_script():
    input_script = request.data.decode("utf-8")
    tool = RefactoringTool(fixer_names=get_fixers_from_package("lib2to3.fixes"))

    try:
        tree = tool.refactor_string(input_script + "\n", "script")
    except Exception as e:
        return str(e), 500

    return str(tree), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
