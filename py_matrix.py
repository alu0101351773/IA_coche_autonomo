
class Matriz:
    # Metodos

    # Constructor
    def __init__(self, new_height = 1, new_width = 1):
        self.inner_matrix = []
        self.height = new_height
        self.width = new_width

        self.resize(self.height, self.width)


    # Redimensionar la matriz dinamicamente
    def resize(self, new_height, new_width):
         del self.inner_matrix
         self.height = new_height
         self.width = new_width

         self.inner_matrix = [[0 for i in range(new_height)] for j in range(new_width)]      


    # Mostrar la matriz en terminal
    def print(self):
        for i in range(self.height):
            print(self.inner_matrix[i])


    # Getter del valor en la matriz
    def get_value(self, x, y):
        return self.inner_matrix[x][y]
    

    # Setter del valor en la matriz
    def set_value(self, x, y, value):
        self.inner_matrix[x][y] = value

    
    # Getter de la anchura
    def get_width(self):
        return self.width


    # Getter de la anchura
    def get_height(self):
        return self.height
    # Atributos
    # self.inner_matrix

    # [x][y] 
    # x = altura
    # y = anchura#