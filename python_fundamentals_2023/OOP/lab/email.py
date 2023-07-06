class Email:
    def __int__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def print_email(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent:\n" \
               f"{self.is_sent}"


emails = []
command = input()
while command != 'Stop':
    senders = command.split(' ')[0]
    receivers = command.split(' ')[1]
    contents = command.split(' ')[2]
    email = Email(senders, receivers, contents)
    emails.append(email)
    command = input()
    send_emails = [int(x) for x in input().split(', ')]
for x in send_emails:
    emails[x].send()
for mail in emails:
    mail.print_email()

