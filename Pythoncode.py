def validate_email(emailValidator):
    
    forbidden_domains = {
        "@scam", "@spam", "@fakeemail", "@trashmail",
        "@pleasenotspam", "@therealtaylorswift", "@sendmoney"
    }
    acceptable_tlds = {".com", ".ca", ".org", ".net", ".gov", ".edu"}

   
    if emailValidator.count("@") != 1:
        return "Invalid"
    
    local_part, domain = emailValidator.split("@")

    if not all(c.isalnum() or c in ".-" for c in local_part):
        return "Invalid"
    
    if '.' not in domain:
        return "Invalid"
    
    domain_parts = domain.rsplit(".", 1)
    if len(domain_parts) != 2:
        return "Invalid"
    
    second_part_domain, top_part_domain = domain_parts
    top_part_domain = "." + top_part_domain  

    if top_part_domain not in acceptable_tlds:
        return "Invalid"
    
    if "@" + second_part_domain in forbidden_domains:
        return "Forbidden"
    
    return "Valid"

def main():
     entered_emails = list(input("Please enter the email addresses separated by spaces: ").split())

     for all_emails in entered_emails:
        output_desicion = validate_email(all_emails)
        print(output_desicion)

if __name__ == "__main__":
    main()



