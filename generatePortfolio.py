import json
from datetime import datetime,UTC
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Load JSON data
with Path("data/dinku.json").open(encoding="utf-8") as f:
    data= json.load(f)

# Add any extra content t to the data if needed
data["current_year"] =datetime.now(tz=UTC).year

# Social media icons, to embed the svg file in the html, 
# open the svg files and store the content into new key(svg_data)
# if "social_links" in data:
#     for link in data["social_links"]:
#         if link.get("svg_path"):
#             with Path(link["svg_path"]).open(encoding="utf-8") as svg_file:
#                 link["svg_data"] = svg_file.read()

# Setup Jinja environment by specifying the location of the templates
env = Environment(loader= FileSystemLoader("templates"), autoescape=True)
base_template=env.get_template("_base.html")
index_template=env.get_template("index_template.html")
resume_template=env.get_template("resume_template.html")

# Render the template with data
index_ouput = index_template.render(**data) # '**data'=> unpack the dictionary and pass to the tempalte ( allows u to use {{name}} instead of {{data.name}})
resume_ouput = resume_template.render(**data)
# This is equivalent to...
# index_output = index_template.render(name=data["name"], label=data["label"]...)
# resume_output = resume_template.render(name=data["name"], label=data["label"]...)

# Write the output(rendered using jinja) to HTML file
with Path("index.html").open("w", encoding="utf-8") as f:
    f.write(index_ouput)
with Path("resume.html").open("w", encoding="utf-8") as f:
    f.write(resume_ouput)

print("HTML file generated successfully")
