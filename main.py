from classes import Site_csa
import csv


menssagem_para_formulario="""Gostaria de fazer parte do grupo CSA por enxergar uma oportunidade 
                             evoluir como profissional à medida que contribuo nas atividades e no
                             desenvolvimento da empresa."""

bot=Site_csa()
bot.iniciar_navegador()
bot.acessar_seguimentos("blog")
bot.carregar_all_news()

informacoes_noticias=bot.get_informacoes()
with open('infor.csv', mode='w', newline='') as csv_file:
    
    fieldnames = ["titulo","data","resumo","url"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for c in informacoes_noticias:
        writer.writerow(c)

    print("Informações salvas!")

enviar_formulario=bot.formulario("Edno","9899054639","CSA","hotmail.com",menssagem_para_formulario,"Vaga para Dev","http://www.csa-ma.com.br/")
if enviar_formulario!=True:
    print("Erro de validacao dos dados!")
else:
    print("Formulario enviado!")

bot.close_driver()

