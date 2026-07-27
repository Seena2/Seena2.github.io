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
if "social_links" in data:
    for link in data["social_links"]:
        if link.get("svg_path"):
            with Path(link["svg_path"]).open(encoding="utf-8") as svg_file:
                link["svg_data"] = svg_file.read()

# Setup Jinja environment by specifying the location of the templates
env = Environment(loader= FileSystemLoader("templates"), autoescape=True)
base_template=env.get_template("_base.html")
index_template=env.get_template("index_template.html")
resume_template=env.get_template("resume_template.html")
projects_template=env.get_template("projects_template.html")
blogs_template=env.get_template("blogs_template.html")
courses_template=env.get_template("courses_template.html")
contact_template=env.get_template("contact_template.html")

# Render the template with data
index_output = index_template.render(**data) # '**data'=> unpack the dictionary and pass to the tempalte ( allows u to use {{name}} instead of {{data.name}})
resume_output = resume_template.render(**data)
projects_output = projects_template.render(**data)
blogs_output = blogs_template.render(**data)
courses_output = courses_template.render(**data)
contact_output = contact_template.render(**data)

# This is equivalent to...
# index_output = index_template.render(name=data["name"], label=data["label"]...)
# resume_output = resume_template.render(name=data["name"], label=data["label"]...)

# Write the output(rendered using jinja) to HTML file
with Path("index.html").open("w", encoding="utf-8") as f:
    f.write(index_output)
with Path("resume.html").open("w", encoding="utf-8") as f:
    f.write(resume_output)
with Path("projects.html").open("w", encoding="utf-8") as f:
    f.write(projects_output)
with Path("blogs.html").open("w", encoding="utf-8") as f:
    f.write(blogs_output)
with Path("courses.html").open("w", encoding="utf-8") as f:
    f.write(courses_output)
with Path("contact.html").open("w", encoding="utf-8") as f:
    f.write(contact_output)

print("HTML file generated successfully")
