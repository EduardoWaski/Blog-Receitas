from models import *
from db_config import *

'''
BOVINOS
'''

cupim_queijo = Recipe(
"../static/img/recipe_images/cupim_queijo.jpeg",

"Cupim com Queijo",

"""Acenda a churrasqueira com cerca de 40 minutos de antecedência. O objetivo é ter uma brasa bem quente, mas sem labareda
Acomode uma grelha de inox a 10 cm acima da brasa. Se você tiver uma grelha Argentina pode usar;
Enquanto a churrasqueira aquece, retire o Cupim da geladeira e deixe chegar em temperatura ambiente;
Seque bem a carne com auxílio de papel toalha;
Acomode o cupim na grelha ao fundo da churrasqueira e sele cada lado por cerca de 2 minutos, virando a peça para que doure toda por igual;
Retire a peça do fogo e suspenda a grelha para uma altura de pelo menos 20 cm da brasa;
Acomode a peça de carne sobre a parte brilhante do papel alumínio;
Espalhe a manteiga por toda a extensão da carne. Você pode usar um pincel ou as mãos para fazer isso. Se certifique que toda a carne está envolvida em manteiga;
Adicione a pimenta do reino, o sal de parrilla e dê cerca de 8 voltas no papel alumínio por toda a peça de carne;
Acomode o cupim bem embrulhado no papel alumínio na grelha já posicionada a 20 cm da brasa;
Asse o cupim por cerca de 5h, virando a carne com cuidado para não rasgar o papel, a cada 30 minutos;
Retire o cupim do fogo e deixe descansar por mais 30 minutos ainda embrulhado no papel alumínio;
Abra o papel alumínio, retire a carne e com uma faca bem afiada, corte a peça ao meio na horizontal;
Recheie a carne com metade das fatias de queijo mussarela, metade das fatias de queijo provolone e feche novamente com a metade superior da carne;
Distribua o restante das fatias de queijo sobre a carne;
Coloque brasa em uma assadeira redonda e furada própria pra churrasco e aproxime bem do queijo para gratinar, cerca de 2 cm de distância já são suficiente;
Você pode gratinar o queijo também com um maçarico ou pré-aquecer o forno a 280° por 10 minutos e levar a carne para assar por 12 minutos ou só até gratinar;
Sirva o cupim com queijo acompanhado de farofa e molho à campanha (vinagrete).""",

"""4kg de Cupim
4 colheres de sopa de manteiga em ponto de pomada
Pimenta do reino moída na hora a gosto
2 colheres de sopa de sal de parrilla
Papel alumínio o quanto baste
100g de mussarela fatiada
100g de queijo provolone em fatias""",

"Bovinos"
)

#if not recipes_collection.find_one({'name':cupim_queijo.name}):

recipes_collection.insert_one(cupim_queijo.__dict__)

steak_tartare = Recipe(
"../static/img/recipe_images/steak_tartare.jpeg",

"Steak Tartare",

"""Certifique-se de que o Filet Mignon está bem resfriado antes de começar;
Com uma faca bem afiada, corte a carne em cubos bem pequenos ou pique finamente à mão, conforme sua preferência.
Em uma tigela, misture a gema de ovo, a mostarda Dijon, as alcaparras, a cebola roxa, os picles, o molho inglês, o molho de pimenta (se usar), e o azeite de oliva;
Tempere com sal e Mix de Pimenta a gosto.
Adicione a carne à tigela com o molho e misture delicadamente para que todos os ingredientes fiquem bem incorporados;
Prove e ajuste o tempero, se necessário;
Molde o steak tartare em um aro em cima de uma torrada ou fatia de pão crocante para acompanhar;
Decore com cebolinha ou salsinha picada por cima.""",

"""200g de Filet Mignon, cortado em cubos bem pequenos
1 gema de ovo fresco
1 colher de sopa de mostarda Dijon
1 colher de sopa de alcaparras picadas
1 colher de sopa de cebola roxa bem picada
1 colher de sopa de picles de pepino picado
1 colher de chá de molho inglês
1 colher de chá de molho de pimenta (opcional)
1 colher de chá de azeite de oliva extra virgem
Sal a gosto
Mix de Pimenta a gosto
Cebolinha picada a gosto (opcional)
Salsinha picada a gosto (opcional)
Torradas de sua preferência a gosto""",

"Bovinos"

)

#if not recipes_collection.find_one({'name': steak_tartare.name}):

recipes_collection.insert_one(steak_tartare.__dict__)




lingua_boi = Recipe(
"../static/img/recipe_images/lingua_boi.jpeg",

"Língua de Boi",

"""Em uma panela de pressão adicione a Língua, o
sal, as folhas de louro, o vinagre, as folhas de alho poró e a cebola. Cubra com água até o limite da panela e tampe;
Leve ao fogo alto até pegar pressão;
Assim que pegar pressão, reduza o fogo para médio e deixe cozinhar por 40 minutos;
Desligue o fogo e deixe a pressão sair sozinha;
Retire a língua da panela e dispense o que ficou na panela;
Transfira a carne para uma tábua e retire a membrana que envolve a peça. Ela fica esbranquiçada após o pré-cozimento e sai com facilidade ao ser puxada;
Fatie a língua em pedaços com espessura aproximada de 2cm, espessura de um dedo;

Aqueça uma panela grande em fogo médio;
Adicione o bacon picado e frite até dourar;
Mantenha a panela no fogo, retire o bacon e reserve;
Adicione o azeite, a cebola, o pimentão e a cenoura. Refogue tudo por cerca de 6 minutos ou até que os legumes comecem a dourar;
Adicione o alho, o alho poró e refogue por mais 2 minutos;
Volte com o bacon, adicione a língua pré-cozida e fatiada, misture tudo bem para incorporar;
Adicione o tomate, o tomilho, a páprica doce, o colorau, a pimenta calabresa, acerte o sal e misture bem;
Diminua o fogo para o mínimo e tampe a panela. Cozinhe por 30 minutos, mexendo de vez em quando para não queimar. Se necessário, adicione um pouquinho de água;
Desligue o fogo e sirva a língua salpicando a salsinha picada acompanhada de purê de batata.""",

"""5kg de Língua Friboi 
1 colher de chá de sal
3 folhas de louro
1 colher de sopa de vinagre
30g de folhas de alho poró
200g de cebola descascada e picada grosseiramente
100g de bacon picadinho
2 colheres de sopa de azeite
1/2 xícara de cebola picadinha
1/2 xícara de pimentão vermelho picadinho e sem sementes
1/4 xícara de cenoura sem casca e picadinha
1 colher de sopa de alho picadinho
1/4 xícara de alho poró fatiado fininho 
300g de tomate italiano picado
1 colher de sopa de tomilho debulhado (opcional)
1 colher de chá de páprica doce
1/2 colher de chá de colorau
1/4 colher de chá de pimenta calabresa (opcional)
1/4 xícara de folhas de salsa picadas
Sal a gosto""",

"Bovinos"
)

#if not recipes_collection.find_one({'name': lingua_boi.name}):

recipes_collection.insert_one(lingua_boi.__dict__)


'''
AVES
'''

lasanha_frango = Recipe(
"../static/img/recipe_images/lasanha_frango.jpeg",

"Lasanha de Frango",

"""Aqueça uma panela média em fogo médio. Coloque a manteiga para derreter e logo em seguida a farinha de trigo. Mexa bem com um fouet (batedor de claras). Assim que dissolver com completo a farinha na manteiga, acrescente aos poucos o leite integral, mexa sempre;
Cozinhe em fogo alto por 10 minutos, mexa sempre;
Tempere o molho branco com sal e noz moscada;
Retire do fogo o molho e cubra com um plástico filme, deixe em contato com o molho. Reserve por alguns minutos para perder um pouco a temperatura;
Aqueça o forno a 190°C;
Coloque uma porção de molho no fundo de um refratário de aproximadamente 20 x 40;
Comece as camadas com massa de lasanha. Em seguida uma porção de molho, uma porção de Peito de Frango Defumado Marba e queijo mussarela. Repita o processo até finalizar os ingredientes ou a altura do refratário;
Polvilhe o queijo parmesão ralado e leve ao forno por 15 a 20 minutos ou até que doure o topo da lasanha;
Retire do forno e deixe descansar alguns minutos antes de servir.""",

"""500g de Peito de Frango Defumado Marba (ralado)
2 colheres (sopa) de manteiga sem sal
3 colheres (sopa) farinha de trigo
750ml de leite integral
Noz moscada a gosto
Sal a gosto
500g de massa de lasanha fresca
350g de mussarela (ralada ou fatiada)
¼ de xícara de queijo parmesão (ralado)""",

"Aves"

)

if not recipes_collection.find_one({'name': lasanha_frango.name}):
    recipes_collection.insert_one(lasanha_frango.__dict__)


vatapa_frango = Recipe(
"../static/img/recipe_images/vatapa_frango.jpeg",

"Vatapá de Frango",

"""Em um liquidificador, coloque um pouco do leite, o leite de coco, o creme de leite, os pães, a cebola, o caldo de galinha e o sal a gosto e bata até obter uma mistura homogênea, reservando em seguida;
Refogue o frango com o azeite de dendê e o molho de pimenta a gosto;
Adicione a mistura do liquidificador à panela e vá mexendo, em fogo médio, até ferver e ganhar consistência;
Por fim, adicione o restante do leite, deixe ferver por mais alguns minutos e sirva.""",

"""1kg de Frango Sem Miúdos DaGranja cozido e desfiado
1,5l de leite
1 cebola picadinha
2 cubos de caldo de galinha
6 pães amanhecidos
1 caixa de creme de leite
200ml de leite de coco
100ml de azeite de dendê
Molho de pimenta a gosto
Sal a gosto""",

"Aves"
)

if not recipes_collection.find_one({'name': vatapa_frango.name}):
    recipes_collection.insert_one(vatapa_frango.__dict__)

sopa_frango = Recipe(
"../static/img/recipe_images/sopa_frango.jpeg",

"Sopa de Frango",

"""Em uma panela grande, derreta a e refogue o Filé de Peito de Frango em Cubos até que fique douradinho;
Junte a abobrinha, a cenoura, a batata, os tomates, a vagem, o alho, a cebola e refogue por 2 minutos;
Adicione o caldo de legumes e deixe ferver por 10 minutos. Depois, junte a couve e desligue o fogo;
Sirva com queijo ralado e torradinhas.""",

"""300g de Filé de Peito de Frango em Cubos
3 colheres de sopa de Margarina Doriana com Sal
3 batatas cortadas em cubinhos
1 cenoura cortada em cubinhos
1 abobrinha cortada em cubinhos
3 folhas de couve cortadas bem fininhas em tirinhas
2 tomates cortados em cubinhos
100 g de vagem picada
2 dentes de alho picados
1 cebola picada
2 litros de caldo de legumes
Sal a gosto
Pimenta a gosto
Queijo ralado a gosto""",

"Aves"

)

if not recipes_collection.find_one({'name': sopa_frango.name}):
    recipes_collection.insert_one(sopa_frango.__dict__)

""""
PESCADOS
"""

salmao_alcaparra = Recipe(
"../static/img/recipe_images/salmao_alcaparra.jpeg",

"Salmão com Alcaparras",

"""Descongele o Filé de Salmão em Pedaços de acordo com as instruções da embalagem;
Preaqueça o forno a 180ºC;
Tempere o salmão com sal, pimenta do reino e as folhas de endro picadas;
Aqueça uma frigideira antiaderente de fundo grosso em fogo médio;
Adicione o azeite e assim que aquecer, adicione o salmão com a carne voltada para baixo;
Frite o salmão por cerca de 5 minutos ou até que a carne doure;
Vire o salmão com muito cuidado para não desmanchar o peixe, se preferir use um prato como apoio para virar o lombo e frite a pele por mais 5 minutos;
Transfira o lombo de salmão para uma assadeira ou tabuleiro, cubra com papel alumínio e leve ao forno por 10 minutos.
Enquanto o salmão assa, em uma panelinha adicione o suco e raspas de limão siciliano, as alcaparras, o azeite, sal e pimenta do reino;
Misture o molho e leve ao fogo baixo, mexendo sempre por 3 minutos, só até o azeite aquecer;
Desligue o fogo, retire o salmão do forno e sirva regando o molho de alcaparras por cima.""",

"""1 embalagem de Filé de Salmão em Pedaços
Sal
Pimenta-do-reino
2 colheres de sopa de folhas de endro picados
4 colheres de sopa de azeite
Para o molho:
Suco e raspas de 1 limão siciliano
3 colheres de sopa de alcaparras
1/4 xícara de azeite
Sal à gosto
Pimenta-do-reino à gosto""",

"Pescados"
)

if not recipes_collection.find_one({'name': salmao_alcaparra.name}):
    recipes_collection.insert_one(salmao_alcaparra.__dict__)

arroz_camarao = Recipe(
"../static/img/recipe_images/arroz_camarao.jpeg",

"Arroz com Camarão Cremoso",

"""Para descongelar o Camarão Descascado, siga as instruções da embalagem;
Em uma frigideira, aqueça o azeite e refogue a cebola picada até ficar translúcida. 
Junte o alho e deixe dourar;
Adicione os camarões e refogue até ficarem rosados; 
Misture os cubos de tomate sem pele e sementes cortados em cubos;
Tempere com o sal e a pimenta a gosto e desligue o fogo;
Retire o refogado da panela e reserve;
Na mesma panela, junte o arroz e refogue, mexendo sem parar por 1 minuto;
Despeje o caldo de camarões e espere o arroz cozinhar até reduzir o líquido;
Quando estiver quase pronto e restar um pouco de líquido, misture o leite de coco, a manteiga, o refogado de camarão e o queijo parmesão;
Tampe a panela, desligue o fogo e deixe descansar por 1 minuto;
Coloque o arroz cremoso com camarão em uma travessa e decore com a pimenta biquinho.""",

"""1 pacote de Camarão Descascado
3 colheres de sopa de azeite
1 cebola pequena 
3 dentes de alho
2 tomates
Pimenta-do-reino
2 xícaras de chá de arroz branco
4 xícaras de chá de caldo de camarão
1 garrafinha de leite de coco 200ml
1 colher de sopa de manteiga
1/4 de xícara de chá de queijo parmesão ralado
Pimenta biquinho em conserva para decorar
Sal """,

"Pescados"
)

if not recipes_collection.find_one({'name': arroz_camarao.name}):
    recipes_collection.insert_one(arroz_camarao.__dict__)


file_tilapia = Recipe(
"../static/img/recipe_images/file_tilapia.jpeg",

"Filé de Tilápia com Legumes",

"""Descongele os Filés de Tilápia 600g de acordo com as instruções da embalagem.
Tempere com o sal, o limão e a pimenta. Cubra e leve à geladeira, enquanto prepara os legumes.
Lave e corte os tomates ao meio. Retire as sementes e coloque de boca para baixo sobre papel toalha para secar.
Lave o cará/inhame, descasque, lave novamente e corte em rodelas grossas.
Coloque em uma panela, cubra com água e coloque uma pitada de sal. Tampe a panela e quando levantar fervura, deixe cozinhar até ficar macio porém sem desmanchar.
Escorra e reserve a água.
Corte os brócolis em buquês, lave e afervente por 50 segundos na mesma água que cozinhou o inhame. Escorra e passe na água bem gelada para cessar o cozimento.
Descasque as cebolas e corte em pétalas.
Em um refratário grande acomode os legumes, regue com o azeite, tempere com sal e pimenta.
Leve ao forno pré-quecido a 200 graus e asse por aproximadamente 30 minutos, virando delicadamente na metade do tempo.
Retire do forno, com uma espátula junte os legumes ao redor do refratário abrindo espaço para as tilápias.
Acomode as tilápias no meio, volte ao forno por aproximadamente 20 minutos até dourarem.
Lave e seque as folhas de manjericão.
No liquidificador ou no processador bata: o azeite, as castanhas, o alho e o queijo.
Junte as folhas de manjericão, o gelo e bata novamente até formar um molho.
Tempere com o sal e a pimenta.
Sirva com a tilápia.""",

"""1 pacote de Filé de Tilápia 600g
Sal a gosto
Sumo de 1⁄2 limão
Pimenta-do-reino moída na hora a gosto
Azeite para regar
4 tomates italianos
2 inhames
1 maço de brócolis
2 cebolas
Para o pesto de manjericão

2 xícaras de chá de folhas de manjericão
1⁄2 xícara de chá de castanha de caju torrada
1 xícara de chá de queijo parmesão ralado
1 dente de alho
1⁄2 xícara de chá de azeite
1 pitada de sal
Pimenta-do-reino moída na hora a gosto
2 pedras de gelo""",

"Pescados"
)


if not recipes_collection.find_one({'name': file_tilapia.name}):
    recipes_collection.insert_one(file_tilapia.__dict__)


"""
Bolos
"""

bolo_chocolate_morango = Recipe(
"../static/img/recipe_images/bolo_chocolate_morango.jpeg",

"Bolo de Chocolate com Morango",

"""Preaqueça o forno a 180° C. 
Na tigela da batedeira, junte os ovos, a margarina sem sal, o açúcar e o chocolate em pó. Bata em velocidade mínima até ficar homogêneo;
Sem parar de bater, adicione a farinha e água por partes, intercalando as adições e só adicionando uma parte quando a anterior estiver incorporada;
Retire da batedeira, junte o fermento e misture delicadamente com uma espátula. 
Unte uma forma de fundo removível (tamanho de 25 centímetros de diâmetro) com Doriana sem Sal e chocolate em pó. Leve ao forno por aproximadamente 30 minutos;
Em uma panela, junte o creme de leite, o leite condensado, o leite integral, o chocolate branco e o amido de milho. Com o fogo ainda desligado, misture bem para dissolver o amido;
Leve a mistura ao fogo baixo e mexa até engrossar. O ponto ideal é quando você passar a espátula no fundo da panela e a massa abrir um caminho que demore mais de 5 segundos para fechar. 
Em seguida, desligue o fogo, espere esfriar totalmente e transfira para um saco de confeiteiro;
Com uma faca serrilhada grande, corte a massa do bolo ao meio. 
Espalhe o recheio no bolo em uma das metades e adicione os morangos picados no centro. Acomode a outra massa por cima e reserve;
Em uma panela, aqueça o creme de leite fresco em fogo médio até começar a ferver;
Enquanto o creme de leite aquece, pique o chocolate e transfira para uma tigela. Derrame o creme de leite ainda quente por cima, espere 2 minutos e misture até formar um creme brilhoso;
Cubra o bolo com a ganache de chocolate, decore com morangos e leve à geladeira até o momento de servir.""",

"""150g de Margarina Doriana sem Sal derretida + para untar
4 ovos
1 xícara de açúcar
1 xícara de chocolate em pó + para untar
2 xícaras de farinha
1 xícara de água 
1 colher de sopa de fermento

Para o recheio

1 lata de leite condensado
⅓ caixinha de creme de leite
½ xícara de leite integral
100g de chocolate branco
4 colheres de sopa de amido de milho
½ xícara de morango picado

Para a ganache de chocolate

2 xícaras de chocolate meio amargo 
½ xícara de creme de leite fresco
Morangos para decorar""",

"Bolos"
)

if not recipes_collection.find_one({'name': bolo_chocolate_morango.name}):
    recipes_collection.insert_one(bolo_chocolate_morango.__dict__)


bolo_banana = Recipe(
"../static/img/recipe_images/bolo_banana.jpeg",

"Bolo de Banana com Aveia",

"""A cobertura é a primeira etapa dessa receita. Em uma panela, junte o açúcar e a água. Cozinhe em fogo baixo até que a mistura atinja uma cor amarronzada; 
Retire do fogo e adicione em uma forma untada com Margarina sem Sal;
Fatie as bananas e adicione por cima do caramelo. 
Preaqueça o forno a 180ºC;
Derreta a Margarina sem Sal e adicione ao liquidificador. Junte os ovos, as bananas e o açúcar. Bata na velocidade mínima por 5 minutos ou até formar um creme homogêneo;
Adicione a canela e a aveia ao liquidificador e bata por cerca de 2 minutos até ficar uniforme;
Transfira para uma tigela. Acrescente o fermento, misturando cuidadosamente com uma espátula, e adicione à forma que já está com a calda;
Leve ao forno por 40 minutos ou até o bolo crescer e dourar. Espere amornar e desenforme.""",

"""1 xícara de Margarina sem Sal + para untar
4 bananas prata 
4 ovos
1 xícara de açúcar
1 ½ xícara de aveia em flocos
1 colher de chá de canela em pó
2 colheres de sopa de fermento químico em pó""",

"Bolos"
)

if not recipes_collection.find_one({'name': bolo_banana.name}):
    recipes_collection.insert_one(bolo_banana.__dict__)

bolo_ingles = Recipe(
"../static/img/recipe_images/bolo_ingles.jpeg",

"Bolo Inglês Clássico",

"""Preaqueça o forno a 170 ºC (temperatura média). Unte com manteiga uma fôrma para bolo inglês de 22 cm X 10 cm. Cubra o fundo e laterais maiores da fôrma com um pedaço de papel-manteiga de 28 cm X 18 cm — o papel cortado um pouco maior que a fôrma facilita na hora de desenformar o bolo. Unte o papel também com manteiga.
Numa tigela pequena, quebre um ovo de cada vez e transfira para uma tigela maior — se um estiver estragado, você não perde a receita. Adicione o leite, a essência de baunilha e misture bem com um garfo.
Na tigela da batedeira, peneire a farinha, o açúcar, o sal e o fermento. Utilizando a raquete da batedeira, bata em velocidade baixa apenas para misturar os ingredientes. Ainda em velocidade baixa, adicione metade dos ingredientes líquidos em fio. Acrescente a manteiga e bata por cerca de 1 minuto até a manteiga e os ovos serem incorporados pela farinha — pare de bater e raspe a lateral da tigela com a espátula quantas vezes forem necessárias para misturar os ingredientes de maneira uniforme.
Aumente a velocidade da batedeira para média e adicione o restante dos ingredientes líquidos em duas etapas, batendo bem a cada adição para incorporar.
Transfira a massa de bolo para a forma untada e nivele com uma espátula para deixar o bolo bem retinho. Leve ao forno para assar por cerca de 1 hora. Para saber se o bolo está assado, espete um palito na massa: se sair limpo, é sinal de que o bolo está pronto; caso contrário, deixe assar por mais alguns minutos.
Retire o bolo do forno e espere 1 hora antes de desenformar. Espere esfriar completamente para servir.""",

"""1⅓ de xícara (chá) de farinha de trigo
150 g de manteiga cortada em cubos, em ponto pomada
¾ de xícara (chá) de açúcar
3 ovos
3 colheres (sopa) de leite
1 colher (chá) de essência de baunilha
1 colher (chá) de fermento em pó
1 pitada de sal""",

"Bolos"
)

if not recipes_collection.find_one({'name': bolo_ingles.name}):
    recipes_collection.insert_one(bolo_ingles.__dict__)


"""
DOCES
"""


doce_amendoim = Recipe(
"../static/img/recipe_images/doce_amendoim.jpeg",

"Doce de Amendoim",

"""Em uma panela de fundo grosso, junte o amendoim inteiro e o amendoim moído, o açúcar e a Margarina com Sal. Cozinhe em fogo baixo até o açúcar derreter e caramelizar. Junte o leite condensado, o leite integral e o sal, cozinhe em fogo baixo até desgrudar do fundo da panela;
Desligue o fogo, junte o bicarbonato e continue mexendo até parar de espumar. Transfira o doce para uma forma untada com Doriana e leve à geladeira até esfriar por completo;
Desenforme, corte o doce de amendoim em cubos, passe no açúcar de confeiteiro e sirva.""",

"""1 colher de sopa de Margarina com Sal + para untar
½ xícara de amendoim torrado sem pele
½ xícara de amendoim moído
½ xícara de açúcar refinado
¼ lata de leite condensado
¼ xícara de leite integral
1 pitada de sal
½ colher de chá de bicarbonato de sódio
Açúcar de confeiteiro""",

"Doces"
)

if not recipes_collection.find_one({'name': doce_amendoim.name}):
    recipes_collection.insert_one(doce_amendoim.__dict__)

mousse_maracuja = Recipe(
"../static/img/recipe_images/mousse_maracuja.jpeg",

"Mousse de Maracujá",

"""Em uma tigela, adicione a farinha de trigo, açúcar, a margarina, a castanha de caju picada e a canela. Misture tudo até ficar uma farofa;
Em um tabuleiro, adicione a farofa espalhada e asse por 20 minutos a 180ºC. Retire e reserve.
No liquidificador, adicione a polpa de maracujá, o leite condensado e o creme de leite. Bata até ficar homogêneo;
Coloque em taças individuais e leve para gelar por 1 hora;
Retire as taças da geladeira, adicione o crumble por cima e decore com folhas de hortelã.""",

"""1 unidade de maracujá
1 lata de leite condensado
200ml de creme de leite fresco
1 ramo de hortelā
100g de Margarina sem Sal
1 xícara de farinha de trigo
1 colher de chá de canela
100gr de castanha de caju""",

"Doces"
)


if not recipes_collection.find_one({'name': mousse_maracuja.name}):
    recipes_collection.insert_one(mousse_maracuja.__dict__)

pave_pacoca = Recipe(
"../static/img/recipe_images/pave_pacoca.jpeg",

"Pavê de Paçoca",

"""Em uma batedeira, bata em velocidade baixa a Margarina com Sal e o açúcar até formar um creme fofo e esbranquiçado;
Esfarele e misture as paçocas, batendo somente para incorporar e reserve;
Também na batedeira, limpe o batedor e bata o creme de leite fresco e bem gelado com uma pitada de açúcar em outra tigela, até ponto de chantilly, deve ficar cremoso e aerado;
Misture o chantilly delicadamente no creme de Doriana com paçoca e reserve na geladeira;
Em uma panela adicione o amendoim e cubra com água;
Leve ao fogo alto para ferver e cozinhe por 15 minutos após levantar fervura;
Escorra o amendoim e transfira para um liquidificador;
Adicione a água filtrada e bata muito bem, por cerca de 5 minutos;
Apoie um voal ou pano de prato bem limpo sobre uma peneira e coe o leite. Você pode guardar o bagaço do amendoim para outras receitas;
Umedeça biscoito de champanhe no leite de amendoim e distribua no fundo de uma travessa alta;
Cubra com o creme de paçoca e intercale camadas de biscoito champanhe umedecido com o creme até finalizar com o creme;
Cubra o pavê com as paçocas em rolha esfareladas e decore com o amendoim torrado e sem pele;
Leve para a geladeira por pelo menos 30 minutos e sirva.""",

"""150g de Margarina com Sal
1/2 xícara de açúcar + 1 pitada
250ml de creme de leite fresco gelado
20 paçocas rolha
1 xícara de amendoim torrado sem casca e sal
3 xícaras de água filtrada + para cozinhar
300g de biscoito champagne 
10 paçocas rolha
Amendoim torrado sem pele a gosto para decorar""",

"Doces"
)


if not recipes_collection.find_one({'name': pave_pacoca.name}):
    recipes_collection.insert_one(pave_pacoca.__dict__)

