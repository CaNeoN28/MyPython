cid = input('Informe o nome de uma cidade : ')
cid = cid.strip()
cid = cid.lower()

print('Começa com Santo : {}'.format('santo' in cid.split()[0]))
