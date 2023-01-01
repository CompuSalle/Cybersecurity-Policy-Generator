import random

# List of policy elements to include in the generated policy
policy_elements = [
    "All employees must use strong passwords and regularly update them.",
    "All devices must have up-to-date antivirus software installed.",
    "Do not share login credentials with anyone.",
    "Do not open email attachments from unknown senders.",
    "Do not click on links in emails from unknown senders.",
    "Do not disclose personal information, such as social security numbers or bank account numbers, to anyone online.",
    "Report any suspicious activity or potential security threats to IT immediately.",
    "Do not download software or apps from untrusted sources.",
    "Use caution when accessing public WiFi networks.",
    "Drink Coffee"
]

# Function to generate a cybersecurity policy document
def generate_policy(company_name):
  # Initialize the policy document with a header and the company name
  policy = "CYBERSECURITY POLICY\n\n"
  policy += "This policy applies to all employees of " + company_name + ".\n\n"
  policy += "PURPOSE:\n\n"
  # Add a purpose statement to the policy
  policy += "The purpose of this policy is to ensure the secure handling of sensitive information and to protect the company's systems and networks from cybersecurity threats.\n\n"
  policy += "POLICY:\n\n"
  # Add the policy elements to the policy document
  for element in policy_elements:
    policy += "- " + element + "\n"
  # Add a disclaimer to the policy
  policy += "\nAny violations of this policy will result in disciplinary action, up to and including termination of employment.\n"
  return policy

# Set the company name
company_name = "Compusalle Company"
# Generate and print the policy
print(generate_policy(company_name))
