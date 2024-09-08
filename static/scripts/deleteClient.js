const deleteButton = document.querySelectorAll(".delete-button");


deleteButton.addEventListenerAll("click", async (event) =>{
    try{
        const client = event.target.closest('tr');
        const id = client.querySelector("td:first-child").textContent;

        const sendClientId = await fetch(`http://127.0.0.1:5000/clients/${id}`,{
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' }
        })

        client.remove();

    } catch(error){
        console.error('Erro ao deletar cliente:', error);
    }
    

    
})