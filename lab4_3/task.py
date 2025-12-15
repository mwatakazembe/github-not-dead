import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker
import random

fake = Faker()

np.random.seed(42)
random.seed(42)

years = [2019, 2020, 2021, 2022, 2023]
specialties = ['computer science', 'mathematics', 'physics', 'chemistry', 'biology', 'economics', 'law', 'psychology']
study_forms = ['full-time', 'part-time', 'evening']
subjects = ['mathematics', 'language', 'physics', 'chemistry', 'biology', 'history']

def generate_student_data(num_students):
    students = []
    for _ in range(num_students):
        year = random.choice(years)
        specialty = random.choice(specialties)
        
        subject_scores = {}
        for subject in subjects:
            subject_scores[subject] = np.random.normal(loc=70, scale=15)
            subject_scores[subject] = max(0, min(100, subject_scores[subject]))
        
        certificate_avg = np.random.normal(loc=8.0, scale=0.8)
        certificate_avg = max(5.0, min(10.0, certificate_avg))
        
        total_score = np.mean(list(subject_scores.values())) + certificate_avg
        
        student = {
            'full_name': fake.name(),
            'admission_year': year,
            'study_form': random.choice(study_forms),
            'subject_scores': subject_scores,
            'certificate_avg': round(certificate_avg, 2),
            'total_score': round(total_score, 2),
            'specialty': specialty,
            'address': fake.address().replace('\n', ', '),
            'mobile': fake.phone_number()
        }
        students.append(student)
    
    return students

student_data = generate_student_data(5000)
df = pd.DataFrame(student_data)

subject_df = pd.json_normalize(df['subject_scores'])
subject_df.columns = [f'score_{col}' for col in subject_df.columns]
df = pd.concat([df.drop('subject_scores', axis=1), subject_df], axis=1)

plt.figure(figsize=(12, 6))
subject_columns = [col for col in df.columns if col.startswith('score_')]
yearly_subject_means = df.groupby('admission_year')[subject_columns].mean()
plt.plot(yearly_subject_means.index, yearly_subject_means.values)
plt.xlabel('year')
plt.ylabel('average score')
plt.title('average subject scores by year')
plt.legend([col.replace('score_', '') for col in subject_columns])
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
yearly_certificate_avg = df.groupby('admission_year')['certificate_avg'].mean()
plt.plot(yearly_certificate_avg.index, yearly_certificate_avg.values, marker='o', linewidth=2)
plt.xlabel('year')
plt.ylabel('average certificate score')
plt.title('average certificate score dynamics')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
passing_scores = df.groupby(['admission_year', 'specialty'])['total_score'].min().reset_index()
passing_scores_pivot = passing_scores.pivot(index='admission_year', columns='specialty', values='total_score')
plt.plot(passing_scores_pivot.index, passing_scores_pivot.values)
plt.xlabel('year')
plt.ylabel('passing score')
plt.title('passing score dynamics by specialty')
plt.legend(passing_scores_pivot.columns, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
specialty_counts = df.groupby(['admission_year', 'specialty']).size().unstack()
specialty_counts.plot(kind='bar', stacked=True, ax=plt.gca())
plt.xlabel('year')
plt.ylabel('number of students')
plt.title('number of admitted students by specialty')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
study_form_counts = df.groupby(['admission_year', 'study_form']).size().unstack()
study_form_counts.plot(kind='bar', stacked=True, ax=plt.gca())
plt.xlabel('year')
plt.ylabel('number of students')
plt.title('distribution of study forms')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
study_form_distribution = df['study_form'].value_counts()
plt.pie(study_form_distribution.values, labels=study_form_distribution.index, autopct='%1.1f%%')
plt.title('overall study form distribution')
plt.show()