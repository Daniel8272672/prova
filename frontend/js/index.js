// Referências para elementos do DOM
const addTaskBtn = document.getElementById("addTaskBtn");
const modal = document.getElementById("taskModal");
const closeModal = modal.querySelector(".close");
const taskForm = document.getElementById("taskForm");
const titleInput = document.getElementById("taskTitle");
const descInput = document.getElementById("taskDescription");
const taskIdInput = document.getElementById("taskId");
const taskCategoryInput = document.getElementById("taskCategory");
const taskColorInput = document.getElementById("taskColor");
const categoryFilter = document.getElementById("categoryFilter");
const logoutBtn = document.getElementById("logoutBtn"); // Adicionar referência ao botão de logout se existir no index.html

let currentUser = null; // Para armazenar o usuário logado
let usersTasks = JSON.parse(localStorage.getItem("usersTasks")) || {}; // Todos os dados de usuários

// Função para carregar o usuário logado ao carregar a página
function loadCurrentUser() {
  const storedUser = sessionStorage.getItem("currentUser");
  if (storedUser) {
    currentUser = JSON.parse(storedUser);
  }
}

// Funções de Gerenciamento de Tarefas por Usuário
function saveUserData() {
  if (currentUser) {
    // Garante que as tarefas do usuário atual estão atualizadas antes de salvar
    usersTasks[currentUser.username].tasks = tasks;
  }
  localStorage.setItem("usersTasks", JSON.stringify(usersTasks));
  renderTasks(); // Renderiza após salvar
}

function loadTasksForCurrentUser() {
  if (currentUser && usersTasks[currentUser.username]) {
    tasks = usersTasks[currentUser.username].tasks;
  } else {
    tasks = []; // Sem usuário logado ou usuário sem tarefas
  }
  renderTasks();
}

// Renderiza tarefas (AGORA DEPENDE DO tasks do currentUser)
function renderTasks() {
  document.querySelectorAll(".task-list").forEach(list => list.innerHTML = "");

  const selectedCategory = categoryFilter.value;

  // Garante que 'tasks' está definido antes de filtrar
  const tasksToRender = tasks || []; // Usa tasks do currentUser ou um array vazio

  const filteredTasks = tasksToRender.filter(task => {
    return selectedCategory === "" || task.category === selectedCategory;
  });

  filteredTasks.forEach(task => {
    const card = document.createElement("div");
    card.className = "task";
    card.draggable = true;
    card.dataset.id = task.id;

    if (task.color && task.color !== "none") {
      card.classList.add(task.color);
    }

    card.innerHTML = `
      <strong>${task.title}</strong>
      <p>${task.description || ""}</p>
      <p class="task-category">Categoria: ${task.category || "Nenhuma"}</p>
      <div class="controls">
        <button onclick="editTask('${task.id}')">Editar</button>
        <button onclick="deleteTask('${task.id}')">Excluir</button>
      </div>
    `;
    card.addEventListener("dragstart", dragStart);
    document.querySelector(`#${task.status} .task-list`).appendChild(card);
  });
}

// Abrir modal (mantida, mas verifica se está logado)
function openModal(task = {}) {
  if (!currentUser) {
    alert("Por favor, faça login para gerenciar tarefas.");
    return;
  }
  modal.style.display = "flex";
  taskIdInput.value = task.id || "";
  titleInput.value = task.title || "";
  descInput.value = task.description || "";
  taskCategoryInput.value = task.category || "trabalho";
  taskColorInput.value = task.color || "none";
}

// Fechar modal (mantida)
closeModal.onclick = () => modal.style.display = "none";
window.onclick = e => { if (e.target === modal) modal.style.display = "none"; };

// Nova tarefa (mantida, mas usa currentUser.username para salvar)
addTaskBtn.onclick = () => openModal();

// Salvar tarefa (AGORA SALVA AS TAREFAS NO USUÁRIO CORRETO)
taskForm.onsubmit = e => {
  e.preventDefault();
  if (!currentUser) {
    alert("Erro: Nenhum usuário logado para salvar tarefas.");
    modal.style.display = "none";
    return;
  }

  const id = taskIdInput.value || Date.now().toString();
  const title = titleInput.value.trim();
  const description = descInput.value.trim();
  const category = taskCategoryInput.value;
  const color = taskColorInput.value;

  // Certifique-se de que o array de tarefas para o usuário existe
  if (!usersTasks[currentUser.username]) {
    usersTasks[currentUser.username] = { tasks: [] };
  }

  const userTasks = usersTasks[currentUser.username].tasks; // Referência às tarefas do usuário logado
  const index = userTasks.findIndex(t => t.id === id);

  if (index > -1) {
    userTasks[index].title = title;
    userTasks[index].description = description;
    userTasks[index].category = category;
    userTasks[index].color = color;
  } else {
    userTasks.push({ id, title, description, status: "todo", category: category, color: color });
  }
  tasks = userTasks; // Atualiza o array 'tasks' global para refletir as mudanças
  saveUserData(); // Salva TODOS os dados de usuários
  modal.style.display = "none";
};

// Editar tarefa (mantida, mas verifica se está logado)
function editTask(id) {
  if (!currentUser) return; // Não permite editar se não estiver logado
  const task = tasks.find(t => t.id === id);
  if (task) openModal(task);
}

// Excluir tarefa (mantida, mas usa currentUser.username para excluir)
function deleteTask(id) {
  if (!currentUser) return; // Não permite excluir se não estiver logado
  usersTasks[currentUser.username].tasks = usersTasks[currentUser.username].tasks.filter(t => t.id !== id);
  tasks = usersTasks[currentUser.username].tasks; // Atualiza o array 'tasks' global
  saveUserData();
}

// Drag and Drop (mantida, mas usa currentUser.username para atualizar)
function dragStart(e) {
  if (!currentUser) return; // Não permite drag se não estiver logado
  e.dataTransfer.setData("text/plain", e.target.dataset.id);
}
document.querySelectorAll(".column").forEach(col => {
  col.addEventListener("dragover", e => e.preventDefault());
  col.addEventListener("drop", e => {
    if (!currentUser) return; // Não permite drop se não estiver logado
    const id = e.dataTransfer.getData("text/plain");
    const task = tasks.find(t => t.id === id); // Procura na lista atual de tarefas
    if (task) {
      task.status = col.dataset.status;
      saveUserData(); // Salva todos os dados, o que incluirá a mudança de status
    }
  });
});

// Event listener para o filtro de categoria
categoryFilter.addEventListener("change", renderTasks);

// Lógica de Logout (se você tiver um botão de logout em index.html)
if (logoutBtn) {
  logoutBtn.onclick = () => {
    sessionStorage.removeItem("currentUser"); // Limpa o usuário da sessão
    currentUser = null;
    window.location.href = "vc.html"; // Redireciona de volta para a tela de login
  };
}


// Inicialização: Carrega o usuário e as tarefas ao carregar a página
function init() {
  loadCurrentUser(); // Tenta carregar o usuário da sessão
  if (currentUser) {
    loadTasksForCurrentUser(); // Se houver usuário, carrega as tarefas dele
  } else {
    // Se não houver usuário logado (ex: acessou index.html diretamente),
    // você pode redirecionar para a tela de login ou mostrar uma mensagem.
    // Por simplicidade, vamos redirecionar:
    window.location.href = "vc.html";
  }
}

init(); // Chama a função de inicialização