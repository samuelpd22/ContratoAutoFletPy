
from flet import *
from docx import Document

#WORD




def main(page):
    page.window_width = 400
    page.window_height = 600
    page.update()

    dict_values = {
        'contratante' :'',
        'medida_judicial':'',
        'outra_parte':'',
        'prolabore':'',
        'honorario':'',
        'comarca':'',
        'data':''
    }
    def fecha_banner(e):
        page.banner.open=False
        page.update()


    def gera_contrato(e):
        dict_values['contratante'] = contratante.value
        dict_values['medida_judicial'] = medida_judicial.value
        dict_values['outra_parte'] = outra_parte.value
        dict_values['prolabore'] = prolabore.value
        dict_values['honorario'] = honorario.value
        dict_values['comarca'] = comarca.value
        dict_values['data'] = data.value

        for val in dict_values.values():
            if not val:
                page.banner.open=True
                page.update()
                return
        print("Já e possivel criar o contrato")

        criar_contrato(dict_values)

    def criar_contrato(dados_cliente):
        # Carrega o modelo de contrato existente
        
        document = Document("./contrato.docx")

        # Preenche o documento com os dados do cliente
        for paragraph in document.paragraphs:
            for key, value in dados_cliente.items():
                if key in paragraph.text:
                    paragraph.text = paragraph.text.replace(key, value)

        # Salva o documento preenchido
        nome_arquivo_saida = "./contrato_preenchido.docx"
        document.save(nome_arquivo_saida)
        print(f"Contrato salvo como '{nome_arquivo_saida}'")
    


    page.banner = Banner(
        bgcolor=colors.AMBER_100,
        leading=Icon(
            icons.DANGEROUS_SHARP,
            color=colors.RED_400,
            size=40
        ),
        content=Text("Opa! Preencha todos os campos.", color="black"),
        actions=[
            TextButton("Entendi",on_click=fecha_banner)
        ]
    )



    titulo = Text(value='Gerador de Contrato', size=20,weight='bold')

    contratante = TextField(label="Nome do Contratante")
    medida_judicial = TextField(label="Medida Judicial")
    outra_parte = TextField(label="Nome do Reu")
    prolabore = TextField(label="Prolabore", prefix_text='R$ ')
    honorario = TextField(label="Porcentagem", suffix_text=' %')
    comarca = TextField(label="Comarca")
    data = TextField(label="Data")
    botao_gerar = FilledButton(text="Gerar Contrato", on_click=gera_contrato)

    page.add(
       Row(
            controls=[
                titulo,
            ]
       ),
        Row(
            controls=[
                contratante,
                
            ]
       ),
       Row(
            controls=[
                medida_judicial
            ]
       ),
        Row(
            controls=[
                outra_parte
            ]
       ),
        Row(
            controls=[
                prolabore
            ]
       ),
        Row(
            controls=[
                honorario
            ]
       ),
        Row(
            controls=[
                comarca
            ]
       ),
        Row(
            controls=[
                data
            ]
       ),
        Row(
            controls=[
                botao_gerar
            ]
       )
    )
    



app(target=main)

