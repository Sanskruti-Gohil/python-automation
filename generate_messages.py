import pandas as pd
import os
import re


input_file = 'cleaned_output.csv'
df = pd.read_csv(input_file)


output_dir = 'messages'
os.makedirs(output_dir, exist_ok=True)

def create_message(row):
    first_name = row.get('first_name', 'there')
    job_title = row.get('Job Title', '').strip()
    has_joined = row.get('has_joined_event', False)
    
    if has_joined:
        return f"Hey {first_name}, thanks for joining our session! As a {job_title or 'valued attendee'}, we think you’ll love our upcoming AI workflow tools. Want early access?"
    else:
        return f"Hi {first_name}, sorry we missed you at the last event! We’re preparing another session that might better suit your interests as a {job_title or 'professional'}."

email_message_list = []

for idx, row in df.iterrows():
    email = row.get('email', 'unknown@example.com')
    message = create_message(row)
    
   
    safe_email = re.sub(r'[^A-Za-z0-9]+', '_', email)
    filename = os.path.join(output_dir, f"{safe_email}.txt")
    
    
    with open(filename, 'w') as f:
        f.write(message)
    
    email_message_list.append({'email': email, 'message': message})


output_csv = 'personalized_messages.csv'
pd.DataFrame(email_message_list).to_csv(output_csv, index=False)

print(f"Generated personalized messages saved in '{output_dir}' folder and '{output_csv}' file.")
