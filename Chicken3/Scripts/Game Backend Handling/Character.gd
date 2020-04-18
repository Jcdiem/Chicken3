extends Node

#Character parent class for define the essentials of all other char types
class_name Character
	
export(String) var title;
export(int) var level;
export(Array) var statArray;
export(String) var descriptionShort;
export(String) var descriptionLong;

func _init(title, level, statArray, descriptionShort, descriptionLong):
	self.title = title;
	self.level = level;
	self.statArray = statArray;
	self.descriptionShort = descriptionShort;
	self.descriptionLong = descriptionLong;
	
	print("Char "+title+" has been made");
	
