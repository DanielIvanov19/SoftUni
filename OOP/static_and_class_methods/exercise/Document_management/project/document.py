from project.category import Category
from project.topic import Topic


class Document:
    tags = []
    def __init__(self, id: int, category_id: int, topic_id: int, file_name: str):
        self.id = id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name

    @classmethod
    def from_instances(cls, id: int, category: Category, topic: Topic, file_name: str):
        return cls(id, category.id, topic.id, file_name)

    @staticmethod
    def add_tag(tag_content: str):
        if tag_content not in Document.tags:
            Document.tags.append(tag_content)

    @staticmethod
    def remove_tag(tag_content: str):
        if tag_content in Document.tags:
            Document.tags.remove(tag_content)


    def edit(self, file_name: str):
        self.file_name = file_name

    def __repr__(self):
        if Document.tags:
            tag_repr = ', '.join(Document.tags)
        else:
            tag_repr = ''
        return f"Document {self.id}: {self.file_name}; category {self.category_id}," \
               f" topic {self.topic_id}, tags: {tag_repr}"


