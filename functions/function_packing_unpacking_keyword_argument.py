mySkills = {
    'python': '80%',
    'dart': '90%',
    'data_science': '75%'
}

def show_skills(**skills):
    print(type(skills))

    for skill, value in skills.items():
        print(f"{skill} -> {value}")

show_skills(pyhton = "80%", dart = "90%", data_science = "75%")
# show_skills(**mySkills)
