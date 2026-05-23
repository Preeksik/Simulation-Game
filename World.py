from Position import Position
from Organisms.Plant import Plant
from Action import Action
from ActionEnum import ActionEnum


class World(object):

	def __init__(self, worldX, worldY):
		self.__worldX = worldX
		self.__worldY = worldY
		self.__turn = 0
		self.__organisms = []
		self.__newOrganisms = []
		self.__separator = ' '
		self.plague_turns = 0

	@property
	def worldX(self):
		return self.__worldX

	@property
	def worldY(self):
		return self.__worldY

	@property
	def turn(self):
		return self.__turn

	@turn.setter
	def turn(self, value):
		self.__turn = value

	@property
	def organisms(self):
		return self.__organisms

	@organisms.setter
	def organisms(self, value):
		self.__organisms = value

	@property
	def newOrganisms(self):
		return self.__newOrganisms

	@newOrganisms.setter
	def newOrganisms(self, value):
		self.__newOrganisms = value

	@property
	def separator(self):
		return self.__separator

	def addOrganism(self, newOrganism):
		newOrgPosition = Position(xPosition=newOrganism.position.x, yPosition=newOrganism.position.y)

		if self.positionOnBoard(newOrgPosition):
			self.organisms.append(newOrganism)
			self.organisms.sort(key=lambda org: org.initiative, reverse=True)
			return True
		return False

	def positionOnBoard(self, position):
		return position.x >= 0 and position.y >= 0 and position.x < self.worldX and position.y < self.worldY

	def getOrganismFromPosition(self, position):
		pomOrganism = None

		for org in self.organisms:
			if org.position == position:
				pomOrganism = org
				break
		if pomOrganism is None:
			for org in self.newOrganisms:
				if org.position == position:
					pomOrganism = org
					break
		return pomOrganism

	def getNeighboringPositions(self, position):
		result = []
		pomPosition = None

		for y in range(-1, 2):
			for x in range(-1, 2):
				pomPosition = Position(xPosition=position.x + x, yPosition=position.y + y)
				if self.positionOnBoard(pomPosition) and not (y == 0 and x == 0):
					result.append(pomPosition)
		return result

	def filterFreePositions(self, fields):
		result = []

		for field in fields:
			if self.getOrganismFromPosition(field) is None:
				result.append(field)
		return result

	def filterPositionsWithoutAnimals(self, fields):
		result = []
		pomOrg = None

		for filed in fields:
			pomOrg = self.getOrganismFromPosition(filed)
			if pomOrg is None or isinstance(pomOrg, Plant):
				result.append(filed)
		return result

	
