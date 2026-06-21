extends CharacterBody2D

@export var speed: float = 200.0

func _ready():
	print("Player loaded!")

func _physics_process(delta):
	# Simple movement for testing
	velocity = Vector2.ZERO
	
	if Input.is_action_pressed("ui_right"):
		velocity.x += speed
	if Input.is_action_pressed("ui_left"):
		velocity.x -= speed
	if Input.is_action_pressed("ui_down"):
		velocity.y += speed
	if Input.is_action_pressed("ui_up"):
		velocity.y -= speed
	
	move_and_slide()
