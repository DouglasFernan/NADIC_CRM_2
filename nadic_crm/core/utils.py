def is_founder(user):
    # Verifique se o usuário está autenticado e se pertence ao grupo "Fundador"
    return user.is_authenticated and user.groups.filter(name='Fundador').exists()
