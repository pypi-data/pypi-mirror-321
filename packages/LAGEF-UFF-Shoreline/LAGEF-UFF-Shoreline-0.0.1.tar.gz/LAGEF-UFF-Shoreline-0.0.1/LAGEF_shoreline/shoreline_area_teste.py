import ee
import geemap
import ee
import geemap
import pandas as pd
import skimage.filters as filters
import numpy as np
import matplotlib.pyplot as plt
import random
import os

####################################################################################

Map = geemap.Map()

#################################################################################### MAIN FUNCTION
####################################################################################
####################################################################################
#################################################################################### MAIN FUNCTION

def processar_imagens(start_dateNuv,roi,path1,row1,porcentagem_nuvem_roi,file_path,sheet_name,min_mare,max_mare):

      # Definir o intervalo de datas para busca das imagens
      end_dateNuv = start_dateNuv.advance(1, 'year')

      # Determinar a coleção do Landsat com base na data
      landsat_collection = ee.ImageCollection(
          ee.Algorithms.If(
              start_dateNuv.difference(ee.Date('2013-01-01'), 'year').gte(0),
              ee.ImageCollection('LANDSAT/LC08/C02/T1_L2'),  # Objeto Landsat 8
              ee.ImageCollection('LANDSAT/LT05/C02/T1_L2')   # Objeto Landsat 5
          )
      ).filterDate(start_dateNuv, end_dateNuv) \
      .filterBounds(roi) \
      .filter(ee.Filter.lt('CLOUD_COVER', 100))

      # Aplicar o fator de escala e o offset à coleção
      landsat_collection = landsat_collection##.map(apply_scale_factor)

      # Obter a primeira imagem da coleção
      first_image = landsat_collection.first()

      # Obter o ID da imagem e imprimir
      image_id = first_image.get('system:id').getInfo()
      #print(f"ID da imagem utilizada: {image_id}")

      def cloud_coverage(image):
          # Selecionar a banda de qualidade (QA_PIXEL) para identificar pixels de nuvens
          qa = image.select('QA_PIXEL')

          # Criar uma máscara para pixels de nuvens (bits 3 e 5 no QA_PIXEL)
          cloud_mask = qa.bitwiseAnd(1 << 3).Or(qa.bitwiseAnd(1 << 5))

          # Calcular a área total da ROI
          total_area = roi.area()

          # Calcular a área coberta por nuvens na ROI
          cloud_area = cloud_mask.multiply(ee.Image.pixelArea()).reduceRegion(
              reducer=ee.Reducer.sum(),
              geometry=roi,
              scale=30,
              maxPixels=1e9
          ).get('QA_PIXEL')

          # Calcular a área total da imagem
          image_area = image.geometry().area()

          # Calcular a área coberta por nuvens na imagem completa
          image_cloud_area = cloud_mask.multiply(ee.Image.pixelArea()).reduceRegion(
              reducer=ee.Reducer.sum(),
              geometry=image.geometry(),
              scale=30,
              maxPixels=1e9
          ).get('QA_PIXEL')

          # Calcular a porcentagem de cobertura de nuvens
          cloud_percentage_roi = ee.Number(cloud_area).divide(total_area).multiply(100)
          cloud_percentage_image = ee.Number(image_cloud_area).divide(image_area).multiply(100)

          return image.set('cloud_coverage_roi', cloud_percentage_roi).set('cloud_coverage_image', cloud_percentage_image)
      # Aplicar a função a cada imagem na coleção
      landsat_with_cloud_coverage = landsat_collection.map(cloud_coverage)

      # Recuperar os IDs das imagens e as porcentagens de cobertura de nuvens
      image_ids2 = landsat_with_cloud_coverage.aggregate_array('system:id').getInfo()
      cloud_percentages_roi = landsat_with_cloud_coverage.aggregate_array('cloud_coverage_roi').getInfo()
      cloud_percentages_image = landsat_with_cloud_coverage.aggregate_array('cloud_coverage_image').getInfo()

      # Definindo o intervalo de datas para busca das imagens
      start_dateMar = start_dateNuv
      end_dateMar = end_dateNuv

      # Definir o path e row específicos para a Baía de Guanabara
      path = path1
      row = row1

      # Carregar a coleção de imagens Landsat 8
      landsat_collectionMar = landsat_with_cloud_coverage \
                            .filterDate(start_dateMar, end_dateMar) \
                            .filter(ee.Filter.eq('WRS_PATH', path)) \
                            .filter(ee.Filter.eq('WRS_ROW', row))

      # Recuperar os IDs das imagens filtradas e as porcentagens de cobertura de nuvens na ROI
      image_idsMar = landsat_collectionMar.aggregate_array('system:id').getInfo()
      cloud_percentages_roiMar = landsat_collectionMar.aggregate_array('cloud_coverage_roi').getInfo()

      # Função para extrair a data dos IDs das imagens
      def extract_date_from_id(image_id):
          date_str = image_id.split('_')[-1]
          return pd.to_datetime(date_str, format='%Y%m%d')

      # Criar um DataFrame com as datas das imagens e porcentagens de nuvens na ROI
      image_dates_df = pd.DataFrame({
          'image_id': image_idsMar,
          'image_date': [extract_date_from_id(image_id) for image_id in image_idsMar],
          'cloud_coverage_roi': cloud_percentages_roiMar
      })

      # Adicionar índice à coluna de data do DataFrame de imagens e garantir o tipo datetime
      image_dates_df['image_date'] = pd.to_datetime(image_dates_df['image_date'])
      image_dates_df.set_index('image_date', inplace=True)

      # Carregar a tabela de marés a partir da planilha específica
      tides_df = pd.read_excel(file_path, sheet_name=sheet_name)

      # Converter a coluna 'Data' para datetime no DataFrame de marés e garantir o tipo correto
      tides_df['Data'] = pd.to_datetime(tides_df['Data'], format='%d/%m/%Y')

      # Filtrar os valores de marés entre 0,51 e 0,96 e a hora de 9h  ## USANDO 0.59 e 1.03
      filtered_tides_df = tides_df[
          (tides_df['valor'] >= min_mare) &
          (tides_df['valor'] <= max_mare) &
          (tides_df['Horat'] == 9)
      ].copy()

      # Adicionar índice à coluna de data do DataFrame de marés e garantir o tipo datetime
      filtered_tides_df['Data'] = pd.to_datetime(filtered_tides_df['Data'])
      filtered_tides_df.set_index('Data', inplace=True)

      # Ordenar os DataFrames pelas datas (necessário para merge_asof)
      image_dates_df.sort_index(inplace=True)
      filtered_tides_df.sort_index(inplace=True)

      # Combinar os DataFrames pelas datas usando merge_asof
      combined_df = pd.merge_asof(
          image_dates_df,
          filtered_tides_df,
          left_index=True,
          right_index=True,
          direction='nearest',
          tolerance=pd.Timedelta('1D')
      )

      # Filtrar imagens com menos de x% de cobertura de nuvens na ROI
      filtered_combined_df = combined_df[combined_df['cloud_coverage_roi'] < porcentagem_nuvem_roi]  # USANDO 0.01

      # Obter os IDs das imagens correspondentes, removendo os NaNs resultantes da junção
      matching_image_ids = filtered_combined_df.dropna(subset=['valor'])['image_id'].tolist()

      #print(matching_image_ids)

      # Função para aplicar máscara de nuvens
      def mask_l8_sr(image):
          qa_mask = image.select('QA_PIXEL').bitwiseAnd(int('11111', 2)).eq(0) #11111
          saturation_mask = image.select('QA_RADSAT').eq(0)
          #optical_bands = image.select('SR_B.').multiply(0.0000275).add(-0.2)
          #thermal_bands = image.select('ST_B.*').multiply(0.00341802).add(149.0) #.updateMask(qa_mask)
          return image.updateMask(saturation_mask) \
                      .updateMask(qa_mask)
                      #.addBands(optical_bands, None, True) \
                      #.addBands(thermal_bands, None, True) \

      # Carregar a coleção de imagens Landsat
      landsat8 = landsat_collection

      # Definir o ID da imagem base manualmente ##estou testando a coleção de SR
      base_image_id = matching_image_ids[0]

      # Selecionar a imagem base pelo ID
      base_image = ee.Image(base_image_id)

      # Função para determinar as bandas de visualização com base na coleção
      def get_visualization_bands(image):
          # Verificar a coleção da imagem (Landsat 8 ou Landsat 5)
          if 'LC08' in image.get('system:id').getInfo():
              # Definir as bandas para Landsat 8
              return ['SR_B4', 'SR_B3', 'SR_B2']  # Red, Green, Blue
          elif 'LT05' in image.get('system:id').getInfo():
              # Definir as bandas para Landsat 5
              return ['SR_B3', 'SR_B2', 'SR_B1']  # Red, Green, Blue
          else:
              # Caso a coleção não seja reconhecida
              return []

      # Obter as bandas para visualização automaticamente
      visualization_bands = get_visualization_bands(base_image)

      # Definir parâmetros de visualização
      visualization = {
          'bands': visualization_bands,
          'min': 0,
          'max': 0.2
      }

      # Aplicar a máscara de nuvens na imagem base
      combined_image = base_image

      # Período do mosaico de referência (base abaixo da imagem única)
      start_date = start_dateNuv
      end_date = end_dateNuv

      # Filtrar e mascarar a coleção de imagens no período de referência
      filtered_collection = landsat8.filterDate(start_date, end_date).filterBounds(roi).map(mask_l8_sr)

      # Criar um mosaico mediano das imagens de referência
      reference_mosaic = filtered_collection.median()

      #reference_mosaic = reference_mosaic.select(reference_mosaic.bandNames()).multiply(0.0000275).add(-0.2)

      # Função para preencher os pixels nublados da imagem base com o mosaico de referência
      def fill_cloud_pixels(base, reference):
          # Criar uma máscara para os pixels nublados
          cloud_mask = base.mask().Not()
          # Preencher os pixels nublados com os pixels do mosaico de referência
          filled = base.unmask(reference)
          return filled


      # Preencher os pixels nublados da imagem base com o mosaico de referência
      corrected_image = fill_cloud_pixels(combined_image, reference_mosaic)

      comp = combined_image.clip(roi)

      # Função para obter as bandas corretas dependendo da coleção de imagem (Landsat 5 ou Landsat 8)
      def get_bands_for_mndwi(image):
          # Verificar a coleção da imagem (Landsat 8 ou Landsat 5)
          if 'LC08' in image.get('system:id').getInfo():
              # Landsat 8: B3 (Green), B6 (SWIR), B5 (NIR), B4 (Red), B2 (Blue)
              return {
                  'GREEN': image.select('SR_B3'),
                  'SWIR': image.select('SR_B6'),
                  'NIR': image.select('SR_B5'),
                  'RED': image.select('SR_B4'),
                  'BLUE': image.select('SR_B2')
              }
          elif 'LT05' in image.get('system:id').getInfo():
              # Landsat 5: B2 (Green), B5 (SWIR), B4 (NIR), B3 (Red), B1 (Blue)
              return {
                  'GREEN': image.select('SR_B2'),
                  'SWIR': image.select('SR_B5'),
                  'NIR': image.select('SR_B4'),
                  'RED': image.select('SR_B3'),
                  'BLUE': image.select('SR_B1')
              }
          else:
              # Caso a coleção não seja reconhecida
              return None

      # Selecionar as bandas corretas para a imagem base
      bands = get_bands_for_mndwi(comp)

      # Verificar se as bandas foram corretamente identificadas
      if bands:
          # Calcular o MNDWI
          mndwi = comp.expression(
              '(GREEN - SWIR) / (GREEN + SWIR)',
              bands
          ).rename('mndwi')

          # Parâmetros de visualização para o MNDWI
          mndwi_vis_params = {
              'min': -1,
              'max': 1,
              'palette': ['00FFFF', '0000FF']
          }

          # Adicionar o MNDWI ao mapa
          #Map.add_ee_layer(mndwi, mndwi_vis_params, 'MNDWI', 1)

      else:
          print('Coleção de imagem não reconhecida para MNDWI.')
      #Map

      # Obter uma coleção de pixels da imagem MNDWI
      mndwi_pixels = mndwi.sample(roi, scale=30).reduceColumns(ee.Reducer.toList(), ['mndwi']).get('list')

      # Converter a coleção de pixels em uma lista e, em seguida, em um array NumPy
      mndwi_values = np.array(ee.List(mndwi_pixels).getInfo())

      # Aplicar o threshold de Otsu multi-nível
      otsu_thresholds = filters.threshold_multiotsu(mndwi_values, classes=3) ## classes
      print("Otsu Thresholds:", otsu_thresholds)

      # Criar imagens binárias com base nos thresholds de Otsu
      binary_mndwi_classes = []
      for i in range(len(otsu_thresholds) + 1):
          if i == 0:
              binary_class = mndwi.expression('mndwi <= threshold ? 1 : 0', {
                  'mndwi': mndwi,
                  'threshold': otsu_thresholds[i]
              }).rename(f'binary_class_{i}')  # Água
          elif i == len(otsu_thresholds):
              binary_class = mndwi.expression('mndwi > threshold ? 1 : 0', {
                  'mndwi': mndwi,
                  'threshold': otsu_thresholds[i - 1]
              }).rename(f'binary_class_{i}')  # Continente
          else:
              binary_class = mndwi.expression('mndwi > threshold_min && mndwi <= threshold_max ? 1 : 0', {
                  'mndwi': mndwi,
                  'threshold_min': otsu_thresholds[i - 1],
                  'threshold_max': otsu_thresholds[i]
              }).rename(f'binary_class_{i}')  # Lama

          binary_mndwi_classes.append(binary_class)

      # Combinar as classes em uma única imagem
      final_result = ee.Image(binary_mndwi_classes[0]).multiply(1)
      for i in range(1, len(binary_mndwi_classes)):
          final_result = final_result.add(binary_mndwi_classes[i].multiply(i + 1))

      # clip
      final_result_clip = final_result.clip(roi)

      # Extrair automaticamente o primeiro limiar
      first_threshold = otsu_thresholds[1] # Primeiro limiar - otsu_thresholds[0]

      # Criar uma imagem binária com base no primeiro limiar
      binary_mndwi_first_threshold = mndwi.expression('mndwi > threshold ? 1 : 0', {
          'mndwi': mndwi,
          'threshold': first_threshold
      }).rename('binary_mndwi_first_threshold')

      binary_mndwi_first_threshold = binary_mndwi_first_threshold.clip(roi)

      ### daqui para frente será para o tratamento visual dos dados
      ## Selecionar a resolução que os resultados serão exportados mais tarde
      # QUANTO MAIOR A RESOLUÇÃO MAIS SMOOTH O RESULTADO
      expresm = 15

      ##será necessário add um limiar (threshold) também a resolução em m acima para elimiar erros e ilhas, por exemplo
      # em caso de um corpo hídrico maior, ou falhas maiores, próximas a linha de costa que se imagina deve setar o valor maior
      waterbodysizem = 5000 ## para o RJ usar cerca de 5000
      islandsizem = 900 ## para o RJ usar cerca de 3000

      ##agora sera feito um def para binarizar a água e terra aplicando as duas o filtro de corpos hidricos e resolução.
      def removerfalhas(water_image, waterbodysizem, islandsizem, expresm):
          water_image = water_image.int()

          #definir os próximos, a proximidade, com os parametros setados
          pixland = ee.Number(waterbodysizem).divide(expresm).int()
          pixwater = ee.Number(islandsizem).divide(expresm).int()

          #remover corpos hidricos no continente
          landfill = water_image.addBands(water_image)\
              .reduceConnectedComponents(ee.Reducer.median(), 'binary_mndwi_first_threshold', pixland)\
              .unmask(99).eq(99).And(water_image.neq(0))

          # remover ilhas e erros pequenos
          waterfill = landfill.addBands(landfill)\
              .reduceConnectedComponents(ee.Reducer.median(), 'binary_mndwi_first_threshold_1', pixwater)\
              .unmask(99).eq(99).And(landfill.neq(1))

          #limite entre terra e agua com os limites já feitos acima
          return waterfill

      # binarizar e visualizar todos os dados feitos no bloco acima
      limiteat = removerfalhas(binary_mndwi_first_threshold, waterbodysizem, islandsizem, expresm)
      limitevis = {'min': 0, 'max': 1, 'palette': ['white', 'black']}

      #converter a linha de costa do raster para um vetor
      vetor = limiteat.selfMask() \
          .reduceToVectors(
              geometry=roi,
              scale=expresm,
              eightConnected=True,
              maxPixels=1e20,
              tileScale=16
          )

      #adicionar o produto em vetor ao mapa e verificar se esta correto.
      Map.add_ee_layer(vetor, {'color': 'blue'}, 'aguavetor')
      Map

      # Supondo que a variável 'imagem' seja a imagem do Landsat ou outro dataset com a data associada
      imagem = comp  # Substitua pelo ID correto

      # Obter a data da imagem (ano)
      data_imagem = imagem.get("system:time_start").getInfo()
      ano_imagem = ee.Date(data_imagem).format("YYYY").getInfo()  # Extrai o ano da imagem

      # Calcular a área do ROI em metros quadrados e converter para km²
      roi_area_m2 = roi.area().getInfo()  # Área em metros quadrados
      roi_area_km2 = roi_area_m2 / 1e6  # Converter para km²
      #print(f"Área do ROI ({ano_imagem}): {roi_area_km2} km²")

      # Calcular a área do vetor (linha de costa) com um erro de margem de 1 metro
      vetor_area_m2 = vetor.geometry().area(maxError=1).getInfo()  # Área em metros quadrados
      vetor_area_km2 = vetor_area_m2 / 1e6  # Converter para km²
      #print(f"Área do vetor (linha de costa) ({ano_imagem}): {vetor_area_km2} km²")

       # Retornando o vetor e as áreas como um dicionário
      return {
        'vetor': vetor,
        'area_vetor': f"Área do vetor (linha de costa) ({ano_imagem}): {vetor_area_km2} km²",
        'area_roi': f"Área do ROI ({ano_imagem}): {roi_area_km2} km²"
    }

#################################################################################### TIDE FUNCTION
####################################################################################
####################################################################################
####################################################################################

def print_tide_statistics(file_path, sheet_name):
    """
    Carrega uma planilha de marés, calcula estatísticas descritivas e imprime os resultados.

    Parâmetros:
        file_path (str): Caminho para o arquivo Excel - entre aspas simples.
        sheet_name (str): Nome da aba da planilha que contém os dados - entre aspas simples.
    """
    # Carregar a tabela de marés a partir da planilha especificada
    tides_df = pd.read_excel(file_path, sheet_name=sheet_name)

    # Calcular as estatísticas descritivas para a coluna 'valor'
    summary_stats = tides_df['valor'].describe(percentiles=[0.25, 0.5, 0.75])

    # Renomear as colunas
    summary_stats = summary_stats.rename({
        'min': 'Min.',
        '25%': '1st Qu.',
        '50%': 'Median',
        'mean': 'Mean',
        '75%': '3rd Qu.',
        'max': 'Max.'
    })

    # Selecionar e reordenar as colunas
    summary_stats = summary_stats[['count', 'Min.', '1st Qu.', 'Median', 'Mean', '3rd Qu.', 'Max.']]

    # Imprimir as estatísticas descritivas
    print(summary_stats)


#################################################################################### RESULTS
####################################################################################
####################################################################################
####################################################################################

## loop para todos os anos

def process_annual_images(start_year, end_year, processar_imagens, roi, path1, row1, porcentagem_nuvem_roi, file_path, sheet_name, min_mare, max_mare, Map):
    """
    Processa imagens para um intervalo de anos e gera resultados com cores aleatórias.

    Parâmetros:
        start_year (int): Ano inicial para o processamento.
        end_year (int): Ano final para o processamento (exclusivo).
        processar_imagens (function): Função que processa imagens e retorna resultados.
        roi (object): Região de interesse.
        path1, row1 (int): Caminho e linha da imagem.
        porcentagem_nuvem_roi (float): Porcentagem máxima de nuvem permitida na ROI.
        file_path (str): Caminho do arquivo de entrada.
        sheet_name (str): Nome da planilha no arquivo.
        min_mare, max_mare (float): Limites mínimos e máximos da maré.
        Map (object): Mapa interativo para adicionar camadas.

    Retorna:
        dict: Dicionários contendo resultados por ano, áreas do vetor e áreas do ROI.
    """
    # Dicionários para armazenar os vetores e áreas
    resultados_por_ano = {}
    areas_vetor = {}
    areas_roi = {}

    # Função para gerar uma cor aleatória no formato hexadecimal
    def gerar_cor_aleatoria():
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))

    # Loop para processar imagens de start_year até end_year
    for ano in range(start_year, end_year):
        try:
            # Define a data de início como o primeiro dia de janeiro do ano
            data_inicio = ee.Date(f'{ano}-01-01')

            # Chama a função processar_imagens com todos os argumentos necessários
            resultado = processar_imagens(data_inicio, roi, path1, row1, porcentagem_nuvem_roi, file_path, sheet_name, min_mare, max_mare)

            # Armazena o vetor e as áreas no dicionário
            resultados_por_ano[ano] = resultado
            areas_vetor[ano] = resultado['area_vetor']
            areas_roi[ano] = resultado['area_roi']

            # Gera uma cor aleatória para o ano
            cor_aleatoria = gerar_cor_aleatoria()

            # Adiciona o vetor ao mapa com a cor gerada aleatoriamente
            if 'vetor' in resultado and isinstance(resultado['vetor'], (ee.FeatureCollection, ee.Feature, ee.Geometry)):
                Map.add_layer(resultado['vetor'], {'color': cor_aleatoria, 'width': 2}, f'Vetor {ano} ({cor_aleatoria})')
            else:
                print(f"Vetor inválido ou não encontrado para o ano {ano}")

            # Exibe as informações de área no console
            print(f"Ano: {ano} - Área do vetor: {resultado['area_vetor']} km²")
            print(f"Ano: {ano} - Área do ROI: {resultado['area_roi']} km²")

        except Exception as e:
            # Se ocorrer um erro, imprime uma mensagem e pula para o próximo ano
            print(f"Erro ao processar o ano {ano}: {e}")
            continue  # Pula para o próximo ano

    return resultados_por_ano, areas_vetor, areas_roi

#################################################################################### EXPORTS
####################################################################################
####################################################################################
####################################################################################

#Função que irá processar a exportação dos vetores e a criação da tabela Excel
# Função para exportar resultados para o Google Drive
# Função para exportar vetores e tabela
def exportar_resultados(resultados_teste, output_path):
    # Inicializa uma lista para acumular os dados de área
    tabela_acumulada = []

    # Lista para armazenar as tarefas de exportação
    export_tasks = []

    # Extrai os resultados dos anos (considerando que resultados_teste é uma tupla com a estrutura correta)
    resultados_por_ano, _, _ = resultados_teste  # Desempacotando a tupla

    # Percorrer os resultados do teste por ano
    for ano, resultado in resultados_por_ano.items():
        try:
            # Verifica se o vetor está presente para o ano
            vetor = resultado['vetor']
            area_vetor = resultado['area_vetor']
            area_roi = resultado['area_roi']

            # Exporta o vetor como SHP
            export_vetor = ee.FeatureCollection(vetor)
            export_task = ee.batch.Export.table.toDrive(
                collection=export_vetor,
                description=f'vetor_{ano}_linha_de_costa',
                fileFormat='SHP',
                folder=output_path  # Usando o caminho definido pelo usuário
            )
            export_tasks.append(export_task)

            # Acumula os dados da tabela para o ano
            tabela_acumulada.append({
                'Ano': ano,
                'Área do vetor (km²)': area_vetor,
                'Área do ROI (km²)': area_roi
            })
        except Exception as e:
            print(f"Erro ao processar o ano {ano}: {e}")
    
    # Criar DataFrame com os dados acumulados
    df_tabela = pd.DataFrame(tabela_acumulada)

    # Exporta a tabela com as informações de área como arquivo Excel
    tabela_path = f"{output_path}/tabela_areas_total.xlsx"
    df_tabela.to_excel(tabela_path, index=False)

    # Retorna as tarefas de exportação para execução no Google Earth Engine
    return export_tasks
