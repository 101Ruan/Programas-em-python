import os
i = 0
while True:
	open(f"argv{i}.txt", "w").write("worm detected!")
	i += 1