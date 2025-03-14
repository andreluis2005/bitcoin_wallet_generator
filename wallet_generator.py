from bitcoinlib.keys import Key

# Gerar chave privada e endereço Bitcoin
key = Key()

# Exibir informações
print("🚀 Carteira Bitcoin Gerada com Sucesso!")
print(f"🔑 Chave Privada: {key.wif}")
print(f"🏦 Endereço Bitcoin: {key.address}")

# Salvar em um arquivo
with open("bitcoin_wallet.txt", "w") as file:
    file.write(f"Chave Privada: {key.wif}\n")
    file.write(f"Endereço Bitcoin: {key.address}\n")

print("📄 Dados salvos em 'bitcoin_wallet.txt'")
