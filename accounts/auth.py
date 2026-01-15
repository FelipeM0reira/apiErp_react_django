from rest framework.exceptions import AuthenticationFailed, ApiException

from django.contrib.auth.hashers import check_password, make_password

from accounts.models import User

from companies.models import Enterprise, Employee

class Authentication:
  def signin(self, email=None, password=None) -> User:
    exception_auth = AuthenticationFailed("Email e/ou senha incorreto(s).")
    
    user_exists = User.objects.filter(email=email).exists()
    
    if not user_exists:
      raise exception_auth
    
    user = User.objects.filter(email=email).first()
    
    if not check_password(password, user.password):
      raise exception_auth

    return user
  
  def signup(self, name, email, password, type_account='owner', company_id=False):
    if not name or name == '':
      raise ApiException("O nome é obrigatório.")
    
    if not email or email == '':
      raise ApiException("O email é obrigatório.")
    
    if not password or password == '':
      raise ApiException("A senha é obrigatória.")
    
    if type_account == 'employee' and not company_id:
      raise ApiException("O ID da empresa é obrigatório para cadastro de funcionário.")
    
    user = User
    if user.objects.filter(email=email).exists():
      raise ApiException("Já existe uma conta cadastrada com esse email.")
    
    password_hashed = make_password(password)
    
    created_user = user.objects.create(
      name=name, 
      email=email, 
      password=password_hashed,
      is_owner=0 if type_account == 'employee' else 1,
    )
    
    if type_account == 'owner':
      Enterprise.objects.create(
        name='Nome da empresa',
        user_id=created_user.id,
      )
      
    if type_account == 'employee':
      Employee.objects.create(
        enterprise_id=company_id or created_enterprise.id,
        user_id=created_user.id,
      )
      
    return created_user