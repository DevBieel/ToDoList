//Criando a função de busca com a lupa
let lupa = document.getElementById('lupa')
let formularioBusca = document.getElementById('formularioBusca');

lupa.addEventListener('click', () =>{
    formularioBusca.submit();
})

//Função para exibir o sweetAlert de deletar uma task
const deleteButtons = document.querySelectorAll('.botao-deletar');

deleteButtons.forEach((deleteButton) =>{
    deleteButton.addEventListener('click', function(event){
        event.preventDefault();

        let deleteLink = this.getAttribute('href');

        Swal.fire({
            icon: 'info',
            title: 'Atenção',
            text: 'Deseja realmente deletar essa tarefa?',
            showConfirmButton: true,
            showDenyButton: true,
            confirmButtonText: 'Sim, quero deletar',
            denyButtonText: 'Cancelar',
        }).then((result) =>{
            if(result.isConfirmed){
                window.location.href = deleteLink;
            }
        })
    })
})

//Exibindo a mensagen de que a task foi deletada
const removeAlert = () =>{
    let mensagens = document.querySelector('.mensagens');
    setTimeout(() =>{
        mensagens.style.display = 'none';
    }, 3000);
}

window.addEventListener('load', removeAlert());

