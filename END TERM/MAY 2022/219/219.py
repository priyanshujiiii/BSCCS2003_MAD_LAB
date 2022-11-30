from jinja2 import Template

temp = """{% set numbers = studs | map(attribute = "mark")|list %}
{{numbers |min}} {{numbers | max}}"""

studs=[
    {"stud_name":"Reeta","mark":"92"},
    {"stud_name":"Veena","mark":"88"},
    {"stud_name":"Meena","mark":"62"},
    {"stud_name":"uma","mark":"98"},
]
t1 = """{% for i in studs -%}
            {{i}}
        {%- endfor %}"""

output = Template(temp)
out = Template(t1)
print(output.render(studs =studs))
print(out.render(studs=studs))
