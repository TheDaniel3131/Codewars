class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    
    def is_worth_it(self):
        removed_draft_weight = self.draft - (1.5 * self.crew)
        if removed_draft_weight > 20:  
            return True;
        else:
            return False;