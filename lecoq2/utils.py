from datetime import datetime

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer,Image
from django.http import HttpResponse



def format_numero(value):
    return f'{value:.0f}'

def format_decimal2(value):
    return f'R$ {value:.2f}'

from babel.numbers import format_currency

def format_decimal(value):
    formatted_value = format_currency(value, 'BRL', locale='pt_BR')
    return formatted_value

def gerar_pdf_pedido(pedido):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="pedido_{pedido.cod_cliente.nome}_{pedido.data_entrega}.pdf"'

    doc = SimpleDocTemplate(response, pagesize=letter,topMargin=10)
    story = []

    """custom_style = ParagraphStyle(
        name='CustomStyle',
        fontName='Helvetica-Bold',  # Nome da fonte em negrito
        fontSize=12,  # Tamanho da fonte
        alignment=1,  # Alinhamento (0=esquerda, 1=centro, 2=direita)
        textColor=colors.blue,  # Cor do texto
        leading=14,  # Espaçamento entre linhas
        spaceAfter=6,  # Espaçamento após o parágrafo
        leftIndent=12,  # Recuo à esquerda
        rightIndent=12,  # Recuo à direita
        backColor=colors.yellow,  # Cor de fundo do parágrafo
        bulletFontName='Helvetica',  # Nome da fonte para marcadores
        bulletFontSize=12,  # Tamanho da fonte para marcadores
        bulletIndent=12,  # Recuo dos marcadores
        bulletColor=colors.red,  # Cor dos marcadores
        spaceBefore=6,  # Espaçamento antes do parágrafo
        bulletOffsetY=-2,  # Ajuste vertical dos marcadores
        wordWrap='LTR',  # Quebra de linha
        allowWidows=1,  # Permitir viúvas (última linha de um parágrafo no topo da página)
        allowOrphans=1  # Permitir órfãos (primeira linha de um parágrafo no final da página)
    )"""



    style_custom = ParagraphStyle(
        name='CustomStyle',
        fontName='Helvetica-Bold',  # Nome da fonte
        fontSize=14,  # Tamanho da fonte
        alignment=2,
        textColor=colors.red  # Cor do texto
    )

    styles = getSampleStyleSheet()
    style_title = styles['Title']
    style_head1 = styles['Heading1']
    style_head2 = styles['Heading2']
    style_head3 = styles['Heading3']
    style_head4 = styles['Heading4']
    style_bullet= styles['Bullet']
    style_deff  = styles['Definition']
    style_code  = styles['Code']
    style_right = ParagraphStyle(name='RightStyle', alignment=2)  # 2 corresponde à direita

    data_hora_atual     = datetime.now()
    data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
    data_pedido     = pedido.data_entrega
    data_pedido_fmt = data_pedido.strftime("%d/%m/%Y")

    story.append(Paragraph(f"{data_hora_formatada}", style_right))

    style_image = ParagraphStyle(
        name='ImageStyle',
        alignment=1,  # Alinhamento (0=esquerda, 1=centro, 2=direita)
    )

    logo_path = 'http://zuca.site/image/LogoBrancaLeCoqGrande.jpg'
    logo = Image(logo_path, width=240, height=90)
    logo.hAlign = 'LEFT'  # Alinhar a imagem à esquerda
    story.append(logo)
    espaco = Spacer(1, 20)
    story.append(espaco)

    story.append(Paragraph(f"Cliente .: {pedido.cod_cliente.nome} ", style_head2))
    story.append(
        Paragraph(f"Data do Pedido .: {data_pedido_fmt}        - Responsável .: {pedido.cod_cliente.responsavel}",
                  style_head2))

    espaco = Spacer(1, 20)  # Altura do espaço em branco (em pontos)
    story.append(espaco)

    data = [['             Produto             ', ' Qtd ',  ' Devolução ', 'Qtd Cobrazado','   Preço   ', '  Sub Total  ']]

    for item in pedido.itenspedido_set.all():
        qtde       = format_numero(item.quantidade)
        qtde_dev   = format_numero(item.quantidade_dev)
        qtde_total = format_numero(item.quantidade-item.quantidade_dev)
        preco      = format_decimal(item.preco)
        subtotal   = format_decimal(item.quantidade*item.preco)

        data.append([item.cod_prod.nome, qtde, qtde_dev, qtde_total, preco, subtotal])
    altura_linha = 20
    table = Table(data)
    style_table = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                              ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                              ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                              ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                              ('FONTSIZE', (0, 0), (-1, 0), 12),
                              ('FONTSIZE', (0, 1), (-1, 1), 12),
                              ('FONTSIZE', (0, 2), (-1, 2), 12),
                              ('FONTSIZE', (0, 3), (-1, 3), 12),
                              ('FONTSIZE', (0, 4), (-1, 4), 12),
                              ('FONTSIZE', (0, 5), (-1, 5), 12),
                              ('FONTSIZE', (0, 6), (-1, 6), 12),
                              ('FONTSIZE', (0, 7), (-1, 7), 12),
                              ('FONTSIZE', (0, 8), (-1, 8), 12),
                              ('FONTSIZE', (0, 9), (-1, 9), 12),

                              # Definir o tamanho da fonte para 14
                              ('BOTTOMPADDING', (0, 0), (-1, 0), 14),
                              ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                              ('FONTBOLD', (0, 1), (-1, -1), 1),
                              ('FONTITALIC', (0, 1), (-1, -1), 1),
                              ('GRID', (0, 0), (-1, -1), 1, colors.black),
                              # Adicione as linhas abaixo para configurar as bordas das células
                              ('LINEBELOW', (0, 1), (-1, -1), 1, colors.black),
                              ('LINEABOVE', (0, -1), (-1, -1), 1, colors.black),
                              ('LINEAFTER', (-1, 0), (-1, -1), 1, colors.black),
                              ('LINEBEFORE', (0, 0), (0, -1), 1, colors.black),
                              ])


    table.setStyle(style_table)

    story.append(table)
    story.append(espaco)
    story.append(Paragraph(f"Valor do Pedido {format_decimal(pedido.valor)}", style_custom))

    doc.build(story)
    return response
