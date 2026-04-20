extends Node2D

signal health_changed(new_health)
signal character_died

@export var max_health: int = 100
var current_health: int:
	set(value):
		current_health = clampi(value, 0, max_health)
		health_changed.emit(current_health)
		if current_health <= 0:
			character_died.emit()

func _ready() -> void:
	current_health = max_health
	health_changed.connect(_on_health_changed)
	character_died.connect(_on_character_died)
	
	print("キャラクター準備完了。HP: ", current_health)
	take_damage(30)
	take_damage(80)

func take_damage(amount: int) -> void:
	print(amount, " のダメージを受けた！")
	current_health -= amount

func _on_health_changed(new_health: int) -> void:
	print("現在のHPが ", new_health, " に更新されました。")

func _on_character_died() -> void:
	print("キャラクターが死亡しました。ゲームオーバー。")
