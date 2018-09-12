class State(object):

    def __init__(self, state_name):
        self.name = state_name
        self.transitions = dict()

hungry = State('hungry dog')
full = State('full dog')
tired = State('tired dog')
asleep = State('asleep dog')

hungry.transitions['feed'] = full
hungry.transitions['walk'] = hungry
hungry.transitions['pet'] = hungry
hungry.transitions['show mail'] = hungry

full.transitions['feed'] = full
full.transitions['walk'] = tired
full.transitions['pet'] = tired
full.transitions['show mail'] = hungry

tired.transitions['feed'] = full
tired.transitions['pet'] = asleep
tired.transitions['show mail'] = asleep

asleep.transitions['pet'] = hungry
asleep.transitions['show mail'] = asleep
