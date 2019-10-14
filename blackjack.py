import random
import os
'''
A fazeres:
Nome das cartas (A,J,K,Q)
Partida teste para iniciantes
Desempate
'''

q=10 #figuradas valem 10
j=10
k=10
A=11 #ás vale 11 se uma mão não estourar
binicial=[A, 2, 3, 4, 5, 6, 7, 8, 9, 10, q, j, k]*4 #um baralho tem 4 conjuntos desses
naipes=["♣","♥","♠","♦"]
baralho=(binicial)
#baralho=bpaus+bcopas+bespadas+bouros
mj=[] #mão jogador
mj2=[]
mj3=[]
mc=[] #mão croupier
ls=["Sim","sim","s","S"] #lista com sim
ln=["Não","não","nao","Nao","n","N"] #lista com nao
lcar=["carta", "cartas", "car", "Carta", "Cartas"]
lcon=["continuar", "con", "Continuar"]
d=1000 #dinheiro
m="carta" #para entrar no loop
abc="n"
jogadores=[0,5,20]
limpa = lambda: os.system('cls')
ayuda="Inicialmente, você apostará um valor. Após isso, você receberá duas cartas. Estas cartas terão um valor somado; se tal soma passar de 21, você estourou e perdeu. (Cartas numéricas valem seu próprio número, cartas figuradas valem 10, e o Ás vale 11. Entretanto, se sua mão valer mais de 21, mas você tem um Ás, o Ás passa a valer 1). Ganha quem tiver o número mais alto perto de 21, sem ultrapassa-lo. Se suas cartas iniciais tiverem um valor baixo, você pode pedir mais cartas quanto quiser." #texto para iniciantes
print("♠ ♥ ♣ ♦ Bem-vindo à mesa de Blackjack! ♠ ♥ ♣ ♦")
perg=input("Você sabe jogar Blackjack? ")
while perg in ln:
    print("Sem problemas!")
    print(ayuda)
    abc=input("Entendeu? ")
    if abc in ls:
        break
    else:
        continue

print("Regras e funcionamento adicionais:")
print("1: Não aposte mais dinheiro do que tem!")
print("2: Aposte valores inteiros!")
print("3: Se suas cartas iniciais somarem 21 pontos, você automaticamente ganha 1,5x o que apostou.")
print("4: Se você ganhar/perder de outra forma você ganha/perde exatamente o que apostou.")
print("5: Enquanto a mão do croupier for menor que a sua, ele vai puxar cartas até atingir no mínimo 17 pontos.")
print("6: Se quiser lembrar como jogar Blackjack, digite 'ajuda'")
print("7: Se quiser lembrar com quantos baralhos está jogando, digite 'baralho(s)'")
print("8: Se quiser que o jogo pare, digite 'desisto' ou 'fim'.")

print("Se divirta!")
qtj=0
while qtj<1 or qtj>3:
    qtj=int(input("Quantos jogadores participarão? "))
    if qtj>3:
        print("Nosso jogo só suporta até 3 jogadores!")
        continue
    elif qtj<1:
        print("Você não digitou um valor válido.")
        continue
    nj=qtj
i=0
while nj>0 and qtj != 1:
  print("Insira o nome do jogador", nj)
  japp=(input())
  jogadores[i]=japp
  if jogadores[0]==jogadores[1] or jogadores[0]==jogadores[2] or jogadores[1]==jogadores[2]:
    print("Por favor use nomes diferentes!")
    continue
  nj-=1
  i+=1
q=0 #para entrar no loop
inp="s" #para entrar no loop
while q<1 or q>10 or inp in ln:
    inp='s'
    q=int(input("Com quantos baralhos quer jogar? "))
    if q>10:
        print("O máximo são 10 baralhos!")
        continue
    elif q<1:
        print("Você não digitou um valor válido.")
        continue
    elif q>3:
        inp=input("O jogo funciona optimamente com menos baralhos, tem certeza de que quer continuar? ")
    if inp in ln:
        continue
    elif inp in ls:
        break  

baralho=baralho*q
#print(baralho)
while d!=0:
    limpa()
    mj.clear()
    mc.clear()
    print("Você tem: R$", d)
    b=(input('Aposte um valor inteiro: '))
    if b=="ajuda" or b=="Ajuda":
        print(ayuda)
        continue
    if b=="baralho" or b=="baralhos" or b=="Baralho" or b=="Baralhos":
        print("Você está jogando com", q, "baralho(s).")
        continue
    if b=="desisto" or b=="fim":
        print("Que pena!")
        break
    a=int(b)
    if a<1:
      print("Você apostou um valor inválido!")
      continue
    if a>d:
        print("Não aposte mais dinheiro do que tem!")
        print("Você foi penalizado em: R$", 0.1*d, "por tentar trapacear!")
        d=d-(0.1*d)
        continue
    mj.append(random.choice(baralho))
    mj.append(random.choice(baralho))
    if sum(mj)>21 and A in mj:
        subs=mj.index(A)
        mj[subs]=1
    if sum(mj)>21:
        print("Você estourou com as cartas", mj, "!")
        d=d-a
        continue
    if sum(mj)==21:
        d=d+((1.5)*a)
        print("Parabéns, você ganhou um Blackjack com as cartas", mj, "!")
        continue
    print("Você tem as cartas: ", mj, "totalizando: ", sum(mj), ", você gostaria de mais uma carta ou quer continuar?")
    m=input("Responda com 'continuar' ou 'carta': ")
    if m in lcar:
        while m not in lcon:
            #m=input("Responda com 'continuar' ou 'carta': ")
            mj.append(random.choice(baralho))
            if sum(mj)>21 and A in mj:
              subs=mj.index(A)
              mj[subs]=1
            if sum(mj)>21:
                print("Você estourou com as cartas", mj, "totalizando:", sum(mj), "!")
                d=d-a
                break
            elif sum(mj)==21:
                d=d+((1.5)*a)
                print("Parabéns, você ganhou um Blackjack com as cartas", mj, "!")
                break
            print("Você tem as cartas: ", mj, "totalizando: ", sum(mj), ", você gostaria de mais uma carta ou quer continuar?")
            m=input("Responda com 'continuar' ou 'carta': ")
    if sum(mj)>21:
      continue
    if sum(mj)==21:
      continue
    mc.append(random.choice(baralho))
    mc.append(random.choice(baralho))
    print("O croupier tem as cartas: ", mc, "totalizando: ", sum(mc))
    while sum(mc)<17 and sum(mc)<sum(mj):
        mc.append(random.choice(baralho))
        print("O croupier tem as cartas: ", mc, "totalizando: ", sum(mc))
    if sum(mc)>21 and A in mc:
        subs=mc.index(A)
        mc[subs]=1
    if sum(mc)>21:
        print("O croupier estourou!")
        d=d+a
        print("Você ganhou!")
        continue
    if sum(mc)>sum(mj):
        d=d-a
        print("Você perdeu.")
        continue
    elif sum(mj)>sum(mc):
        d=d+a
        print("Você ganhou!")
        continue
    elif sum(mj)==sum(mc):
        print("É um empate!")
        continue
if d==0:    
    print("Seu dinheiro acabou!")
print("Obrigado por jogar nosso jogo!")
print("Volte sempre!")
