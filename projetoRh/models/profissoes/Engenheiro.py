from projetoRh.models.Endereco import Endereco
from projetoRh.models.enums.EstadoCivil import EstadoCivil
from projetoRh.models.enums.Setor import Setor
from projetoRh.models.enums.Sexo import Sexo
from projetoRh.models.profissoes.Funcionario import Funcionario


class Engenheiro(Funcionario):
    def __init__(self, id: int, nome: str, dataNascimento: str, crea:str,sexo: Sexo, estadoCivil: EstadoCivil, telefone: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float, email: str, endereco: Endereco) -> None:
        super().__init__(id, nome, dataNascimento, sexo, estadoCivil, telefone, cpf, rg, matricula, setor, salario, email, endereco)
        self.crea = crea
    def __str__(self) -> str:
        return super().__str__(f"\nCrea:{self.crea}")
