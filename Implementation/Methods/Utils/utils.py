def safe_for_injection(parametre):
    forbidden_words = ["delete", "alter", "create", "select", "where", "from", "drop"]
    for i in forbidden_words:
        if i in parametre.lower():
            return False
    return True
