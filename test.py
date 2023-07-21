def format_description(description):
        text = description
        lines = description.split('\n')
        if len(lines) < 2:
            for i in range(len(description)//55):
                if (i + 1)*55 < len(description):
                    lines.append(text[i*55: (i + 1)*55 ])
                else:
                    lines.append(text[i*55:])
        print(lines)
        if len(description) > 55:
            last_space_index = text[:55].rfind(' ')
            if last_space_index == -1:
                text = description[:55] + '\n' + description[55:]  
            else:
                text = text[:last_space_index] + '\n' + text[last_space_index + 1:]
        return text


a = 'Mais uma vez copiando a descrição para tentar formatá-la no código desse aplicativo lindo chamado milafoods. agora estou tmb assistindo instagram aqui do lado, enfim'
print(format_description(a))
