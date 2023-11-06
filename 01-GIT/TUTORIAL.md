##### Iniciar um repositório local ou clonar um repositório remoto
`git init` or `git clone` 
##### Baixar atualizações do repositório traz oq está remoto e faz o merge com o local
`git pull`
##### Adiconar arquivos para area de Staged
`git add <arquivo>` ou todos arquivos `git add .`
##### Verificar status das modificações
`git status`
##### criar commit
`git commit -m "msg"v`

##### enviar arquivos para o repositório remoto
`git push`
##### verifciar os logs / histórico das modificações
`git log -- ultimos commits / historico e pega o hash`
##### restaurar arquivo modificado
`git restore <nome_arquivo>`
##### restaurar arquivo da area staged para area changes
`git restore --staged (volta p changes)`
##### verifica repositorio remoto
`git remote ( verifica remoto)`
##### envia arquivos para repositorio remoto
`git push origin <branch>`

##### Comandos diff, fetch e pull
`git fetch` (baixa tudo que nao tem no local)
##### verificar diferença 
`git diff`
##### verificar diferença dos arquivos da area de Staged
`git diff --staged`
##### verificar diferença dos aquivos das branchs indicadas
`git diff origin/master`

##### Comandos Branch
##### (lista as ramificções)
<b>HEAD --> PONTEIRO DE ONDE ESTAMOS</b>

`git branch <nome branch>`
`git log --online --decorate` <b>(nos indica os comitis e onde estamos apontados)</b>
`git checkout <branch>` <B>(move para branch )</B>


##### voltar p branch master
`git checkout <master>`

##### Merge entre branchs

 EX: de dentro da master a  gente uni com outra branch
`git merge <branch>`