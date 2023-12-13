import random
import string

# create   a function
   def generate_id() -> str:
       return "".join(random.choices(string.ascii_uppercase,k=12))

    class person:
        def_init_(self,name: str,adress:str):
        self.name = name
        self.adress = adress

        def_str_(self)-> str:
          return f"{self.name},{slef.adress}"

        # main functions
    def main() -> None:
        person = person(name="jhon",address="123 main st")
        print(person)