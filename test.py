def format_text(text, color):
    colors = {
        'verde': '\033[32m',
        'vermelho': '\033[31m',
        'reset': '\033[0m'
    }
    return f"{colors[color]}{text}{colors['reset']}"

print(format_text("O acesso à categoria 'Todos' foi bem-sucedido!", 'verde'))
print(format_text("-► Item 'roupateste' encontrado na categoria 'Todos'", 'verde'))
print(format_text("-► Item 'Cal' encontrado na categoria 'Todos'", 'verde'))
print(format_text("-► Item 'Oculos SP' encontrado na categoria 'Todos'", 'verde'))
print(format_text("-► Item 'Miçanga BA' encontrado na categoria 'Todos'", 'verde'))
print('')

print(format_text("O acesso à categoria 'Roupas' foi bem-sucedido!", 'verde'))
print(format_text("-► Item 'roupateste' encontrado na categoria 'Roupas'", 'verde'))
print('')

print(format_text("O acesso à categoria 'Calçados' foi bem-sucedido!", 'verde'))
print(format_text("-► Item 'Cal' não encontrado na categoria 'Calçados'", 'vermelho'))
print('')

print(format_text("O acesso à categoria 'Acessórios' foi bem-sucedido!", 'verde'))
print(format_text("-► Item 'Oculos SP' não encontrado na categoria 'Acessórios'", 'vermelho'))
print(format_text("-► Item 'Miçanga BA' não encontrado na categoria 'Acessórios'", 'vermelho'))
print('')

print(format_text("O acesso à categoria 'Elemento Inexistente' não foi bem-sucedido! (Categoria não encontrada)", 'vermelho'))
print(format_text("-► Item 'Acesorio3(nao existe)' não encontrado na categoria 'Todos'", 'vermelho'))
print('')
