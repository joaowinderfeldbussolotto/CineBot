<div align="center">
  <h1>CineBot - Desenvolvimento de um chatbot utilizando o Amazon Lex V2</h1>
</div>

<div align="center">
  <p>Equipe 1</p>

  | Nome                                 | Linkedin                                                                                 |
  | ---------------                      | -------------------------------------------------------------------                      |
  | Cristofer Gaier Sais                 | [Link](https://www.linkedin.com/in/cristofer-sais-a293591a0)                             |
  | João Victor Winderfeld Bussolotto    | [Link](https://www.linkedin.com/in/jo%C3%A3o-victor-winderfeld-bussolotto-aaa914145/)    |
  | Josué Mendonça                       | [Link](https://www.linkedin.com/in/josu%C3%A9-mendon%C3%A7a-dev77/)                      |    
  | Luiz Paulo Grafetti Terres           | [Link](https://www.linkedin.com/in/luiz-paulo-grafetti-terres-aa577a274/)                |      


</div>

***

<a name="ancora"></a>
## 📖 Sumário
- [1 - Objetivo](#ancora1)
  - [1.1 - Tecnologias Utilizadas](#ancora1-1)
- [2 - Desenvolvimento do Projeto](#ancora2)
  - [2.1 - Desenvolvimento da Base de Dados](#ancora2-1)
  - [2.2 - Desenvolvimento das APIs](#ancora2-2)
  - [2.3 - Desenvolvimento do Chatbot com Amazon Lex V2](#ancora2-3)
  - [2.4 - Desenvolvimento das Funções Lambda para Integração com o Chatbot](#ancora2-4)
- [3 - Acesso à Aplicação e Como Utilizá-la](#ancora3)
- [4 - Estrutura de Pastas do Projeto](#ancora4)
- [5 - Arquitetura AWS](#ancora5)
- [6 - Dificuldades conhecidas](#ancora6)
- [7 - Licença](#ancora7)

***
<a id="ancora1"></a>
# 1 - Objetivo

O objetivo principal desta sprint era desenvolver um chatbot utilizando o Amazon Lex V2 e conectá-lo a uma plataforma de mensageria, neste caso, o `Slack`. A equipe se propôs a criar um chatbot chamado `CineBot`, capaz de interagir com clientes de um cinema e mostrar os filmes em cartaz, sessões disponíveis, reservar ingressos e cancelar reservas. O `CineBot` foi projetado para interpretar as intenções dos usuários e, em seguida, invocar funções implementadas no AWS Lambda para atender a essas intenções.
***

<a id="ancora1-1"></a>
- ## 1.1 - Tecnologias Utilizadas

  <div style="display: inline-block" align="center">
    <img align="center" alt="Python" height="30" src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" />
    <img align="center" alt="Git" height="28" width="42" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg">
    <img align="center" alt="AWS" height="28" width="42" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Amazon_Web_Services_Logo.svg/1024px-Amazon_Web_Services_Logo.svg.png" />
    <img align="center" alt="Serverless" height="28" width="42" src="https://assets-global.website-files.com/60acbb950c4d6606963e1fed/611631cd314b2abec6c29ec0_bolt.svg" />
    <img align="center" alt="Amazon API Gateway" height="28" width="42" src="https://d2q66yyjeovezo.cloudfront.net/icon/fb0cde6228b21d89ec222b45efec54e7-0856e92285f4e7ed254b2588d1fe1829.svg" />
    <img align="center" alt="Amazon Lambda" height="28" width="42" src="https://d2q66yyjeovezo.cloudfront.net/icon/945f3fc449518a73b9f5f32868db466c-926961f91b072604c42b7f39ce2eaf1c.svg" />
    <img align="center" alt="Amazon RDS" height="28" width="42" src="https://d2q66yyjeovezo.cloudfront.net/icon/1d374ed2a6bcf601d7bfd4fc3dfd3b5d-c9f69416d978016b3191175f35e59226.svg" />
    <img align="center" alt="Amazon Lex" height="28" width="42" src="https://d2q66yyjeovezo.cloudfront.net/icon/16660b27a03cc547adc54a269bc4a69e-7d762d8739de54214018a7d757540c79.svg" />
        <img align="center" alt="MySQL" height="28" width="42" src="https://www.mysql.com/common/logos/logo-mysql-170x115.png" />



  </div>

***
<a id="ancora2"></a>

# 2 - Desenvolvimento do Projeto

<a id="ancora2-1"></a>

- ## 2.1 - Desenvolvimento da Base de Dados
  A construção do banco de dados MySQL utilizando o `Amazon RDS` foi essencial para o nosso projeto. A tabela "filmes" está relacionada com a tabela "sessoes", permitindo que cada sessão seja associada a um filme específico. A tabela "sessoes" também está relacionada com a tabela "salas", o que permite identificar a sala onde uma sessão ocorrerá. Além disso, as tabelas "reservas" e "poltronas" estão relacionadas através da tabela intermediária "reservas_poltronas" garantindo que cada reserva possa incluir várias poltronas. 

  <div align="center">
    <img src = "./assets/ERRDiagram.png">
  </div>

<a id="ancora2-2"></a>

- ## 2.2 - Desenvolvimento das APIs
  Desenvolvemos APIs utilizando o framework `Serverless`, que foram implantadas como funções Lambdas na AWS e integradas ao `Amazon API Gateway`. Essas APIs desempenham um papel fundamental na relação entre o Banco de Dados MySQL disponibilizado pelo `Amazon RDS` e o `CineBot`. Elas permitem consultas sobre filmes em cartaz, disponibilidade de sessões, reserva de ingressos e cancelamento de reservas, possibilitando uma grande experiência aos usuários ao interagirem com o `CineBot`.

<a id="ancora2-3"></a>

- ## 2.3 - Desenvolvimento do Chatbot com Amazon Lex V2


<a id="ancora2-4"></a>

- ## 2.4 - Desenvolvimento das Funções Lambda para Integração com o Chatbot

 
***

<a id="ancora3"></a>

# 3 - Acesso à Aplicação e Como Utilizá-la 

### **[Link](https://join.slack.com/t/cinebot/shared_invite/zt-230mdlfty-ZnXD1152TADTj6EGxtvNQg)**

Para utilizar o `CineBot` no `Slack`, basta iniciar uma conversa com ele e selecionar uma das intents disponíveis: "Consultar Filmes" para obter informações sobre filmes em exibição, "Reservar Ingressos" para fazer uma reserva, "Sessões Disponíveis" para consultar as sessões disponíveis ou "Cancelar Reserva" para cancelar uma reserva existente. O `CineBot` guiará você através de diálogos e menu interativo, fornecendo respostas rápidas e informações relevantes para facilitar a sua experiência.

<a id="ancora4"></a>

# 4 - Estrutura de Pastas do Projeto

- **bot-backend**
  - **controllers**
    - `movie_controller.py`
    - `reservation_controller.py`
    - `session_controller.py`
  - **core**
    - `config.py`
    - `database.py`
  - **models**
    - `__all_models.py`
    - `Base.py`
    - `Movie.py`
    - `Reservation.py`
    - `ReservationSeat.py`
    - `Room.py`
    - `Seat.py`
    - `Session.py`
  - **services**
    - `movie_service.py`
    - `reservation_service.py`
    - `session_service.py`
  - `.env`
  - `requirements.txt`
  - `serverless.yml`
  - `utils.py`

- **bot-lex-v2**
  - `.env`
  - `config.py`
  - `handleReservation.py`
  - `requirements.txt`
  - `router.py`
  - `serverless.yml`
  - `session.py`  
  - `showMovies.py`  
  - `utils.py`

***

<a id="ancora5"></a>

# 5 - Arquitetura AWS

- ## Banco de Dados: 

  <div align="center">
    <img src = "">
  </div>

- ## APIs: 

  <div align="center">
    <img src = "">
  </div>

- ## CineBot: 

  <div align="center">
    <img src = "">
  </div>

- ## Funções Lambda CineBot: 

  <div align="center">
    <img src = "">
  </div>



***

<a id="ancora6"></a>
# 6 - Dificuldades conhecidas

1. Deploy das funções lambdas com bibliotecas externas.
2. Desenvolvimento da lógica de negócio em relação ao tempo.



<a id="ancora7"></a>
# 7 - Licença

Este projeto está licenciado sob a Licença MIT - consulte o [Link](https://mit-license.org/) para obter mais detalhes.