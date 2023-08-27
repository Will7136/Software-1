class Vector:
    def __init__(self, data = None, *values):
        
        if (values == ()) and (data != None):
            for x in range (0,len(data)):
                if type(data[x]) != float:
                    data[x] = float(data[x])
            self._vector = data.copy()
        elif (values != ()):
            new_data = []
            for y in range (0, len(values) + 1):
                if y == 0:
                    if type(data) != float:
                        data = float(data)
                    new_data.append(data)
                else:
                    if values[y - 1] != float:
                        new_data.append(float(values[y - 1]))
                    else:
                        new_data.append(values[y-1])
            self._vector = new_data.copy()
        else:
            self._vector = []
        pass


    def __str__(self):

        if len(self._vector) != 0:
            output = f"<{self._vector[0]}"
            for x in range (1, len(self._vector)):
                output += f", {self._vector[x]}"
        else:
            output = "<"
        output += ">"
        return output

    def dim(self):
        return len(self._vector)

    def get(self, index):
        return self._vector[index]
    
    def set(self, index, value):
        self._vector[index] = value
    
    def scalar_product(self, scalar):
        scal_Product = Vector([])
        for x in range(0, len(self._vector)):
            scal_Product._vector.append(self._vector[x] * scalar)
        return scal_Product
    
    def add(self, other_vector):
        
        if type(other_vector) != Vector:
            raise TypeError
        if len(self._vector) != len(other_vector._vector):
            raise ValueError
            
        new_vector = Vector([])
        for x in range(0, len(self._vector)):
            new_vector._vector.append(self._vector[x] + other_vector._vector[x])
            
        return new_vector

       
    def equals(self, other_vector):
        
        if isinstance(other_vector, Vector) == False:
            return False
        if len(other_vector._vector) != len(self._vector):
            return False
        
        for x in range (0, len(self._vector)):
            if other_vector._vector[x] != self._vector[x]:
                return False
        return True

    def __eq__(self, other_vector):
        return(self.equals(other_vector))

    def __ne__(self, other_vector):
        return not (self.equals(other_vector))

    def __add__(self, other_vector):
        return self.add(other_vector)

    def __rmul__(self, scalar):
        return self.scalar_product(scalar)
    
    def __mul__(self, scalar):
        raise TypeError
    
    def __iadd__(self, other_vector):
        return self.add(other_vector)
    
    def __imul__(self, scalar):
        return self.scalar_product(scalar)
