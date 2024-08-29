const deleteButton = document.querySelector("#delete-button");


deleteButton.addEventListener("click", async (event) =>{
    const client = event.target.closest('tr');
    const id = client.querySelector("td:first-child").textContent;

    
    
    
})