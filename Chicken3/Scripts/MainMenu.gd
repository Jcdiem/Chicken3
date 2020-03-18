extends Control



# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_newGameBtn_pressed():
	print("Starting a new game");

func _on_loadGameBtn_pressed():
	print("Showing load game menu");

func _on_settingsBtn_pressed():
	print("Showing settings menu");
	get_tree().change_scene("res://Scenes/Menus/SettingsMainMenu.tscn");
	

func _on_exitBtn_pressed():
	print("Quitting game from menu");
	get_tree().quit();
