# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dsi_schema_assurance',
 'dsi_schema_assurance.detectors',
 'dsi_schema_assurance.utils']

package_data = \
{'': ['*']}

install_requires = \
['pyshacl==0.29.0', 'rdflib==7.1.1', 'requests==2.32.3', 'setuptools==68.2.2']

setup_kwargs = {
    'name': 'dsi-schema-assurance',
    'version': '0.0.2',
    'description': 'Package for schema assurance.',
    'long_description': '<h1 align=\'center\'>\n    <strong> Schema Validation </strong>\n</h1>\n\n<p align=\'center\'>\n    Validate your RDF data against an ontology and SHACL files - even when the data instance lacks datatypes definition.\n</p>\n\n\n<div align="center">\n\n  <a href="code coverage">![coverage](https://img.shields.io/badge/coverage-96%25-brightgreen)</a>\n  <a href="tests">![tests](https://img.shields.io/badge/tests-62%20passed%2C%200%20failed-brightgreen)</a>\n  <a href="python version">![sbt_version](https://img.shields.io/badge/python-3.10-blue?logo=python&logoColor=white)</a>\n\n</div>\n\n## **1. Intro**\n\nThe Resource Description Framework (RDF) is a method to describe and exchange graph data.\n\nAn RDF data instance can be complemented with two additional artefacts that enable RDF schema validation:\n\n- **Ontology**: describes the concepts and resources of a data instance using RDF language and allows for the detection of logically impossible assertions in the model.\n- **SHACL (Shapes Constraint Language)**: a W3C standard that describes and validates the contents of RDF graphs instances.\n\nSometimes RDF data might lack datatypes definition. Under these circumstances, W3C states that when no datatype is specified, the data is by default considered `Literal` (the equivalent of a `string`).\n\nThese can be tricky. In that scenario, a standard validation will not produce the desired validation outcome. It can also be especially challenging when the data instance cannot be altered to comply with the W3C standard, be it by the standard definition (e.g., CIM), or by the inability to alter the source system to add the datatypes.\n\nThis is where the Schema Validation comes in. It dynamically injects the datatypes into the data instance, inferring the datatypes by navigating the hierarchy, and validates it against the desired ontologies and SHACL files.\n\n## **2. How to Use - _high level_**\n\n```python\nfrom rdflib import Graph\n\nfrom neso_utils import SchemaCertifier\n\ndata_graph = Graph()\ndata_graph.parse(data_path, format=\'xml\')\n\nshacl_graph = Graph()\nshacl_graph.parse(shacl_path, format=\'turtle\')\n\nont_graph = Graph()\nont_graph.parse(ont_path, format=\'xml\')\n\nvalidation_result = SchemaCertifier(\n    data_graph=data_graph,\n    shacl_graph=shacl_graph,\n    ont_graph=ont_graph,\n).run()\n```\n\n**Note:** there\'s still some indefinition around how we\'re going to package all the modules together, which means that the way to use the Schema Validation might change in the future.\n\n## **3. How it works under the hood**\n\n<p align="center">\n    <img src="./.docs/schema_certifier_mo.png" width="1200" height="250">\n</p>\n\nThis solution divides itself into three main parts:\n\n- The **_Datatypes Hunter_**: extracts the datatypes from ontologies or SHACLs.\n- The **_Datatypes Injector_**: injects the datatypes into the RDF data instance.\n- The **_Validator_**: validates the RDF data instance against the ontologies and SHACL files.\n\nLet\'s dive into each one of them.\n\n### **3.1. Datatypes Hunter**\n\nAs stated before, the datatypes hunter is the module that will be responsible for the following:\n- extract the datatypes by parsing either an ontology or a SHACL file;\n- the parsing is done via SPARQL queries;\n- the queries naviagate through a nested hierarchy like the one in the image below:\n\n<p align="center">\n    <img src="./.docs/ontology_hierarchy.png" width="500" height="550">\n</p>\n\nAdditionally, it\'s important to retain something about it\'s implementation. We have an hunter that is fully dedicated for the ontologies, and another one for the SHACL files.\n\nThis is because the ontologies and the SHACL files have different structures, and therefore, different strategies to extract the datatypes.\n\n### **3.2. Datatypes Injector**\n\nSingle function that injects the datatypes, collected by the `DatatypeHunter`, to the RDF data instance.\n\n### **3.3. Validator**\n\nLast but not least, the validator script contains the SchemaCertifier class. This class is the one that will be responsible for the validation of the data.\n\nGoing back to module mentioned (Datatypes Hunter), this module will be responsible for concialiating the outcomes of the hunters (if the user provides both ontologies and SHACL files).\n\nBy default, the SHACLs are more assertive when it comes to datatypes definition, and therefore, the datatypes obtained from these will be the ones responsible for dictating the final datatypes.\n\nThis module leverages the pyshacl to perform the validation.\n\nThe user can choose the specs that will be leveraged on the validation process.\n\n---\n\n## **A1. Tests and Coverage**\n\nTo run the tests and coverage, use the following command:\n\n```bash\n❯ coverage run -m unittest discover tests/\n```\n\nthe current coverage report is the following:\n\n```bash\nName                                     Stmts   Miss  Cover\n------------------------------------------------------------\nschema_assurance/detectors/ddl.py            3      0   100%\nschema_assurance/detectors/ontology.py      27      0   100%\nschema_assurance/detectors/shacl.py          6      0   100%\nschema_assurance/injector.py                17      0   100%\nschema_assurance/utils/pandas.py            18      0   100%\nschema_assurance/validator.py              120      7    94%\n------------------------------------------------------------\nTOTAL                                      191      7    96%\n```\n',
    'author': 'Joao Nisa',
    'author_email': 'joao.nisa@mesh-ai.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
