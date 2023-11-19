def writefilescans(url: str, frameworks: dict, directories: list, file_name: str):
    with open(f"{file_name}.txt", "at") as file:
        # Escrever a URL do site no arquivo
        file.write(f"URL: {url}\n\n")
        
        for framework, details in frameworks.items():
            # Escrever informações sobre cada framework
            file.write(f"Framework: {framework}\n")
            file.write(f"Version: {details['version']}\n")
            file.write(f"Exist: {details['exist']}\n\n")

            # Verificar se há plugins e temas e escrever no arquivo
            if details['plugins'] is not None:
                file.write("Plugins:\n")
                for plugin in details['plugins']:
                    file.write(f"- {plugin}\n")

            if details['themes'] is not None:
                file.write("Themes:\n")
                for theme in details['themes']:
                    file.write(f"- {theme}\n")

            file.write("\n")  # Adicionar linha em branco entre as frameworks

        # Escrever informações sobre os diretórios
        file.write("Directories:\n")
        for directorie in directories:
            file.write(f"- {directorie}\n")

        file.write("\n")  # Adicionar linha em branco entre os diretórios

        file.close()