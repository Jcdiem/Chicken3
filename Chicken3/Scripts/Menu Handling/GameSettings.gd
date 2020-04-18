extends Node

class GameSettings:
	export var backgroundColor = Color(0,0,0);
	
	func changeColorScheme(backgroundColoredRectangle,r,g,b):
		
		#Background color values (stored for readability)
		var bR = r;
		var bG = g;
		var bB = b;
		
		#Foreground color values (currently not used)
		var fR = abs(r-250);
		var fG = abs(g-250);
		var fB = abs(b-250);
		
		backgroundColoredRectangle.set_frame_color(Color(bR,bG,bB));

	func _init():
		print("New settings sheet created")
