class Task:
    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str):
        if new_name != self.name:
            self.name = new_name
            return new_name
        return 'Name cannot be the same.'

    def change_due_date(self, new_due_date: str):
        if self.due_date == new_due_date:
            return "Date cannot be the same."

        self.due_date = new_due_date

        return new_due_date

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if 0 <= comment_number < len(self.comments):
            self.comments[comment_number] = new_comment
            return ', '.join(self.comments)

        return 'Cannot find comment.'

    def details(self):
        return f'Name: {self.name} - Due Date: {self.due_date}'



