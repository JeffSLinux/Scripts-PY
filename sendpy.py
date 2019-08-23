import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#def get_contacts(filename):
#    """
#    Return two lists names, emails containing names and email addresses
#    read from a file specified by filename.
#    """
    
#    names = []
#    emails = []
#    with open(filename, mode='r', encoding='utf-8') as contacts_file:
#        for a_contact in contacts_file:
#            names.append(a_contact.split()[0])
#            emails.append(a_contact.split()[1])
#    return names, emails

#def read_template(filename):
#    """
#    Returns a Template object comprising the contents of the 
#    file specified by filename.
#    """
#    
#    with open(filename, 'r', encoding='utf-8') as template_file:
#        template_file_content = template_file.read()
#    return Template(template_file_content)
#

def main():
    MY_ADDRESS = input('Email Atenticacao: ')
    PASSWORD = input('Senha mail: ')
    SERVER = input('Servidor: ')
    PORTA = input('Porta: ')
    PARA = input('Para Destino: ')
    MSG = str(input("Digite a msg: "))
    #names, emails = get_contacts('mycontacts.txt') # read contacts
    message_template = MSG


    # set up the SMTP server
    s = smtplib.SMTP(host=SERVER, port=PORTA)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    #for name, email in zip(names, emails):
    msg = MIMEMultipart()       # create a message
    name = 'teste'
 
        # add in the actual person name to the message template
    #message = message_template.substitute(PERSON_NAME=name.title())
    message = MSG

        # Prints out the message body for our sake
    print(MSG)

        # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']=PARA
    msg['Subject']=MSG
        
        # add in the message body
    msg.attach(MIMEText(message, 'plain'))
        
        # send the message via the server set up earlier.
    s.send_message(msg)
    del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
if __name__ == '__main__':
    main()
