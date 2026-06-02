- Explique a diferença entre os métodos HTTP `PUT` e `PATCH`.

- Você possui um endpoint `GET` que anteriormente respondia em aproximadamente 300ms e passou a responder em 10 segundos. O endpoint realiza consultas ao banco de dados e retorna uma lista paginada de dados.
Descreva seu processo de investigação e responda: Quais são as possíveis causas da degradação de performance ? Como você validaria a solução antes de colocá-la em produção?

- Explique o conceito de indexação em bancos de dados relacionais.

- Explique as diferenças entre `PRIMARY KEY` e `UNIQUE` em bancos de dados SQL.

- Em produção, usuários relatam lentidão intermitente em operações de escrita. Durante a investigação, você identifica que existem transações aguardando locks no banco. O que são locks em bancos relacionais ?

- Em produção, você recebe alertas de que um endpoint específico que antes respondia em ~200ms passou a responder em ~8s de forma intermitente. O endpoint consulta o banco de dados e faz chamadas a um serviço externo. Não houve deploy recente. Descreva seu processo completo de investigação e resolução, incluindo as ferramentas que utilizaria e as hipóteses que investigaria.

- Você tem uma task Celery que processa pagamentos. Em produção, observa-se que alguns pagamentos são cobrados duas vezes. Ao investigar, descobre que a task pode ser executada mais de uma vez em certos cenários. Explique:

- Você tem um endpoint Django que precisa chamar 5 microserviços externos em sequência para montar uma resposta consolidada. O tempo médio de resposta de cada serviço é 300ms, resultando em ~1.5s de latência total. Como você resolveria esse problema? Discuta pelo menos duas abordagens, seus trade-offs e como cada uma se encaixa em um projeto Django tradicional (WSGI) versus Django com ASGI.

- Revise o código abaixo de uma view DRF e aponte todos os problemas que você identificar:
```python
class UserDataView(APIView):
    permission_classes = []

    def get(self, request):
        user_id = request.query_params.get('user_id')
        user = User.objects.get(id=user_id)
        data = {
            "name": user.name,
            "email": user.email,
            "password": user.password,
            "token": user.auth_token,
        }
        return Response(data, status=200)
```

- Revise o código abaixo usado em um endpoint que retorna uma lista de consultas com dados do paciente e do profissional:
```python
def get_consultations(request):
    consultations = Consultation.objects.filter(active=True)
    result = []
    for c in consultations:
        result.append({
            "id": c.id,
            "patient": c.patient.name,
            "professional": c.professional.name,
            "date": c.date,
        })
    return JsonResponse({"data": result})
```

- Analise o trecho de Dockerfile abaixo e aponte problemas de segurança, performance e boas práticas:
```dockerfile
FROM python:3.11
WORKDIR /code
COPY . .
RUN pip install -r requirements.txt
ENV SECRET_KEY=minha-chave-secreta-123
ENV DEBUG=True
EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
```

- Você está projetando uma API REST para gerenciar planos de dieta de pacientes. Avalie as rotas abaixo e proponha melhorias seguindo as boas práticas REST:
```
POST   /createDietPlan
GET    /getDietPlan?patient=123
PUT    /updateDietPlan?id=5
DELETE /deleteDietPlan?id=5
GET    /getDietPlanItems?plan=5
POST   /addItemToDietPlan
```





