#!/usr/bin/env python3

# Create scene files with no encoding issues

scenes = {
    "asteroid.tscn": """[gd_scene load_steps=2 format=3]

[ext_resource type="Script" path="res://scripts/asteroid.gd" id="1"]

[sub_resource type="CircleShape2D" id="2"]
radius = 25.0

[node name="Asteroid" type="Area2D"]
script = ExtResource("1")

[node name="CollisionShape2D" type="CollisionShape2D" parent="."]
shape = SubResource("2")

[node name="Polygon2D" type="Polygon2D" parent="."]
color = Color.LIGHT_GRAY
polygon = PackedVector2Array(25, 0, 18, -17, 0, -25, -18, -17, -25, 0, -18, 17, 0, 25, 18, 17)
""",
    "bullet.tscn": """[gd_scene load_steps=2 format=3]

[ext_resource type="Script" path="res://scripts/bullet.gd" id="1"]

[sub_resource type="CircleShape2D" id="2"]
radius = 3.0

[node name="Bullet" type="Area2D"]
script = ExtResource("1")

[node name="CollisionShape2D" type="CollisionShape2D" parent="."]
shape = SubResource("2")

[node name="ColorRect" type="ColorRect" parent="."]
offset_left = -3.0
offset_top = -3.0
offset_right = 3.0
offset_bottom = 3.0
color = Color.YELLOW

[connection signal="area_entered" from="." to="." method="_on_area_entered"]
""",
    "player.tscn": """[gd_scene load_steps=2 format=3]

[ext_resource type="Script" path="res://scripts/player.gd" id="1"]

[sub_resource type="CapsuleShape2D" id="2"]
radius = 8.0
height = 24.0

[node name="Player" type="CharacterBody2D"]
script = ExtResource("1")

[node name="CollisionShape2D" type="CollisionShape2D" parent="."]
shape = SubResource("2")

[node name="Sprite2D" type="Polygon2D" parent="."]
color = Color.WHITE
polygon = PackedVector2Array(0, -15, -10, 10, -5, 5, 5, 5, 10, 10)
""",
    "main.tscn": """[gd_scene load_steps=3 format=3]

[ext_resource type="Script" path="res://scripts/game_manager.gd" id="1"]
[ext_resource type="PackedScene" path="res://scenes/player.tscn" id="2"]

[node name="Main" type="Node2D"]

[node name="GameManager" type="Node2D" parent="."]
script = ExtResource("1")

[node name="Player" parent="." instance=ExtResource("2")]
position = Vector2(512, 300)

[node name="UI" type="CanvasLayer" parent="."]

[node name="ScoreLabel" type="Label" parent="UI"]
offset_left = 10.0
offset_top = 10.0
offset_right = 210.0
offset_bottom = 40.0
text = "Score: 0"

[node name="LivesLabel" type="Label" parent="UI"]
anchors_left = 0.5
anchors_right = 0.5
offset_left = -100.0
offset_top = 10.0
offset_right = 100.0
offset_bottom = 40.0
text = "Lives: 3"

[node name="WaveLabel" type="Label" parent="UI"]
anchors_left = 1.0
anchors_right = 1.0
offset_left = -210.0
offset_top = 10.0
offset_right = -10.0
offset_bottom = 40.0
text = "Wave: 1"

[node name="GameOverLabel" type="Label" parent="UI"]
anchors_left = 0.5
anchors_top = 0.5
anchors_right = 0.5
anchors_bottom = 0.5
offset_left = -150.0
offset_top = -50.0
offset_right = 150.0
offset_bottom = 50.0
text = "GAME OVER"
"""
}

for filename, content in scenes.items():
    with open(f"c:/projects/trash-driods/scenes/{filename}", "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print(f"Created {filename}")
