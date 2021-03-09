class Room: # entire class provided
    def __init__(self, name): 
        self.name = name

    def __eq__(self, other):
        return self.name == other.name
        
    def __repr__(self): 
        return "Room(name: {})".format(self.name)


class Task:
    def __init__(self, n):
        self.name = n
        self.isCompleted = False

    def __eq__(self, other):
        return (self.name, self.isCompleted) == (other.name, other.isCompleted)
            
    def __repr__(self): # provided
        return "Task(name: {}, isCompleted: {})".format(self.name, self.isCompleted)


class Crewmate:
    def __init__(self, n, c, a = ()):
        self.name = n 
        self.color = c
        self.accessories = a
        self.isAlive = True
        self.tasksDone = 0

    def doTask(self, task):
        if task.isCompleted == False:
            task.isCompleted = True
            self.tasksDone += 1
            return self.tasksDone
        else:
            return "Nothing to do here."

    def vote(self, amongus):
        for n in amongus.crewmates + amongus.impostors:
            if n.name != self.name and n.name[0] == self.name[0] and n.isAlive and self.isAlive:
                return n
            
    def callMeeting(self, amongus):
        votingList = []
        votingdict = {}
        for n in amongus.crewmates + amongus.impostors:
                votingList.append(n.vote(amongus))
        for v in votingList:
            if v.name not in votingdict:
                votingdict[v.name] = 1
            else:
                votingdict[v.name] += 1
        p = ""
        for person, vote in votingdict.items():
            if vote == max(votingdict.values()):
                p = person
        otherp = ""
        for p1 in amongus.crewmates + amongus.impostors:
            if p == p1.name:
                otherp = p1
                p1.isAlive = False
        if type(otherp) == Impostor:
            return otherp.name + " was An Impostor."
        else:
            return otherp.name + " was not An Impostor."
 
    def __repr__(self): # provided 
        return "Crewmate(name: {}, color: {})".format(self.name, self.color)

    def __eq__(self, other): # provided
        return (self.name, self.color, self.accessories) == (other.name, other.color, other.accessories)


class Impostor:
    def __init__(self, n, c, a = ()):
        self.name = n
        self.color = c
        self.accessories = a
        self.isAlive = True
        self.eliminateCount = 0

    def eliminate(self, player):
        if type(player) == Impostor:
            return "They're on your team -_-"
        elif type(player) == Crewmate:
            player.isAlive = False
            self.eliminateCount += 1
            
    def vote(self, amongus):
       for n in amongus.crewmates + amongus.impostors:
            if n.name != self.name and n.name[0] == self.name[0] and n.isAlive and self.isAlive:
                return n
    
    def __str__(self):
        return "My name is " + self.name + " and I'm an impostor."
    
    def __repr__(self): # provided
        return "Impostor(name: {}, color: {})".format(self.name, self.color)

    def __eq__(self, other): # provided 
        return (self.name, self.color, self.accessories) == (other.name, other.color, other.accessories)


class AmongUs: 
    def __init__(self, mP):
        self.maxPlayers = mP
        self.rooms = {}
        self.crewmates = []
        self.impostors = []
        
    def registerPlayer(self, player):
        if (len(self.impostors) + len(self.crewmates)) >= self.maxPlayers:
            return "Lobby is full."
        if player in self.crewmates or player in self.impostors:
            return "Player with name: " + player.name + " exists."
        else:
            if type(player) == Crewmate:
                self.crewmates.append(player)
            elif type(player) == Impostor:
                self.impostors.append(player)
       
    def registerTask(self, task, room):
        for t in self.rooms.values():
            if task in t:
                return "This task has already been registered."
        else:
            self.rooms[room.name] = []
            self.rooms[room.name].append(task)
                
    def gameOver(self):
        for crewmate in self.crewmates:
            if crewmate.isAlive == False:
                return "Defeat! All crewmates have been eliminated."
            else:
                return "Game is not over yet!"
        for impostor in self.impostors:
            if impostor.isAlive == False:
                return "Victory! All impostors have been eliminated."
            else:
                return "Game is not over yet!"

    def __repr__(self): # provided
        return "AmongUs(maxPlayers: {})".format(self.maxPlayers)

c = Crewmate("Summer", "blue")
a= AmongUs(4)
print(c.vote(a))

