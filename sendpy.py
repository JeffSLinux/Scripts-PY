import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def main():
    MY_ADDRESS = input('Email Atenticacao: ')
    PASSWORD = input('Senha mail: ')
    SERVER = input('Servidor: ')
    PORTA = input('Porta: ')
    PARA = input('Para Destino: ')
    NAME = input('somento o nome:')
    MSG = str(input("Digite a msg: "))
    message_template = MSG


    # Configurar o smtp server
    s = smtplib.SMTP(host=SERVER, port=PORTA)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    msg = MIMEMultipart()       # create a message
    name = NAME 
 
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
