extends Node


# Declare member variables here. Examples:
var backgroundColor = Color(0,0,0);

func changeColorScheme(backgroundColoredRectangle,r,g,b):
	#Background color values
	var bR = r;
	var bG = g;
	var bB = b;
	
	#Foreground color values
	var fR = abs(r-250);
	var fG = abs(g-250);
	var fB = abs(b-250);
	
	backgroundColoredRectangle.set_frame_color(Color(r,g,b));


# Called when the node enters the scene tree for the first time.
func _ready():
	changeColorScheme(get_node('Background'),0,0,0);

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
