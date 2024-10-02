
class Produit:


    def __init__(self,id,description,prix) -> None:
        self.id = id
        self.description = description
        self.prix = prix

    def __str__(self) -> str:
        return f"Id: {self.id} - Description: {self.description} - Prix: {self.prix}"
    
    def __eq__(self, other: object) -> bool:
        return self.id == other.id