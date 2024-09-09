const deleteButton = document.querySelectorAll(".delete-button");

console.log(deleteButton);


deleteButton.forEach(button =>{
    button.addEventListener("click", async (event) =>{
        event.preventDefault();
        try{
            const client = event.target.closest('tr');
            const id = client.querySelector("td:first-child").textContent;
    
            const sendClientId = await fetch(`http://127.0.0.1:5000/clients/${id}`,{
                method: 'DELETE',
                headers: { 'Content-Type': 'application/json' }
            })
    
            client.remove();
            Location.reload()
    
        } catch(error){
           console.error('Erro ao deletar cliente:', error);
        }
        
        
        
    })
})

