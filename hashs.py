from hashlib import sha256

hash0 = sha256(b"0000000000000000000000000000000000000000000000000000000000000000").hexdigest()
hash1 = sha256(b"1111111111111111111111111111111111111111111111111111111111111111").hexdigest()
rodada = 1
count = 1

while 1:
	x = hash0.find("00000000")
	y = hash1.find("11111111")
	if x > -1 and y > -1:
		print(f"Encontrou na rodada: {rodada}\nHash0 é: {hash0}\nHash1 é: {hash1}\n")
		break
	else:
		rodada = rodada + 1
		count = count + 1
		hash0 = sha256(hash0.encode("ascii")).hexdigest()
		hash1 = sha256(hash1.encode("ascii")).hexdigest()
		if count >= 10000000:
			print(f"Fazer Backup. Rodada Atual é: {rodada}\nHash0 é: {hash0}\nHash1 é: {hash1}\n")
			count = 0
