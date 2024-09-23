import re
text = '''In today’s digital world communication is key Many professionals prefer using email for their correspondence 
 For instance, you might reach out to jane.doe@example.com for inquiries Another useful contact could be john.smith@domain.com for project updates 
  Don’t forget to connect with alice.jones@email.com regarding collaboration opportunities 
  For support you can always email support@service.org Lastly for newsletters consider signing up with info@company.net
 '''

pattern = r'[A-Z|a-z|0-9|.]{1,}+@[A-Z|a-z|0-9]{1,}.[A-Z|a-z|0-9]{1,}'

# pattern = r'\w{1,}+@\w{1,}+.\w{1,}'
searched = re.findall(pattern, text)
print(searched)






