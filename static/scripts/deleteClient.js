const deleteButton = document.querySelector("#delete-button");


deleteButton.addEventListener("click", async (event) =>{
    const client = event.target.closest('tr');
    const id = client.querySelector("td:first-child").textContent;

    const sendClient = await fetch(`http://127.0.0.1:5000/clients/${id}`,{
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
    })
    
    
})