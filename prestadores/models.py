from django.db import models
from usuarios.models import User
from core.helpers import validate_CPF, validate_file_extension
 



def identidade_frente_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.nr_cpf_cgc, "id_frente_"+filename)

def identidade_verso_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.nr_cpf_cgc, "id_verso_"+filename)
def comp_resid_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.nr_cpf_cgc, "comp_resid_"+filename)

def comp_cnpj_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.cd_fornecedor, "comp_cnpj_"+filename)


class Especialidade(models.Model):
    nm_especialidade = models.CharField(blank=False, max_length=100)
    def __str__(self):
        return self.nm_especialidade

class Fornecedor(models.Model):
    cd_fornecedor = models.IntegerField(verbose_name="Código Fornecedor MV", default=0, unique=False,blank=True, null=True)
    nm_fornecedor = models.CharField(verbose_name="Razão Social", max_length=200,blank=True, null=True)
    nm_fantasia= models.CharField(verbose_name="Nome Fantasia", max_length=200,blank=True, null=True)
    comprovante_cnpj = models.FileField(upload_to=comp_cnpj_directory_path, validators=[validate_file_extension], blank=True, null=True)

    def __str__(self):
        return self.nm_fornecedor        
       

STATUS_CADASTRO = (
    ('PENDENTE', 'Aguardando Validação'),
    ('VALIDADO', 'Validado (Ativo)'),
    ('INVALIDO', 'Inválido'),
    ('INATIVO', 'Inativo'),
)
class PrestadorPessoaFisica(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Enviado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    status=models.CharField(max_length=30, choices=STATUS_CADASTRO, default='PENDENTE')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    cd_prestador = models.IntegerField(unique=False,blank=True, null=True)
    nm_prestador = models.CharField(verbose_name="Nome Completo", max_length=100)
    nr_cpf_cgc = models.CharField(verbose_name="CPF",max_length=11,validators=[validate_CPF])
    dt_nascimento = models.DateField(verbose_name="Data de Nascimento", blank=True, null=True)
    ds_email = models.EmailField(verbose_name="Email", max_length=200, blank=True, null=True)
    nr_cep = models.CharField(verbose_name="CEP", max_length=8,blank=True, null=True)
    ds_endereco = models.CharField(verbose_name="Endereço", max_length=200, blank=True, null=True)
    ds_complemento = models.CharField(verbose_name="Complemento", max_length=20, blank=True, null=True)
    ds_bairro = models.CharField(verbose_name="Bairro", max_length=200, blank=True, null=True)
    nm_cidade = models.CharField(verbose_name="Cidade", max_length=200, blank=True, null=True)
    cd_uf = models.CharField(verbose_name="UF", max_length=200, blank=True, null=True)
    nr_fone_contato = models.CharField(verbose_name="Telefone para Contato", max_length=20,blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True,verbose_name="Observações")
    data_insercao = models.DateTimeField(auto_now_add=True)
    identidade_frente =models.FileField(verbose_name="Documento", upload_to=identidade_frente_directory_path,validators=[validate_file_extension], blank=True, null=True)
    especialidades = models.OneToOneField(Especialidade, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.nm_prestador)


