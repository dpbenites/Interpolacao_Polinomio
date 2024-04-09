import matplotlib.pyplot as plt
from poli import Operation, func, polinomial
import numpy as np

coord_list = [ (0,1) , (1,6) , (2,5) , (3,24) , (4,6), (5,10)]

coef_matrix = Operation(coord_list)[0]
x_list = Operation(coord_list)[1]
y_list = Operation(coord_list)[2]

## defining the range of the plot

x = np.arange(-1,6,0.01)
y = polinomial(array=coef_matrix, x=x )

import re



def write_func(coef_matrix):
    n = coef_matrix.shape[0]
    function = ''
    for i in range(n):

        if i==0: 
            function += f'{round(coef_matrix[0][0] ,2)} '
        
        else:

            if coef_matrix[i] < 0:
                function+= f'{round(coef_matrix[i][0],2)}x^{i}  '

            elif coef_matrix[i] == 0:
                function+= ''


            else:
                function+= f'+{round(coef_matrix[i][0],2)}x^{i}  '


        # String original
    string_original = function

    # Adiciona chaves em torno dos expoentes
    string_formatada = re.sub(r'x\^(\d+)', r'x^{\1}', string_original)

    return string_formatada

text = write_func(coef_matrix=coef_matrix)
text = f'$p(x) = {text}$'


fig , ax = plt.subplots(figsize = (12,8))
ax.scatter(x_list, y_list, marker = 's', color = 'orange', label = 'pontos entrada', s = 10)
ax.plot(x,y ,color = 'red', label = 'polinômio')

## inserindo a equação:

ax.text(0.5, 45 , text, fontsize = 12 , color= 'black', fontweight = 'bold')

ax.set_ylabel('$p(x)$')
ax.set_xlabel('$x$')

ax.set_ylim(-10, 50)

ax.legend(loc='upper right')

# Retirando as bordas
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Centralizar o eixo x com os tickers em x = 0
ax.spines['bottom'].set_position(('data', 0))
# Centralizar o eixo y com os tickers em y = 0
ax.spines['left'].set_position(('data', 0))

plt.savefig('polinomio.pdf', dpi = 600)
plt.show()
