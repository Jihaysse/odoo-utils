import re

# Change the model and the email server here if necessary
model = 'account.move'
mail_server = 'eupj03'
    
def find_duplicate_emails(input_string):
    escaped_model = model.replace('.', r'\.')  # Escape the dot in the model
    pattern = f'(\d+)-{escaped_model}@{mail_server}\>\' successfully sent '
    
    sent_emails = {}
    
    for line in input_string.split('\n'):
        if line.endswith(f"{model}@{mail_server}>' successfully sent "):
            matches = re.findall(pattern, line)
            for match in matches:
                sent_emails[match] = sent_emails.get(match, 0) + 1
                       
    # Remove where sent_emails[key] == 1 as we only want to see duplicates
    sent_emails = {key: value for key, value in sent_emails.items() if value != 1} 
    return sent_emails

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    
    try:
        with open(file_path, 'r') as file:
            input_string = file.read()

        duplicates = find_duplicate_emails(input_string)
        if duplicates:
            print("\nDuplicate emails found:")
            for invoice_id in duplicates:
                print(f'{model} {invoice_id} | {duplicates[invoice_id]} times')
        else:
            print("\nNo duplicate emails found.")
    
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
