const form = document.querySelector("#client-form");
const table = document.querySelector(".table");





form.addEventListener("submit", (event) =>{
    event.preventDefault();

    const name = document.querySelector("#name").value;
    const email = document.querySelector("#email").value;

    fetch('http://127.0.0.1:5000/clients', { 
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: name, email: email })
      })
      .then(response => response.json())
      .then(data => {
        const novaLinha = `
          <tr>
            <td>${data.id}</td> 
            <td>${data.name}</td>
            <td>${data.email}</td>
             <td><button type="button" class="btn btn-primary edit-button">Editar</button> 
             <button type="button" class="btn btn-danger delete-button">Deletar</button></td>
          </tr>
        `;
        table.innerHTML += novaLinha;
        form.reset();
      })
      .catch(error => console.error('Erro:', error));


})