// Referências para elementos da tela de login
const loginScreen = document.getElementById("loginScreen");
const kanbanApp = document.getElementById("kanbanApp");
const loginForm = document.getElementById("loginForm");
const usernameInput = document.getElementById("username");
const passwordInput = document.getElementById("password");
const loginMessage = document.getElementById("loginMessage");
const registerBtn = document.getElementById("registerBtn");

// Referências para elementos do Kanban (mantidas)
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
const logoutBtn = document.getElementById("logoutBtn"); // Nova referência para o botão de logout

let currentUser = null; // Armazena o usuário atualmente logado
// As tarefas agora serão armazenadas por usuário
let usersTasks = JSON.parse(localStorage.getItem("usersTasks")) || {};

// Funções de Gerenciamento de Login/Usuário
function saveUserData() {
  localStorage.setItem("usersTasks", JSON.stringify(usersTasks));
}

function loadTasksForCurrentUser() {
  if (currentUser) {
    tasks = usersTasks[currentUser.username] || [];
  } else {
    tasks = []; // Sem usuário logado, sem tarefas
  }
  renderTasks();
}

function showLoginScreen() {
  loginScreen.classList.remove("hidden");
  kanbanApp.classList.add("hidden");
  loginMessage.textContent = ""; // Limpa a mensagem de login
  usernameInput.value = "";
  passwordInput.value = "";
}

function showKanbanApp() {
  loginScreen.classList.add("hidden");
  kanbanApp.classList.remove("hidden");
  renderTasks(); // Renderiza as tarefas do usuário logado
}

// Lógica de Login
loginForm.onsubmit = (e) => {
  e.preventDefault();
  const username = usernameInput.value.trim();
  const password = passwordInput.value.trim();

  // Simples validação: verifica se o usuário existe e a senha corresponde
  if (usersTasks[username] && usersTasks[username].password === password) {
    currentUser = { username: username }; // Define o usuário logado
    loginMessage.textContent = ""; // Limpa qualquer mensagem de erro

    // Armazena o usuário logado no sessionStorage ou localStorage antes de redirecionar
    // Isso é crucial para que index.html saiba quem está logado
    sessionStorage.setItem("currentUser", JSON.stringify(currentUser)); // Usando sessionStorage para limpar após fechar o navegador

    // Redireciona para a página do Kanban
    window.location.href = "index.html"; // Redireciona para a página do Kanban
  } else {
    loginMessage.textContent = "Usuário ou senha inválidos.";
  }
};
// Lógica de Registro (cria um novo usuário no localStorage)
registerBtn.onclick = () => {
  const username = usernameInput.value.trim();
  const password = passwordInput.value.trim();

  if (username === "" || password === "") {
    loginMessage.textContent = "Preencha usuário e senha para cadastrar.";
    return;
  }

  if (usersTasks[username]) {
    loginMessage.textContent = "Este usuário já existe. Tente outro nome.";
  } else {
    usersTasks[username] = {
      password: password,
      tasks: [] // Inicializa um array de tarefas vazio para o novo usuário
    };
    saveUserData();
    loginMessage.textContent = "Usuário cadastrado com sucesso! Faça login.";
    loginMessage.style.color = "#28a745"; // Cor verde para sucesso
  }
};

// Lógica de Logout
logoutBtn.onclick = () => {
  currentUser = null; // Limpa o usuário logado
  showLoginScreen(); // Volta para a tela de login
  tasks = []; // Limpa as tarefas exibidas
  renderTasks(); // Renderiza sem tarefas
};


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
      // Não precisa chamar renderTasks aqui, pois saveUserData já faz isso
    }
  });
});

// A função saveTasks agora é descontinuada em favor de saveUserData
function saveTasks() {
  if (currentUser) {
    usersTasks[currentUser.username].tasks = tasks; // Garante que as tarefas do usuário atual estão atualizadas
  }
  localStorage.setItem("usersTasks", JSON.stringify(usersTasks));
  renderTasks();
}

// Event listener para o filtro de categoria
categoryFilter.addEventListener("change", renderTasks);

// Inicialização: Verifica se o usuário está logado ao carregar a página
function init() {
  // Poderíamos tentar carregar um usuário da sessão anterior aqui,
  // mas para manter a simplicidade do "frontend apenas",
  // sempre começaremos na tela de login.
  showLoginScreen();
}

init(); // Chama a função de inicialização