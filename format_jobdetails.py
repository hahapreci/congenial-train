import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('job_details.csv')
def determine_in_demand_skills(skill):
    # Subset the data to include only job postings that require Python as a skill
    df_python = df[df['Required Skills'].str.contains(skill, case=False)]
    # Combine all the required skills into a single string
    all_python_skills = ' '.join(df_python['Required Skills'].tolist())
    # Split the skills string into individual skills
    python_skills_list = all_python_skills.split(', ')
    # Remove the skill 'python' to represent accurate data
    cleaned_skills_list = [skill for skill in python_skills_list if skill.strip().lower() != 'python']
    # Create a Series to count the frequency of each skill
    skills_counts = pd.Series(cleaned_skills_list).value_counts()
    # Get the top 5 skills
    top_5_skills_counts = skills_counts.head(5)

    # print("Top 7 skills and their counts:")
    # print(top_5_skills_counts)

    # Plot the filtered top 5 skills as a bar graph
    plt.figure(figsize=(10, 6))
    ax = top_5_skills_counts.plot(kind='bar', color='skyblue')

    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom',
                    fontsize=10, color='black')

    plt.xlabel('Skills')
    plt.ylabel('Number of Occurrences')
    plt.title(f"Top 5 Skills to Learn As Someone Who Knows {skill}")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def determine_in_demand_positions(number):
    top_on_demand_job = df['Job Title'].value_counts().head(number)
    # print(f'Top {number} in-demand jobs:')
    # print(top_on_demand_job)

    # Plot the top in-demand jobs as a bar graph
    plt.figure(figsize=(10, 6))
    ax = top_on_demand_job.plot(kind='bar', color='lightgreen')

    # Adding annotations above the bars
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom',
                    fontsize=10, color='black')

    plt.xlabel('Job Titles')
    plt.ylabel('Number of Occurrences')
    plt.title(f"Top {number} in-demand jobs")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


print(determine_in_demand_skills('Python'))
print(determine_in_demand_positions(5))
