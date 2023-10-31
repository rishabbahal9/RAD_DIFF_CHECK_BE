from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
from dotenv import dotenv_values

config=dotenv_values(".env")

app = Flask(__name__)
CORS(app)
api=Api(app)


class Template(Resource):
    def get(self, template_id):
        print("Template ID" + str(template_id))
        return {"content": """EXAM:
CT [_laterality_] [Generic Bone], [without or with] IV contrast

CLINICAL HISTORY:

TECHNIQUE:
Axial images were acquired through the [_laterality_] [generic bone]
[without or with] IV contrast. Reformatted images were reviewed.
Dose reduction technique was used including one or more of the following:
automated exposure control, adjustment of mA and kV according to patient size,
and/or iterative reconstruction.

COMPARISON:
None provided.

FINDINGS:

BONES:
No acute fracture or focal osseous lesion.

JOINTS:
No dislocation. The joint spaces are normal.

SOFT TISSUES:
The soft tissues are unremarkable.

IMPRESSION:

1. No acute osseous abnormality.
"""}

api.add_resource(Template, "/get-report-template/<template_id>")

if __name__ == "__main__":
    app.run(port=config["PORT"], debug= True if config["DEBUG"]=="True" else False)