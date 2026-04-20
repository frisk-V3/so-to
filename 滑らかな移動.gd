extends CharacterBody2D

@export var max_speed: float = 300.0
@export var acceleration: float = 1200.0
@export var friction: float = 800.0

func _physics_process(delta: float) -> void:
	var input_vector := Vector2.ZERO
	input_vector.x = Input.get_axis("ui_left", "ui_right")
	input_vector.y = Input.get_axis("ui_up", "ui_down")
	input_vector. = input_vector.normalized()

	if input_vector != Vector2.ZERO:
		# 加速処理
		velocity = velocity.move_toward(input_vector * max_speed, acceleration * delta)
	else:
		# 摩擦による停止
		velocity = velocity.move_toward(Vector2.ZERO, friction * delta)

	move_and_slide()
	
	# 画面外に出ないように制限する処理
	var screen_size = get_viewport_rect().size
	position.x = clamp(position.x, 0, screen_size.x)
	position.y = clamp(position.y, 0, screen_size.y)
