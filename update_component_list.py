#!/usr/bin/env python
# -*- coding: utf-8 -*

import os
import json

with open("project.json", "r") as file:
    project = json.load(file)

# clear actual inputs
project["project"]["steps"][0]["inputs"] = []

# list all json files
path = "."
files = os.listdir(path)
files.sort()

# generate a list of input components
for file in files:
    if (file[-4:] == "json") and (file != "project.json"):
        project["project"]["steps"][0]["inputs"].append(
            {"component": {"slug": file[:-5], "quantity": 1}}
        )

# update file
with open("project.json", "w") as outfile:
    json.dump(project, outfile, indent=4)
