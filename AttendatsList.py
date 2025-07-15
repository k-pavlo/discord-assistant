class AttendatsList:
    def __init__(self, title, date, prime_storyteller):
        self.date = date
        self.title = title
        self.prime_storyteller = prime_storyteller
        self.attendants = ""
    
    def append(self, name: str):
        name_num = self.attendants.count("\n") + 1
        self.attendants += f"{name_num}. {name}\n"
    
    def print_list(self):
        return f"{self.date} - **{self.title}**\n**Оповідачі:** @{self.prime_storyteller} \n**Гравчині:**\n{self.attendants}"