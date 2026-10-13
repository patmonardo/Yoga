for chapter in $(seq 1 8); do
	echo "$chapter"
	./build.sh --chapter "$chapter" --kind karika
	./build.sh --chapter "$chapter" --kind bhasya
done
