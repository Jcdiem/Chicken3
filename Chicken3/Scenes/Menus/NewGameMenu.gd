extends Control

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


func _on_Button_pressed():
	print("Going back to main menu from New Game menu");
	get_tree().change_scene("res://Scenes/Menus/MainMenu.tscn");


func _on_newCharButton_pressed():
	var newChar = Character.new("TestMan",62,"Man","Man that does that testing!",[1,2,3]);
