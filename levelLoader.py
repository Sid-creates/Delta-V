import json


class Level:
    def __init__(self, file_path):
        self.file_path = file_path
        self.load()
        self.parse()
        
    def parse_objects(self):
        self.objects = []
        for obj in self.level_data["objects"]:
            self.objects.append(obj)
    
    def parse_sprites(self):
        self.sprites = []
        for sprite in self.level_data["sprites"]:
            self.sprites.append(sprite)
    
    def parse(self):
        self.parse_objects()
        self.parse_sprites()

    def load(self):
        with open(self.file_path, 'r') as file:
            level_data = json.load(file)
        self.level_data = level_data

    def save(self, level_data):
        with open(self.file_path, 'w') as file:
            json.dump(level_data, file, indent=4)


if __name__ == "__main__":
    level = Level('levels/level1.json')
    print(json.dumps(level.sprites, indent=2))
    print(json.dumps(level.objects, indent=2))