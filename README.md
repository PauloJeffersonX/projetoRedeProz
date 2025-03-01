# Projeto: Instância EC2 para a Banda do Miguel

## Descrição

Este projeto consiste na criação e configuração de uma instância Amazon EC2 para a banda do Miguel, com o objetivo de armazenar e gerenciar sua documentação e arquivos importantes na nuvem.  Utilizamos o Amazon Linux 2 como sistema operacional e exploramos recursos como Elastic Block Storage (EBS) para gerenciamento de armazenamento.

## Objetivos

*   Criar uma instância EC2 com Amazon Linux 2.
*   Conectar-se à instância via SSH.
*   Criar e anexar um volume EBS à instância.
*   Formatar e montar o volume EBS em um diretório específico.
*   Criar um arquivo de texto no volume montado.
*   Verificar o status do volume, espaço em disco e conteúdo do arquivo.

## Passos Realizados

1.  **Configuração da Instância EC2:**
    *   Acessamos o Console da AWS e navegamos até o serviço EC2.
    *   Criamos uma nova instância EC2 utilizando a imagem Amazon Linux 2.
    *   Escolhemos um tipo de instância adequado às necessidades de recursos. (Ex: t2.micro)

2.  **Conexão via SSH:**
    *   Após a criação da instância, utilizamos a chave privada (.pem) para conectar via SSH.
    *   Executamos o comando SSH para acessar o terminal da instância:

        ```bash
        ssh -i "sua_chave.pem" ec2-user@<seu_endereco_ip_publico>
        ```

3.  **Gerenciando o Armazenamento:**
    *   Exploramos as opções de armazenamento oferecidas pelo Amazon EC2.
    *   Criamos um novo volume Elastic Block Storage (EBS) com um tamanho de 8GB.
    *   Anexamos o volume à instância EC2. (Observar o nome do dispositivo. Ex: /dev/xvdf)

4.  **Formatando e Montando o Volume:**
    *   Formatamos o volume recém-criado utilizando o sistema de arquivos ext4:

        ```bash
        sudo mkfs -t ext4 /dev/xvdf
        ```
        (Substitua `/dev/xvdf` pelo nome do dispositivo correto)

    *   Criamos um diretório para montar o volume:

        ```bash
        sudo mkdir /data
        ```

    *   Montamos o volume no diretório criado:

        ```bash
        sudo mount /dev/xvdf /data
        ```
        (Substitua `/dev/xvdf` pelo nome do dispositivo correto)

    * Teste a montagem:
    ```bash
    sudo mount -a
    ```

5.  **Criação de Arquivos:**
    *   Criamos um arquivo de texto simples utilizando o editor `nano`:

        ```bash
        sudo nano /data/lista_de_musicas.txt
        ```

    *   Adicionamos algumas músicas à lista e salvamos o arquivo.

6.  **Explorando Recursos:**
    *   Utilizamos os seguintes comandos para verificar o status do volume montado, o espaço em disco disponível e o conteúdo do arquivo criado:

        ```bash
        ls -l /data
        df -h
        mount | grep /data
        cat /data/lista_de_musicas.txt
        ```

## Resultados

O resultado final foi a criação de uma instância EC2 funcional com um volume EBS montado, onde a banda do Miguel pode armazenar e gerenciar seus arquivos.  O print da tela com a execução dos comandos no passo 6 foi incluído como comprovação.

## Considerações Finais

*   É importante lembrar de interromper ou encerrar a instância EC2 após o uso para evitar custos adicionais.
*   Este projeto serviu como uma introdução ao Amazon EC2 e EBS, e pode ser expandido para incluir outros serviços da AWS, como S3 para backup e CloudWatch para monitoramento.
*   A segurança da instância deve ser considerada, configurando regras de firewall adequadas e gerenciando as chaves SSH de forma segura.
