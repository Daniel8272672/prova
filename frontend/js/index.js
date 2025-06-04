const addTaskBtn = document.getElementById("addTaskBtn");
const modal = document.getElementById("taskModal");
const closeModal = modal.querySelector(".close");
const taskForm = document.getElementById("taskForm");
const titleInput = document.getElementById("taskTitle");
const descInput = document.getElementById("taskDescription");
const taskIdInput = document.getElementById("taskId");
const taskCategoryInput = document.getElementById("taskCategory");
const taskColorInput = document.getElementById("taskColor"); // Nova referência para a cor/tag
const categoryFilter = document.getElementById("categoryFilter");

let tasks = JSON.parse(localStorage.getItem("tasks")) || [];

// Renderiza tarefas
function renderTasks() {
  document.querySelectorAll(".task-list").forEach(list => list.innerHTML = "");

  const selectedCategory = categoryFilter.value;

  const filteredTasks = tasks.filter(task => {
    return selectedCategory === "" || task.category === selectedCategory;
  });

  filteredTasks.forEach(task => {
    const card = document.createElement("div");
    card.className = "task";
    card.draggable = true;
    card.dataset.id = task.id;

    // Adiciona a classe de cor se houver
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

// Abrir modal
function openModal(task = {}) {
  modal.style.display = "flex";
  taskIdInput.value = task.id || "";
  titleInput.value = task.title || "";
  descInput.value = task.description || "";
  taskCategoryInput.value = task.category || "trabalho";
  taskColorInput.value = task.color || "none"; // Define a cor no modal
}

// Fechar modal
closeModal.onclick = () => modal.style.display = "none";
window.onclick = e => { if (e.target === modal) modal.style.display = "none"; };

// Nova tarefa
addTaskBtn.onclick = () => openModal();

// Salvar tarefa
taskForm.onsubmit = e => {
  e.preventDefault();
  const id = taskIdInput.value || Date.now().toString();
  const title = titleInput.value.trim();
  const description = descInput.value.trim();
  const category = taskCategoryInput.value;
  const color = taskColorInput.value; // Captura a cor do input

  const index = tasks.findIndex(t => t.id === id);
  if (index > -1) {
    tasks[index].title = title;
    tasks[index].description = description;
    tasks[index].category = category;
    tasks[index].color = color; // Atualiza a cor
  } else {
    tasks.push({ id, title, description, status: "todo", category: category, color: color }); // Adiciona a cor na nova tarefa
  }
  saveTasks();
  modal.style.display = "none";
};

// Editar tarefa
function editTask(id) {
  const task = tasks.find(t => t.id === id);
  if (task) openModal(task);
}

// Excluir tarefa
function deleteTask(id) {
  tasks = tasks.filter(t => t.id !== id);
  saveTasks();
}

// Drag and Drop
function dragStart(e) {
  e.dataTransfer.setData("text/plain", e.target.dataset.id);
}
document.querySelectorAll(".column").forEach(col => {
  col.addEventListener("dragover", e => e.preventDefault());
  col.addEventListener("drop", e => {
    const id = e.dataTransfer.getData("text/plain");
    const task = tasks.find(t => t.id === id);
    if (task) {
      task.status = col.dataset.status;
      saveTasks();
    }
  });
});

// Salvar e renderizar
function saveTasks() {
  localStorage.setItem("tasks", JSON.stringify(tasks));
  renderTasks();
}

// Event listener para o filtro de categoria
categoryFilter.addEventListener("change", renderTasks);

// Inicialização
renderTasks();