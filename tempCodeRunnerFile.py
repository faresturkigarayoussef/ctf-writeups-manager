import json 
with open("writeups.json", "r") as file:
    data = json.load(file)
with open("writeups.json", "w") as file:
    json.dump(data, file, indent=4)

    
class writeup :
    def __init__(self, title, category, platform, difficulty, solution):
        self.title = title
        self.category = category
        self.platform = platform
        self.difficulty = difficulty
        self.solution = solution

    def create (self) :
        file=f'open({self.title}.txt,'w')'
        file.write(f"title :   {self.title}\n" )
        file.write(f"category  {self.category}\n")
        file.write(f"platform {self.platform}")
        file.write(f"difficulty : {self.difficulty}\n")
        file.write(f"solution : {self.solution}\n")
        file.close()