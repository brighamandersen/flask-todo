function enableEditMode(todoId) { 
  const todoContent = document.querySelector(`#todo-content-${todoId}`);
  todoContent.style.display = 'none';
  const editForm = document.querySelector(`#edit-form-${todoId}`);
  editForm.style.display = 'flex';
}

function disableEditMode(todoId) { 
  const todoContent = document.querySelector(`#todo-content-${todoId}`);
  todoContent.style.display = 'inline';
  const editForm = document.querySelector(`#edit-form-${todoId}`);
  editForm.style.display = 'none';
}