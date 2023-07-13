class Website:

    def __init__(self, name, popularity, front_end, back_end):
        self.name = name
        self.popularity = popularity
        self.front_end = front_end
        self.back_end = back_end

    def __str__(self):
        return f'{self.name} (Frontend:{self.front_end}|Backend:{self.back_end})'
