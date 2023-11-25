import json
class Discipline:
    def __init__(self, name):
        self.name = name
        self.topics = []

    def add_topic(self, topic):
        self.topics.append(topic)

    def display_info(self):
        print(f"Discipline: {self.name}")
        print("Topics:")
        for topic in self.topics:
            print(f"- {topic}")
    
    def to_dict(self):
        topics_dict = {self.name: [topic.name for topic in self.topics]}
        return topics_dict

    def create_json_file(self):
        data = self.to_dict()
        json_filename = f"{self.name.lower().replace(' ', '_')}_topics.json"
        with open(json_filename, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

class Topic:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Topic: {self.name}")
