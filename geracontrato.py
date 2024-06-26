
from flet import *

def main(page):
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
    data = TextField(label="XX/XX/XXXX")
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

