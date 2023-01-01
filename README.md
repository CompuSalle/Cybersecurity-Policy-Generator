# Cybersecurity Policy Generator
This Python script generates customizable cybersecurity policy documents for businesses. It includes a list of policy elements that can be customized to fit the specific needs of a company, as well as a purpose statement and disclaimer.

## How to use
To use the policy generator, simply set the **company_name** variable to the name of your company and call the **generate_policy** function. The function will return a string containing the generated policy document.

```python
import policy_generator

company_name = "Compusalle Company"
policy = policy_generator.generate_policy(company_name)
print(policy)
```

You can customize the policy elements by modifying the **policy_elements** list in the **policy_generator** module.
