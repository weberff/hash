from hashlib import sha256

hash = sha256(b"fa826abbb817e3932b11111111c05a892440ee62572bd1e3c16cffbff4531c88").hexdigest()
rodada = 180940076
count = 0

while 1:
	x = hash.find("11111111")
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
