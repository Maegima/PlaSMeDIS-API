from configuration.configuration import flaskApp

class Usuario(flaskApp.db.Model):
    __tablename__ = 'usuarios'
    id = flaskApp.db.Column(flaskApp.db.Integer, primary_key=True)
    real_name = flaskApp.db.Column(flaskApp.db.String(80), nullable=False)
    user_name = flaskApp.db.Column(flaskApp.db.String(80), unique=True, nullable=False)
    password = flaskApp.db.Column(flaskApp.db.String(80), nullable=False)
    email = flaskApp.db.Column(flaskApp.db.String(120), unique=True, nullable=True)
    verificado = flaskApp.db.Column(flaskApp.db.Boolean, default=False, nullable=False)
    sexo = flaskApp.db.Column(flaskApp.db.String(1), nullable=True)
    nascimento = flaskApp.db.Column(flaskApp.db.String(20), nullable=True)
    cor = flaskApp.db.Column(flaskApp.db.String(10), nullable=True)
    telefone = flaskApp.db.Column(flaskApp.db.String(20), nullable=True)
    rua = flaskApp.db.Column(flaskApp.db.String(100), nullable=True)
    numero_casa = flaskApp.db.Column(flaskApp.db.Integer, nullable=True)
    data_registro = flaskApp.db.Column(flaskApp.db.DateTime, nullable=True)
    bairro = flaskApp.db.Column(flaskApp.db.Integer, flaskApp.db.ForeignKey('bairros.id'), nullable=False)
    user_type = flaskApp.db.Column(flaskApp.db.Integer, flaskApp.db.ForeignKey('privilegios.id'), nullable=False)

    def __init__(self, real_name, password, user_name, user_type, bairro):
        import datetime
        self.real_name = real_name
        self.password = password
        self.verificado = False
        self.user_name = user_name
        self.user_type = user_type
        self.data_registro = datetime.datetime.now()
        self.bairro = bairro

class Privilegio(flaskApp.db.Model):
    __tablename__ = 'privilegios'
    id = flaskApp.db.Column(flaskApp.db.Integer, primary_key=True)
    user_type = flaskApp.db.Column(flaskApp.db.String(80), unique=True, nullable=False)

    def __init__(self, user_type):
        self.user_type = user_type

class Bairro(flaskApp.db.Model):
    __tablename__ = 'bairros'
    id = flaskApp.db.Column(flaskApp.db.Integer, primary_key=True)
    nome = flaskApp.db.Column(flaskApp.db.String(80), unique=True, nullable=False)

    def __init__(self, nome):
        self.nome = nome

class Postagem(flaskApp.db.Model):
    __tablename__ = 'postagens'
    id = flaskApp.db.Column(flaskApp.db.Integer, primary_key=True)
    titulo = flaskApp.db.Column(flaskApp.db.String(400), nullable=False)
    texto = flaskApp.db.Column(flaskApp.db.String(400), nullable=False)
    criador = flaskApp.db.Column(flaskApp.db.Integer, flaskApp.db.ForeignKey('usuarios.id'), nullable=False)
    categoria = flaskApp.db.Column(flaskApp.db.Integer, flaskApp.db.ForeignKey('categorias.id'), nullable=False)
    selo = flaskApp.db.Column(flaskApp.db.Boolean, default=False, nullable=False)

    def __init__(self, titulo, texto, criador, categoria):
        self.titulo = titulo
        self.texto = texto
        self.criador = criador
        self.categoria = categoria

class Categoria(flaskApp.db.Model):
    __tablename__ = 'categorias'
    id = flaskApp.db.Column(flaskApp.db.Integer, primary_key=True)
    nome = flaskApp.db.Column(flaskApp.db.String(80), unique=True, nullable=False)

    def __init__(self, nome):
        self.nome = nome

class Comentario(flaskApp.db.Model):
    __tablename__ = 'comentarios'
    id = flaskApp.db.Column(flaskApp.db.Integer, primary_key=True)
    texto = flaskApp.db.Column(flaskApp.db.String(400), nullable=False)
    criador = flaskApp.db.Column(flaskApp.db.Integer, flaskApp.db.ForeignKey('usuarios.id'), nullable=False)
    postagem = flaskApp.db.Column(flaskApp.db.Integer, flaskApp.db.ForeignKey('postagens.id'), nullable=False)
    resposta = flaskApp.db.Column(flaskApp.db.Integer, flaskApp.db.ForeignKey('comentarios.id'), nullable=True)

    def __init__(self, texto, criador, postagem, resposta):
        self.texto = texto
        self.criador = criador
        self.postagem = postagem
        self.resposta = resposta

class Form_Socioeconomico(flaskApp.db.Model):
    __tablename__ = 'form_socioeconomico'
    id = flaskApp.db.Column(flaskApp.db.Integer, primary_key=True)
    nome_rep_familia = flaskApp.db.Column(flaskApp.db.String(100), nullable=False)
    pessoa = flaskApp.db.Column(flaskApp.db.Integer, flaskApp.db.ForeignKey('usuarios.id'), nullable=False)
    qtd_pessoas_familia = flaskApp.db.Column(flaskApp.db.Integer, nullable=False)
    qtd_criancas = flaskApp.db.Column(flaskApp.db.Integer, nullable=False)
    gestante = flaskApp.db.Column(flaskApp.db.Boolean, nullable=False)
    qtd_amamentando = flaskApp.db.Column(flaskApp.db.Integer, nullable=False)
    qtd_criancas_deficiencia = flaskApp.db.Column(flaskApp.db.Integer, nullable=False)
    preenchido = flaskApp.db.Column(flaskApp.db.Boolean, nullable=False, default="False")
    pessoa_amamenta = flaskApp.db.Column(flaskApp.db.Boolean, nullable=False, default="False")
    qtd_gestantes = flaskApp.db.Column(flaskApp.db.Integer, nullable=False)
    def __init__(self, nome_rep_familia, pessoa, qtd_pessoas_familia, qtd_criancas, gestante, qtd_amamentando, qtd_criancas_deficiencia, qtd_gestantes, pessoa_amamenta):
        self.nome_rep_familia = nome_rep_familia
        self.pessoa = pessoa
        self.qtd_pessoas_familia = qtd_pessoas_familia
        self.qtd_criancas = qtd_criancas
        self.gestante = gestante
        self.qtd_amamentando = qtd_amamentando
        self.qtd_criancas_deficiencia = qtd_criancas_deficiencia
        self.qtd_gestantes = qtd_gestantes
        self.pessoa_amamenta = pessoa_amamenta
        self.preenchido = True
