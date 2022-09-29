import openpyxl

#Carregando arquivo
book = openpyxl.load_workbook('Planilha de compras.xlsx')

#Selecionando uma página
frutas_page = book['Frutas']

#Imprir dados de cada linha 
for rows in frutas_page.iter_rows(min_row=2,max_row=5):
    #Modificar valores e nomes dentro da planilha
    for cell in rows:
        if cell.value == 'Banana':
            cell.value == 'Fruta1' 
            
#Salvar alterações
book.save('Planilha de compras v2.xlsx')   

        
        
    