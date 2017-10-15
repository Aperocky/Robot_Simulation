echo "Calculating... "


java -jar Robotarium.jar $1 $2 $3
python3 battle_animation.py $3
