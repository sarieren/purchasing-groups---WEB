import smtplib
from datetime import datetime

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import connection as connection

MY_ADDRESS = 'shoshnacohen@gmail.com'
PASSWORD = 'Sari1998@'


def get_contacts(info): #filename


    names = []
    emails = []
    message = []

    for i in info:
        names.append(i["user_name"])
        emails.append(i["user_mail"])
        m = "Hello " + i["user_name"] +",\n" + "Today, the "+ i["group_name"] + " purchasing group is rnding" +"\n" + "Good Bye"
        message.append(Template(m))
    
    return names, emails, message


# def read_template(): #filename
#     """
#     Returns a Template object comprising the contents of the 
#     file specified by filename.
#     """

#     # with open(filename, 'r', encoding='utf-8') as template_file:
#     #     template_file_content = template_file.read()

#     template_file_content = "hello world"
#     return Template(template_file_content)


def send_message():

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 
    n = now.split(" ")

    query = ''' select user_name, user_mail, group_name
    from purchaser natural join groups natural join user
    where id = group_id and user_name = manager and manager = user_name
    and end_date = '{}' '''.format(n[0])
    res = connection.do_query(query)


    names, emails, messages = get_contacts(res)  # read contacts 'mycontacts.txt'
    #message_template = read_template() #'message.txt'

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email, message  in zip(names, emails, messages):
        msg = MIMEMultipart()  # create a message

        # add in the actual person name to the message template
        message = message.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From'] = MY_ADDRESS
        msg['To'] = email
        msg['Subject'] = "Group Buy"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg

    # Terminate the SMTP session and close the connection
    s.quit()
