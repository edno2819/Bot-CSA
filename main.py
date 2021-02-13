from classes import Site_csa
import csv


menssagem_para_formulario="""Gostaria de fazer parte do grupo CSA por enxergar uma oportunidade 
                             evoluir como profissional à medida que contribuo nas atividades e no
                             desenvolvimento da empresa."""

a=Site_csa()
a.iniciar_navegador()
a.acessar_seguimentos("blog")
a.carregar_all_news()

informacoes_noticias=a.get_informacoes()
with open('infor.csv', mode='w', newline='') as csv_file:
    
    fieldnames = ["titulo","data","resumo","url"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for c in informacoes_noticias:
        writer.writerow(c)

    print("Informações salvas!")

enviar_formulario=a.formulario("Edno","9899054639","CSA","hotmail.com",menssagem_para_formulario,"Vaga para Dev","http://www.csa-ma.com.br/")
if enviar_formulario!=True:
    print("Erro de validacao dos dados!")
else:
    print("Formulario enviado!")

a.close_driver()

