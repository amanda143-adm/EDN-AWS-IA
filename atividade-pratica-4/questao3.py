def valida_senha(senha):
    if len(senha) < 8:
        return False

    if not any(c.isdigit() for c in senha):
        return False

    return True

senha = input("Digite uma senha: ")
if valida_senha(senha):
    print("Senha válida.")
else:
    print("Senha inválida. A senha deve ter até 8 caracteres, conter pelo menos um número")