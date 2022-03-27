from hashlib import sha256

hash = sha256(b"9ba625062944a00000000dbb732f62d5f2c5adebe3fa39d5ebeba1fff18f11bf").hexdigest()
rodada = 416471300
count = 0

while 1:
	x = hash.find("00000000")
	if x > -1:
		print(f"Encontrou na rodada: {rodada}\nHash é: {hash}")
		break
	else:
		rodada = rodada + 1
		count = count + 1
		hash = sha256(hash.encode("ascii")).hexdigest()
		if count >= 10000000:
			print(f"Rodada Atual é: {rodada}")
			count = 0
