import flet as ft
import sql_funcoes as sf


def main(page: ft.Page):
    

    db = "agenda.db"
    
    sf.criarTabelaContatos(db)

    #Funcoes dos botoes dos menus
    def on_keyboard_event(e):
        if e.key == 'Enter' and body.content == bodyInserir:
            if len(cxNome.value) != 0 and len(cxSobrenome.value) != 0 and len(cxEmail.value) != 0:
                inserirDadosBtn(e)
    
    def ativarBtnInserir(e):
        txtCadastroOk.visible = False
        if len(cxNome.value) != 0 and len(cxSobrenome.value) != 0 and len(cxEmail.value) != 0:
            btnInserir.disabled = False
        else:
            btnInserir.disabled = True
            #txtCadastroOk.visible = True
            
        page.update()
            
        

    def inserirDadosBtn(e):
        
        sf.inserirDados(db,cxNome.value, cxSobrenome.value, cxEmail.value)
        
        cxNome.value = ""
        cxSobrenome.values = ""
        cxEmail.value = ""
        
        txtCadastroOk.visible = True
        
        page.update()
    
    def atualizarDadosBtn(e):
        sf.atualizarDados(
            db,
            cxNome.value,
            cxSobrenome.value,
            cxEmail.value,
            cxId.value)
        
        cxNome.value = ""
        cxSobrenome.value = ""
        cxEmail.value = ""
        
        txtCadastroOk.visible = True
        
        page.update()
    
    def apagarDadosBtn(e):
        
        sf.apagarDados(db,cxId.value)
    
    def consultarIdBtn(e):
        dados = sf.selecionarDadosId(db,cxId.value)
        
        if dados:
            dado = dados[0]
            
            cxNome.value = dado[1]
            cxSobrenome.value = dado[2]
            cxEmail.value = dado[3]
        else:
            cxNome.value = ""
            cxSobrenome.value = ""
            cxEmail.value = ""  
        
        page.update()         
    # ------------ Componentes (OBjetos)
    
    txtCadastroOk = ft.Container(
        ft.Text("Cadstro Realizado com sucesso"),
        bgcolor=ft.colors.GREEN,
        padding=10,
        alignment=ft.alignment.center,
        visible=False
    )
    
    #ID
    txtId = ft.Text("ID")
    cxId = ft.TextField(
        label="Digite o seu ID",
        text_align=ft.TextAlign.LEFT,
    )
    #Nome
    txtNome = ft.Text("Nome")
    cxNome = ft.TextField(
        label="Digite o nome da pessoa",
        text_align=ft.TextAlign.LEFT,
        on_change=ativarBtnInserir
    )

    #Sobrenome
    txtSobrenome = ft.Text("Sobrenome")
    cxSobrenome = ft.TextField(
        label="Digite o Sobrenome da pessoa",
        text_align=ft.TextAlign.LEFT,
        on_change=ativarBtnInserir
    )
    
    #Email
    txtEmail = ft.Text("Email")
    cxEmail = ft.TextField(
        label="Digite o Email da pessoa",
        text_align=ft.TextAlign.LEFT,
        on_change=ativarBtnInserir
    )
    
    #Botoes
    btnInserir = ft.ElevatedButton("Cadastar", disabled=True, on_click=inserirDadosBtn)
    
    btnAtualizar = ft.ElevatedButton("Atualizar", on_click=atualizarDadosBtn)
    
    btnApagar = ft.ElevatedButton("Apagar", on_click=apagarDadosBtn)
    
    btnConsultar = ft.ElevatedButton("Consultar", on_click=consultarIdBtn)
    
    
    
    bodyInicial = ft.Text(
        "Seja Bem vindo ao Programa de Agenda de Clientes"
    )
    
    bodyInserir = ft.Column(
        [
            txtNome,
            cxNome,
            txtSobrenome,
            cxSobrenome,
            txtEmail,
            cxEmail,
            btnInserir,
            txtCadastroOk
        ],
    )
    
    bodyApagar = ft.Column([
            txtId,
            cxId,
            btnConsultar,
            txtNome,
            cxNome,
            txtSobrenome,
            cxSobrenome,
            txtEmail,
            cxEmail,
            btnApagar
    ],)
    
    bodyAtualizar = ft.Column([
            txtId,
            cxId,
            btnConsultar,
            txtNome,
            cxNome,
            txtSobrenome,
            cxSobrenome,
            txtEmail,
            cxEmail,
            btnAtualizar
    ],)

    
    def menuInserir(e):
        body.content = bodyInserir
        page.update()
        
        
    def menuApagar(e):
        body.content = bodyApagar
        page.update()
        
        
    def menuAtualizar(e):
        body.content = bodyAtualizar
        page.update()
        
    def menuSelecionarDados(e):
        dados = sf.selecionarTodosDados(db)
        bodyListaDados = ft.Column()
        
        for dado in dados:
            bodyListaDados.controls.append(
                ft.Row(
                        [
                        ft.Container(
                            ft.Text(dado[0]),
                            bgcolor=ft.colors.GREY,
                            border_radius=10,
                            padding = 15,
                            margin = 3,
                            width= 50        
                                    ),
                        ft.Container(
                            ft.Text(dado[1]),
                            bgcolor=ft.colors.GREY,
                            border_radius=10,
                            padding = 15,
                            margin = 3,
                            width= 250        
                                    ),
                        ft.Container(
                            ft.Text(dado[2]),
                            bgcolor=ft.colors.GREY,
                            border_radius=10,
                            padding = 15,
                            margin = 3,
                            width= 250        
                                    ),
                        ft.Container(
                            ft.Text(dado[3]),
                            bgcolor=ft.colors.GREY,
                            border_radius=10,
                            padding = 15,
                            margin = 3,
                            width= 500        
                            ),
                    ]
                )
            )
            
        body.content = bodyListaDados
        page.update()
            
    page.on_keyboard_event = on_keyboard_event
    #menu de opções
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.DATASET),
        leading_width=100,
        title=ft.Text("Agenda de Clientes"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.ADD, on_click=menuInserir),   # INSERIR DADOS
            ft.IconButton(ft.icons.REMOVE, on_click=menuApagar), # APAGAR DADOS0
            ft.IconButton(ft.icons.UPDATE, on_click=menuAtualizar), # ATUALIZAR DADOS
            ft.IconButton(ft.icons.LIST_ALT_SHARP, on_click=menuSelecionarDados), #SELECIONAR TODOS
        ]
        
    )

    # Corpo Principal - Body
    body = ft.Container(
        content=bodyInicial
    )

    #Parte central da tela
    page.add(
        body
    )

ft.app(target=main)