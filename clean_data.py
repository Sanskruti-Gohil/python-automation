import pandas as pd

input_file = 'C:/Users/spgoh/Downloads/Data - Sheet1.csv'
df = pd.read_csv(input_file)

df = df.drop_duplicates(subset='email')

df['has_joined_event'] = df['has_joined_event'].str.strip().str.lower().map({'yes': True, 'no': False})

linkedin_col = next((col for col in df.columns if 'linkedin' in col.lower()), None)

if linkedin_col:
    df['linkedin_incomplete'] = df[linkedin_col].isnull() | df[linkedin_col].astype(str).str.strip().eq('')
else:
    print("⚠️ Warning: No LinkedIn profile column found!")
    df['linkedin_incomplete'] = True  

job_title_col = next((col for col in df.columns if 'job' in col.lower() and 'title' in col.lower()), None)

if job_title_col:
    df['job_title_missing'] = df[job_title_col].isnull() | df[job_title_col].astype(str).str.strip().eq('')
else:
    print("⚠️ Warning: No Job Title column found!")
    df['job_title_missing'] = True

output_file = 'cleaned_output.csv'
df.to_csv(output_file, index=False)

print(f"Cleaned data saved to {output_file}")
