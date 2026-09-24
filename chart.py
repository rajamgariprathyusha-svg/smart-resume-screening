import matplotlib.pyplot as plt
import os


def create_skill_chart(matched, missing):

    labels = ["Matched Skills", "Missing Skills"]
    sizes = [len(matched), len(missing)]

    plt.figure(figsize=(5, 5))
    plt.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Skill Match Analysis")

    os.makedirs("static/charts", exist_ok=True)

    plt.savefig("static/charts/skill_chart.png")

    plt.close()